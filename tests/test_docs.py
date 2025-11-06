from textwrap import dedent
import unittest

import pandas as pd

from iaca import docs

class TestGenerateComponentMarkdown(unittest.TestCase):
    
    def setUp(self):
        self.doc_sys = docs.DocSystem()

    def test_with_value(self):

        component_type = "my_component"

        comp = pd.Series({
            "value": "example_value",
            "my_field": 1.0,
            "my_other_field": "cat"
        })
        expected_output = dedent("""
        **my_component:** example_value
        - my_field: 1.0
        - my_other_field: cat
        """
        )[1:]
        output = self.doc_sys.generate_component_markdown(
            comp,
            component_type
        )
        self.assertEqual(output, expected_output)

    def test_without_value(self):

        component_type = "my_component"

        comp = pd.Series({
            "value": pd.NA,
            "my_field": 1.0,
            "my_other_field": "cat"
        })
        expected_output = dedent("""
        **my_component:**
        - my_field: 1.0
        - my_other_field: cat
        """
        )[1:]
        output = self.doc_sys.generate_component_markdown(
            comp,
            component_type
        )
        self.assertEqual(output, expected_output)

    def test_without_value_or_fields(self):

        component_type = "my_component"

        comp = pd.Series({
            "value": pd.NA,
        })
        expected_output = dedent("""
        **my_component**
        """
        )[1:]
        output = self.doc_sys.generate_component_markdown(
            comp,
            component_type
        )
        self.assertEqual(output, expected_output)