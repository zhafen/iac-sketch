import unittest

from iac_sketch import sketch


class TestArchitect(unittest.TestCase):

    def setUp(self):
        self.test_pattern = "./public/components/*.yaml"
        self.architect = sketch.Architect(self.test_pattern)

    def test_etl(self):
        registry = self.architect.perform_registry_etl()

        assert "link" in registry
        assert "link" in registry["compinst"].index.get_level_values("entity")

