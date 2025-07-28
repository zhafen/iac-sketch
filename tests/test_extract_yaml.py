import unittest
import pandas as pd
from textwrap import dedent

from iac_sketch.extract import YAMLExtractor


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
        
        df = self.extractor.extract_entities_from_yaml(yaml_content, source="test")
        
        self.assertEqual(len(df), 3)  # 2 components + 1 metadata
        self.assertEqual(df.iloc[0]["entity"], "test_entity")
        self.assertEqual(df.iloc[0]["component_type"], "component1")
        self.assertTrue(pd.isna(df.iloc[0]["component"]))
        
        # Check metadata component
        metadata_row = df[df["component_type"] == "metadata"].iloc[0]
        self.assertEqual(metadata_row["component"]["source"], "test")
        self.assertEqual(metadata_row["component"]["n_comps"], 3)

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
        
        df = self.extractor.extract_entities_from_yaml(yaml_content, source="test")
        
        self.assertEqual(len(df), 3)  # 2 components + 1 metadata
        
        # Check first component
        comp1 = df.iloc[0]
        self.assertEqual(comp1["component_type"], "component1")
        self.assertEqual(comp1["component"]["value"], "value1")
        
        # Check second component
        comp2 = df.iloc[1]
        self.assertEqual(comp2["component_type"], "component2")
        self.assertEqual(comp2["component"]["value"], "value2")
        self.assertEqual(comp2["component"]["extra_field"], "extra_value")

    def test_extract_yaml_with_entity_key(self):
        """Test extraction where component has key matching entity name."""
        yaml_content = dedent(
            """
            test_entity:
              - component1:
                  component1: entity_value
            """
        )
        
        df = self.extractor.extract_entities_from_yaml(yaml_content, source="test")
        
        comp1 = df.iloc[0]
        self.assertEqual(comp1["component_type"], "component1")
        self.assertEqual(comp1["component"]["value"], "entity_value")

    def test_empty_yaml(self):
        """Test extraction of empty YAML."""
        df = self.extractor.extract_entities_from_yaml("", source="test")
        self.assertEqual(len(df), 0)

    def test_invalid_yaml(self):
        """Test extraction of invalid YAML raises appropriate error."""
        invalid_yaml = "invalid: yaml: content: ["
        
        with self.assertRaises(ValueError) as context:
            self.extractor.extract_entities_from_yaml(invalid_yaml, source="test")
        
        self.assertIn("Error parsing YAML from test", str(context.exception))


if __name__ == "__main__":
    unittest.main()
