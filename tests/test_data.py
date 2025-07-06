import unittest

import pandas as pd
from pandera import dtypes
from pandera.engines import pandas_engine

from iac_sketch import data


class TestField(unittest.TestCase):

    def test_default(self):

        field_key = "my_field [int]"
        field_value = "This is my field"

        field = data.Field.from_kv_pair(field_key, field_value)
        assert field.name == "my_field"
        assert dtypes.Int().check(field.dtype)
        assert field.description == "This is my field"
        assert field.multiplicity == "0..*"

    def test_dict_provided(self):

        field_key = "my_field [int]"
        field_value = {
            "description": "This is my field",
            "multiplicity": "0..1",
        }

        field = data.Field.from_kv_pair(field_key, field_value)
        assert field.name == "my_field"
        assert dtypes.Int().check(field.dtype)
        assert field.description == "This is my field"
        assert field.multiplicity == "0..1"

    def test_multiplicity_in_brackets(self):

        field_key = "my_field [int|1..1]"
        field_value = "This is my field"

        field = data.Field.from_kv_pair(field_key, field_value)
        assert field.name == "my_field"
        assert dtypes.Int().check(field.dtype)
        assert field.description == "This is my field"
        assert field.multiplicity == "1..1"

    def test_nested_brackets(self):

        field_key = "my_field [dict[str, str]]"
        field_value = "This is my field"

        field = data.Field.from_kv_pair(field_key, field_value)
        assert field.name == "my_field"
        assert field.dtype is None
        assert field.dtype_str == "dict[str, str]"
        assert field.description == "This is my field"
        assert field.multiplicity == "0..*"

    def test_default_provided(self):

        field_key = "my_field [str] = 0..*"
        field_value = "This is my field"

        field = data.Field.from_kv_pair(field_key, field_value)
        assert field.name == "my_field"
        assert pandas_engine.Engine.dtype(str).check(field.dtype)
        assert field.description == "This is my field"
        assert field.default == "0..*"

class TestRegistry(unittest.TestCase):
    def test_view_multiple_simple(self):
        components = {
            "comp1": pd.DataFrame({
                "entity": ["entity1", "entity2"],
                "comp_ind": [0, 0],
                "field1": [1, 2],
            }),
            "comp2": pd.DataFrame({
                "entity": ["entity1"],
                "comp_ind": [1],
                "field2": ["a"],
            }),
        }
        registry = data.Registry(components)
        assert len(registry.components) == 2
        assert "comp1" in registry.components
        assert "comp2" in registry.components

    def test_set(self):
        components = {
            "comp_a": pd.DataFrame({
                "entity": ["entity1", "entity2"],
                "comp_ind": [0, 0],
                "field_1": [1, 2],
            }),
            "compinst": pd.DataFrame({
                "entity": ["entity1", "entity2"],
                "comp_ind": [0, 0],
                "component_type": ["comp_a", "comp_a"],
            }).set_index(["entity", "comp_ind"], drop=False),
        }
        registry = data.Registry(components)
        
        new_component = pd.DataFrame({
            "entity": ["entity1", "entity3"],
            "comp_ind": [0, 0],
            "field_1": [1, -2],
        })
        
        registry.set("comp_a", new_component, mode="overwrite")

        assert "comp_a" in registry.components
        assert len(registry["comp_a"]) == 2
        assert registry["comp_a"]["field_1"].tolist() == [1, -2]
        assert registry["compinst"].sort_index()["entity"].tolist() == ["entity1", "entity3"]

    def test_set_upsert_mode(self):
        components = {
            "comp_a": pd.DataFrame({
                "entity": ["entity1", "entity2"],
                "comp_ind": [0, 0],
                "field_1": [1, 2],
            }),
            "compinst": pd.DataFrame({
                "entity": ["entity1", "entity2"],
                "comp_ind": [0, 0],
                "component_type": ["comp_a", "comp_a"],
            }).set_index(["entity", "comp_ind"]),
        }
        registry = data.Registry(components)
        
        new_component = pd.DataFrame({
            "entity": ["entity1", "entity3"],
            "comp_ind": [0, 0],
            "field_1": [-1, -2],
        })

        registry.set("comp_a", new_component, mode="upsert")

        assert "comp_a" in registry.components
        assert len(registry["comp_a"]) == 3
        assert registry["comp_a"].sort_index()["field_1"].tolist() == [-1, 2, -2]
        assert registry["compinst"].sort_index()["entity"].tolist() == ["entity1", "entity2", "entity3"]

    def test_sync_comp_inds(self):
        components = {
            "comp_a": pd.DataFrame({
                "entity": ["entity1", "entity1", "entity2", "entity2", "entity2", "entity3"],
                "comp_ind": [0, pd.NA, 0, 0, pd.NA, pd.NA],
                "field_1": [1, 1, 2, 2, 2, 3],
            }),
            "compinst": pd.DataFrame({
                "entity": ["entity1", "entity2",],
                "comp_ind": [0, 0],
                "component_type": ["comp_a", "comp_a"],
            }).set_index(["entity", "comp_ind"]),
        }
        registry = data.Registry(components)
        
        expected = pd.DataFrame({
            "entity": ["entity1", "entity1", "entity2", "entity2", "entity3"],
            "comp_ind": [0, 1, 0, 1, 0],
            "field_1": [1, 1, 2, 2, 3],
        })
        expected_compinsts = pd.DataFrame({
            "entity": ["entity1", "entity1", "entity2", "entity2", "entity3"],
            "comp_ind": [0, 1, 0, 1, 0],
            "component_type": ["comp_a"] * 5,
        }).set_index(["entity", "comp_ind"])

        actual = registry.sync_comp_inds("comp_a", registry["comp_a"], mode="upsert")

        pd.testing.assert_frame_equal(actual, expected)
        pd.testing.assert_frame_equal(registry["compinst"], expected_compinsts)
