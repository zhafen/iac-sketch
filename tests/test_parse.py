import unittest

import numpy as np
import pandas as pd
from pandas.testing import assert_frame_equal

from iac_sketch import data, parse


class TestParser(unittest.TestCase):

    def setUp(self):
        self.test_data_dir = "./public/components"
        self.parse_sys = parse.ParseSystem()

    def test_extract(self):

        registry = self.parse_sys.extract(self.test_data_dir)

        assert "component" in registry

    def test_transform(self):

        registry = self.parse_sys.extract(self.test_data_dir)
        registry = self.parse_sys.transform(registry)

        assert "component" in registry
        assert "link" in registry["component"]["entity"].values
        assert "data" not in registry


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
        actual = self.parse_sys.general_parsecomp(
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
                    },
                },
            ]
        )

        entities_by_group = entities.groupby("component_entity")
        actual = self.parse_sys.general_parsecomp("timestamp", entities_by_group)

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

    def test_parsecomp_component(self):

        entities = pd.DataFrame(
            [
                {
                    "entity": "my_simple_component",
                    "comp_ind": 0,
                    "component_entity": "component",
                    "component": pd.NA,
                },
                {
                    "entity": "my_other_component",
                    "comp_ind": 0,
                    "component_entity": "component",
                    "component": pd.NA,
                },
                {
                    "entity": "my_other_component",
                    "comp_ind": 1,
                    "component_entity": "data",
                    "component":
                        {
                            "my_field [int]": "This is a test field.",
                            "my_other_field [bool]": "This is another test field.",
                        },
                },
            ]
        )

        entities_by_group = entities.groupby("component_entity")
        actual = self.parse_sys.parsecomp_component(entities_by_group)

        expected = pd.DataFrame(
            [
                # the component and data entities are defined by use
                {
                    "entity": "component",
                    "comp_ind": np.nan,
                    "data_comp_ind": np.nan,
                    "data": np.nan,
                    "defined": False,
                    "unparsed_data": np.nan,
                    "valid": False,
                    "valid_message": "undefined",
                },
                {
                    "entity": "data",
                    "comp_ind": np.nan,
                    "data_comp_ind": np.nan,
                    "data": np.nan,
                    "defined": False,
                    "unparsed_data": np.nan,
                    "valid": False,
                    "valid_message": "undefined",
                },
                {
                    "entity": "my_other_component",
                    "comp_ind": 0,
                    "data_comp_ind": 1,
                    "data": {
                        "my_field": data.Field("my_field", "int", "This is a test field."),
                        "my_other_field": data.Field("my_other_field", "bool", "This is another test field."),
                    },
                    "defined": True,
                    "unparsed_data": {
                        "my_field [int]": "This is a test field.",
                        "my_other_field [bool]": "This is another test field.",
                    },
                    "valid": True,
                    "valid_message": "",
                },
                {
                    "entity": "my_simple_component",
                    "comp_ind": 0,
                    "data_comp_ind": np.nan,
                    "data": np.nan,
                    "defined": True,
                    "unparsed_data": np.nan,
                    "valid": True,
                    "valid_message": "",
                },
            ]
        )
        actual = actual.drop(columns="data")
        expected = expected.drop(columns="data")
        assert_frame_equal(actual, expected)

    def test_parsecomp_links(self):

        entities = pd.DataFrame(
            [
                {
                    "entity": "my_workflow",
                    "comp_ind": 0,
                    "component_entity": "links",
                    "component": {
                        "edges": (
                            """my_first_task --> my_second_task
                            my_second_task --> my_third_task
                            """
                        ),
                        "link_type": "dependency",
                    }
                },
            ]
        )

        entities_by_group = entities.groupby("component_entity")
        actual = self.parse_sys.parsecomp_links(entities_by_group)

        expected = pd.DataFrame(
            [
                {
                    "entity": "my_workflow",
                    "comp_ind": 1,
                    "source": "my_first_task",
                    "target": "my_second_task",
                    "link_type": "dependency",
                },
                {
                    "entity": "my_workflow",
                    "comp_ind": 2,
                    "source": "my_second_task",
                    "target": "my_third_task",
                    "link_type": "dependency",
                },
            ]
        )
        assert_frame_equal(actual, expected)
