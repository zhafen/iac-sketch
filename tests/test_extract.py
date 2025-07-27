import ast
import unittest

from iac_sketch import extract
from textwrap import dedent


class TestPythonExtractor(unittest.TestCase):
    """Test suite for the ComponentVisitor class from extract.py"""

    def setUp(self):
        self.extractor = extract.PythonAstExtractor("test_python_extractor.py")

    def test_extract_function(self):

        input_python = dedent(
            """
            def my_function(x):
                return x + 1
            """
        )
        entities = self.extractor.extract_from_input(input_python)
        assert len(entities) == 2

        # Module component
        comp = entities.iloc[0]
        assert comp["entity"] == ""
        assert comp["comp_key"] == "test_python_extractor"
        assert comp["component_type"] == "Module"
        assert comp["component"]["body"] == ["test_python_extractor.my_function"]

        # Function component
        comp = entities.iloc[1]
        assert comp["entity"] == "test_python_extractor"
        assert comp["comp_key"] == "my_function"
        assert comp["component_type"] == "FunctionDef"
        assert comp["component"]["name"] == "my_function"

    def test_extract_class(self):

        input_python = dedent(
            """
            class MyClass:

                def __init__(self, b: int = 1):
                    self.b = b

                def my_method(self, x: int) -> int:
                    return x + self.b
            """
        )
        entities = self.extractor.extract_from_input(input_python)
        assert len(entities) == 4

        # Module component
        comp = entities.iloc[0]
        assert comp["entity"] == ""
        assert comp["comp_key"] == "test_python_extractor"
        assert comp["component_type"] == "Module"
        assert comp["component"]["body"] == ["test_python_extractor.MyClass"]

        # Class component
        comp = entities.iloc[1]
        assert comp["entity"] == "test_python_extractor"
        assert comp["comp_key"] == "MyClass"
        assert comp["component_type"] == "ClassDef"
        assert comp["component"]["name"] == "MyClass"
        assert comp["component"]["body"] == [
            "test_python_extractor.MyClass.__init__",
            "test_python_extractor.MyClass.my_method",
        ]

        # Constructor component
        comp = entities.iloc[2]
        assert comp["entity"] == "test_python_extractor.MyClass"
        assert comp["comp_key"] == "__init__"
        assert comp["component_type"] == "FunctionDef"
        assert comp["component"]["name"] == "__init__"

        # Method component
        comp = entities.iloc[3]
        assert comp["entity"] == "test_python_extractor.MyClass"
        assert comp["comp_key"] == "my_method"
        assert comp["component_type"] == "FunctionDef"
        assert comp["component"]["name"] == "my_method"

    def test_extract_import(self):
        
        input_python = dedent(
            """
            import os
            import sys, ast
            from math import sqrt
            """
        )
        entities = self.extractor.extract_from_input(input_python)
        assert len(entities) == 5

        # Module component
        comp = entities.iloc[0]
        assert comp["entity"] == ""
        assert comp["comp_key"] == "test_python_extractor"
        assert comp["component_type"] == "Module"
        assert comp["component"]["body"] == [
            "test_python_extractor.0",
            "test_python_extractor.1",
            "test_python_extractor.2",
            "test_python_extractor.3",
        ]

        # Import os component
        comp = entities.iloc[1]
        assert comp["entity"] == "test_python_extractor"
        assert comp["comp_key"] == "0"
        assert comp["component_type"] == "Import"
        assert comp["component"]["module"] == "os"

        # Import sys component
        comp = entities.iloc[2]
        assert comp["entity"] == "test_python_extractor"
        assert comp["comp_key"] == "1"
        assert comp["component_type"] == "Import"
        assert comp["component"]["module"] == "sys"

        # Import ast component
        comp = entities.iloc[3]
        assert comp["entity"] == "test_python_extractor"
        assert comp["comp_key"] == "2"
        assert comp["component_type"] == "Import"
        assert comp["component"]["module"] == "ast"

        # Import sqrt component
        comp = entities.iloc[4]
        assert comp["entity"] == "test_python_extractor"
        assert comp["comp_key"] == "3"
        assert comp["component_type"] == "ImportFrom"
        assert comp["component"]["names"] == ["sqrt"]