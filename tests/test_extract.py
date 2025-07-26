import ast
import unittest

from iac_sketch import extract


class TestComponentVisitor(unittest.TestCase):
    """Test suite for the ComponentVisitor class from extract.py"""

    def setUp(self):
        self.visitor = extract.ComponentVisitor()

    def test_extract_function(self):

        python_input = """
        def my_function(x):
            return x + 1
        """
        self.visitor.visit(ast.parse(python_input))
        assert self.visitor.components == ["my_function"]