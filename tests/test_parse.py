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

class TestParseFieldDefinition(unittest.TestCase):

    def setUp(self):
        self.test_data_dir = "./public/components"
        self.parser = parse.Parser(self.test_data_dir)

    def test_default(self):

        field_key = "my_field [int]"
        field_value = "This is my field"

        field_definition = self.parser.parse_field_definition(field_key, field_value)
        assert field_definition["field"] == "my_field"
        assert field_definition["type"] == "int"
        assert field_definition["description"] == "This is my field"
        # Default multiplicity
        assert field_definition["multiplicity"] == "1..*"

    def test_dict_provided(self):

        field_key = "my_field [int]"
        field_value = {
            "description": "This is my field",
            "multiplicity": "0..1",
        }

        field_definition = self.parser.parse_field_definition(field_key, field_value)
        assert field_definition["field"] == "my_field"
        assert field_definition["type"] == "int"
        assert field_definition["description"] == "This is my field"
        assert field_definition["multiplicity"] == "0..1"

    def test_multiplicity_in_brackets(self):

        field_key = "my_field [int|0..*]"
        field_value = "This is my field"

        field_definition = self.parser.parse_field_definition(field_key, field_value)
        assert field_definition["field"] == "my_field"
        assert field_definition["type"] == "int"
        assert field_definition["description"] == "This is my field"
        assert field_definition["multiplicity"] == "0..*"

        
