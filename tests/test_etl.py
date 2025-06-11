# Dummy transformer for testing
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import StandardScaler

import unittest

import numpy as np
import pandas as pd
from pandas.testing import assert_frame_equal

from iac_sketch import data, etl


class TestExtractSystem(unittest.TestCase):

    def setUp(self):
        self.test_filename_pattern = "./public/components/*.yaml"
        self.extract_sys = etl.ExtractSystem()

    def test_extract(self):

        registry = self.extract_sys.extract_entities(self.test_filename_pattern)

        assert "component" in registry

class TestTransformSystem(unittest.TestCase):

    def setUp(self):
        self.test_filename_pattern = "./public/components/*"
        self.extract_sys = etl.ExtractSystem()
        self.transform_sys = etl.TransformSystem()
class TestApplyTransform(unittest.TestCase):

    def setUp(self):
        self.transform_sys = etl.TransformSystem()

    def test_apply_transform(self):
        registry = data.Registry({
            "fit_component": pd.DataFrame({
                "entity": ["a", "b"],
                "value": [1.0, 2.0]
            }).set_index("entity"),
            "other": pd.DataFrame({
                "entity": ["c", "d"],
                "value": [10.0, 20.0]
            }).set_index("entity"),
        })

        transformer = StandardScaler()
        new_registry = self.transform_sys.apply_transform(
            registry,
            transformer,
            fit_components="fit_component",
            apply_components=["fit_component", "other"]
        )

        # StandardScaler should standardize the 'value' column
        # For 'component', mean=1.5, std=0.5, so values become [-1, 1]
        comp_values = new_registry["fit_component"]["value"].values
        np.testing.assert_allclose(comp_values, [-1.0, 1.0], atol=1e-6)

        # For 'other', values are transformed using the same scaler
        # (10-1.5)/0.5 = 17, (20-1.5)/0.5 = 37
        other_values = new_registry["other"]["value"].values
        np.testing.assert_allclose(other_values, [17.0, 37.0], atol=1e-6)

    # def test_parsecomp_component_and_validate(self):

    #     registry = self.extract_sys.extract_entities(self.test_filename_pattern)
    #     transform_sys = etl.TransformSystem()
    #     registry = transform_sys.apply_transforms(registry, [])  # Replace [] with actual transforms if needed

    #     comp_df = registry["component"]
    #     comp_def = registry["component"].loc["component"]
    #     assert "valid_data" in comp_df.columns
    #     assert "valid_data_message" in comp_df.columns
    #     assert comp_def["valid_data"]

class TestParseGeneralComponents(unittest.TestCase):

    def setUp(self):
        self.test_filename_pattern = "./public/components"
        self.extract_sys = etl.ExtractSystem()
        self.transform_sys = etl.TransformSystem()

    def test_parse_general_component(self):
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
        actual = self.transform_sys.base_parsecomp("description", registry)
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
                                "timestamp": "1970-01-01",
                                "seconds": 0,
                                "timezone": "UTC",
                            },
                        },
                    ]
                )
            }
        )
        actual = self.transform_sys.base_parsecomp("timestamp", registry)
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