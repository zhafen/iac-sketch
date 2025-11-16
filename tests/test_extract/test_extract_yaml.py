import os
import unittest
import tempfile
from textwrap import dedent

import pandas as pd

from iaca.extract import YAMLExtractor


class TestYAMLExtractor(unittest.TestCase):
    """Test suite for YAMLExtractor class."""

    def setUp(self):
        self.extractor = YAMLExtractor()

    def test_extract_simple_yaml(self):
        """Test extraction of simple YAML with string components."""
        yaml_content = dedent(
            """
            test_entity:
              - component1
              - component2
            """
        )

        entities = self.extractor.extract_from_input(yaml_content, source="test")

        self.assertEqual(len(entities), 2) 
        self.assertEqual(entities[0]["entity"], "test_entity")
        self.assertEqual(entities[0]["component_type"], "component1")
        self.assertTrue(pd.isna(entities[0]["component"]))

    def test_extract_yaml_with_values(self):
        """Test extraction of YAML with component values."""
        yaml_content = dedent(
            """
            test_entity:
              - component1: value1
              - component2:
                  value: value2
                  extra_field: extra_value
            """
        )

        entities = self.extractor.extract_from_input(yaml_content, source="test")

        self.assertEqual(len(entities), 2)

        # Check first component
        comp1 = entities[0]
        self.assertEqual(comp1["component_type"], "component1")
        self.assertEqual(comp1["component"]["value"], "value1")

        # Check second component
        comp2 = entities[1]
        self.assertEqual(comp2["component_type"], "component2")
        self.assertEqual(comp2["component"]["value"], "value2")
        self.assertEqual(comp2["component"]["extra_field"], "extra_value")

    def test_extract_nested_yaml(self):
        """Test extraction of nested YAML structures with multiple levels."""
        yaml_content = dedent(
            """
            test_entity:
                - component1: value1
                - children:
                    child_test_entity:
                        - component1: value2
                        - children:
                            grandchild_test_entity:
                                - component1: value3
            """
        )

        entities = self.extractor.extract_from_input(yaml_content, source="test")

        self.assertEqual(len(entities), 5)

        # Check first component (parent)
        comp1 = entities[0]
        self.assertEqual(comp1["entity"], "test_entity")
        self.assertEqual(comp1["component_type"], "component1")
        self.assertEqual(comp1["component"]["value"], "value1")

        # Check second component (child)
        comp2 = entities[1]
        self.assertEqual(comp2["entity"], "child_test_entity")
        self.assertEqual(comp2["component_type"], "component1")
        self.assertEqual(comp2["component"]["value"], "value2")

        # Check third component (grandchild)
        comp3 = entities[2]
        self.assertEqual(comp3["entity"], "grandchild_test_entity")
        self.assertEqual(comp3["component_type"], "component1")
        self.assertEqual(comp3["component"]["value"], "value3")

        # Check child-grandchild relationship
        comp4 = entities[3]
        self.assertEqual(comp4["entity"], "child_test_entity")
        self.assertEqual(comp4["component_type"], "child")
        self.assertEqual(comp4["component"]["value"], "grandchild_test_entity")

        # Check parent-child relationship
        comp5 = entities[4]
        self.assertEqual(comp5["entity"], "test_entity")
        self.assertEqual(comp5["component_type"], "child")
        self.assertEqual(comp5["component"]["value"], "child_test_entity")


    def test_extract_yaml_with_entity_key(self):
        """Test extraction where component has key matching entity name."""
        yaml_content = dedent(
            """
            test_entity:
              - component1:
                  component1: entity_value
            """
        )

        entities = self.extractor.extract_from_input(yaml_content, source="test")

        comp1 = entities[0]
        self.assertEqual(comp1["component_type"], "component1")
        self.assertEqual(comp1["component"]["value"], "entity_value")

    def test_empty_yaml(self):
        """Test extraction of empty YAML."""
        df = self.extractor.extract_from_input("", source="test")
        self.assertEqual(len(df), 0)

    def test_invalid_yaml(self):
        """Test extraction of invalid YAML raises appropriate error."""
        invalid_yaml = "invalid: yaml: content: ["

        with self.assertRaises(ValueError) as context:
            self.extractor.extract_from_input(invalid_yaml, source="test")

        self.assertIn("Error parsing YAML from test", str(context.exception))

    def test_extract_from_file(self):
        """Test extraction from a file using the extract() method."""
        # Create a temporary YAML file for testing

        yaml_content = dedent(
            """
            test_entity:
              - component1: value1
              - component2: value2
            """
        )

        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".yaml", delete=False
        ) as tmp_file:
            tmp_file.write(yaml_content)
            tmp_file_path = tmp_file.name

        try:
            entities = self.extractor.extract(tmp_file_path, root_dir=os.getcwd())
            self.assertEqual(len(entities), 2)
            self.assertEqual(entities[0]["entity"], "test_entity")
        finally:
            os.unlink(tmp_file_path)


if __name__ == "__main__":
    unittest.main()
