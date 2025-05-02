import unittest

import pandas as pd

from iac_sketch import parse


class TestParser(unittest.TestCase):

    def setUp(self):
        self.test_data_dir = "./public/components"
        self.parser = parse.Parser(self.test_data_dir)

    def test_extract(self):

        self.parser.extract()

        assert "component" in self.parser.entities["entity"].values

    def test_transform(self):

        self.parser.extract()
        self.parser.transform()

        assert "component" in self.parser.components
        assert "link" in self.parser.components["component"].index
        assert "data" not in self.parser.components


class TestField(unittest.TestCase):

    def test_default(self):

        field_key = "my_field [int]"
        field_value = "This is my field"

        field = parse.Field.from_kv_pair(field_key, field_value)
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

        field = parse.Field.from_kv_pair(field_key, field_value)
        assert field.name == "my_field"
        assert field.type == "int"
        assert field.description == "This is my field"
        assert field.multiplicity == "0..1"

    def test_multiplicity_in_brackets(self):

        field_key = "my_field [int|1..1]"
        field_value = "This is my field"

        field = parse.Field.from_kv_pair(field_key, field_value)
        assert field.name == "my_field"
        assert field.type == "int"
        assert field.description == "This is my field"
        assert field.multiplicity == "1..1"

    def test_nested_brackets(self):

        field_key = "my_field [dict[str, str]]"
        field_value = "This is my field"

        field = parse.Field.from_kv_pair(field_key, field_value)
        assert field.name == "my_field"
        assert field.type == "dict[str, str]"
        assert field.description == "This is my field"
        assert field.multiplicity == "0..*"