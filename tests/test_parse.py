import unittest

from iac_sketch import parse


class TestParser(unittest.TestCase):

    def setUp(self):
        self.test_data_dir = "./public/components"
        self.parser = parse.Parser(self.test_data_dir)

    def test_extract(self):

        self.parser.extract()

        assert "component" in self.parser.entities["entity"].values

    def test_transform(self):

        self.parser.extract()
        self.parser.transform()

        assert "component" in self.parser.comps
        assert "link" in self.parser.comps["component"]["entity"].values
        assert "data" not in self.parser.comps