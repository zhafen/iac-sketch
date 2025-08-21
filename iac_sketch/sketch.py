import importlib

import pandas as pd

from . import data, etl


class Architect:

    def __init__(
        self,
        filename_patterns: str | list[str] = [],
        extract_sys: etl.ExtractSystem = None,
        transform_sys: etl.TransformSystem = None,
    ):
        self.filename_patterns = filename_patterns
        self.extract_sys = extract_sys if extract_sys else etl.ExtractSystem()
        self.transform_sys = transform_sys if transform_sys else etl.TransformSystem()

    def perform_registry_etl(
        self,
        filename_patterns: str | list[str] = None,
    ):
        """
        Main ETL workflow: extract, load, preprocess, system transforms, user transforms.
        """
        filename_patterns = (
            filename_patterns if filename_patterns else self.filename_patterns
        )
        self.registry = self.extract_sys.extract_entities(filename_patterns)
        self.registry = self.transform_sys.apply_preprocess_transforms(self.registry)
        self.registry = self.transform_sys.apply_system_transforms(self.registry)
        self.registry = self.transform_sys.apply_postprocess_transforms(self.registry)
        return self.registry

    def validate_registry(self) -> tuple[bool, dict[str, pd.DataFrame]]:
        """

        iac_sketch
        ----------
        todo: Order tests by their priority.
        """

        # Prepare summary dataframe
        tests = self.registry.view(["test", "code"])
        tests["errors"] = pd.NA
        tests["test_passed"] = pd.NA

        test_results = {}
        for entity, row in tests.iterrows():

            # Skip when there's no test code
            if pd.isna(row["code.value"]):
                continue

            try:
                # Get the test function from the code path
                module_path, test_func_name = row["code.value"].rsplit(".", 1)
                module = importlib.import_module(module_path)
                test_func = getattr(module, test_func_name)

                # Call the test function if it is callable
                test_result: pd.DataFrame = test_func(self.registry)

                # Store results
                test_results[entity] = test_result
                tests.loc[entity, "test_passed"] = test_result.empty
                tests.loc[entity, "errors"] = ""

            # A bare except is okay here because we're logging.
            except Exception as e:  # pylint: disable=W0718
                tests.loc[entity, "errors"] = e

        return tests, test_results
