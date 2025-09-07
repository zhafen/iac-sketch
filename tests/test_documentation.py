from textwrap import dedent
import unittest

import pandas as pd

from iac_sketch import documentation

class TestDocumentationSystem(unittest.TestCase):
    
    def setUp(self):
        self.doc_sys = documentation.DocumentationSystem()

    def test_generate_component_markdown_with_value(self):

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