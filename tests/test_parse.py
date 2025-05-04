import unittest

from iac_sketch import parse


class TestParser(unittest.TestCase):

    def setUp(self):
        self.test_data_dir = "./public/components"
        self.parser = parse.ParseSystem()

    def test_extract(self):

        entities = self.parser.extract(self.test_data_dir)

        assert "component" in entities["entity"].values

    def test_transform(self):

        entities = self.parser.extract(self.test_data_dir)
        comps = self.parser.transform(entities)

        assert "component" in comps
        assert "link" in comps["component"]["entity"].values
        assert "data" not in comps