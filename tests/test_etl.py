import os
import unittest

import networkx as nx
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
        assert not registry["component"].index.has_duplicates

    def test_extract_twice(self):
        """Running extract twice in a row should yield the same result.
        At the time this test was written, it did not.
        """

        registry = self.extract_sys.extract_entities()
        registry = self.extract_sys.extract_entities()

        assert "component" in registry
        assert "component" in registry.keys()
        assert not registry["component"].index.has_duplicates


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
        assert "is_valid" in new_registry["component_a"].columns
        assert "errors" in new_registry["component_b"].columns
        assert "is_valid" in new_registry["component_b"].columns

    def test_apply_preprocess_transforms(self):

        registry = self.extract_sys.extract_entities()
        registry = self.transform_sys.apply_preprocess_transforms(registry)
        assert registry["compdef"].attrs["is_valid"], registry["compdef"].attrs[
            "errors"
        ]

    def test_apply_preprocess_transforms_different_root_dir(self):
        """Tests are meant to be run from the root directory of the repo,
        but for this test we move into the "tests" directory and then run
        the extraction from there.

        Components
        ----------
        - todo:
            value: >
                This and the previous test should probably be part of a different test
                class that is more comprehensive than "TestTransformSystem"
            priority: 0.1
        """

        os.chdir("tests")

        registry = self.extract_sys.extract_entities(root_dir="..")
        registry = self.transform_sys.apply_preprocess_transforms(registry)
        assert registry["compdef"].attrs["is_valid"], registry["compdef"].attrs[
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
                            "comp_key": 0,
                            "component": {"value": "This entity is a test entity."},
                        },
                        {
                            "entity": "my_other_entity",
                            "comp_key": 0,
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
                    "comp_key": 0,
                    "value": "This entity is a test entity.",
                },
                {
                    "entity": "my_other_entity",
                    "comp_key": 0,
                    "value": "This entity is also a test entity.",
                },
            ]
        ).set_index(["entity", "comp_key"])
        assert_frame_equal(registry["description"], expected)

    def test_component_normalizer_complex(self):
        registry = data.Registry(
            {
                "timestamp": pd.DataFrame(
                    [
                        {
                            "entity": "my_time",
                            "comp_key": 0,
                            "component": {"value": "2023-10-01"},
                        },
                        {
                            "entity": "my_other_time",
                            "comp_key": 0,
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
                    "entity": "my_other_time",
                    "comp_key": 0,
                    "value": "1970-01-01",
                    "seconds": 0.0,
                    "timezone": "UTC",
                },
                {
                    "entity": "my_time",
                    "comp_key": 0,
                    "value": "2023-10-01",
                    "seconds": np.nan,
                    "timezone": np.nan,
                },
            ]
        ).set_index(["entity", "comp_key"])
        assert_frame_equal(actual, expected)

    def test_component_normalizer_for_component_component(self):

        registry = data.Registry(
            {
                "component": pd.DataFrame(
                    [
                        {
                            "entity": "my_component",
                            "comp_key": 0,
                            "component": {
                                "multiplicity": "1",
                            },
                        },
                        {
                            "entity": "my_other_component",
                            "comp_key": 0,
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
                    "comp_key": 0,
                    "multiplicity": "1",
                },
                {
                    "entity": "my_other_component",
                    "comp_key": 0,
                    "multiplicity": pd.NA,
                },
            ]
        ).set_index(["entity", "comp_key"])
        assert_frame_equal(registry["component"], expected)

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
        registry = self.extract_sys.extract_entities(input_yaml=yaml_str)
        registry = self.transform_sys.normalize_components(registry)
        registry = self.transform_sys.extract_compdefs(registry)
        expected = pd.DataFrame(
            [
                {
                    "entity": "my_other_component",
                    # comp_key is set to 4 because there are three components
                    # defined above and one metadata component, so the next is 4
                    "comp_key": "4",
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
                    "is_defined": True,
                    "unparsed_fields": {
                        "my_field [int]": "This is a test field.",
                        "my_other_field [bool]": "This is another test field.",
                    },
                    "is_valid": True,
                    "errors": "",
                    "multiplicity": "1",
                },
                {
                    "entity": "my_simple_component",
                    # comp_key is set to 2 because there is one component
                    # defined above and one metadata component, so the next is 2
                    "comp_key": "2",
                    "fields": {},
                    "is_defined": True,
                    "unparsed_fields": {},
                    "is_valid": True,
                    "errors": "",
                },
                {
                    "entity": "this_is_a_fictional_component",
                    # comp_key is set to 0 because this entity is first defined
                    # during the component definition extraction
                    "comp_key": "0",
                    "fields": {},
                    "is_defined": False,
                    "unparsed_fields": {},
                    "is_valid": False,
                    "errors": "Component definition does not exist. ",
                },
            ]
        ).set_index(["entity", "comp_key"])

        actual = registry["compdef"].copy()

        # Check fields for my_other_component
        my_component_actual_fields = actual.loc["my_other_component", "fields"].iloc[0]
        assert "my_field" in my_component_actual_fields
        assert "my_other_field" in my_component_actual_fields
        for field_name, field in my_component_actual_fields.items():
            assert isinstance(field, data.Field), f"{field_name} is not a Field object"
            assert (
                field.name == field_name
            ), f"{field_name} does not match the field name"

        # Then check the frame
        expected = expected.drop(columns="fields")
        actual = actual.drop(columns="fields").loc[expected.index, expected.columns]
        assert_frame_equal(actual, expected)

    def test_component_validator(self):

        registry = data.Registry({})
        # We do the rare case of setting the components directly
        # This should never be done unless you want to override the indexing
        # and know what you're doing.
        registry.components["compdef"] = pd.DataFrame(
            [
                {
                    "entity": "my_component",
                    "comp_key": 1,
                    "fields": {
                        "entity": data.Field(
                            name="entity",
                            dtype="str",
                        ),
                        "comp_key": data.Field(
                            name="comp_key",
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
                    "is_defined": True,
                    "unparsed_fields": {
                        "my_field [int]": "This is a test field.",
                        "my_other_field [bool]": "This is another test field.",
                    },
                    "is_valid": True,
                    "errors": "",
                    "multiplicity": "0..1",
                },
            ]
        ).set_index("entity")
        registry["my_component"] = pd.DataFrame(
            [
                {
                    "entity": "my_entity",
                    "comp_key": 0.0,
                    "my_field": 42,
                    "my_other_field": True,
                },
                {
                    "entity": "my_other_entity",
                    "comp_key": 1.0,
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
            components_mapping={
                "my_component": data.View("my_component"),
            },
        )

        expected = pd.DataFrame(
            [
                {
                    "entity": "my_entity",
                    "comp_key": 0,
                    "my_field": 42,
                    "my_other_field": True,
                },
                {
                    "entity": "my_other_entity",
                    "comp_key": 1,
                    "my_field": -1,
                    "my_other_field": False,
                },
            ]
        ).set_index("entity")

        actual = registry["my_component"].copy()
        assert actual.attrs["is_valid"], actual.attrs["errors"]

        assert_frame_equal(actual, expected)


class TestSystemTransformers(unittest.TestCase):

    def setUp(self):
        self.test_filename_pattern = "./public/components/*"
        self.extract_sys = etl.ExtractSystem()
        self.transform_sys = etl.TransformSystem()

    def test_links_parser(self):
        registry = data.Registry(
            {
                "links": pd.DataFrame(
                    [
                        {
                            "entity": "my_workflow",
                            "comp_key": "0",
                            "value": "my_first_task --> my_second_task\nmy_second_task --> my_third_task",
                            "link_type": "depended_on_by",
                        },
                        {
                            "entity": "my_other_workflow",
                            "comp_key": "0",
                            "value": "my_first_task --> my_third_task",
                            "link_type": "depended_on_by",
                        },
                    ]
                ),
                "compinst": pd.DataFrame(
                    {
                        "entity": ["my_workflow", "my_other_workflow"],
                        "comp_key": ["0", "0"],
                        "component_type": ["links", "links"],
                    }
                ),
            }
        )

        registry = self.transform_sys.apply_transform(
            registry,
            transform.LinksParser(),
            components_mapping={"link": data.View("links")},
            mode="upsert",
        )

        actual = registry["link"]
        expected = (
            pd.DataFrame(
                [
                    {
                        "entity": "my_workflow",
                        "comp_key": "1",
                        "link_type": "depended_on_by",
                        "source": "my_first_task",
                        "target": "my_second_task",
                    },
                    {
                        "entity": "my_workflow",
                        "comp_key": "2",
                        "link_type": "depended_on_by",
                        "source": "my_second_task",
                        "target": "my_third_task",
                    },
                    {
                        "entity": "my_other_workflow",
                        "comp_key": "1",
                        "link_type": "depended_on_by",
                        "source": "my_first_task",
                        "target": "my_third_task",
                    },
                ]
            )
            .set_index(["entity", "comp_key"])
            .sort_index()
        )
        assert_frame_equal(actual, expected)

    def test_link_collector(self):

        input_yaml = """
        requirement_0:
        - requirement

        test_0:
        - test
        - satisfies: requirement_0

        task_0:
        - task
        - satisfies: requirement_0
        - depended_on_by: task_1

        task_1:
        - task

        task_2:
        - task

        requirement_0_0:
        - requirement
        - parent: requirement_0

        # This entity tests that despite the link_type being depended_on_by,
        # what shows up in the link component is the non-reverse link type.
        # It also checks that we don't duplicate links.
        workflow_0:
        - links:
            value: |
                task_0 --> task_1
                task_1 --> task_2
            link_type: depended_on_by
        """

        registry = self.extract_sys.extract_entities(input_yaml=input_yaml)
        registry = self.transform_sys.apply_preprocess_transforms(registry)
        registry = self.transform_sys.apply_transform(
            registry,
            transform.LinksParser(),
            components_mapping={"link": data.View("links")},
            mode="upsert",
        )
        registry = self.transform_sys.apply_transform(
            registry,
            transform.LinkCollector(),
            components_mapping={"link": data.View("link")},
            mode="upsert",
        )

        actual = registry["link"]

        # comp_keys get set at runtime, so we don't check them here
        expected = (
            pd.DataFrame(
                [
                    {
                        "entity": "requirement_0_0",
                        "comp_key": pd.NA,
                        "link_type": "parent",
                        "source": "requirement_0_0",
                        "target": "requirement_0",
                    },
                    {
                        "entity": "task_0",
                        "comp_key": pd.NA,
                        "link_type": "satisfies",
                        "source": "task_0",
                        "target": "requirement_0",
                    },
                ]
            )
            .set_index(["entity", "comp_key"])
            .sort_index()
        )

        for _, row in expected.iterrows():

            link_df_for_entity = actual.loc[row.name[0]]
            matching_rows = link_df_for_entity.loc[
                link_df_for_entity["link_type"] == row["link_type"]
            ]

            if len(matching_rows) != 1:
                raise ValueError(
                    "Test entities are designed to have exactly one component with the "
                    f"expected link_type, but found {len(matching_rows)} "
                    f"for {row.name[0]} with link_type {row['link_type']}"
                )

            assert matching_rows.iloc[0]["source"] == row["source"]
            assert matching_rows.iloc[0]["target"] == row["target"]

        # Check that we have the expected workflow links
        depends_ons = actual.query("link_type == 'depends_on'")
        assert len(depends_ons.query("source == 'task_1' and target == 'task_0'")) == 1
        assert len(depends_ons.query("source == 'task_2' and target == 'task_1'")) == 1

    def test_build_graph_from_links(self):
        input_yaml = """
        link_0:
        - link:
            source: task_1
            target: task_0
            link_type: depends_on

        link_1:
        - link:
            source: task_3
            target: task_2
            link_type: depends_on
        """

        registry = self.extract_sys.extract_entities(input_yaml=input_yaml)
        registry = self.transform_sys.apply_preprocess_transforms(registry)
        registry = self.transform_sys.build_graph_from_links(registry)
        actual = registry["node"]

        # This is the first time these entities show up, so comp_key is 0 for all
        expected = pd.DataFrame(
            [
                {"entity": "task_0", "comp_key": "0", "connected_component_group": 0},
                {"entity": "task_1", "comp_key": "0", "connected_component_group": 0},
                {"entity": "task_2", "comp_key": "0", "connected_component_group": 1},
                {"entity": "task_3", "comp_key": "0", "connected_component_group": 1},
            ]
        ).set_index("entity")
        assert_frame_equal(actual.loc[expected.index, expected.columns], expected)

        assert hasattr(registry, "graph")
        assert isinstance(registry.graph, nx.DiGraph)

    def test_analyze_requirements(self):
        input_yaml = """
        test_infrastructure:
        - infrastructure

        test_requirement:
        - requirement: test_infrastructure

        child_requirement:
        - requirement
        - parent: test_requirement

        grandchild_requirement:
        - requirement:
            priority: 0.2
        - parent: child_requirement
        """

        registry = self.extract_sys.extract_entities(input_yaml=input_yaml)
        registry = self.transform_sys.apply_preprocess_transforms(registry)
        registry = self.transform_sys.apply_transform(
            registry,
            transform.LinksParser(),
            components_mapping={"link": data.View("links")},
            mode="upsert",
        )
        registry = self.transform_sys.apply_transform(
            registry,
            transform.LinkCollector(),
            components_mapping={"link": data.View("link")},
            mode="upsert",
        )
        registry = self.transform_sys.build_graph_from_links(registry)
        registry = self.transform_sys.apply_transform(
            registry,
            transform.RequirementAnalyzer(),
            components_mapping={"requirement": data.View("requirement")},
            mode="overwrite",
        )
        actual = registry["requirement"]

        # This is the first time these entities show up, so comp_key is 0 for all
        expected = pd.DataFrame(
            [
                {
                    "entity": "test_requirement",
                    "comp_key": "0",
                    "value": "test_infrastructure",
                },
                {
                    "entity": "child_requirement",
                    "comp_key": "0",
                    "value": "test_infrastructure",
                },
                {
                    "entity": "grandchild_requirement",
                    "comp_key": "0",
                    "value": "test_infrastructure",
                },
            ]
        ).set_index("entity")
        assert_frame_equal(actual.loc[expected.index, expected.columns], expected)
