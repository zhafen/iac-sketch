import ast

import pandas as pd

class PythonAstExtractor(ast.NodeVisitor):

    def __init__(self, source: str):
        self.source = source
        self.path = [source]
        self.entities = []
        self.comp_count = 0

    def extract_from_input(self, input_python: str) -> pd.DataFrame:

        self.visit(ast.parse(input_python))

        return pd.DataFrame(self.entities)

    def generic_visit(self, node):

        entity, comp_key = self.get_node_id(node)

        # Create a component
        comp = {}
        self.comp_count = 0
        for field_key, field_value in ast.iter_fields(node):
            comp[field_key] = self.parse_field(field_value)

        component = {
            "entity": entity,
            "comp_key": comp_key,
            "component_type": node.__class__.__name__,
            "component": comp,
        }
        self.entities.append(component)

        self.path.append(comp_key)
        super().generic_visit(node)

        self.path.pop()

    def get_node_id(self, node):

        # Get the path
        if "name" in node._fields:
            comp_key = node.name
        else:
            comp_key = str(self.comp_count)
            self.comp_count += 1

        entity = ".".join(self.path)

        return entity, comp_key

    def get_node_path(self, node):

        entity, comp_key = self.get_node_id(node)
        return f"{entity}.{comp_key}"

    def parse_field(self, field_value):

        if isinstance(field_value, list):
            return [self.parse_field(item) for item in field_value]
        if isinstance(field_value, dict):
            return {key: self.parse_field(value) for key, value in field_value.items()}
        if isinstance(field_value, ast.Constant):
            return field_value.value
        if isinstance(field_value, ast.AST):
            return self.get_node_path(field_value)
        raise ValueError(f"Unsupported field type: {type(field_value)}")