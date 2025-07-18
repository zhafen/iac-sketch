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
        return self.registry

    def validate_registry(self) -> tuple[bool, dict[str, pd.DataFrame]]:

        invalids = {}

        tests = self.registry.view(["test", "code"])
        for entity, row in tests.iterrows():
            if row["code.value"]:

                try:
                    # Get the test function from the code path
                    module_path, test_func_name = row["code.value"].rsplit(".", 1)
                    module = importlib.import_module(module_path)
                    test_func = getattr(module, test_func_name)

                    # Call the test function if it is callable
                    invalids[entity] = test_func(self.registry)
                # A bare except is okay here because we're logging.
                except Exception as e: # pylint: disable=W0718
                    invalids[entity] = (
                        f"Test function {row['code.value']} is invalid: {e}"
                    )
            else:
                invalids[entity] = "Test code is missing."

        is_valid = all(
            df.empty if not isinstance(df, str) else False for df in invalids.values()
        )

        return is_valid, invalids
