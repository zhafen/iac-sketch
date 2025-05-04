import unittest

from iac_sketch import sketch


class TestArchitect(unittest.TestCase):

    def setUp(self):
        self.test_data_dir = "./public/components"
        self.architect = sketch.Architect(self.test_data_dir)

    def test_parse(self):
        registry = self.architect.parse()

        assert "component" in registry.components
        assert "link" in registry.components["component"]["entity"].values
        assert "data" not in registry.components

