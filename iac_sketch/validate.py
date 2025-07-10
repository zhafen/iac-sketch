import pandas as pd

from . import data

class ValidationSystem:

    def validate_requirements(self, registry: data.Registry) -> pd.DataFrame:

        reqs = registry["requirement"]
        invalid_reqs = reqs.query("~is_satisfied")

        return invalid_reqs

    def validate_components(
        self,
        registry: data.Registry,
        invalid_component_columns: list = [
            "source",
            "fields",
            "is_defined",
            "is_valid",
            "errors",
        ],
    ) -> pd.DataFrame:

        component_defs = registry.view(["compdef", "metadata"])
        invalid_components = component_defs.query("~valid")[invalid_component_columns]

        return invalid_components

    def validate_tasks(self, registry: data.Registry) -> pd.DataFrame:

        tasks = registry["task"]
        invalid_tasks = tasks[~tasks["implemented"]]

        return invalid_tasks

    def validate_testcases(self, registry: data.Registry) -> pd.DataFrame:

        testcases = registry["testcase"]
        invalid_testcases = testcases[~testcases["passing"]]

        return invalid_testcases

    def validate_connectivity(self, registry: data.Registry) -> pd.DataFrame:
        """
        Validate the connectivity of entities in the registry.
        This checks if all entities are connected to at least one other entity.
        """
        connectivity = registry["connectivity"]
        invalid_entities = connectivity[~connectivity["connected"]]

        return invalid_entities
