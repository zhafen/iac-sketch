import importlib
import textwrap

from IPython.display import display
import pandas as pd

from . import etl


class Architect:

    def __init__(
        self,
        filename_patterns: str | list[str] = [],
        root_dir: str = None,
        extract_sys: etl.ExtractSystem = None,
        transform_sys: etl.TransformSystem = None,
    ):
        self.filename_patterns = filename_patterns
        self.root_dir = root_dir
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
        self.registry = self.extract_sys.extract_entities(
            filename_patterns, root_dir=self.root_dir
        )
        self.registry = self.transform_sys.apply_preprocess_transforms(self.registry)
        self.registry = self.transform_sys.apply_system_transforms(self.registry)
        self.registry = self.transform_sys.apply_postprocess_transforms(self.registry)
        return self.registry

    def validate_registry(
        self,
        show: bool = True,
    ) -> tuple[bool, dict[str, pd.DataFrame]]:
        """

        Components
        ----------
        - todo: >
            Currently we're only set up to run tests that are not part of a class.
            We may want to hook into pytest to extend the functionality, or we could
            just add a minor addition to check if the module is a parent and if so, run that.
        """

        # Prepare summary dataframe
        tests = self.registry.view(["test", "code", "satisfies", "FunctionDef"])
        tests["errors"] = pd.NA
        tests["test_passed"] = pd.NA

        # Join requirements
        requirements = self.registry.view(["requirement", "description"])
        tests = tests.reset_index().merge(
            requirements,
            left_on="satisfies.value",
            right_on="entity",
            how="left",
        ).sort_values("requirement.priority", ascending=False)

        test_results = {}
        for _, row in tests.iterrows():
            entity = row["entity"]

            # Skip when there's no test code
            if not pd.isna(row["code.value"]):
                module_path, test_func_name = row["code.value"].rsplit(".", 1)
            elif not pd.isna(row["FunctionDef"]):
                pass

            try:
                # Get the test function from the code path
                module = importlib.import_module(module_path)
                test_func = getattr(module, test_func_name)

                # Call the test function if it is callable
                test_result: pd.DataFrame = test_func(self.registry)

                # Store results
                test_results[entity] = test_result
                tests.loc[entity, "test_passed"] = test_result.empty
                tests.loc[entity, "errors"] = ""

                # Print results
                if show:
                    print(f"{entity}:")
                    print(
                        f"requirement: {row['satisfies.value']}    priority: {row['requirement.priority']}"
                    )
                    wrapped_desc = "\n    ".join(
                        textwrap.wrap(str(row["description.value"]), width=76)
                    )
                    print(f"description: {wrapped_desc}")
                    if test_result.empty:
                        print("Test passed!")
                    else:
                        display(test_results[entity])
                    print("")

            # A bare except is okay here because we're logging.
            except Exception as e:  # pylint: disable=W0718
                tests.loc[entity, "errors"] = e

        return tests, test_results
