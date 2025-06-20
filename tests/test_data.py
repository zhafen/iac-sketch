import unittest

import pandas as pd
from pandera import dtypes

from iac_sketch import data


class TestField(unittest.TestCase):

    def test_default(self):

        field_key = "my_field [int]"
        field_value = "This is my field"

        field = data.Field.from_kv_pair(field_key, field_value)
        assert field.name == "my_field"
        assert field.dtype == dtypes.Int()
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
        assert field.dtype == dtypes.Int()
        assert field.description == "This is my field"
        assert field.multiplicity == "0..1"

    def test_multiplicity_in_brackets(self):

        field_key = "my_field [int|1..1]"
        field_value = "This is my field"

        field = data.Field.from_kv_pair(field_key, field_value)
        assert field.name == "my_field"
        assert field.dtype == dtypes.Int()
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
        assert field.dtype == "str"
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