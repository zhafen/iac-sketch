import unittest

from iac_sketch import sketch


class TestArchitect(unittest.TestCase):

    def setUp(self):
        self.test_data_dir = "./public/components"
        self.architect = sketch.Architect(self.test_data_dir)

    def test_etl(self):
        registry = self.architect.perform_registry_etl()

        assert "component" in registry.components
        assert "link" in registry.components["component"]["entity"].values

