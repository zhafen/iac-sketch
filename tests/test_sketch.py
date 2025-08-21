import unittest

import pandas as pd

from iac_sketch import sketch


class TestArchitect(unittest.TestCase):

    def setUp(self):
        self.architect = sketch.Architect()

    def test_etl(self):
        registry = self.architect.perform_registry_etl()

        assert "link" in registry
        assert "link" in registry["compinst"].index.get_level_values("entity")

    def test_validate(self):
        self.architect.perform_registry_etl()
        tests, test_results = self.architect.validate_registry()

        expected_tests = [
            "test_fully_designed",
            "test_fully_implemented",
            "test_fully_defined",
            "test_fully_connected",
            "test_no_todos",
        ]
        for test_name in expected_tests:
            assert test_name in test_results, (
                f"Test {test_name} is missing from test_results. "
                f"test_results: {list(test_results.keys())}"
            )
            assert isinstance(test_results[test_name], pd.DataFrame), (
                f"Test results for {test_name} should be a DataFrame, "
                f"got: {test_results[test_name]}"
            )
            assert test_results[
                test_name
            ].empty, (
                f"Test results for {test_name} should be empty, got {test_results[test_name]}"
            )

        assert tests.loc[expected_tests, "test_passed"].all()

class TestArchitectExampleCode(TestArchitect):

    def setUp(self):
        self.architect = sketch.Architect("./tests/test_data/example_manifest/*.yaml")
