import unittest

import numpy as np
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
                "comp_key": [0, 0],
                "field1": [1, 2],
            }),
            "comp2": pd.DataFrame({
                "entity": ["entity1"],
                "comp_key": [1],
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
                "comp_key": [0, 0],
                "field_1": [1, 2],
            }),
            "compinst": pd.DataFrame({
                "entity": ["entity1", "entity2"],
                "comp_key": [0, 0],
                "component_type": ["comp_a", "comp_a"],
            }).set_index(["entity", "comp_key"]),
        }
        registry = data.Registry(components)
        
        new_component = pd.DataFrame({
            "entity": ["entity1", "entity3"],
            "comp_key": [0, 0],
            "field_1": [1, -2],
        })
        
        registry.set("comp_a", new_component, mode="overwrite")

        expected = pd.DataFrame({
            "entity": ["entity1", "entity3"],
            "comp_key": [0, 0],
            "field_1": [1, -2],
        }).set_index(["entity", "comp_key"])
        expected_compinsts = pd.DataFrame({
            "entity": ["entity1", "entity3"],
            "comp_key": [0, 0],
            "component_type": ["comp_a", "comp_a"],
        }).set_index(["entity", "comp_key"])

        pd.testing.assert_frame_equal(registry["comp_a"], expected)
        pd.testing.assert_frame_equal(registry["compinst"], expected_compinsts)


    def test_set_upsert_mode(self):
        components = {
            "comp_a": pd.DataFrame({
                "entity": ["entity1", "entity2"],
                "comp_key": [0, 0],
                "field_1": [1, 2],
            }),
            "compinst": pd.DataFrame({
                "entity": ["entity1", "entity2"],
                "comp_key": [0, 0],
                "component_type": ["comp_a", "comp_a"],
            }).set_index(["entity", "comp_key"]),
        }
        registry = data.Registry(components)
        
        new_component = pd.DataFrame({
            "entity": ["entity1", "entity3"],
            "comp_key": [0, 0],
            "field_1": [-1, -2],
        })

        registry.set("comp_a", new_component, mode="upsert")

        expected = pd.DataFrame({
            "entity": ["entity1", "entity2", "entity3"],
            "comp_key": [0, 0, 0],
            "field_1": [-1, 2, -2],
        }).set_index(["entity", "comp_key"])
        expected_compinsts = pd.DataFrame({
            "entity": ["entity1", "entity2", "entity3"],
            "comp_key": [0, 0, 0],
            "component_type": ["comp_a", "comp_a", "comp_a"],
        }).set_index(["entity", "comp_key"])

        pd.testing.assert_frame_equal(registry["comp_a"], expected)
        pd.testing.assert_frame_equal(registry["compinst"], expected_compinsts)

    def test_sync_comp_keys(self):
        components = {
            "comp_a": pd.DataFrame({
                "entity": ["entity1", "entity1", "entity2", "entity2", "entity2", "entity3"],
                "comp_key": [0, pd.NA, 0, 0, pd.NA, pd.NA],
                "field_1": [1, 1, 2, 2, 2, 3],
            }),
            "compinst": pd.DataFrame({
                "entity": ["entity1", "entity2",],
                "comp_key": [0, 0],
                "component_type": ["comp_a", "comp_a"],
            }).set_index(["entity", "comp_key"]),
        }
        registry = data.Registry(components)
        
        expected = pd.DataFrame({
            "entity": ["entity1", "entity1", "entity2", "entity2", "entity3"],
            "comp_key": [0, 1, 0, 1, 0],
            "field_1": [1, 1, 2, 2, 3],
        })
        expected_compinsts = pd.DataFrame({
            "entity": ["entity1", "entity1", "entity2", "entity2", "entity3"],
            "comp_key": [0, 1, 0, 1, 0],
            "component_type": ["comp_a"] * 5,
        }).set_index(["entity", "comp_key"])

        actual = registry.sync_comp_keys("comp_a", registry["comp_a"], mode="upsert")

        pd.testing.assert_frame_equal(actual, expected)
        pd.testing.assert_frame_equal(registry["compinst"], expected_compinsts)

    def test_reset_index(self):
        registry = data.Registry({})

        # We'll test with this dataframe
        comp_a = pd.DataFrame({
            "entity": ["entity1", "entity2"],
            "comp_key": [0, 0],
            "field_1": [1, 2],
        })

        # The expected is actually the same as comp_a
        expected = comp_a.copy()

        # Test for when comp_a has a few options for indices
        actual = registry.reset_index(comp_a)
        pd.testing.assert_frame_equal(actual, expected)
        actual = registry.reset_index(comp_a.set_index(["entity", "comp_key"]))
        pd.testing.assert_frame_equal(actual, expected)
        actual = registry.reset_index(comp_a.set_index(["entity"]))
        pd.testing.assert_frame_equal(actual, expected)

class TestView(unittest.TestCase):
    def test_view(self):
        components = {
            "comp1": pd.DataFrame({
                "entity": ["entity1", "entity2"],
                "comp_key": [0, 0],
                "field1": [1, 2],
            }),
            "comp2": pd.DataFrame({
                "entity": ["entity1"],
                "comp_key": [1],
                "field2": ["a"],
            }),
        }
        registry = data.Registry(components)

        actual = registry.resolve_view(data.View(["comp1", "comp2"]))

        expected = pd.DataFrame({
            "entity": ["entity1", "entity2"],
            "comp1.field1": [1, 2],
            "comp2.field2": ["a", pd.NA],
        }).set_index("entity")

        pd.testing.assert_frame_equal(actual, expected)

    def test_view_multiple_in_comp(self):
        components = {
            "comp1": pd.DataFrame({
                "entity": ["entity1", "entity1", "entity2"],
                "comp_key": [0, 2, 0],
                "field1": [0, 1, 2],
            }),
            "comp2": pd.DataFrame({
                "entity": ["entity1"],
                "comp_key": [1],
                "field2": ["a"],
            }),
        }
        registry = data.Registry(components)

        actual = registry.resolve_view(data.View(["comp1", "comp2"]))

        expected = pd.DataFrame({
            "entity": ["entity1", "entity1", "entity2"],
            "comp1.field1": [0, 1, 2],
            "comp2.field2": ["a", "a", pd.NA],
        }).set_index("entity")

        pd.testing.assert_frame_equal(actual, expected)

    def test_view_multiple_in_both_comps(self):
        components = {
            "comp1": pd.DataFrame({
                "entity": ["entity1", "entity1", "entity2"],
                "comp_key": [0, 2, 0],
                "field1": [0, 1, 2],
            }),
            "comp2": pd.DataFrame({
                "entity": ["entity1", "entity1",],
                "comp_key": [1, 3],
                "field2": ["a", "b"],
            }),
        }
        registry = data.Registry(components)

        actual = registry.resolve_view(data.View(["comp1", "comp2"]))

        expected = pd.DataFrame({
            "entity": ["entity1", "entity1", "entity1", "entity1", "entity2"],
            "comp1.field1": [0, 0, 1, 1, 2],
            "comp2.field2": ["a", "b", "a", "b", pd.NA],
        }).set_index("entity")

        pd.testing.assert_frame_equal(actual, expected)

    def test_three_comps(self):
        components = {
            "comp1": pd.DataFrame({
                "entity": ["entity1", "entity1", "entity2"],
                "comp_key": [0, 2, 0],
                "field1": [0, 1, 2],
            }),
            "comp2": pd.DataFrame({
                "entity": ["entity1", "entity1",],
                "comp_key": [1, 3],
                "field2": ["a", "b"],
            }),
            "comp3": pd.DataFrame({
                "entity": ["entity1", "entity2",],
                "comp_key": [4, 1],
                "field3": [-1, -2],
            }),
        }
        registry = data.Registry(components)

        actual = registry.resolve_view(data.View(["comp1", "comp2", "comp3"]))

        expected = pd.DataFrame({
            "entity": ["entity1", "entity1", "entity1", "entity1", "entity2"],
            "comp1.field1": [0, 0, 1, 1, 2],
            "comp2.field2": ["a", "b", "a", "b", pd.NA],
            "comp3.field3": [-1, -1, -1, -1, -2],
        }).set_index("entity")

        pd.testing.assert_frame_equal(actual, expected)
