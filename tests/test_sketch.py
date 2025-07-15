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
        is_valid, invalids = self.architect.validate_registry()

        expected_tests = [
            "test_fully_designed",
            "test_fully_implemented",
            "test_fully_defined",
            "test_fully_connected",
        ]
        for test_name in expected_tests:
            assert test_name in invalids, (
                f"Test {test_name} is missing from invalids. "
                f"invalids: {list(invalids.keys())}"
            )
            assert isinstance(invalids[test_name], pd.DataFrame), (
                f"Invalids for {test_name} should be a DataFrame, "
                f"got {type(invalids[test_name])}"
            )
            assert invalids[
                test_name
            ].empty, (
                f"Invalids for {test_name} should be empty, got {invalids[test_name]}"
            )

        assert is_valid
