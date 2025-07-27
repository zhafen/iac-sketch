import ast
import unittest

from iac_sketch import extract
from textwrap import dedent


class TestPythonExtractor(unittest.TestCase):
    """Test suite for the ComponentVisitor class from extract.py"""

    def setUp(self):
        self.extractor = extract.PythonAstExtractor("test_python_extractor")

    def test_extract_function(self):

        input_python = dedent(
            """
            def my_function(x):
                return x + 1
            """
        )
        entities = self.extractor.extract_from_input(input_python)
        assert len(entities) == 2
        comp = entities.iloc[1]
        assert comp["entity"] == "test_python_extractor"
        assert comp["comp_key"] == "my_function"
        assert comp["component_type"] == "FunctionDef"
        assert comp["component"]["name"] == "my_function"