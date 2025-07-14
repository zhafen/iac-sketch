import pandas as pd

from . import data, etl

class Architect:

    def __init__(
        self,
        filename_patterns: str | list[str] = [],
        extract_sys: etl.ExtractSystem = None,
        transform_sys: etl.TransformSystem = None,
        valid_sys: validate.ValidationSystem = None,
    ):
        self.filename_patterns = filename_patterns
        self.extract_sys = extract_sys if extract_sys else etl.ExtractSystem()
        self.transform_sys = transform_sys if transform_sys else etl.TransformSystem()
        self.valid_sys = valid_sys if valid_sys else validate.ValidationSystem()

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

    def validate_registry(self, registry: data.Registry) -> tuple[bool, dict[str, pd.DataFrame]]:

        invalids = {}

        tests = registry.view("test")
        for entity, row in tests.iterrows():
            if row["implementation"]:

                try:
                    # Get the test function from the implementation path
                    module_path, test_func_name = row["implementation"].rsplit(".", 1)
                    module = importlib.import_module(module_path)
                    test_func = getattr(module, test_func_name, None)

                    # Call the test function if it is callable
                    invalids[entity] = test_func(registry)
                except (ImportError, AttributeError) as e:
                    invalids[entity] = (
                        f"Test function {row['implementation']} is invalid: {e}"
                    )
            else:
                invalids[entity] = "Test implementation is missing."

        is_valid = all(df.empty for df in invalids.values())

        return is_valid, invalids