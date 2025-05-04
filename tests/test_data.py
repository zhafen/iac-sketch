import unittest

from iac_sketch import data


class TestField(unittest.TestCase):

    def test_default(self):

        field_key = "my_field [int]"
        field_value = "This is my field"

        field = data.Field.from_kv_pair(field_key, field_value)
        assert field.name == "my_field"
        assert field.type == "int"
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
        assert field.type == "int"
        assert field.description == "This is my field"
        assert field.multiplicity == "0..1"

    def test_multiplicity_in_brackets(self):

        field_key = "my_field [int|1..1]"
        field_value = "This is my field"

        field = data.Field.from_kv_pair(field_key, field_value)
        assert field.name == "my_field"
        assert field.type == "int"
        assert field.description == "This is my field"
        assert field.multiplicity == "1..1"

    def test_nested_brackets(self):

        field_key = "my_field [dict[str, str]]"
        field_value = "This is my field"

        field = data.Field.from_kv_pair(field_key, field_value)
        assert field.name == "my_field"
        assert field.type == "dict[str, str]"
        assert field.description == "This is my field"
        assert field.multiplicity == "0..*"

    def test_default_provided(self):

        field_key = "my_field [str] = 0..*"
        field_value = "This is my field"

        field = data.Field.from_kv_pair(field_key, field_value)
        assert field.name == "my_field"
        assert field.type == "str"
        assert field.description == "This is my field"
        assert field.default == "0..*"