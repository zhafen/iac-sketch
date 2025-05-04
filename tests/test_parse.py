import unittest

import numpy as np
import pandas as pd
from pandas.testing import assert_frame_equal

from iac_sketch import parse


class TestParser(unittest.TestCase):

    def setUp(self):
        self.test_data_dir = "./public/components"
        self.parse_sys = parse.ParseSystem()

    def test_extract(self):

        entities = self.parse_sys.extract(self.test_data_dir)

        assert "component" in entities["entity"].values

    def test_transform(self):

        entities = self.parse_sys.extract(self.test_data_dir)
        comps = self.parse_sys.transform(entities)

        assert "component" in comps
        assert "link" in comps["component"]["entity"].values
        assert "data" not in comps


class TestParseGeneralComponents(unittest.TestCase):

    def setUp(self):
        self.test_data_dir = "./public/components"
        self.parse_sys = parse.ParseSystem()

    def test_parse_general_component(self):

        entities = pd.DataFrame(
            [
                {
                    "entity": "my_entity",
                    "comp_ind": 0,
                    "component_entity": "description",
                    "component": "This entity is a test entity.",
                },
                {
                    "entity": "my_other_entity",
                    "comp_ind": 0,
                    "component_entity": "description",
                    "component": "This entity is also a test entity.",
                },
            ]
        )

        entities_by_group = entities.groupby("component_entity")
        actual = self.parse_sys.general_parse_component(
            "description", entities_by_group
        )

        expected = pd.DataFrame(
            [
                {
                    "entity": "my_entity",
                    "comp_ind": 0,
                    "description": "This entity is a test entity.",
                },
                {
                    "entity": "my_other_entity",
                    "comp_ind": 0,
                    "description": "This entity is also a test entity.",
                },
            ]
        )
        assert_frame_equal(actual, expected)

    def test_parse_general_component_complex(self):

        entities = pd.DataFrame(
            [
                {
                    "entity": "my_time",
                    "comp_ind": 0,
                    "component_entity": "timestamp",
                    "component": "2023-10-01",
                },
                {
                    "entity": "my_other_time",
                    "comp_ind": 0,
                    "component_entity": "timestamp",
                    "component": {
                        "timestamp": "1970-01-01",
                        "seconds": 0,
                        "timezone": "UTC",
                    }
                },
            ]
        )

        entities_by_group = entities.groupby("component_entity")
        actual = self.parse_sys.general_parse_component(
            "timestamp", entities_by_group
        )

        expected = pd.DataFrame(
            [
                {
                    "entity": "my_time",
                    "comp_ind": 0,
                    "timestamp": "2023-10-01",
                    "seconds": np.nan,
                    "timezone": np.nan,
                },
                {
                    "entity": "my_other_time",
                    "comp_ind": 0,
                    "timestamp": "1970-01-01",
                    "seconds": 0.0,
                    "timezone": "UTC",
                },
            ]
        )
        assert_frame_equal(actual, expected)


class TestParseComponentTypes(unittest.TestCase):

    def setUp(self):
        self.test_data_dir = "./public/components"
        self.parse_sys = parse.ParseSystem()

    def test_parse_component_component(self):
        entities = self.parse_sys.extract(self.test_data_dir)
        comps = self.parse_sys.transform(entities)

        assert "component" in comps
        assert "link" in comps["component"]["entity"].values
        assert "data" not in comps
