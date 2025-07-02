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
        registry = data.Registry(
            {
                "component_a": pd.DataFrame(
                    {"entity": ["a", "b"], "value": [1.0, 2.0]}
                ).set_index("entity"),
                "component_b": pd.DataFrame(
                    {"entity": ["c", "d"], "value": [10.0, 20.0]}
                ).set_index("entity"),
            }
        )

        new_registry = self.transform_sys.apply_transform(
            registry,
            transform.LogPrepper(),
            components_mapping={
                "component_a": data.View("component_a"),
                "component_b": data.View("component_b"),
            },
        )

        assert "errors" in new_registry["component_a"].columns
        assert "valid" in new_registry["component_a"].columns
        assert "errors" in new_registry["component_b"].columns
        assert "valid" in new_registry["component_b"].columns

    def test_apply_preprocess_transforms(self):

        registry = self.extract_sys.extract_entities()
        registry = self.transform_sys.apply_preprocess_transforms(registry)
        assert registry["compdef"].attrs["valid"], registry["compdef"].attrs[
            "errors"
        ]

class TestPreprocessTransformers(unittest.TestCase):

    def setUp(self):
        self.test_filename_pattern = "./public/components/*"
        self.extract_sys = etl.ExtractSystem()
        self.transform_sys = etl.TransformSystem()

    def test_component_normalizer(self):
        registry = data.Registry(
            {
                "description": pd.DataFrame(
                    [
                        {
                            "entity": "my_entity",
                            "comp_ind": 0,
                            "component": {"value": "This entity is a test entity."},
                        },
                        {
                            "entity": "my_other_entity",
                            "comp_ind": 0,
                            "component": {
                                "value": "This entity is also a test entity."
                            },
                        },
                    ]
                )
            }
        )
        registry = self.transform_sys.apply_transform(
            registry,
            transform.ComponentNormalizer(),
            components_mapping={"description": data.View("description")},
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
                            "component": {"value": "2023-10-01"},
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
            components_mapping={"timestamp": data.View("timestamp")},
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
                        },
                    ]
                )
            }
        )
        registry = self.transform_sys.normalize_components(registry)
        expected = pd.DataFrame(
            [
                {
                    "entity": "my_component",
                    "comp_ind": 0,
                    "multiplicity": "1",
                },
                {
                    "entity": "my_other_component",
                    "comp_ind": 0,
                    "multiplicity": pd.NA,
                },
            ]
        )
        assert_frame_equal(registry["compdef"], expected)

    def test_component_def_extractor(self):
        yaml_str = """
            my_simple_component:
            - component

            my_other_component:
            - component:
                multiplicity: "1"
            - fields:
                my_field [int]: This is a test field.
                my_other_field [bool]: This is another test field.
            - this_is_a_fictional_component
        """
        registry = self.extract_sys.extract_entities(input=yaml_str)
        registry = self.transform_sys.normalize_components(registry)
        registry = self.transform_sys.extract_compdefs(registry)
        expected = pd.DataFrame(
            [
                {
                    "entity": "my_other_component",
                    "comp_ind": 0.0,
                    "comp_ind_fields": 1.0,
                    "fields": {
                        "my_field": data.Field(
                            name="my_field",
                            dtype="int",
                            description="This is a test field.",
                        ),
                        "my_other_field": data.Field(
                            name="my_other_field",
                            dtype="bool",
                            description="This is another test field.",
                        ),
                    },
                    "defined": True,
                    "unparsed_fields": {
                        "my_field [int]": "This is a test field.",
                        "my_other_field [bool]": "This is another test field.",
                    },
                    "valid": True,
                    "errors": "",
                    "multiplicity": "1",
                },
                {
                    "entity": "my_simple_component",
                    "comp_ind": 0.0,
                    "comp_ind_fields": np.nan,
                    "fields": {},
                    "defined": True,
                    "unparsed_fields": {},
                    "valid": True,
                    "errors": "",
                },
                {
                    "entity": "this_is_a_fictional_component",
                    "comp_ind": np.nan,
                    "comp_ind_fields": np.nan,
                    "fields": {},
                    "defined": False,
                    "unparsed_fields": {},
                    "valid": False,
                    "errors": "Component definition does not exist. ",
                },
            ]
        ).set_index("entity")
        actual = registry["compdef"].copy()
        expected = expected.drop(columns="fields")
        actual = actual.drop(columns="fields").loc[expected.index, expected.columns]
        assert_frame_equal(actual, expected)

    def test_component_validator(self):

        registry = data.Registry({})
        registry["compdef"] = pd.DataFrame(
            [
                {
                    "entity": "my_component",
                    "comp_ind": 0.0,
                    "comp_ind_fields": 1.0,
                    "fields": {
                        "entity": data.Field(
                            name="entity",
                            dtype="str",
                        ),
                        "comp_ind": data.Field(
                            name="comp_ind",
                            dtype="int",
                            coerce=True,
                        ),
                        "my_field": data.Field(
                            name="my_field",
                            dtype="int",
                            description="This is a test field.",
                        ),
                        "my_other_field": data.Field(
                            name="my_other_field",
                            dtype="bool",
                            description="This is another test field.",
                            coerce=True,
                        ),
                    },
                    "defined": True,
                    "unparsed_fields": {
                        "my_field [int]": "This is a test field.",
                        "my_other_field [bool]": "This is another test field.",
                    },
                    "valid": True,
                    "errors": "",
                    "multiplicity": "0..1",
                },
            ]
        ).set_index("entity", drop=False)
        registry["my_component"] = pd.DataFrame(
            [
                {
                    "entity": "my_entity",
                    "comp_ind": 0.0,
                    "my_field": 42,
                    "my_other_field": True,
                },
                {
                    "entity": "my_other_entity",
                    "comp_ind": 1.0,
                    "my_field": -1,
                    "my_other_field": 0,
                },
            ]
        )

        # We don't use TransformSystem.normalize_components here because
        # we want to test the ComponentValidator directly for one definition.
        registry = self.transform_sys.apply_transform(
            registry,
            transform.ComponentValidator(),
            components_mapping={"my_component": data.View("my_component")},
        )
        expected = pd.DataFrame(
            [
                {
                    "entity": "my_entity",
                    "comp_ind": 0,
                    "my_field": 42,
                    "my_other_field": True,
                },
                {
                    "entity": "my_other_entity",
                    "comp_ind": 1,
                    "my_field": -1,
                    "my_other_field": False,
                },
            ]
        ).set_index("entity", drop=False)
        actual = registry["my_component"].copy()
        assert_frame_equal(actual, expected)

class TestSystemTransformers(unittest.TestCase):

    def setUp(self):
        self.test_filename_pattern = "./public/components/*"
        self.extract_sys = etl.ExtractSystem()
        self.transform_sys = etl.TransformSystem()


    def test_parsecomp_links(self):
        registry = data.Registry({
            "links": pd.DataFrame(
                [
                    {
                        "entity": "my_workflow",
                        "comp_ind": 0,
                        "links": "my_first_task --> my_second_task\nmy_second_task --> my_third_task",
                        "link_type": "dependency",
                    },
                    {
                        "entity": "my_other_workflow",
                        "comp_ind": 0,
                        "links": "my_first_task --> my_third_task",
                        "link_type": "dependency",
                    },
                ]
            ).set_index(["entity", "comp_ind"], drop=False)
        })

        registry = self.transform_sys.apply_transform(
            registry,
            transform.LinksParser(),
            components_mapping={"link": data.View("links")},
            mode="append",
        )

        actual = registry["link"]
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
        ).set_index("entity", drop=False)
        assert_frame_equal(actual, expected)
        assert registry["metadata"]["n_comps"].max() == 4
