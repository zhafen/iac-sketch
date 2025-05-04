import unittest

from iac_sketch import architect


class TestArchitect(unittest.TestCase):

    def setUp(self):
        self.test_data_dir = "./public/components"
        self.architect = architect.Architect(self.test_data_dir)

    def test_parse(self):
        self.architect.parse()

        assert "component" in self.architect.comps
        assert "link" in self.architect.comps["component"]["entity"].values
        assert "data" not in self.architect.comps