"""The utils module contains convenience methods that do not depend on any other code
inside ra_lib. Functions added here should be used in multiple contexts,
or at the very least they should be general purpose.
"""

import re

import pandas as pd
from pyspark.sql import SparkSession, Window
from pyspark.sql import functions as sqlfn
from pyspark.sql.dataframe import DataFrame
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql.connect.dataframe import DataFrame as ConnectDataFrame


class UtilsSystem:
    """UtilsSystem is the main class of the utils module.

    One of UtilsSystem's main functions is to record table history for auditing purposes.
    This involves the use of a selected table ("current_df") and its history ("history_df").
    This system operates under a few requirements:
    1. current_df contains a series of snapshots of different groups at different times
    2. history_df contains the changes in group membership, up to and including the earliest snapshot per group stored in current_df.
    If these assumptions are followed then current_df and history_df can be operated in a manner to allow current_df to receive
    concurrent updates without conflict. Note that both current_df and history_df must include the full data needed to reproduce
    the earliest snapshot per group. This enables us to record both the 
    """

    def __init__(
        self,
        change_type_col: str = "change_type",
        change_time_col: str = "change_datetime",
    ):
        """Construct an instance of UtilsSystem.

        TODO: Reconcile what should and shouldn't be an attribute. We probably don't want change_type_col and change_time_col
        to be parameters because it should be vanishingly rare that we use something other than the defaults.

        Parameters
        ----------
        self.change_time_col : str
            Column name for the column that tracks changes in history tables.
        self.change_type_col : str
            Column name for the column that tracks change type in history tables.
        """
        # Get the spark session
        self.spark = SparkSession.builder.getOrCreate()
        self.change_type_col = change_type_col
        self.change_time_col = change_time_col

    def query_history_dataframe(
        self,
        history_df: DataFrame,
        id_cols: list[str],
        time_observed: str | pd.Timestamp = None,
    ) -> DataFrame:
        """Given a dataframe history_df that records the rows inserted and deleted
        from a table "original_table", this method identifies the rows that were
        present in original_table at the specified time.

        This could be done in spark sql, but we opt to do it using pyspark because
        it's easier to parameterize. For example, id_col here can either be a single
        column name or a list of column names.

        Parameters:
        ----------
        history_df : DataFrame
            A dataframe recording the history of a table. It should consist of at
            least id_col and self.change_time_col.
        id_col : str | list[str]
            One or more columns that uniquely identifies a given row in the table that
            history_df is based on. For example, for cohort_patients this is
            ["report_id", "patient_id", "patient_id_type"].
        time : str | pd.Timestamp, optional
            The time at which you want to get the rows in original_table. Defaults
            to the current time.

        Returns
        -------
        DataFrame
            The dataframe tracked by history_df at the specified time.
        """

        # Toss out rows that don't exist at the target time
        if time_observed is not None:
            history_df = history_df.filter(sqlfn.col(self.change_time_col) < time_observed)

        # Create a window
        w = Window.partitionBy(id_cols).orderBy(sqlfn.desc(self.change_time_col))

        # Get and then filter on row number
        history_df_with_rn = history_df.withColumn("rn", sqlfn.row_number().over(w))
        df_at_time = history_df_with_rn.filter("rn = 1").drop("rn")

        return df_at_time

    def get_history_updates(
        self,
        history_df: DataFrame,
        current_df: DataFrame,
        group_key: str,
        time_col: str,
        id_cols: list[str],
    ) -> DataFrame:
        """Given a dataframe current_df with changes tracked in a table history_table,
        update history_table with a record of the latest changes.

        Parameters
        ----------
        history_table_path : str
            Location of the table containing the history
        current_df : DataFrame
            DataFrame containing the current version of the table.
        id_col : str | list[str]
            One or more columns that uniquely identifies a given row in the table that
            history_df is based on. For example, for cohort_patients this is
            ["report_id", "patient_id", "patient_id_type"].
        time_col_in_current_df : str
            Column containing the time a change was made to current_df
        time_between_updates : pd.Timedelta, optional
            Allowed time between updates, by default pd.Timedelta(1, "d"). Multiple
            updates closer together than time_between_updates will be counted as
            a single update.

        Side Effects
        ------------
        table at history_table_path:
            This table is updated.

        Returns
        -------
        DataFrame
            A dataframe showing the changes made to the history table.
        """

        # Get and store the changes between cohorts recorded in cohort_patients_df
        changelog_df = self.get_grouped_dataframe_changelog(
            current_df,
            group_key=group_key,
            time_col=time_col,
            id_cols=id_cols,
        )

        # If we want to use the changelog to update the history,
        # we need to drop updates that are already recorded,
        # which we do by anti-joining on group_key and update time.
        history_updates_df = changelog_df.join(
            history_df.select([group_key, "change_datetime"]),
            on=[group_key, "change_datetime"],
            how="left_anti",
        )

        # Return
        return history_updates_df.select(id_cols + ["change_type", "change_datetime"])

    def get_history_summary(self, history_df: DataFrame, group_cols: str, time_col: str):

        t_0 = history_df.select(sqlfn.min(time_col)).collect()[0][0]

        return history_df.withColumn(
            "t_0", sqlfn.lit(t_0)
        ).withColumn(
            "timedelta", sqlfn.datediff(time_col, "t_0")
        ).groupby(
            ["timedelta", time_col] + group_cols
        ).count().orderBy(
            ["timedelta"] + group_cols
        )

    def get_grouped_dataframe_changelog(
        self,
        df: pd.DataFrame,
        group_key: str,
        time_col: str,
        id_cols: list[str],
        use_spark: bool = True,
    ):

        # Convert get_dataframe_changelog into a function that takes a single argument.
        # NB: This function cannot include any references to the class object, or it will fail.
        # Also NB: A single argument means no default arguments either.
        def fn_to_apply(df: pd.DataFrame):
            return get_dataframe_changelog(
                df,
                time_col=time_col,
                id_cols=id_cols,
            )

        # Assemble the schema
        id_fields = df.select(id_cols).schema.fields
        other_fields = [
            StructField(self.change_type_col, StringType()),
            StructField(
                self.change_time_col, df.select(time_col).schema.fields[0].dataType
            ),
            StructField("update", IntegerType()),
        ]
        schema = StructType(id_fields + other_fields)

        # When debugging it can be useful to not use spark
        if not use_spark:
            change_df = self.spark.createDataFrame(
                df.toPandas().groupby(group_key).apply(fn_to_apply)
            )
            return self.create_matching_dataframe(change_df, schema)

        return df.groupBy(group_key).applyInPandas(fn_to_apply, schema)

    def get_dataframe_diff(
        self,
        old_df: DataFrame,
        new_df: DataFrame,
        id_cols: list[str],
        time_col_in_new_df: str = None,
        diff_time: str | pd.Timestamp = None,
    ) -> DataFrame | tuple[DataFrame]:
        """Compare a new dataframe with the data in the old dataframe to identify
        rows that were inserted or deleted.

        The diff only tracks the insertion and deletion of rows, not updates
        Regarding tracking exact updates and querying a table at an arbitrary time,
        the best option for that is probably to use delta lake table history.
        While it's only maintained for 7 days by default, we could export from it to
        an archival location. The code in this module can be used to test the solution.

        On timestamps:
        - The new dataframe can contain data from multiple updates if
            it has a time column, but only the most recent change will be added.
        - The timestamp for changes, when not provided, is the time of function call
        - If time_col_in_new_df is provided and diff_time is not then we use the
            the latest time in new_df for the diff_time for deleted rows

        Assumptions:
        - No values in old_df are recorded after any values in new_df or after diff_time
        - In order for a row to be tracked as deleted it must exist in the history
            table but not the new dataframe.

        Parameters
        ----------
        old_df : DataFrame
            Previous version of the dataframe.
        new_df : DataFrame
            Updated version of the dataframe.
        id_col : str | list[str]
            One or more columns that uniquely identifies a given row in the table that
            history_df is based on. For example, for cohort_patients this is
            ["report_id", "patient_id", "patient_id_type"].
        time_col_in_new_df : str, optional
            If provided this is the column containing the time a change was made in
            new_df.
        diff_time : str | pd.Timestamp, optional
            The time at which this operation takes place. Defaults to now.

        Returns
        -------
        DataFrame
            A dataframe containing id_col, a column tracking when a row was inserted
            or deleted ("change_datetime" by default), and a column tracking the type
            of change ("inserted" or "deleted"; "change_type" by default)
        """

        # Return early if given an empty dataframe,
        # allowing both speed and an arbitrary input
        if new_df.count() == 0:
            return

        # Since we only track insertion and deletion, we drop any columns that are
        # not id_col or time_col_in_new_df
        old_df = old_df.select(id_cols)
        selected_cols = id_cols + [time_col_in_new_df]
        new_df = new_df.select(selected_cols)

        # Choose the first time a row shows up
        new_df = new_df.groupby(id_cols).agg(
            sqlfn.min(time_col_in_new_df).alias(time_col_in_new_df)
        )

        # Get the diff time
        if diff_time is None:
            if time_col_in_new_df is None:
                diff_time = pd.Timestamp.now()
            else:
                # if time_col_in_new_df is provided and diff_time is not then we use the maximum of
                # time_col_in_new_df for the diff_time for deleted rows
                diff_time = new_df.select(sqlfn.max(time_col_in_new_df)).collect()[0][0]
        if isinstance(diff_time, str):
            diff_time = pd.Timestamp(diff_time)

        # Set the diff timestamp to diff_time for deletions and,
        # if new_df does not have a time column, insertions
        old_df = old_df.withColumn(self.change_time_col, sqlfn.lit(diff_time))
        if time_col_in_new_df is None:
            new_df = new_df.withColumn(self.change_time_col, sqlfn.lit(diff_time))
        else:
            new_df = new_df.withColumnRenamed(time_col_in_new_df, self.change_time_col)
            # Ensure old_df time type matches new_df time type
            new_df_time_dtype = dict(new_df.dtypes)[self.change_time_col]
            old_df = old_df.withColumn(
                self.change_time_col,
                old_df[self.change_time_col].cast(new_df_time_dtype),
            )

        # Get rows that are being inserted
        inserted_df = new_df.join(old_df, on=id_cols, how="left_anti")
        # Add the change_type column
        inserted_df = inserted_df.withColumn(
            self.change_type_col, sqlfn.lit("inserted")
        )

        # Get rows that are being deleted
        deleted_df = old_df.join(new_df, on=id_cols, how="left_anti")
        # Add the change_type column
        deleted_df = deleted_df.withColumn(self.change_type_col, sqlfn.lit("deleted"))

        # Combine inserted and deleted to get the full update dataframe
        diff_df = inserted_df.union(deleted_df)

        return diff_df

    def create_matching_dataframe(
        self, source_df: pd.DataFrame | DataFrame, target_schema: StructType
    ) -> DataFrame:
        """PySpark's createDataFrame does not validate column order when creating
        spark DataFrames from pandas DataFrames, which can result in schema mismatch.
        The same schema mismatch can occur between spark DataFrames. This function
        ensures that at least the columns match.

        This function does not ensure type matching between spark DataFrames at this
        time, but that would be straightforward enough to implement.

        Parameters
        ----------
        source_df : pd.DataFrame | DataFrame
            pandas or spark DataFrame to reformat
        target_schema : StructType
            spark schema to match

        Returns
        -------
        DataFrame
            source_df reformatted
        """

        # Convert to spark if not yet spark, preserving schema
        columns = [col.name for col in target_schema]
        if not isinstance(source_df, (DataFrame, ConnectDataFrame)):
            df = source_df[columns]
            matched_df = self.spark.createDataFrame(df, schema=target_schema)
        # If already spark, ensure correct columns and order
        # This does *not* ensure correct type, as of right now
        else:
            matched_df = source_df.select(columns)

        return matched_df

    def sanitize_dirname(self, name: str, space_sub: str = "_") -> str:
        """
        Sanitizes a directory name by removing invalid characters
        and replacing spaces with underscores.

        Parameters
        ----------
        name: str
            The original directory name.

        Returns
        -------
        str
            A sanitized directory name.
        """

        # Define a regular expression pattern to match valid characters
        # Here we are allowing alphanumeric characters, underscores, dashes, and periods.
        sanitized_name = re.sub(r"\s+", space_sub, name.lower())
        sanitized_name = re.sub(r"[^\w\-.]", "", sanitized_name)

        # Remove leading or trailing whitespace
        sanitized_name = sanitized_name.strip()

        return sanitized_name


def get_dataframe_changelog(
    df: pd.DataFrame,
    time_col: str,
    id_cols: list[str],
):
    """DataFrame changelog will be used as a UDF with spark,
    so keeping it as a function that's not part of a class is preferred.
    """

    changelog_cols = id_cols + ["change_type", "change_datetime", "update"]

    # Loop through updates
    df_by_time = df.groupby(time_col, sort=True)
    diff_dfs = []
    for i, (t_i, df_i) in enumerate(df_by_time):

        # At the earliest time there's nothing to compare to
        if i == 0:
            inserted = df_i.copy()
            inserted = inserted.rename(columns={time_col: "change_datetime"})
            inserted["change_type"] = "inserted"
            inserted["update"] = i
            diff_dfs.append(inserted[changelog_cols])
            df_prev = df_i
            continue

        # Compare
        diff = df_i.merge(
            df_prev[id_cols],
            on=id_cols,
            how="outer",
            indicator=True,
        )

        # Store deleted
        deleted = diff.query("_merge == 'right_only'").copy()
        deleted["change_datetime"] = t_i
        deleted["change_type"] = "deleted"
        deleted["update"] = i
        diff_dfs.append(deleted[changelog_cols])

        # Store inserted
        inserted = diff.query("_merge == 'left_only'").copy()
        inserted = inserted.rename(columns={time_col: "change_datetime"})
        inserted["change_type"] = "inserted"
        inserted["update"] = i
        diff_dfs.append(inserted[changelog_cols])

        # Update variables tracking previous
        df_prev = df_i

    # Combine
    if len(diff_dfs) == 0:
        return pd.DataFrame()

    # Assemble final product
    diff_df = pd.concat(diff_dfs, ignore_index=True)
    # diff_df["report_id"] = report_id

    return diff_df
