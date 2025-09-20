from dataclasses import dataclass, field

import numpy as np
import tqdm
import pandas as pd
from pyspark.sql.dataframe import DataFrame
from pyspark.sql.connect.dataframe import DataFrame as ConnectDataFrame
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, collect_list, explode, lit, max, when

from .environment import EnvironmentSystem
from .utils import UtilsSystem


class CohortSystem:

    # The combination of these columns uniquely identifies a patient
    id_cols = ["report_id", "patient_id", "patient_id_type"]

    def __init__(
        self,
        environment_sys: EnvironmentSystem = None,
        utils_sys: UtilsSystem = None,
        cohort_patients_path: str = None,
        cohort_patients_history_path: str = None,
    ):
        """TODO: After the code is in place, review names for consistent naming."""

        # Create the dependent objects if not passed
        self.spark = SparkSession.builder.getOrCreate()
        self.environment_sys = (
            environment_sys if environment_sys is not None else EnvironmentSystem()
        )
        self.utils_sys = utils_sys if utils_sys is not None else UtilsSystem()

        # Store the cohort patients path and the cohort patients history path
        if cohort_patients_path is None:
            cohort_patients_path = self.environment_sys.get("cohort_patients_path")
        self.cohort_patients_path = self.environment_sys.get_used_path(
            cohort_patients_path
        )
        if cohort_patients_history_path is None:
            cohort_patients_history_path = self.environment_sys.get(
                "cohort_patients_history_path"
            )
        self.cohort_patients_history_path = self.environment_sys.get_used_path(
            cohort_patients_history_path
        )

    @property
    def cohort_patients_df(self):
        """We make the cohort patients dataframe easily accessible,
        but also always pointing to the catalog location."""
        return self.spark.table(self.cohort_patients_path)

    @property
    def cohort_patients_history_df(self):
        """We make the cohort patients history dataframe easily accessible,
        but also always pointing to the catalog location."""
        return self.spark.table(self.cohort_patients_history_path)

    def load_cohort(self, report_id: str, view_name: str = "cohort") -> DataFrame:

        cohort_df = self.query_cohort_patients(report_id)

        # Get and validate the patient ID type
        patient_id_types = cohort_df.select("patient_id_type").distinct()
        if patient_id_types.count() != 1:
            raise ValueError(
                "Patients in the cohort do not all share the same patient_id_type."
            )
        patient_id_type = patient_id_types.collect()[0][0]
        print(
            f"Loading cohort with size = {cohort_df.count()} and with patient_id_type = {patient_id_type}"
        )

        # Reformat output
        cohort_df = cohort_df.select("patient_id").withColumnRenamed(
            "patient_id", patient_id_type.split(".")[-1]
        )

        if view_name is not None:
            cohort_df.createOrReplaceTempView(view_name)
            print(f"The cohort is saved as a temporary view named '{view_name}'")

        return cohort_df

    def query_cohort_patients(self, report_id: str) -> DataFrame:
        # Get all rows with matching cohort ID
        cohort_df = self.cohort_patients_df.filter(col("report_id") == report_id)

        # Select only the most recent
        update_dts_col = col("meta_updated_datetime")
        most_recent_cohort_update_dts = cohort_df.select(max(update_dts_col)).collect()[
            0
        ][0]
        most_recent_cohort_df = cohort_df.filter(
            update_dts_col == most_recent_cohort_update_dts
        )

        # Check that data was returned
        assert most_recent_cohort_df.count() > 0, f"No patients in cohort {report_id}"

        return most_recent_cohort_df

    def query_cohort_patients_history(
        self,
        report_id: str = None,
        time_observed: str | pd.Timestamp = None,
        drop_deleted: bool = True,
    ) -> DataFrame:

        # Get the full state at that time
        cohort_patients_df_at_time: DataFrame = self.utils_sys.query_history_dataframe(
            history_df=self.cohort_patients_history_df,
            id_cols=self.id_cols,
            time_observed=time_observed,
        )

        # Drop deleted and other cohorts
        if report_id is not None:
            cohort_patients_df_at_time = cohort_patients_df_at_time.filter(
                col("report_id") == report_id
            )
        if drop_deleted:
            cohort_patients_df_at_time = cohort_patients_df_at_time.filter(
                col("change_type") != "deleted"
            )

        return cohort_patients_df_at_time

    def write_empty_cohort_tables(self):

        self.spark.sql(
            f"""
            CREATE TABLE IF NOT EXISTS {self.cohort_patients_path} (
                report_id STRING COMMENT 'ID used to uniquely identify a cohort. Foreign key from research.research_cohort.config.',
                patient_id STRING COMMENT 'ID used to uniquely identify a patient',
                patient_id_type STRING COMMENT 'Source of the patient ID. Format follows [source].[id_name] e.g. clarity.pat_id or nm_bi.ir_id.',
                meta_updated_datetime TIMESTAMP_NTZ COMMENT 'Time last updated. The latest rows are the ones used, when conflicts arise.'
                -- is_recorded BOOLEAN COMMENT 'Whether or not this row is recorded in the cohort_patients_history table.'
            ) COMMENT "This table stores the patients in a given cohort, i.e. the patients associated with a given study. The patients in this table are the patients in a given cohort at present."
            """
        )

        self.spark.sql(
            f"""
            CREATE TABLE IF NOT EXISTS {self.cohort_patients_history_path} (
                report_id STRING COMMENT 'ID used to uniquely identify a cohort. Foreign key from research.research_cohort.config.',
                patient_id STRING COMMENT 'ID used to uniquely identify a patient',
                patient_id_type STRING COMMENT 'Source of the patient ID. Format follows [source].[id_name] e.g. clarity.pat_id or nm_bi.ir_id.',
                change_type STRING COMMENT 'Type of change: inserted or deleted.',
                change_datetime TIMESTAMP_NTZ COMMENT 'Time the change was made.'
            ) COMMENT "This table stores the history of changes to cohort_patients. Only the insertion and deletion of patients is tracked, not any properties related to the patients."
            """
        )

    def append_to_table(self, df: DataFrame | pd.DataFrame, path: str):
        """While there's an option to generate an ID column with spark, we opt not to do that
        because we want to insure consistency between the main and history tables when writing them.
        """

        df_spark = self.utils_sys.create_matching_dataframe(
            df, self.spark.table(path).schema
        )

        # Then append
        df_spark.write.mode("append").saveAsTable(path)

    def get_donotcontact_list(self) -> DataFrame:

        donotcontact = self.spark.sql(
            """
            SELECT distinct pat.pat_id as patient_id
            FROM edr.clarity.PATIENT pat
            INNER JOIN edr.clarity.PATIENT_FYI_FLAGS fyi 
                ON fyi.PATIENT_ID = pat.PAT_ID
            where fyi.PAT_FLAG_TYPE_C = 2020
            """
        )

        # for now return spark df
        return donotcontact

    def filter_cohort_on_donotcontact_list(self, df: DataFrame) -> DataFrame:
        """df format: one column, which is pat_id (clarity patient ID).

        TODO: Apply filter *only* for recruitment.
        """

        donotcontact = self.get_donotcontact_list()
        filtered_on_donotcontactlist_df = df.join(
            donotcontact, on="patient_id", how="left_anti"
        )

        return filtered_on_donotcontactlist_df

    def validate_input_cohort(
        self,
        cohort_df: DataFrame,
        view_name: str,
        patient_id_type: str,
        change_dts: str | pd.Timestamp,
    ) -> tuple[DataFrame, str, pd.Timestamp]:

        # Get the input data
        if cohort_df is None:
            if not self.spark.catalog.tableExists(view_name):
                raise ValueError(
                    f"Saving a cohort requires either a data frame or a view at the specified view_name (currently {view_name})."
                )
            else:
                cohort_df = self.spark.table(view_name)

        # Check the cohort dataframe is indeed a spark dataframe
        if not isinstance(cohort_df, (DataFrame, ConnectDataFrame)):
            raise TypeError("Cohort dataframe must be a spark dataframe.")

        # Check input data structure
        if len(cohort_df.columns) != 1:
            raise ValueError(
                "Cohort dataframe must be a single column containing the patient ids."
            )
        if cohort_df.count() == 0:
            raise ValueError("Number of patients in the provided cohort is 0.")

        # Get and validate the patient_id_type
        cohort_df_column_name = cohort_df.schema[0].name
        if patient_id_type is None:
            patient_id_type = cohort_df_column_name
        if patient_id_type not in VALID_IDS:
            try:
                patient_id_type = ID_MAPPING[patient_id_type]
            except KeyError:
                raise ValueError(
                    f"Unrecognized patient_id_type, {patient_id_type}. Valid options are {VALID_IDS}"
                )

        # Rename the cohort dataframe, now that we've extracted the patient_id type
        cohort_df = cohort_df.withColumnRenamed(cohort_df_column_name, "patient_id")

        # Ensure there are not duplicate IDs
        n_unique = cohort_df.select("patient_id").distinct().count()
        if n_unique != cohort_df.count():
            raise ValueError(
                "Duplicate patient IDs were passed in. The cohort should have no duplicate patient IDs."
            )

        # Ensure the timestamp is the right format
        if isinstance(change_dts, str):
            change_dts = pd.to_datetime(change_dts)

        return cohort_df, patient_id_type, change_dts

    def assemble_cohort_df_for_write(
        self,
        report_id: str,
        cohort_df: DataFrame,
        patient_id_type: str,
        change_dts: pd.Timestamp,
    ):

        # Make a dataframe with the same columns as cohort_patients
        cohort_df = (
            cohort_df.withColumn("report_id", lit(report_id))
            .withColumn("patient_id_type", lit(patient_id_type))
            .withColumn("meta_updated_datetime", lit(change_dts).cast("timestamp_ntz"))
            .withColumn("is_recorded", lit(False))
        )

        return cohort_df

    def write_cohort(
        self,
        report_id: str,
        cohort_df: DataFrame = None,
        view_name: str = "cohort",
        patient_id_type: str = None,
        change_dts: str | pd.Timestamp = "today",
    ):
        """Note: Before writing we filter on the do-not-contact list."""

        # Validate input data
        cohort_df, patient_id_type, change_dts = self.validate_input_cohort(
            cohort_df=cohort_df,
            view_name=view_name,
            patient_id_type=patient_id_type,
            change_dts=change_dts,
        )

        # Filter on do-not-contact
        cohort_df = self.filter_cohort_on_donotcontact_list(cohort_df)

        cohort_df = self.assemble_cohort_df_for_write(
            report_id=report_id,
            cohort_df=cohort_df,
            patient_id_type=patient_id_type,
            change_dts=change_dts,
        )

        # Check if the tables exist, and if not then create them.
        self.write_empty_cohort_tables()

        self.append_to_table(cohort_df, self.cohort_patients_path)

    def update_cohort_patients_history(self) -> tuple[DataFrame]:

        # Update the history table
        history_updates_df = self.utils_sys.get_history_updates(
            self.cohort_patients_history_df,
            self.cohort_patients_df,
            group_key="report_id",
            time_col="meta_updated_datetime",
            id_cols=self.id_cols,
        )

        return history_updates_df

    def clean_cohort_patients(self) -> DataFrame:

        # Basic validation that the cohorts were stored successfully.
        # For this we just check if a row with the same id_cols exists in the history.
        # This is not a comprehensive check.
        n_missing = self.cohort_patients_df.select(self.id_cols).distinct().join(
            self.cohort_patients_history_df.select(self.id_cols).distinct(),
            on=self.id_cols,
            how="left_anti"
        ).count()
        if n_missing > 0:
            raise AssertionError(
                f"{n_missing} (report_id, patient_id, patient_id_type) combinations found in cohort_patients "
                "but not in cohort_patients_history. Exiting without modifying cohort_patients."
            )

        # Filter to select only rows that have the timestamp equal to the most recent timestamp
        most_recent_df = self.cohort_patients_df.groupBy("report_id").agg(max("meta_updated_datetime").alias("most_recent_datetime"))
        updated_cohort_patients_df = self.cohort_patients_df.join(most_recent_df, on="report_id").filter("meta_updated_datetime = most_recent_datetime")

        # Chose correct column names and order
        updated_cohort_patients_df = updated_cohort_patients_df.select(
            self.cohort_patients_df.schema.fieldNames()
        )

        return updated_cohort_patients_df


class ArrayCohortSystem(CohortSystem):

    def query_cohort_patients(self, report_id: int) -> DataFrame:
        # Get the still-array-formatted patients list
        cohort_df = super().query_cohort_patients(report_id)

        # TODO: Fix this comment
        # Explode and rename for consistency with the base class
        # self.id_col = "patient_id", and super().id_col = "patient_id"
        cohort_long_df = cohort_df.withColumn("patient_id", explode(col("patient_id")))

        return cohort_long_df

    def query_cohort_patients_history(
        self, report_id, dts: pd.Timestamp = "today"
    ) -> DataFrame:

        raise NotImplementedError(
            "Tracking history is not yet implemented for array-formatted cohorts."
        )

    def write_empty_cohort_tables(self):
        # Main table
        self.spark.sql(
            f"""
            CREATE TABLE IF NOT EXISTS {self.cohort_patients_path} (
                report_id STRING COMMENT 'ID used to uniquely identify a cohort. Foreign key from research.research_cohort.config.',
                patient_id ARRAY<STRING> COMMENT 'ID used to uniquely identify a patient. An array with one ID per patient.',
                patient_id_type STRING COMMENT 'Source of the patient ID. Format follows [source].[id_name] e.g. clarity.pat_id or nm_bi.ir_id. All patient_id values must be from the same source.',
                meta_updated_datetime TIMESTAMP_NTZ COMMENT 'Time last updated. The latest rows are the ones used, when conflicts arise.'
            ) COMMENT "This table stores the patients in a given cohort, i.e. the patients associated with a given study. The patients in this table are the patients in a given cohort at present."
            """
        )

    def assemble_cohort_df_for_write(
        self,
        report_id: str,
        cohort_df: DataFrame,
        patient_id_type: str,
        change_dts: pd.Timestamp,
    ):

        # Convert to array format.
        # Grouping by + collect_list is the reverse of explode.
        # We need a separate column to group by, so we add the report_id at this time
        cohort_df = (
            cohort_df.groupBy(lit(report_id).alias("report_id"))
            .agg(collect_list("patient_id").alias("patient_id"))
            .withColumn("patient_id_type", lit(patient_id_type))
            .withColumn("meta_updated_datetime", lit(change_dts).cast("timestamp_ntz"))
        )

        return cohort_df

    def archive_cohort_patients(self):

        raise NotImplementedError(
            "Tracking history is not yet implemented for array-formatted cohorts."
        )


@dataclass
class CohortMocker:

    # System to test
    cohort_sys: CohortSystem

    spark: SparkSession = field(default_factory=SparkSession.builder.getOrCreate)

    # Context parameters
    n_all_patients: int = int(1e7) - 10
    n_all_cohorts: int = int(1e3) - 10
    rng: np.random.Generator = field(default_factory=np.random.default_rng)

    # Mock data parameters
    n_cohorts: int = 10
    n_patients: int = 1000
    # The time that the mock data roughly centers on. Defaults to now.
    time_anchor: pd.Timestamp = field(default_factory=pd.Timestamp.now)
    n_updates_prior: int = 7
    n_updates_after: int = 2
    # Time between updates to cohorts
    dt_updates: pd.Timedelta = pd.Timedelta(1, "d")
    # When does updating and archiving occur relative to the anchor time?
    # Default is 1 hour before and after respectively
    dt_anchor_to_update: pd.Timedelta = -pd.Timedelta(1, "h")
    dt_anchor_to_archive: pd.Timedelta = pd.Timedelta(1, "h")

    def __post_init__(self):

        # Times when the cohorts are updated and archived
        self.anchor_datetimes = pd.date_range(
            self.time_anchor - self.n_updates_prior * self.dt_updates,
            self.time_anchor + self.n_updates_after * self.dt_updates,
            freq=self.dt_updates,
        )
        self.update_datetimes = self.anchor_datetimes + self.dt_anchor_to_update
        self.archive_datetimes = self.anchor_datetimes + self.dt_anchor_to_archive

        # Larger context
        get_possible_ids = lambda n: [str(x).zfill(len(str(n))) for x in range(n)]
        self.all_possible_report_ids = get_possible_ids(self.n_all_cohorts)
        self.all_possible_pat_ids = get_possible_ids(self.n_all_patients)

        # Get cohort metadata
        self.report_ids = self.rng.choice(
            self.all_possible_report_ids, size=self.n_cohorts, replace=False
        )

        # Create mock data
        # Random patients associated with a random cohort, inserted at a random time
        base_changelog = pd.DataFrame(
            {
                "report_id": self.rng.choice(self.report_ids, self.n_patients),
                "patient_id": self.rng.choice(self.all_possible_pat_ids, self.n_patients),
                "patient_id_type": "mock_data.mock_id",
                "change_datetime":  self.rng.choice(self.update_datetimes, self.n_patients),
                "change_type": "inserted",
            }
        ).drop_duplicates(subset=["report_id", "patient_id"])
        self.cohort_patients_ids = base_changelog[self.cohort_sys.id_cols]

        # Have patients leave and join until the end of the time available
        changelog_dfs = [base_changelog]
        i = 0
        changelog_i = base_changelog.copy()
        while changelog_i.size > 0:

            # Offset the change time, dropping those changed beyond the end
            changelog_i["change_datetime"] += self.rng.integers(1, self.anchor_datetimes.size, len(changelog_i)) * self.dt_updates
            changelog_i = changelog_i.loc[changelog_i["change_datetime"] <= self.update_datetimes[-1]]

            # Alternate between deleting and inserting
            changelog_i["change_type"] = ["deleted", "inserted"][i % 2]

            # Store a copy
            changelog_dfs.append(changelog_i.copy())

            i += 1

        # Store
        self.omni_cohort_patients_history = self.spark.createDataFrame(
            pd.concat(changelog_dfs, ignore_index=True)
        ).withColumn(
            "change_datetime",
            col("change_datetime").cast("timestamp_ntz"),
        )

        # Set the observed time to the anchor time by default
        self.set_time_observed(self.anchor_datetimes[self.n_updates_prior])

        # # Make the "omniscient" mock data
        # # Loop through and create
        # print("Generating mock data...")
        # dfs = [
        #     self.create_random_cohort(self.report_ids[i], cohort_size)
        #     for i, cohort_size in enumerate(tqdm.tqdm(cohort_sizes))
        # ]
        # self.omni_cohort_patients = pd.concat(dfs, ignore_index=True)

        # # Make an omniscient history too
        # inserts = self.omni_cohort_patients.rename(
        #     columns={"meta_inserted_datetime": "change_datetime"}
        # ).drop(columns=["meta_deleted_datetime"])
        # inserts["change_type"] = "inserted"
        # deletes = self.omni_cohort_patients.rename(
        #     columns={"meta_deleted_datetime": "change_datetime"}
        # ).drop(columns=["meta_inserted_datetime"])
        # deletes["change_type"] = "deleted"       
        # self.omni_cohort_patients_history = self.spark.createDataFrame(
        #     pd.concat([inserts, deletes], ignore_index=True)
        # ).withColumn(
        #     "change_datetime",
        #     col("change_datetime").cast("timestamp_ntz")
        # )

        # # We find the rows that are part of the final update, because these are kept around longer
        # self.final_updates = self.omni_cohort_patients.groupby("report_id")["meta_deleted_datetime"].max().reset_index()
        # self.final_updates["is_final_update"] = True
        # # Join to rows that are part of the final update for a given report_id
        # omni_cohort_patients_temp = self.omni_cohort_patients.merge(
        #     self.final_updates,
        #     on=["report_id", "meta_deleted_datetime"],
        #     how="left",
        # )
        # self.omni_cohort_patients["is_in_final_update"] = omni_cohort_patients_temp["is_final_update"].notna()


    def create_random_cohort(self, report_id: str, cohort_size: int):
        """While not used for bulk creation because it's slow and doesn't mock up reinsertion,
        this is still useful for some test cases.
        """

        # Patient IDs for the cohort
        pat_ids = self.rng.choice(
            self.all_possible_pat_ids, size=cohort_size, replace=False
        )

        # Overall dates during which the cohort is updated
        established_dts, halted_dts = np.sort(
            self.rng.choice(self.update_datetimes, size=2, replace=False)
        )
        update_dates = pd.date_range(established_dts, halted_dts, freq="D")

        # For dates we pick two random dates within the interval,
        # and they become the insert_dts and delete_dts in order.
        unsorted_dates = [
            self.rng.choice(update_dates, size=2, replace=False)
            for _ in range(cohort_size)
        ]
        insert_dts_i, delete_dts_i = np.sort(unsorted_dates, axis=1).T

        df = pd.DataFrame(
            {
                "report_id": report_id,
                "patient_id": pat_ids,
                "patient_id_type": "mock_data.mock_id",
                "meta_inserted_datetime": insert_dts_i,
                "meta_deleted_datetime": delete_dts_i,
            }
        )

        return df

    def set_time_observed(
        self,
        time_observed: pd.Timestamp,
    ):
        self.time_observed = time_observed

        # Update times relative to time_observed
        self.time_last_update = np.max(
            self.update_datetimes[self.update_datetimes <= time_observed]
        )
        self.time_next_update = self.time_last_update + self.dt_updates

        # Archive times relative to time_observed
        self.time_last_archive = np.max(
            self.archive_datetimes[self.archive_datetimes <= time_observed]
        )
        self.time_next_archive = self.time_last_archive + self.dt_updates

        # Ensure the empty dataframes are available
        self.cohort_sys.write_empty_cohort_tables()
        
        # If there's no data yet set up empty dataframes and return
        if pd.isna(self.time_last_update):
            self.cohort_patients_df = self.spark.createDataFrame([], self.cohort_sys.cohort_patients_df.schema)
            self.cohort_patients_history_df = self.spark.createDataFrame([], self.cohort_sys.cohort_patients_history_df.schema)
            return

        # Get the cohort_patients dataframe at this time.
        cohort_patients = self.cohort_sys.utils_sys.query_history_dataframe(
            self.omni_cohort_patients_history,
            id_cols = self.cohort_sys.id_cols,
            time_observed = time_observed,
        )
        cohort_patients = cohort_patients.filter(
            "change_type = 'inserted'"
        )
        cohort_patients = cohort_patients.withColumn(
            "meta_updated_datetime",
            lit(self.time_last_update).cast("timestamp_ntz"),
        )

        # Include data from the last update that hasn't been deleted from cohort_patients
        if not pd.isna(self.time_last_archive) and (self.time_last_update > self.time_last_archive):
            state_in_history = self.cohort_sys.utils_sys.query_history_dataframe(
                self.omni_cohort_patients_history,
                id_cols = self.cohort_sys.id_cols,
                time_observed = time_observed - self.dt_updates,
            )
            state_in_history = state_in_history.filter(
                "change_type = 'inserted'"
            )
            state_in_history = state_in_history.withColumn(
                "meta_updated_datetime",
                lit(self.time_last_update - self.dt_updates).cast("timestamp_ntz"),
            )
            cohort_patients = state_in_history.union(cohort_patients)

        cohort_patients = cohort_patients.select(self.cohort_sys.id_cols + ["meta_updated_datetime"])
        self.cohort_patients_df = self.cohort_sys.utils_sys.create_matching_dataframe(
            cohort_patients, self.cohort_sys.cohort_patients_df.schema
        )

        # If no data is archived yet, set up empty dataframes and return
        if pd.isna(self.time_last_archive):
            self.cohort_patients_history_df = self.spark.createDataFrame([], self.cohort_sys.cohort_patients_history_df.schema)
            return

        # Get the cohort_patients_history dataframe at this time
        cohort_patients_history = self.omni_cohort_patients_history.filter(
            col("change_datetime") <= self.time_last_archive
        )
        self.cohort_patients_history_df = (
            self.cohort_sys.utils_sys.create_matching_dataframe(
                cohort_patients_history,
                self.cohort_sys.cohort_patients_history_df.schema,
            )
        )

    def clear_data(self):

        self.spark.sql(f"DROP TABLE IF EXISTS {self.cohort_sys.cohort_patients_path}")
        self.spark.sql(
            f"DROP TABLE IF EXISTS {self.cohort_sys.cohort_patients_history_path}"
        )
        self.cohort_sys.write_empty_cohort_tables()

    def write_mock_data(self):

        self.clear_data()
        self.cohort_sys.append_to_table(
            self.cohort_patients_df, self.cohort_sys.cohort_patients_path
        )
        self.cohort_sys.append_to_table(
            self.cohort_patients_history_df,
            self.cohort_sys.cohort_patients_history_path,
        )


ID_MAPPING = {
    "ir_id": "nm_bi.ir_id",
    "pat_id": "clarity.pat_id",
    "mock_id": "mock_data.mock_id",
}
VALID_IDS = pd.unique(list(ID_MAPPING.values()))
