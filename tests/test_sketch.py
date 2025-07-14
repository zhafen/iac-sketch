import unittest

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

        assert is_valid
        assert len(invalids) > 0

