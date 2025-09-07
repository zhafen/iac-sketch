import os
import re
import warnings

import IPython
import pandas as pd
from pyspark.errors import PySparkException
from pyspark.sql import SparkSession
from pyspark.sql.functions import lit

class EnvironmentSystem:
    """Note to developers: we might be able to separate out the get logic into a separate system,
    which we can then use to get values from arbitrary classes.
    """

    params_view_name: str
    params_view_path: str

    def __init__(self, report_id: str = None, **provided_params):
        """Throughout we refer to a "parameters view".

        TODO: Currently everything has a "report_id", even when ra_lib is not being used for a report.
        We probably want to use some sort of "ra_lib instance id" instead. But less wordy.

        TODO: Currently the parameters view is only used for ensuring our tests are using test mode.
        It's not clear this is worth the added complexity. Evaluate.

        Parameters
        ----------
        report_id : str
            This ID is defined even when we're not
        """

        # Get essential attributes
        self.spark = SparkSession.builder.getOrCreate()
        self.dbutils = IPython.get_ipython().user_ns["dbutils"]
        if report_id is not None:
            self.report_id = report_id
        else:
            self.report_id = self.get("report_id")
        self.params_view_name = self.get("params_view_name")
        global_temp_database = self.spark.conf.get("spark.sql.globalTempDatabase")
        self.params_view_path = f"{global_temp_database}.{self.params_view_name}"

        # Set up the parameters view if it does not yet exist
        if not self.spark.catalog.tableExists(self.params_view_path):
            params_df = self.spark.createDataFrame(
                [{"params_view_name": self.params_view_name}]
            )
            params_df.createOrReplaceGlobalTempView(self.params_view_name)

        # For each provided parameter we put it into the parameters view
        for key, value in provided_params.items():
            self.set(key, value)
        
        # Finish up by providing easy access to variables we use a lot
        self.workspace = self.get("workspace")
        self.context = self.get("context")

    def get(self, key, *args, **kwargs):

        # If there's a getter method, we always prefer that.
        # This ensures we're getting the most recent version
        # of the parameter.
        if hasattr(self, f"get_{key}"):
            getter_method = getattr(self, f"get_{key}")
            return getter_method(*args, **kwargs)
        
        # We next check if it's a saved parameter
        # By doing this before looking in CONTEXT_VARS
        # we enable users to override parameters that are in
        # CONTEXT_VARS
        saved_params_exist = hasattr(
            self, "params_view_path"
        ) and self.spark.catalog.tableExists(self.params_view_path)
        if saved_params_exist:
            params = self.spark.table(self.params_view_path)
            if key in params.columns:
                return params.select(key).collect()[0][0]

        # If the variable is set in CONTEXT_VARS, then we use that.
        if key in CONTEXT_VARS:
            if (len(args) != 0) or (len(kwargs) != 0):
                raise ValueError(f"Cannot pass in arguments for parameter {key}")
            contexts_value = CONTEXT_VARS[key]
            # When the value changes depending on context,
            # we get the appropriaate value
            if isinstance(contexts_value, dict):
                return contexts_value.get(self.context, None)
            else:
                return contexts_value

        # Return None if everything failed
        self.warn(f'Key "{key}" not found. Returning "None"')
        return

    def set(self, key, value):

        if value is None:
            raise ValueError(
                f"Tried to set the parameter {key} to value, but value is None, which is not allowed."
            )

        # Load the table, override, and rewrite
        spark_value = lit(value)
        params_df = self.spark.table(self.params_view_path)
        params_df = params_df.withColumn(key, spark_value)
        params_df.createOrReplaceGlobalTempView(self.params_view_name)

    def chdir_to_nbdir(self):
        """When run inside a notebook, this changes the working directory to that of the notebook.
        This is the default for Databricks 14+, and is therefore not necessary in those environments.
        """

        os.chdir(f"/Workspace/{self.get('notebook_dirname')}")

    def remove_test_tables(
        self,
        schemas: str | list[str],
    ):
        # For compatilbity with expected format
        if isinstance(schemas, str):
            schemas = [schemas,]

        # Get actual locations (due to override schemas) and choose distinct
        # so we don't run more than we need to.
        schemas = pd.unique([self.get("used_path", schema) for schema in schemas])
        
        for schema in schemas:
            test_prefix = self.get('test_prefix')
            schema = self.get("used_path", schema)
            print(f"Removing tables like '{test_prefix}*' in {schema}")
            try:
                tables_df = self.spark.sql(f"SHOW TABLES IN {schema} LIKE '{test_prefix}*'")
            except PySparkException as ex:
                if ex.getErrorClass() != 'NO_SUCH_CATALOG_EXCEPTION':
                    raise ex
                print(f"    Schema not found.")
                continue

            if tables_df.count() == 0:
                print(f"    No test tables found.")

            try:
                for row in tables_df.select('tableName').collect():
                    table_name = row[0]
                    self.spark.sql(f"DROP TABLE {schema}.{table_name}")
                    print(f"    Removed {table_name}")
            except PySparkException as ex:
                if ex.getErrorClass() != 'UNAUTHORIZED_ACCESS':
                    raise ex
                print(f"    {ex.getErrorClass()}: Cannot drop tables in {schema}")

    @property
    def warn(self):
        """The default warnings.warn function is noisy. While this isn't a major deal,
        we really do want to minimize the amount of possibly confusing text.
        """

        def custom_formatwarning(msg, category, filename, lineno, line=None):
            return f"{category.__name__}: {msg} (Warning location is {filename}:{lineno})\n"

        warnings.formatwarning = custom_formatwarning
        return warnings.warn

    ###################################################################################
    # Getter methods
    ###################################################################################

    def get_used_path(self, path: str) -> str:
        """Wrapping table paths in this function ensures that when in dev
        the table is piped to a location we can write to. We also prepend the table
        name with a label when in test mode.

        Parameters
        ----------
        path : str
            The path to the table in dev or stg.
        dev_schema : str, optional
            The schema the table should be at in dev, by
            default "sandbox.scratch_research"

        Returns
        -------
        str
            The table path, given the environment.
        """

        split_path = path.split(".")

        # Get the schema and tablename
        override_schema = self.get("override_schema")
        if override_schema is not None:
            schema = override_schema
            # The tablename will be the full path of what it would be
            table = "_".join(split_path)
        else:
            schema = ".".join(split_path[:2])
            table = split_path[-1]

        # If the input path is a database/catalog
        if len(split_path) == 1:
            return schema.split(".")[0]
        # If the input path is a schema
        if len(split_path) == 2:
            return schema

        if self.get("test_mode"):
            table = self.get("test_prefix") + table

        return f"{schema}.{table}"

    def get_context(self) -> str:
        return CONTEXTS[(self.get("workspace"), self.get("user_category"))]

    def get_workspace(self) -> str:
        return WORKSPACES[self.spark.conf.get("spark.databricks.workspaceUrl")]

    def get_user_category(self) -> str:
        return "user" if "@nm.org" in self.get("username") else "service"

    def get_user_dir(self) -> str:
        return f"/Workspace/Users/{self.get('username')}"

    def get_username(self) -> str:
        return self.get("notebook_context").userName().get()
    
    def get_params_view_name(self) -> str:

        report_id = self.get("report_id")

        # Sanitize the config id to be a possible sql table name
        table_name_base = re.sub(r'[^\w]', '_', report_id)
        return f"{table_name_base}_params"

    def get_report_id(self, path: str = None) -> str:
        """Parse the notebook path to get identifying information.
        Only having the ID in the notebook directory path prevents having mismatched IDs.

        Returns
        -------
        report_id : str
            The id of the report, as listed in `research_dm.research_cohort.config`. This is typically the id of the AzDO ticket.
        """

        # If the report_id was already set, use that.
        if hasattr(self, "report_id"):
            return self.report_id
        
        if path is None:
            path = self.get("notebook_path")

        # The config ID for reports is specifically formatted as described in the docstring for this function.
        if self.get("used_for_report", path=path):
            dir_path = os.path.dirname(path)
            base_dirname = os.path.basename(dir_path).split("_")[0]
            # Check if the parent directory is like "STU00000001_my-irb-label/report001_my-specific-report-label"
            # i.e. if it's in a properly-namned subdir.
            try:
                assert base_dirname[:6] == "report"
                report_rank = base_dirname[6:]
                base_report_id = os.path.basename(os.path.dirname(dir_path)).split("_")[0]
                return f"{base_report_id}.{report_rank}"
            except (ValueError, AssertionError) as e:
                return base_dirname
        
        # Otherwise the path becomes the ID.
        return path
    
    def get_used_for_report(self, path: str=None) -> bool:
        if path is None:
            path = self.get("notebook_path")
            
        return "reports" in path

    def get_notebook_dirname(self) -> str:
        """Get the name of the notebook directory itself, without any other path information."""

        notebook_path = self.get("notebook_path")
        notebook_dir = os.path.dirname(notebook_path)
        return os.path.basename(notebook_dir)

    def get_notebook_path(self) -> str:
        """When run inside a notebook, this returns the path of the notebook."""
        return self.get("notebook_context").notebookPath().get()

    def get_notebook_context(self) -> str:
        return self.dbutils.notebook.entry_point.getDbutils().notebook().getContext()
    
    def get_secret(
        self,
        secret_key: str,
    ) -> str:

        # Get the specific names for the environment at hand
        scope = self.get("secrets_scope")
        secret_key = self.get(secret_key)

        return self.dbutils.secrets.get(scope, secret_key)


# The workspaces associated with a given workspace url.
WORKSPACES = {
    "adb-2547276306587450.10.azuredatabricks.net": "dev",
    "adb-6223138531581977.17.azuredatabricks.net": "stg",
    "adb-7355274287898061.1.azuredatabricks.net": "prd",
}
# The context is the combination of workspace and type of user.
CONTEXTS = {
    ("dev", "user"): "dev",
    ("stg", "user"): "interactive-stg",
    ("stg", "service"): "stg",
    ("prd", "user"): "interactive-prd",
    ("prd", "service"): "prd",
}

# Workspace-dependent variables
CONTEXT_VARS = {
    "reports_config_path": "research_dm.research_cohort.reports_config",
    "cohort_patients_path": "research_dm.research_cohort.cohort_patients",
    "cohort_patients_history_path": "research_dm.research_cohort.cohort_patients_history",
    "reports_schema": "research_dm.reports",
    "override_schema": {
        "dev": "sandbox.research",
        "interactive-stg": "stg_scratchpad.research",
    },
    "onprem_enabled": {
        "dev": False,
        "interactive-stg": True,
        "stg": True,
        "interactive-prd": True,
        "prd": True,
    },
    "write_enabled": {
        "dev": True,
        "interactive-stg": True,
        "stg": True,
        "interactive-prd": False,
        "prd": True,
    },
    "secrets_scope": {
        "dev": "nma2-research-dev-kv1",
        "interactive-stg": "nma2-research-stg-kv1",
        "stg": "nma2-research-stg-kv1",
        "interactive-prd": "nma2-research-prd-kv1",
        "prd": "nma2-research-prd-kv1",
    },
    "azure_devops_pat_secret_key": "azdo-read-only-pat",
    "7pace_api_key": "7pace-api-key",
    "onprem_service_acct_secret_key": "DFT01-AD-SA-P-RDB-Operating-System-NMWindowsDomainServiceAccounts-NM-ResearchDataAccSVC",
    "onprem_service_acct_user": "nm\ResearchDataAccSVC",
    "onprem_server": {
        "interactive-stg": "edw00td02wv.corp.nm.org\edwids2",
        "stg": "edw00td02wv.corp.nm.org\edwids2",
        "interactive-prd": "edw00pd05wva.corp.nm.org\edwids1",
        "prd": "edw00pd05wva.corp.nm.org\edwids1",
    },
    "onprem_timeout": 0, # 0 means no timeout
    "test_mode": False,
    "test_prefix": "temp_",
}
