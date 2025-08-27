import importlib
import os
import sys
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

        Components
        ----------
        - status: in production
        - satisfies: can_perform_registry_etl
        - todo: >
            Point to the unit test for this, instead of checking the status listed in
            the docstring.
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
        test_kwargs: dict[str, dict] = {},
        show: bool = True,
        captured_exceptions = Exception,
        print_width: int = 80,
    ) -> tuple[bool, dict[str, pd.DataFrame]]:
        """

        Components
        ----------
        - status: in production
        - satisfies: can_execute_tests
        - todo: >
            Point to the unit test for this, instead of checking the status listed in
            the docstring.
        - todo: >
            Currently we're only set up to run tests that are not part of a class.
            We may want to hook into pytest to extend the functionality, or we could
            just add a minor addition to check if the module is a parent and if so,
            run that.
        - todo: >
            Tests that are imported as Python code are currently run as if they were
            solitary scripts, and do not work if there's a relative import
            in the module. Fix this?
        """

        # Prepare summary dataframe
        tests = self.registry.view(["test", "code", "satisfies", "FunctionDef"])
        tests["errors"] = pd.NA
        tests["test_passed"] = pd.NA

        # Join requirements
        requirements = self.registry.view(["requirement", "description"])
        tests = (
            tests.reset_index()
            .merge(
                requirements,
                left_on="satisfies.value",
                right_on="entity",
                how="left",
            )
            .sort_values(
                "requirement.priority",
                ascending=False,
            )
            .set_index("entity")
        )

        test_results = {}
        for entity, row in tests.iterrows():

            # Very generous exception block because we're logging errors
            try:
                # Try loading the test code from the code path
                if not pd.isna(row["code.value"]):
                    module_path, test_func_name = row["code.value"].rsplit()
                # If this is a function itself, we load the code from its module
                elif not pd.isna(row["FunctionDef.name"]):
                    split_entity = entity.rsplit(".", 1)
                    module_filepath, test_func_name = split_entity
                    module_filepath = os.path.abspath(
                        f"{self.root_dir}/{module_filepath}"
                    )
                    module_dir, module_path = os.path.split(module_filepath)
                    sys.path.append(module_dir)
                # Skip when there's no test code
                else:
                    test_results[entity] = pd.DataFrame(
                        [{"error": "No test code found."}]
                    )
                    tests.loc[entity, "test_passed"] = False
                    tests.loc[entity, "errors"] = "ImportError: No test code found."
                    continue

                # Call the test function
                module = importlib.import_module(module_path)
                test_func = getattr(module, test_func_name)
                test_args_i = test_kwargs.get(entity, {})
                test_result: pd.DataFrame = test_func(self.registry, **test_args_i)

                # Store results
                test_results[entity] = test_result
                tests.loc[entity, "test_passed"] = test_result.empty
                tests.loc[entity, "errors"] = ""

            # A bare except is okay here because we're logging.
            except captured_exceptions as e:  # pylint: disable=W0718
                tests.loc[entity, "test_passed"] = False
                tests.loc[entity, "errors"] = e

            # Print results
            if show:
                print(f"entity: {entity}")
                print(
                    f"requirement: {row['satisfies.value']}\npriority: {row['requirement.priority']}"
                )
                wrapped_desc = "\n    ".join(
                    textwrap.wrap(str(row["description.value"]), width=print_width - 4)
                )
                print(f"description:\n    {wrapped_desc}")
                test_passed = tests.loc[entity, 'test_passed']
                print(f"test_passed: {test_passed}")
                if (error := tests.loc[entity, "errors"]) != "":
                    print(f"errors: {error}")
                if not test_passed and entity in test_results:
                    print("failed_components:")
                    display(test_results[entity])
                print("-" * print_width + "\n")

        return tests, test_results
