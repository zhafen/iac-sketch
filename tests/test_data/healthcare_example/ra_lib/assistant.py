import base64
import glob
import os
import shutil
import time

from databricks.sdk import WorkspaceClient
from databricks.sdk.service import workspace
import networkx as nx
import numpy as np
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.dataframe import DataFrame
from pyspark.sql.functions import lit
import sqlalchemy

from . import environment
from . import utils
from . import cohort
from . import query
from . import azdo


class ResearchAssistant:
    """Central class to help Research Analytics team members with their work.

    ResearchAssistant is a "facade", i.e. it provides a simple interface to a
    more-complex backend.
    As such, methods belonging to ResearchAssistant should...
    - Be the primary way any functionality in ra_lib is used
    - Should have have names, arguments, and return values that are as static as possible.
    Following these guidelines will help maintain the stability of ra_lib,
    even when the internal code changes.

    """

    def __init__(
        self,
        report_id: str = None,
        reports_config_path: str = None,
        reports_schema: str = None,
        environment_sys: environment.EnvironmentSystem = None,
        utils_sys: utils.UtilsSystem = None,
        cohort_sys: cohort.CohortSystem = None,
        query_sys: query.OnPremQuerySystem = None,
        azdo_sys: azdo.AzDOSystem = None,
    ):
        """Constructor for Assistant.

        Note to ra_lib developers: If we want to make it easier to create custom
        versions of ResearchAssistant, we can always create a classmethod
        ResearchAssistant.from_config that parses a config and creates
        the ResearchAssistant accordingly.

        Parameters
        ----------
        report_id : str, optional
            Each assistant is created to help with a specific request. The
            report_id identifies that request. Default is None, which has the
            ResearchAssistant retrieve it automatically.
        environment_settings : dict, optional
            Non-default settings passed to environment.EnvironmentSystem.
            EnvironmentSystem helps with handling the navigating the
            Databricks workspaces and changing settings accordingly.
            EnvironmentSystem assumes the user is working in a notebook environment.
        cohort_settings : dict, optional
            Non-default settings passed to cohort.CohortSystem.
            CohortSystem helps work with cohorts, the group of patients associated
            with a study. Not all reports have cohorts, but it is very common.
        query_settings : dict, optional
            Non-default settings passed to query.QuerySystem.
            QuerySystem helps with querying the data. In general Databricks' default
            functionality should be strongly preferred over using QuerySystem.
            QuerySystem's strength is working with on-prem data and blending it
            with cloud data.
        azdo_settings : dict, optional
            Non-default settings passed to azdo.AzDOSystem.
            AzDOSystem is an interface to easily work programmatically with
            Azure Dev Ops.
        """

        # Get the spark session, which is central to interacting with databricks.
        self.spark = SparkSession.builder.getOrCreate()

        # Store the systems
        # We use defaults that can be overridden by passing in another class.
        # EnvironmentSystem is a base requirement.
        if environment_sys is None:
            self.environment_sys = environment.EnvironmentSystem(report_id)
        else:
            self.environment_sys = environment_sys
        self.report_id = self.environment_sys.get("report_id")

        self.utils_sys = utils_sys if utils_sys is not None else utils.UtilsSystem()

        # Get key paths
        if reports_config_path is None:
            reports_config_path = self.environment_sys.get("reports_config_path")
        if reports_schema is None:
            reports_schema = self.environment_sys.get("reports_schema")
        self.reports_config_path = self.environment_sys.get(
            "used_path", reports_config_path
        )
        self.reports_schema = self.environment_sys.get("used_path", reports_schema)

        # The cohort system depends on the environment
        if cohort_sys is None:
            self.cohort_sys = cohort.CohortSystem(
                environment_sys=self.environment_sys,
                utils_sys=self.utils_sys,
            )
        else:
            self.cohort_sys = cohort_sys

        # The query system depends on the cohort system and the environment
        if query_sys is None and self.environment_sys.get("onprem_enabled"):
            try:
                query_sys = query.OnPremQuerySystem(
                    environment_sys=self.environment_sys,
                )
            except Exception as e:
                self.environment_sys.warn(
                    "Failed to initialize on-prem query system. Will not be able to retrieve data from on-prem sources."
                )
        self.query_sys = query_sys

        # The AzDO system depends on the environment
        if azdo_sys is None:
            self.azdo_sys = azdo.AzDOSystem(
                environment_sys=self.environment_sys,
                utils_sys=self.utils_sys,
            )
        else:
            self.azdo_sys = azdo_sys

        # Announce setup complete
        if self.get("used_for_report"):
            print(f"Created ResearchAssistant for {self.report_id}")

    def get_report_config(self, azdo_id: int) -> pd.Series:

        t_start = time.time()

        reports_config = self.generate_reports_config()

        dt_warn = 30.0
        if time.time() - t_start > dt_warn:
            self.environment_sys.warn(
                f"Calling get_report_config took more than {dt_warn} seconds. "
                "Currently get_report_config does a full load of the reports config "
                "each time it's called, because it (was) fast enough to not matter. "
                "If you're reading this, that's no longer the case. Ask a data "
                "engineer or architect to revisit this function. Suggest they use "
                "combine a focused AzDO API call with querying the stored "
                "reports_config table."
            )

        return reports_config.loc[azdo_id]

    def generate_reports_config(self, write: bool = False) -> pd.DataFrame | DataFrame:

        reports_config = self.get_reports_config_base()

        # Add columns that involve some level of complex logic
        reports_config = self.add_report_ids(reports_config)
        reports_config = self.add_report_locations(reports_config)
        reports_config = self.add_report_dir_patterns(reports_config)

        reports_config = self.finalize_reports_config(reports_config)

        if write:
            return self.write_reports_config(reports_config)

        return reports_config

    def get_reports_config_base(self) -> pd.DataFrame:

        # Get the work items that are reports.
        # These serve as the foundation for our config.
        report_work_items = self.azdo_sys.get_report_work_items()

        # Format report_work_items to be the base of the config
        renamed_azdo_columns = {
            "Id": "azdo_id",
            "Title": "azdo_title",
            "State": "state",
            "Tags": "tags",
            "Description": "description",
            "AssignedTo": "assigned_to",
            "Predecessor": "predecessor_azdo_id",
        }
        columns_parsed_from_description = [
            "irb_number",
            "domain",
            "workspace",
            "workspace_folder",
            "is_active",
            "depends_on_onprem",
            "refresh_schedule",
            "is_valid",
            "error_log",
        ]
        reports_config = report_work_items.rename(columns=renamed_azdo_columns)
        reports_config = reports_config[
            list(renamed_azdo_columns.values()) + columns_parsed_from_description
        ]

        return reports_config.set_index("azdo_id", drop=False)

    def add_report_ids(self, reports_config: pd.DataFrame) -> pd.DataFrame:
        """Update the reports_config dataframe with the report_id."""

        # We split the report work items into original reports
        # and updates to the reports. Updates are when there's
        # a predecessor that's also a report.
        is_update = reports_config["predecessor_azdo_id"].notna() & reports_config[
            "predecessor_azdo_id"
        ].isin(reports_config.index)
        original_report_wis = reports_config.loc[~is_update].copy()

        # Base the default report IDs on the azdo_id by default
        original_report_wis["report_id"] = original_report_wis["azdo_id"].apply(
            lambda x: f"ra{x:07d}"
        )

        # Check for irb and do a quick check for basic validity
        has_irb = original_report_wis["irb_number"].notna()
        invalid_irb = reports_config["irb_number"].str[:3] != "STU"
        has_valid_irb = has_irb & ~invalid_irb
        has_invalid_irb = has_irb & invalid_irb
        if has_invalid_irb.any():
            reports_config.loc[has_invalid_irb, "is_valid"] = False
            reports_config.loc[
                has_invalid_irb, "error_log"
            ] += "Report metadata error: invalid IRB "

        # If the study has an IRB we override the azdo_id-based report ID with one based on the study
        # For reports with irbs we calculate the irb rank and then use that as part of the report ID
        irb_reports = original_report_wis.loc[has_valid_irb].copy()
        # Adding irb_rank to the dataframe lets us use it for formatting in "apply"
        irb_reports["irb_rank"] = (
            irb_reports.groupby("irb_number")["azdo_id"].rank().astype(int) - 1
        )
        irb_reports["report_id"] = irb_reports.apply(
            lambda row: f"{row['irb_number']}.{row['irb_rank']:03d}", axis="columns"
        )
        original_report_wis.loc[irb_reports.index, ["irb_rank", "report_id"]] = (
            irb_reports[["irb_rank", "report_id"]]
        )

        # Update the original data
        reports_config.loc[original_report_wis.index, "report_id"] = (
            original_report_wis["report_id"]
        )

        # We link updates to the original using code for working with networks
        # Each component is an original report (lowest ID) with its updates
        updated_report_wis = reports_config.loc[is_update].copy()
        g = nx.from_pandas_edgelist(
            updated_report_wis, source="predecessor_azdo_id", target="azdo_id"
        )
        for component in nx.connected_components(g):
            component_azdo_ids = np.array(sorted(list(component)))
            # Updates inherit the report_id of the original
            reports_config.loc[component_azdo_ids, "report_id"] = reports_config.at[
                component_azdo_ids[0], "report_id"
            ]

        return reports_config

    def add_report_locations(self, reports_config: pd.DataFrame) -> pd.DataFrame:

        # When report location is not provided we default to core + IRB or Research Analytics Internal
        workspace_cols = ["domain", "workspace", "workspace_folder"]
        no_location = reports_config[workspace_cols].isna().all(axis="columns")
        has_irb = reports_config["irb_number"].notna()
        reports_config.loc[no_location & has_irb, workspace_cols] = [
            "Research Core",
            "Research IRB",
            "",
        ]
        reports_config.loc[no_location & ~has_irb, workspace_cols] = [
            "Research Operations",
            "Research Analytics Internal",
            "Main",
        ]

        # Check for defined, but invalid, parameters
        workspaces = self.get_valid_report_locations()
        for col in workspace_cols:
            is_not_valid = ~reports_config[col].isin(workspaces[col])
            # We don't require workspace folders
            if col == "workspace_folder":
                is_valid_after_all = reports_config[col] == ""
                is_not_valid = is_not_valid & ~is_valid_after_all
            reports_config.loc[is_not_valid, "is_valid"] = False
            reports_config.loc[
                is_not_valid, "error_log"
            ] += f"Report metadata error: Invalid {col}. "

        return reports_config

    def get_valid_report_locations(
        self, relative_path: str = "data/metadata/research_workspaces.csv"
    ):
        """This is turned into a function so we can have easier access for reference."""
        workspaces_fp = f"{os.path.dirname(__file__)}/{relative_path}"
        return pd.read_csv(workspaces_fp)

    def add_report_dir_patterns(
        self,
        reports_config: pd.DataFrame,
    ) -> pd.DataFrame:

        def get_report_dir_pattern(row: pd.Series) -> str:
            """This is applied on a per-row basis to get the report pattern."""

            # Workspace details
            report_dir_pattern = f"reports/{self.utils_sys.sanitize_dirname(row['domain'])}/{self.utils_sys.sanitize_dirname(row['workspace'])}"
            if not pd.isna(row["workspace_folder"]):
                report_dir_pattern += "/" + self.utils_sys.sanitize_dirname(
                    row["workspace_folder"]
                )

            if not pd.isna(row["irb_number"]):
                # The irb number becomes the directory base and the irb rank becomes the subdir base
                report_dir_pattern += f"/{row['report_id'].replace('.', '*/report')}*"
            else:
                report_dir_pattern += f"/{row['report_id']}*"

            return report_dir_pattern

        reports_config["report_dir_pattern"] = reports_config.apply(
            get_report_dir_pattern, axis="columns"
        )

        return reports_config

    def finalize_reports_config(self, reports_config: pd.DataFrame) -> pd.DataFrame:

        # Fill in default values for "is_active"
        is_template = reports_config["tags"].apply(lambda tags: "Template" in tags)
        story_is_closed = reports_config["state"] == "Closed"
        is_active_defaults = is_template | story_is_closed
        is_active_is_null = reports_config["is_active"].isna()
        reports_config.loc[is_active_is_null, "is_active"] = is_active_defaults.loc[
            is_active_is_null
        ]

        # Turn off invalid reports
        reports_config["is_active"] = (
            reports_config["is_active"] & reports_config["is_valid"]
        )

        # Turn off on-prem reports when on-prem is not enabled
        if "depends_on_onprem" not in reports_config.columns:
            reports_config["depends_on_onprem"] = True
        else:
            reports_config["depends_on_onprem"] = (
                reports_config["depends_on_onprem"].fillna(True).astype(bool)
            )
        # If on-prem is not enabled, turn off the reports that depend on it
        if not self.environment_sys.get("onprem_enabled"):
            reports_config["is_active"] = (
                reports_config["is_active"] & ~reports_config["depends_on_onprem"]
            )

        # Only keep the most-recent active report as active
        actually_active_azdo_ids = (
            reports_config.query("is_active").groupby("report_id")["azdo_id"].idxmax()
        )
        reports_config["is_active"] = False
        reports_config.loc[actually_active_azdo_ids.values, "is_active"] = True

        # Get whether or not the irb is active.
        reports_config["irb_is_active"] = pd.NA
        has_irb = reports_config["irb_number"].notna()
        reports_irbs = self.spark.createDataFrame(
            reports_config.loc[has_irb, ["irb_number"]]
        )
        studies = self.spark.table(f"{self.get('eirb_schema')}.studies").filter(
            "(study_status in ('Approved', 'External IRB')) and (closed_date is NULL)"
        )
        irb_is_active = (
            reports_irbs.join(
                studies.select("irb_study_id"),
                on=(reports_irbs.irb_number == studies.irb_study_id),
                how="left",
            )
            .toPandas()["irb_study_id"]
            .notna()
            .values
        )
        reports_config.loc[has_irb, "irb_is_active"] = irb_is_active

        # Make active reports visible, and turn off visibility for reports with an IRB
        # where the IRB is inactive
        reports_config["is_visible"] = reports_config["is_active"]
        reports_config.loc[has_irb, "is_visible"] = (
            reports_config.loc[has_irb, "is_visible"]
            & reports_config.loc[has_irb, "irb_is_active"]
        )
        # Templates are set to visible so we can see how they would behave
        reports_config.loc[is_template, "is_visible"] = True

        # Sort
        reports_config = reports_config.sort_values("report_dir_pattern")

        return reports_config

    def write_reports_config(
        self,
        reports_config: pd.DataFrame,
    ) -> DataFrame:
        """
        Note: A function to build a specific table would not normally be incorporated
        into ra_lib.  However, because so much of ra_lib revolves around the config
        table we include and test it as part of ra_lib.
        """

        # Drop so we don't have to worry about schema compatibility
        self.spark.sql(f"DROP TABLE IF EXISTS {self.reports_config_path}")

        # Create the table
        self.spark.sql(
            f"""
            CREATE TABLE {self.reports_config_path} (
                azdo_id INT PRIMARY KEY COMMENT "Azure DevOps work item ID.",
                report_id STRING COMMENT "ID of the report the Azure DevOps work item is associated with. For reports with IRBs this is based on the IRB number and the number of other reports for the same study. For reports without an IRB this is based on the Azure DevOps ID of the original work item.",
                irb_number STRING COMMENT "Study number if provided, e.g. STU00000000.",
                assigned_to STRING COMMENT "Individual the work item is assigned to.",
                domain STRING COMMENT "Power BI Domain for the report. Also used when specifying the location of the report code in the reports repo.",
                workspace STRING COMMENT "Power BI workspace for the report. Also used when specifying the location of the report code in the reports repo.",
                workspace_folder STRING COMMENT "Folder in the Power BI workspace for the report. Also used when specifying the location of the report code in the reports repo.",
                report_dir_pattern STRING COMMENT "Unix filename pattern specifying the directory inside the ra_reports repo that contains the report code.",
                azdo_title STRING COMMENT "Title of the work item.",
                state STRING COMMENT "State of the work item, e.g. 'In Progress' or 'Closed'.",
                tags ARRAY<STRING> COMMENT "Tags associated with the work item.",
                predecessor_azdo_id INT COMMENT "Azure DevOps work item ID of a predecessor linked in the work item. If a work item has a predecessor that is also a report work item (has the 'Report' tag), then the work item is an update to the original report.",
                is_active BOOLEAN COMMENT "If True, then this report is actively refreshed, using the metadata specified by this row. Each work item associated with a report can have an 'is_active' field in the yaml metadata, but only the most recent active work item (largest azdo_id with is_active == True) will be marked as active in this config table. When not specified, is_active defaults to True for work items with state == 'Closed'.",
                refresh_schedule STRING COMMENT "Specification of how often the report should be executed.",
                irb_is_active BOOLEAN COMMENT "For reports with an IRB, whether or not that IRB is active.",
                is_visible BOOLEAN COMMENT "Whether or not any generated data should be visible to the end users.",
                description STRING COMMENT "Description field for the work item. Some values have been extracted from here, e.g. irb_number.",
                is_valid BOOLEAN COMMENT "If False, then some aspect of the work item is incorrectly defined, and this work item will not be used in production. Check the error_log field for details on the issue.",
                error_log STRING COMMENT "Any recorded details on why a given work item may be invalid for specifying report metadata."
            ) COMMENT "This table contains configuration parameters for reports, derived primarily from Azure Devops work items. There is none row per Azure DevOps work item associated with a report. For a given report_id there may be multiple azdo_ids, i.e. multiple work items, but at most one should be active at a given time, as recorded by the `is_active` field."
            """
        )

        # Convert to a spark dataframe with matching schema
        reports_config_spark = self.utils_sys.create_matching_dataframe(
            reports_config, self.spark.table(self.reports_config_path).schema
        )

        # Save
        reports_config_spark.write.format("delta").mode("append").saveAsTable(
            self.reports_config_path
        )

        print(f"Reports config saved to {self.reports_config_path}")

        return self.spark.table(self.reports_config_path)

    def draft_report_structure(
        self,
        report_config: pd.Series,
        study_dir_label: str = None,
        report_dir_label: str = None,
        report_files: list[str] = None,
        ra_reports_path: str = "..",
    ) -> dict:

        is_study = not pd.isna(report_config["irb_number"])
        report_structure = {}

        # Default is no label for study dirs
        if study_dir_label is None:
            study_dir_label = ""
        else:
            study_dir_label = "_" + study_dir_label

        # Default to the azdo title for report dirs
        if report_dir_label is None:
            report_dir_label = self.utils_sys.sanitize_dirname(
                report_config["azdo_title"], space_sub="-"
            )
        report_dir_label = "_" + report_dir_label

        # Assemble the report structure
        report_dir_str = report_config["report_dir_pattern"].replace("*", "{}")

        # Check if there's a parent dir or not
        if is_study:
            report_structure["report_dir"] = report_dir_str.format(
                study_dir_label, report_dir_label
            )
        else:
            report_structure["report_dir"] = report_dir_str.format(report_dir_label)

        # Modify the report dir to account for the location of ra_reports,
        # where all the reports live
        report_structure["report_dir"] = os.path.abspath(
            f"{ra_reports_path}/{report_structure['report_dir']}"
        )

        # Get the report files
        if report_files is None:
            report_files = ["report"]
            if is_study:
                report_files.append("cohort")
        report_structure["report_files"] = report_files

        return report_structure

    def build_report_structure(
        self,
        report_dir: str,
        report_files: list[str],
        template_dir: str = "../reports/research_operations/research_analytics_internal/templates/STU00000000_template-study/report000_on-prem-template",
        template_files: list[str] = None,
        ra_lib_setup_path: str = "./ra_lib_setup",
        str_to_replace: str = "../../../../../../shared_resources/ra_lib_setup",
    ):

        w = WorkspaceClient()

        # Resolve paths
        report_dir = os.path.abspath(report_dir)
        template_dir = os.path.abspath(template_dir)
        ra_lib_setup_path = os.path.abspath(ra_lib_setup_path)
        relative_ra_lib_setup_path = os.path.relpath(
            ra_lib_setup_path, start=report_dir
        )

        # Make the report dir
        os.makedirs(report_dir, exist_ok=True)

        # Set up the report filepaths
        if template_files is not None:
            report_files = template_files
        else:
            report_files = [
                f"{template_dir}/{report_file}" for report_file in report_files
            ]

        # Copy in template files
        for report_file_path in report_files:

            try:
                # Get the template notebook
                export_response = w.workspace.export(
                    path=report_file_path,
                    format=workspace.ExportFormat.SOURCE,
                )

                # Decode, add the setup path to the notebook, and encode again
                notebook_str = base64.b64decode(export_response.content).decode()
                modified_notebook_str = notebook_str.replace(
                    str_to_replace, relative_ra_lib_setup_path
                )
                encoded_notebook = base64.b64encode(
                    modified_notebook_str.encode()
                ).decode()

                # Save the new notebook
                dst_notebook_path = f"{report_dir}/{os.path.basename(report_file_path)}"
                w.workspace.import_(
                    path=dst_notebook_path,
                    content=encoded_notebook,
                    format=workspace.ImportFormat.SOURCE,
                    language=workspace.Language.PYTHON,
                )
            except Exception as e:
                print(
                    f"Tried to copy in the template from {report_file_path} but failed. Exception:\n{e}"
                )

        print(f"Report is ready for editing at:\n    {report_dir}")

    def get(self, key, *args, **kwargs):
        return self.environment_sys.get(key, *args, **kwargs)

    def set(self, key, value):
        return self.environment_sys.set(key, value)

    def save_report_table(
        self,
        report_id: str = None,
        report_df: DataFrame = None,
        view_name: str = "report",
        table_label: str = None,
    ):

        # Get the table name and config id
        if report_id is None:
            report_id = self.environment_sys.get("report_id")
        # Remove common but invalid characters.
        table_name = report_id.replace("-", "_").replace("/", "_").replace(".", "_")

        # Add a label, used when there are multiple tables for a report.
        if table_label is not None:
            table_name += "_" + table_label

        # Get the table path and print info about it.
        table_path = f"{self.reports_schema}.{table_name}"
        print(f"Writing to {table_path}")

        if report_df is None:
            print(f"Loading report table from view '{view_name}'")
            report_df = self.spark.table(view_name)

        # Add the cohort ID column.
        # OPTIMIZE: Having the cohort id for every patient breaks normalization and is inefficient. Change.
        report_df = report_df.withColumn("meta_report_id", lit(report_id))

        # The actual save
        report_df.write.option("overwriteSchema", "true").saveAsTable(
            table_path, format="delta", mode="overwrite"
        )

    def load_cohort(
        self, report_id: str = None, view_name: str = "cohort"
    ) -> DataFrame:
        if report_id is None:
            report_id = self.report_id
        return self.cohort_sys.load_cohort(report_id=report_id, view_name=view_name)

    def save_cohort(
        self,
        report_id: str = None,
        cohort_df: DataFrame = None,
        view_name: str = "cohort",
        patient_id_type: str = None,
    ):
        if report_id is None:
            report_id = self.report_id
        return self.cohort_sys.write_cohort(
            report_id=report_id,
            cohort_df=cohort_df,
            view_name=view_name,
            patient_id_type=patient_id_type,
        )

    def query(
        self,
        sql_query: str,
        view_name: str = None,
        connection: sqlalchemy.engine.base.Connection = None,
        output_as: str = None,
        execute_kwargs: dict = {},
    ) -> DataFrame:

        if self.query_sys is None:
            raise ValueError(
                "No query system is available, likely because this environment does not support on-prem querying."
            )

        return self.query_sys.query(
            sql_query=sql_query,
            view_name=view_name,
            connection=connection,
            output_as=output_as,
            execute_kwargs=execute_kwargs,
        )

    def get_connection(self) -> sqlalchemy.engine.base.Connection:
        return self.query_sys.get_open_connection()
