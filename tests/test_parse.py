import unittest

import pandas as pd

from iac_sketch import parse


class TestParser(unittest.TestCase):

    def setUp(self):
        self.test_data_dir = "./public/components"
        self.parser = parse.Parser(self.test_data_dir)

    def test_extract(self):

        self.parser.extract()

        assert "component" in self.parser.entities.index

    def test_transform(self):

        self.parser.extract()
        self.parser.transform()

        assert "component" in self.parser.components.keys()
        assert "link" in self.parser.components["component"].index

        # The entity component should record every entity
        assert (
            ~pd.Series(self.parser.entities.keys()).isin(
                self.parser.components["entity"].index
            )
        ).sum() == 0
