import ast

import pandas as pd


class PythonAstExtractor(ast.NodeVisitor):

    def __init__(
        self,
        source: str,
        entity_types: list[str] = [
            "FunctionDef",
            "ClassDef",
            "Module",
            "Import",
            "ImportFrom",
        ],
        field_types: list[str] = [
            "alias",
        ],
    ):
        self.source = source
        self.path = []
        self.entities = []
        self.entity_types = tuple(getattr(ast, t) for t in entity_types)
        self.field_types = tuple(getattr(ast, t) for t in field_types)

    def extract_from_input(self, input_python: str) -> pd.DataFrame:

        self.visit(ast.parse(input_python))

        return pd.DataFrame(self.entities)

    def get_node_id(self, node):

        # Get the path
        if isinstance(node, ast.Module):
            comp_key = self.source[:-3]
        elif hasattr(node, "name"):
            comp_key = node.name
        else:
            comp_key = str(self.comp_count)
            self.comp_count += 1
        entity = ".".join(self.path)

        return entity, comp_key

    def get_node_path(self, node):

        entity, comp_key = self.get_node_id(node)
        return f"{entity}.{comp_key}"

    def generic_visit(self, node):

        if not isinstance(node, self.entity_types):
            return

        # Reset component count for each visit
        self.comp_count = 0

        # Get the entity and component key
        entity, comp_key = self.get_node_id(node)
        self.path.append(comp_key)

        # Create a component representing the node
        comp = {}
        for field_key, field_value in ast.iter_fields(node):
            comp[field_key] = self.parse_field(field_value)

        # Format and store
        component = {
            "entity": entity,
            "comp_key": comp_key,
            "component_type": node.__class__.__name__,
            "component": comp,
        }
        self.entities.append(component)

        # Visit children
        super().generic_visit(node)

        # Move back up the path
        self.path.pop()

    def parse_field(self, field_value):

        if isinstance(field_value, list):
            return [self.parse_field(item) for item in field_value]
        if isinstance(field_value, dict):
            return {key: self.parse_field(value) for key, value in field_value.items()}
        if not hasattr(field_value, "__dict__"):
            return field_value
        if isinstance(field_value, self.field_types):
            return dict(ast.iter_fields(field_value))
        if isinstance(field_value, ast.AST):
            return self.get_node_path(field_value)
        raise ValueError(f"Unsupported field type: {type(field_value)}")