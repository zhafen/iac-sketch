import os
import unittest

from iac_sketch.extract import extract_python
from textwrap import dedent


class TestPythonExtractor(unittest.TestCase):
    """Test suite for the ComponentVisitor class from extract.py"""

    def setUp(self):
        self.extractor = extract_python.PythonExtractor()

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
        assert comp["entity"] == "direct_input"
        assert comp["comp_key"] == "module"
        assert comp["component_type"] == "Module"
        assert comp["component"]["body"] == ["direct_input.module.my_function"]

        # Function component
        comp = entities.iloc[1]
        assert comp["entity"] == "direct_input.module"
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
        assert comp["entity"] == "direct_input"
        assert comp["comp_key"] == "module"
        assert comp["component_type"] == "Module"
        assert comp["component"]["body"] == ["direct_input.module.MyClass"]

        # Class component
        comp = entities.iloc[1]
        assert comp["entity"] == "direct_input.module"
        assert comp["comp_key"] == "MyClass"
        assert comp["component_type"] == "ClassDef"
        assert comp["component"]["name"] == "MyClass"
        assert comp["component"]["body"] == [
            "direct_input.module.MyClass.__init__",
            "direct_input.module.MyClass.my_method",
        ]

        # Constructor component
        comp = entities.iloc[2]
        assert comp["entity"] == "direct_input.module.MyClass"
        assert comp["comp_key"] == "__init__"
        assert comp["component_type"] == "FunctionDef"
        assert comp["component"]["name"] == "__init__"

        # Method component
        comp = entities.iloc[3]
        assert comp["entity"] == "direct_input.module.MyClass"
        assert comp["comp_key"] == "my_method"
        assert comp["component_type"] == "FunctionDef"
        assert comp["component"]["name"] == "my_method"

    def test_extract_docstring(self):

        input_python = dedent(
            """
            def my_function(x):
                '''Arbitrary docstring
                split by lines.'''
                return x + 1
            """
        )
        entities = self.extractor.extract_from_input(input_python)
        assert len(entities) == 3

        # Function component
        comp = entities.iloc[1]
        assert comp["entity"] == "direct_input.module"
        assert comp["comp_key"] == "my_function"
        assert comp["component_type"] == "FunctionDef"
        assert comp["component"]["name"] == "my_function"

        # Docstring component
        comp = entities.iloc[2]
        assert comp["entity"] == "direct_input.module.my_function"
        assert comp["comp_key"] == "docstring"
        assert comp["component_type"] == "docstring"
        assert comp["component"]["value"] == "Arbitrary docstring\nsplit by lines."

        comp = entities.iloc[2]

    def test_extract_docstring_components(self):

        input_python = dedent(
            """
            def my_function(x):
                '''Arbitrary docstring
                split by lines.

                iac_sketch
                ----------
                - status: "in production"
                '''
                return x + 1
            """
        )
        entities = self.extractor.extract_from_input(input_python)
        assert len(entities) == 4

        # Function component
        comp = entities.iloc[1]
        assert comp["entity"] == "direct_input.module"
        assert comp["comp_key"] == "my_function"
        assert comp["component_type"] == "FunctionDef"
        assert comp["component"]["name"] == "my_function"

        # Docstring component
        comp = entities.iloc[2]
        assert comp["entity"] == "direct_input.module.my_function"
        assert comp["comp_key"] == "docstring"
        assert comp["component_type"] == "docstring"

        # Yaml components in the docstring
        comp = entities.iloc[3]
        assert comp["entity"] == "direct_input.module.my_function"
        assert comp["comp_key"] == "0"
        assert comp["component_type"] == "status"
        assert comp["component"]["value"] == "in production"

    def test_extract_import(self):

        input_python = dedent(
            """
            import os
            import sys, ast
            from math import sqrt
            """
        )
        entities = self.extractor.extract_from_input(input_python)
        assert len(entities) == 4

        # Module component
        comp = entities.iloc[0]
        assert comp["entity"] == "direct_input"
        assert comp["comp_key"] == "module"
        assert comp["component_type"] == "Module"
        assert comp["component"]["body"] == [
            "direct_input.module.0",
            "direct_input.module.1",
            "direct_input.module.2",
        ]

        # Import os component
        comp = entities.iloc[1]
        assert comp["entity"] == "direct_input.module"
        assert comp["comp_key"] == "0"
        assert comp["component_type"] == "Import"
        assert comp["component"]["names"] == [{"name": "os", "asname": None}]

        # Import sys, ast component
        comp = entities.iloc[2]
        assert comp["entity"] == "direct_input.module"
        assert comp["comp_key"] == "1"
        assert comp["component_type"] == "Import"
        assert comp["component"]["names"] == [
            {"name": "sys", "asname": None},
            {"name": "ast", "asname": None},
        ]

        # Import math component
        comp = entities.iloc[3]
        assert comp["entity"] == "direct_input.module"
        assert comp["comp_key"] == "2"
        assert comp["component_type"] == "ImportFrom"
        assert comp["component"]["module"] == "math"
        assert comp["component"]["names"] == [{"name": "sqrt", "asname": None}]

    def test_extract_calls(self):

        input_python = dedent(
            """
            def my_function(x):
                return x + 1

            x = my_function(5)

            def my_second_function(y):
                return my_function(y) * 2
            """
        )
        entities = self.extractor.extract_from_input(input_python).set_index(
            ["entity", "comp_key"]
        )

        # Check that there is a "Call" component at the below addresses
        assert entities.loc[("direct_input.module", "0"), "component_type"] == "Call"
        assert (
            entities.loc[("direct_input.module.my_second_function", "0"), "component_type"]
            == "Call"
        )

    def test_extract_calls_attributes(self):

        input_python = dedent(
            """
            class MyClass:
                def my_function(self, x):
                    return x + 1

                def my_function_wrapper(self, x):
                    return self.my_function(x)
            """
        )
        entities = self.extractor.extract_from_input(input_python).set_index(
            ["entity", "comp_key"]
        )

        # Check that there is a "Call" component at the below addresses
        ind = ("direct_input.module.MyClass.my_function_wrapper", "0")
        assert entities.loc[ind, "component_type"] == "Call"
        assert entities.loc[ind, "component"]["func"] == "self.my_function"

    def test_real_code(self):
        # Use the current file as input
        filepath = __file__
        entities = self.extractor.extract(filepath)
        dirname = os.path.dirname(os.path.relpath(filepath))
        entities = entities.set_index(["entity", "comp_key"])

        # Test finding this function
        assert entities.loc[
            (
                f"{dirname}.test_extract_python.TestPythonExtractor",
                "test_real_code",
            ),
            "component_type",
        ] == "FunctionDef"

        # Test finding the call
        row = entities.loc[
            (
                f"{dirname}.test_extract_python.TestPythonExtractor.test_real_code",
                "0",
            )
        ]
        assert row["component_type"] == "Call"
        assert row["component"]["func"] == "self.extractor.extract"
