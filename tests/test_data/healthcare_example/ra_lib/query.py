import json

import pandas as pd
import pymssql
from pyspark.sql.dataframe import DataFrame
from pyspark.sql.connect.dataframe import DataFrame as ConnectDataFrame
from pyspark.sql import SparkSession
import sqlalchemy

from .environment import EnvironmentSystem


class OnPremQuerySystem:
    """Class for querying on-prem data.

    Note for developers: This class had POC functionality to filter on-prem data based on cloud ids.
    That was done using sqlalchemy parameters, e.g.
    `connection.execute(sqlalchemy.text("SELECT * FROM my_table WHERE my_table.id in :ids"), {"ids": ids})`
    That functionality has been removed until we have a use case.
    """

    def __init__(
        self,
        environment_sys: EnvironmentSystem = None,
    ):

        # Create the dependent objects if not passed
        self.spark = SparkSession.builder.getOrCreate()
        self.environment_sys = (
            environment_sys
            if environment_sys is not None
            else EnvironmentSystem()
        )

    def query(
        self,
        sql_query: str,
        view_name: str = None,
        connection: sqlalchemy.engine.base.Connection = None,
        output_as: str = None,
        execute_kwargs: dict = {},
    ) -> DataFrame:
        """Main function for querying data."""

        # Automatically include cohort_patient_ids, if it's in the query
        # TODO: Currently this is used by doing e.g. "WHERE pat_id IN :cohort_patient_ids",
        # but it's more efficient to create a table, probably
        if ":cohort_patient_ids" in sql_query:
            cohort_patient_ids = list(
                self.spark.table("cohort").toPandas().values.flatten()
            )
            execute_kwargs.update(
                {"parameters": {"cohort_patient_ids": cohort_patient_ids}}
            )

        # The query itself
        if connection is not None:
            # By default, if we're preserving the connection we don't return the
            # dataframe, so that we don't don't return intermediate results
            output_as = output_as if output_as is not None else "cursor"
            result = self.query_from_connection(
                sql_query,
                view_name,
                connection,
                output_as=output_as,
                execute_kwargs=execute_kwargs,
            )
        else:
            with self.get_open_connection() as connection:
                # For an independent query it's typically more useful to return
                # a dataframe.
                output_as = output_as if output_as is not None else "spark.DataFrame"
                result = self.query_from_connection(
                    sql_query,
                    view_name,
                    connection,
                    output_as=output_as,
                    execute_kwargs=execute_kwargs,
                )

        return result

    
    @property
    def conn(self):

        if not hasattr(self, "_conn"):
            # Get or create a connection to the database
            server = self.environment_sys.get("onprem_server")
            secret = self.environment_sys.get("secret", "onprem_service_acct_secret_key")
            # Sometimes the password is part of a json, sometimes it's not
            try:
                password = json.loads(secret)["password"]
            except json.JSONDecodeError:
                password = secret
            self._conn = Connection(
                server=server,
                user=self.environment_sys.get("onprem_service_acct_user"),
                password=password,
                database="NM_BI",
                timeout=self.environment_sys.get("onprem_timeout")
            )
        return self._conn
    
    def refresh_connection(self):
        """Clears out the _conn attribute so it can be recreated, potentially with updated environment
        parameters."""
        if hasattr(self, "_conn"):
            if hasattr(self._conn, "close"):
                self._conn.close()
            del self._conn

    def get_open_connection(self) -> sqlalchemy.engine.base.Connection:

        return self.conn.engine.connect()

    def query_from_connection(
        self,
        sql_query: str,
        view_name: str,
        connection: sqlalchemy.engine.base.Connection,
        output_as: str = "spark.DataFrame",
        execute_kwargs: dict = {},
    ):

        result = connection.execute(sqlalchemy.text(sql_query), **execute_kwargs)

        return self.convert_cursor(result, output_as, view_name)

    def convert_cursor(
        self,
        cursor: sqlalchemy.engine.CursorResult,
        output_as: str,
        view_name: str = None,
    ):

        # If we're outputting as a view, then that overrides the "output_as" argument
        if view_name is not None:
            output_as = "view"

        output_formats = ["cursor", "pandas.DataFrame", "spark.DataFrame", "view"]
        if output_as not in output_formats:
            raise ValueError(
                f"Unrecognized value of argument output_as, '{output_as}'. Valid options are {output_formats}"
            )

        # Announce the output_as format.
        print(f"Outputting the on-prem query result as a {output_as}")

        if output_as == "cursor":
            return cursor

        result_pdf = pd.DataFrame(cursor.fetchall())
        if output_as == "pandas.DataFrame":
            return result_pdf

        result_sdf = self.spark.createDataFrame(result_pdf)
        if output_as == "spark.DataFrame":
            return result_sdf

        result_sdf.createOrReplaceTempView(view_name)

        return


class Connection:

    def __init__(
        self,
        server: str,
        user: str,
        password: str,
        database: str,
        timeout: str = {},
    ):

        # On-prem credentials
        self.server = server
        self.user = user
        self.password = password
        self.database = database
        self.timeout = timeout

        self.establish_connection()

    def establish_connection(self):
        connection_string = rf"mssql+pymssql://{self.user}:{self.password}@{self.server}/{self.database}"
        self.engine = sqlalchemy.create_engine(connection_string, connect_args={"timeout": self.timeout})


class PyMSSQLConnection(Connection):
    def establish_connection(self):
        self.engine = pymssql.connect(
            server=self.server,
            user=self.user,
            password=self.password,
            database=self.database,
            timeout=self.timeout,
        )
