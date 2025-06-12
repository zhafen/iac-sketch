# Dummy transformer for testing
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import StandardScaler

import unittest

import numpy as np
import pandas as pd
from pandas.testing import assert_frame_equal

from iac_sketch import data, etl, transform


class TestExtractSystem(unittest.TestCase):

    def setUp(self):
        self.test_filename_pattern = "./public/components/*.yaml"
        self.extract_sys = etl.ExtractSystem()

    def test_extract(self):

        registry = self.extract_sys.extract_entities(self.test_filename_pattern)

        assert "component" in registry
        assert "component" in registry.keys()

class TestTransformSystem(unittest.TestCase):

    def setUp(self):
        self.test_filename_pattern = "./public/components/*"
        self.extract_sys = etl.ExtractSystem()
        self.transform_sys = etl.TransformSystem()

    def test_apply_transform(self):
        registry = data.Registry({
            "component_a": pd.DataFrame({
                "entity": ["a", "b"],
                "value": [1.0, 2.0]
            }).set_index("entity"),
            "component_b": pd.DataFrame({
                "entity": ["c", "d"],
                "value": [10.0, 20.0]
            }).set_index("entity"),
        })

        new_registry = self.transform_sys.apply_transform(
            registry,
            transform.LogPrepper(),
            apply_components=["component_a", "component_b"]
        )

        assert "errors" in new_registry["component_a"].columns
        assert "valid" in new_registry["component_a"].columns
        assert "errors" in new_registry["component_b"].columns
        assert "valid" in new_registry["component_b"].columns

    # def test_parsecomp_component_and_validate(self):

    #     registry = self.extract_sys.extract_entities(self.test_filename_pattern)
    #     transform_sys = etl.TransformSystem()
    #     registry = transform_sys.apply_transforms(registry, [])  # Replace [] with actual transforms if needed

    #     comp_df = registry["component"]
    #     comp_def = registry["component"].loc["component"]
    #     assert "valid_data" in comp_df.columns
    #     assert "valid_data_message" in comp_df.columns
    #     assert comp_def["valid_data"]

    def test_component_normalizer(self):
        registry = data.Registry(
            {
                "description": pd.DataFrame(
                    [
                        {
                            "entity": "my_entity",
                            "comp_ind": 0,
                            "component": "This entity is a test entity.",
                        },
                        {
                            "entity": "my_other_entity",
                            "comp_ind": 0,
                            "component": "This entity is also a test entity.",
                        },
                    ]
                )
            }
        )
        registry = self.transform_sys.apply_transform(
            registry,
            transform.ComponentNormalizer(),
        )
        expected = pd.DataFrame(
            [
                {
                    "entity": "my_entity",
                    "comp_ind": 0,
                    "value": "This entity is a test entity.",
                },
                {
                    "entity": "my_other_entity",
                    "comp_ind": 0,
                    "value": "This entity is also a test entity.",
                },
            ]
        )
        assert_frame_equal(registry["description"], expected)

    def test_component_normalizer_complex(self):
        registry = data.Registry(
            {
                "timestamp": pd.DataFrame(
                    [
                        {
                            "entity": "my_time",
                            "comp_ind": 0,
                            "component": "2023-10-01",
                        },
                        {
                            "entity": "my_other_time",
                            "comp_ind": 0,
                            "component": {
                                "value": "1970-01-01",
                                "seconds": 0,
                                "timezone": "UTC",
                            },
                        },
                    ]
                )
            }
        )
        registry = self.transform_sys.apply_transform(
            registry,
            transform.ComponentNormalizer(),
        )
        actual = registry["timestamp"]
        expected = pd.DataFrame(
            [
                {
                    "entity": "my_time",
                    "comp_ind": 0,
                    "value": "2023-10-01",
                    "seconds": np.nan,
                    "timezone": np.nan,
                },
                {
                    "entity": "my_other_time",
                    "comp_ind": 0,
                    "value": "1970-01-01",
                    "seconds": 0.0,
                    "timezone": "UTC",
                },
            ]
        )
        assert_frame_equal(actual, expected)

    def test_component_normalizer_for_component_def(self):

        registry = data.Registry(
            {
                "component": pd.DataFrame(
                    [
                        {
                            "entity": "my_component",
                            "comp_ind": 0,
                            "component": {
                                "multiplicity": "1",
                            },
                        },
                        {
                            "entity": "my_other_component",
                            "comp_ind": 0,
                            "component": pd.NA,
                        }
                    ]
                )
            }
        )
        registry = self.transform_sys.apply_transform(
            registry,
            transform.ComponentNormalizer(),
        )
        expected = pd.DataFrame(
            [
                {
                    "entity": "my_component",
                    "comp_ind": 0,
                    "multiplicity": "1",
                    "value": pd.NA,
                },
                {
                    "entity": "my_other_component",
                    "comp_ind": 0,
                    "multiplicity": pd.NA,
                    "value": pd.NA,
                }
            ]
        )
        assert_frame_equal(registry["component"], expected)



class TestParseComponentTypes(unittest.TestCase):

    def setUp(self):
        self.test_filename_pattern = "./public/components"
        self.extract_sys = etl.ExtractSystem()
        self.transform_sys = etl.TransformSystem()

    def test_parsecomp_component(self):
        yaml_str = """
            my_simple_component:
            - component

            my_other_component:
            - component:
                multiplicity: "1"
            - fields:
                my_field [int]: This is a test field.
                my_other_field [bool]: This is another test field.
        """
        registry = self.extract_sys.extract_entities_from_yaml(yaml_str)
        registry = self.transform_sys.base_transform(registry)
        expected = pd.DataFrame(
            [
                # the component and data entities are defined by use
                {
                    "entity": "component",
                    "comp_ind": np.nan,
                    "fields_comp_ind": np.nan,
                    "fields": np.nan,
                    "defined": False,
                    "unparsed_fields": np.nan,
                    "valid_def": False,
                    "valid_def_message": "undefined",
                },
                {
                    "entity": "fields",
                    "comp_ind": np.nan,
                    "fields_comp_ind": np.nan,
                    "fields": np.nan,
                    "defined": False,
                    "unparsed_fields": np.nan,
                    "valid_def": False,
                    "valid_def_message": "undefined",
                },
                {
                    "entity": "metadata",
                    "comp_ind": np.nan,
                    "fields_comp_ind": np.nan,
                    "fields": np.nan,
                    "defined": False,
                    "unparsed_fields": np.nan,
                    "valid_def": False,
                    "valid_def_message": "undefined",
                },
                {
                    "entity": "my_other_component",
                    "comp_ind": 0,
                    "fields_comp_ind": 1,
                    "fields": {
                        "my_field": data.Field(
                            "my_field", "int", "This is a test field."
                        ),
                        "my_other_field": data.Field(
                            "my_other_field", "bool", "This is another test field."
                        ),
                    },
                    "defined": True,
                    "unparsed_fields": {
                        "my_field [int]": "This is a test field.",
                        "my_other_field [bool]": "This is another test field.",
                    },
                    "valid_def": True,
                    "valid_def_message": "",
                    "multiplicity": "1",
                },
                {
                    "entity": "my_simple_component",
                    "comp_ind": 0,
                    "fields_comp_ind": np.nan,
                    "fields": np.nan,
                    "defined": True,
                    "unparsed_fields": np.nan,
                    "valid_def": True,
                    "valid_def_message": "",
                },
            ]
        ).set_index("entity")
        actual = registry["component"].copy()
        expected = expected.drop(columns="fields")
        actual = actual.drop(columns="fields")[expected.columns]
        assert_frame_equal(actual, expected)

    def test_parsecomp_links(self):
        yaml_str = """
            my_workflow:
            - links:
                links: |
                    my_first_task --> my_second_task
                    my_second_task --> my_third_task
                link_type: dependency
            my_other_workflow:
            - links:
                links: |
                    my_first_task --> my_third_task
                link_type: dependency
        """
        registry = self.extract_sys.extract_entities_from_yaml(yaml_str)
        registry = self.transform_sys.base_transform(registry)
        assert registry["component"].loc["links", "valid_data"]
        actual = self.transform_sys.parsecomp_links(registry)
        expected = pd.DataFrame(
            [
                {
                    "entity": "my_workflow",
                    "comp_ind": 2,
                    "link_type": "dependency",
                    "source": "my_first_task",
                    "target": "my_second_task",
                },
                {
                    "entity": "my_workflow",
                    "comp_ind": 3,
                    "link_type": "dependency",
                    "source": "my_second_task",
                    "target": "my_third_task",
                },
                {
                    "entity": "my_other_workflow",
                    "comp_ind": 2,
                    "link_type": "dependency",
                    "source": "my_first_task",
                    "target": "my_third_task",
                },
            ]
        )
        assert_frame_equal(actual, expected)
        assert registry["metadata"]["n_comps"].max() == 4