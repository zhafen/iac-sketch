import pandas as pd

from . import data

class ValidationSystem:

    def validate_components(self, registry: data.Registry) -> pd.DataFrame:

        component_defs = registry["compdef"]
        invalid_components = component_defs[~component_defs["valid"]]

        return invalid_components

    def validate_requirements(self, registry: data.Registry) -> pd.DataFrame:

        reqs = registry["requirement"]
        invalid_reqs = reqs[~reqs["is_satisfied"]]

        return invalid_reqs

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
