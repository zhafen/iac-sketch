import os
import re

from azure.devops.connection import Connection
from azure.devops.exceptions import AzureDevOpsServiceError
from azure.devops.v7_0.work_item_tracking.models import Wiql, TeamContext
from msrest.authentication import BasicAuthentication
import numpy as np
import pandas as pd
import tqdm
import yaml

from pyspark.sql import SparkSession
from pyspark.sql.dataframe import DataFrame

from .environment import EnvironmentSystem
from .utils import UtilsSystem


DEFAULT_FIELDS = [
    "System.Id",
    "System.Title",
    "System.State",
    "System.WorkItemType",
    "System.IterationPath",
    "System.ChangedDate",
    "System.Tags",
    "System.Description",
    "System.AssignedTo",
    "Microsoft.VSTS.Scheduling.StoryPoints",
    "Microsoft.VSTS.Scheduling.Effort",
    "Microsoft.VSTS.Scheduling.RemainingWork",
    "Microsoft.VSTS.Scheduling.StartDate",
    "System.Parent",
]


class AzDOSystem:

    def __init__(
        self,
        organization_url: str = "https://dev.azure.com/NMHC",
        team: str = "FSM Research Analytics",
        environment_sys: EnvironmentSystem = None,
        utils_sys: UtilsSystem = None,
    ):

        self.spark = SparkSession.builder.getOrCreate()
        self.environment_sys = (
            environment_sys
            if not environment_sys is None
            else EnvironmentSystem()
        )
        self.utils_sys = utils_sys if not utils_sys is None else UtilsSystem()

        credentials = BasicAuthentication(
            "", self.environment_sys.get_secret("azure_devops_pat_secret_key")
        )
        self.connection = Connection(base_url=organization_url, creds=credentials)
        self.wit_client = self.connection.clients.get_work_item_tracking_client()
        self.team_context = TeamContext(team)

    def query(self, wiql_query: str):

        # Get the work item ids for the query
        wiql = Wiql(query=wiql_query)
        return self.wit_client.query_by_wiql(wiql, team_context=self.team_context)

    # straightforward path to getting a DF of work items.
    def get_unparsed_work_items(
        self,
        wi_selection: (
            str | list[int]
        ) = """
            SELECT [System.Id]
            FROM WorkItems
            WHERE [System.AreaPath] = 'FSM Research Analytics'
            """,
        times: list[str | pd.Timestamp] = None,
        fields: list[str] = DEFAULT_FIELDS,
        include_relations: bool = False,
    ) -> pd.DataFrame:
        """Get a pandas dataframe containing queried work items.
        This works by doing two separate queries: one that gets the IDs,
        and a second that gets the fields.

        Parameters
        ----------
        wiql_query : str
            A query for the work items. Should only select [System.Id].

        fields : list[str]
            The specified fields to return.

        Returns
        -------
        pd.DataFrame
            The pandas dataframe of work items.
        """

        # The default query gets all IDs in our project
        if isinstance(wi_selection, list):
            work_item_ids = wi_selection
        else:
            work_item_ids = [wi.id for wi in self.query(wi_selection).work_items]

        # Format arguments. Cannot pass in both expand and fields
        if include_relations:
            get_work_item_kwargs = {"expand": "All"}
        else:
            get_work_item_kwargs = {"fields": fields}

        # Get the details for the work item
        work_items = []
        for i, wi_id in enumerate(tqdm.tqdm(work_item_ids)):
            try:
                if times is None:
                    work_item_response = self.wit_client.get_work_item(wi_id, **get_work_item_kwargs)
                    wi_dict = work_item_response.as_dict()

                    # Start filling out the dictionary that will be the row in the table
                    work_item = {}
                    for field in fields:
                        try:
                            work_item[field] = wi_dict["fields"][field]
                        except KeyError:
                            work_item[field] = np.nan

                    # Add links to other work items
                    if include_relations:
                        n_relation_type = {}
                        for wi_relation in wi_dict["relations"]:
                            relation_type = wi_relation["attributes"]["name"]

                            # Parent is available as a default field
                            if relation_type == "Parent":
                                continue

                            # If there are duplicates we add them as additional columns
                            if n_relation_type.setdefault(relation_type, 0) > 1:
                                key = f"{relation_type}_{n_relation_type[relation_type]:02d}"
                            else:
                                key = relation_type
                            n_relation_type[relation_type] += 1

                            # Store the linked ID, ideally as an int
                            linked_id = wi_relation["url"].split("/")[-1]
                            try:
                                linked_id = int(linked_id)
                            except ValueError:
                                pass
                            work_item[key] = linked_id
                else:
                    work_item = self.get_work_item_at_time(
                        wi_id, fields=fields, time=times[i]
                    )
                    if include_relations:
                        raise NotImplementedError(
                            "Cannot include relations when specifying times currently. "
                            "Changing this could be as simple as deprecating get_work_item_at_time "
                            "in favor of the `as_of` argument."
                        )
            except AzureDevOpsServiceError as e:
                work_item = {"System.Id": wi_id}
            work_items.append(work_item)

        work_items_df = pd.DataFrame(work_items)

        return work_items_df

    def get_work_items(
        self,
        wi_selection: (
            str | list[int]
        ) = """
            SELECT [System.Id]
            FROM WorkItems
            WHERE [System.AreaPath] = 'FSM Research Analytics'
            """,
        times: list[str | pd.Timestamp] = None,
        fields: list[str] = DEFAULT_FIELDS,
        include_relations: bool = False,
        jitter_state_value: bool = False,
        join_self_for_parents: bool = False,
        parse_descriptions: bool = False,
    ) -> pd.DataFrame:
        """Get a pandas dataframe containing queried work items.
        This is different from get_unparsed_work_items in that this call is cleaned up

        Parameters
        ----------
        wi_selection : str
            A query for the work items. Should only select [System.Id].

        fields : list[str]
            The specified fields to return.

        jitter_state_value: bool
            If True, then add random noise to the StateValue, useful for plotting.

        join_self_for_parents: bool
            If True, join the dataframe to itself on ID = Parent.
            This is only sensible if the dataframe contains the parents.

        parse_descriptions: bool
            If True, look for yaml-formatted data in the description and put the attributes into new columns.

        Returns
        -------
        pd.DataFrame
            The pandas dataframe of work items.
        """

        if join_self_for_parents and not isinstance(wi_selection, str):
            raise ValueError(
                "Cannot join self for parents reliably when only selecting a subset."
            )

        work_items = self.get_unparsed_work_items(
            wi_selection, times=times, fields=fields, include_relations=include_relations
        )

        # Clean up names
        work_items.columns = [col.split(".")[-1] for col in work_items.columns]
        if (
            "AssignedTo" in work_items.columns
            and work_items["AssignedTo"].notna().sum() > 0
        ):
            work_items["AssignedTo"] = work_items["AssignedTo"].str["displayName"]
        if "Tags" in work_items.columns and work_items["Tags"].notna().sum() > 0:
            work_items["TagsStr"] = work_items["Tags"].copy()
            work_items["Tags"] = work_items["Tags"].str.split("; ")

        # Map state to a numeric value representing the columns
        if "State" in work_items.columns:
            state_values = {
                "New": 0,
                "In Progress": 1,
                "In Review": 2,
                "Blocked": 2,
                "Closed": 3,
                "Removed": 3,
            }
            work_items["StateValue"] = work_items["State"].map(state_values)

            # Make jittered version of the state values useful for display
            if jitter_state_value:
                rng = np.random.default_rng()
                work_items["JitterStateValue"] = work_items["StateValue"] + rng.normal(
                    size=len(work_items), scale=0.1
                )

        # Get relevant sprints
        if "IterationPath" in work_items.columns:
            sprint_relativenumbers = {
                "Current": 0,
                "Previous": -1,
                "Next": 1,
            }
            sprints = {}
            for key, relative_number in sprint_relativenumbers.items():
                query = f"""
                    SELECT [System.Id]
                    FROM WorkItems
                    WHERE [System.IterationPath] = @CurrentIteration + {relative_number}
                    """
                work_item_id = (
                    self.wit_client.query_by_wiql(
                        Wiql(query), team_context=self.team_context, top=1
                    )
                    .work_items[0]
                    .id
                )
                work_item = self.wit_client.get_work_item(
                    work_item_id, fields=["System.IterationPath"]
                )
                sprints[work_item.as_dict()["fields"]["System.IterationPath"]] = key
            work_items["RelativeIterationPath"] = work_items["IterationPath"].map(
                sprints
            )

        # Add parent title and story points
        if join_self_for_parents:
            work_items = work_items.merge(
                work_items[["Id", "Title", "StoryPoints", "WorkItemType"]],
                left_on="Parent",
                right_on="Id",
                suffixes=("", "Parent"),
                how="left",
            )

        if parse_descriptions:
            work_items = self.parse_work_item_descriptions(work_items)

        return work_items

    def get_work_item_at_time(
        self,
        wi_id: int,
        time: str | pd.Timestamp,
        fields: list[str] = DEFAULT_FIELDS,
    ) -> dict:
        """This can probably be deprecated--the Python api offers the "as_of" argument.
        """

        if isinstance(time, str):
            time = pd.Timestamp(time)

        # Loop through updates
        work_item = {}
        for i, update in enumerate(self.wit_client.get_updates(wi_id)):

            # Good for debugging purposes
            work_item["update_ind"] = i

            # Skip updates that update relations, not fields
            if update.fields is None:
                continue
            updated_fields = update.as_dict()["fields"]

            # Stop layering updates when we get to the right time
            update_time = updated_fields["System.ChangedDate"]["new_value"]
            time = pd.Timestamp(time).tz_localize(None)
            if pd.Timestamp(update_time).tz_localize(None) > time:
                break

            # Update the fields themselves
            for field in fields:
                if field not in updated_fields:
                    continue

                value = updated_fields[field]

                # Special case when the field is empty
                if value == {}:
                    work_item.setdefault(field, {})
                    continue

                work_item[field] = value.get("new_value", None)

        return work_item

    def parse_work_item_descriptions(self, work_items: pd.DataFrame) -> pd.DataFrame:
        """The bottom of the description for some AzDO workitems is
        yaml-formatted metadata.
        """

        # Remove html formatting from descriptions
        # First, replace closing divs with newlines
        descriptions = work_items["Description"].copy()
        descriptions = descriptions.str.replace(r'</div>', '\n', regex=True)
        # Next remove any other tags.
        descriptions = descriptions.str.replace(r'<.*?>', '', regex=True)
        # Other formatting that lingers
        descriptions = descriptions.str.replace(r"\&nbsp\;", " ", regex=True)
        descriptions = descriptions.str.replace(r"\&quot\;", '"', regex=True)

        # Once we have the html removed we split out the yaml and further remove whitespace
        # The division between the rest of the text is when there are three or more hyphens in a row
        descriptions = descriptions.str.rsplit("---").str[-1].str.strip()
        def prune_whitespace(text):
            if not isinstance(text, str):
                return text
            # Split text into lines, clean each line and remove fully empty lines
            lines = text.splitlines()  # Split into lines
            cleaned_lines = [
                # Remove leading/trailing spaces and normalize spaces within each line
                re.sub("\s+", " ", line.strip())
                for line in lines
                # Keep only non-empty lines
                if line.strip()
            ]
            return "\n".join(cleaned_lines)  # Rejoin lines with linebreaks
        work_items["extracted_yaml"] = descriptions.apply(prune_whitespace)

        def load_yaml(row):
            """Function for safely loading yaml."""
            try:
                # Load yaml, including normalizing names
                row["metadata"] = {
                    key.lower().replace(" ", "_"): value
                    for key, value in 
                    yaml.safe_load(row["extracted_yaml"]).items()
                }
            except Exception as e:
                row["is_valid"] = False
                row["error_log"] += "Description parse error: " + repr(e)
                row["metadata"] = {}
            return row

        # Prep the dataframe for loading yaml, then load
        work_items["is_valid"] = True
        work_items["error_log"] = ""
        work_items["metadata"] = pd.NA
        work_items = work_items.apply(load_yaml, axis="columns")

        # Expand out metadata dictionaries
        yaml_metadata = pd.json_normalize(work_items["metadata"])

        # Combine with prior
        return pd.concat([work_items, yaml_metadata], axis="columns")
    
    def get_report_work_items(self):
        """The query used to identify reports.
        """
        return self.get_work_items(
            wi_selection = (
                """SELECT [System.Id]
                FROM WorkItems
                WHERE [System.Tags] Contains "Report"
                AND (
                    [System.AreaPath] = 'FSM Research Analytics'
                    OR [System.AreaPath] = 'Enterprise Data Architecture\Research Team'
                )
                """
            ),
            fields=[
                "System.Id",
                "System.Title",
                "System.State",
                "System.Tags",
                "System.Description",
                "System.AssignedTo",
                "System.Parent",
            ],
            parse_descriptions=True,
            include_relations=True,
        )
