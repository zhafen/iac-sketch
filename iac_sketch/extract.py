import ast

import pandas as pd


class IdAssigner(ast.NodeVisitor):
    """Assigns unique identifiers to AST nodes."""

    def __init__(self, source: str):
        self.source = source
        self.path = []
        self.comp_counts = {}

    def assign_ids(self, tree: ast.AST):
        """Assign IDs to all nodes in the AST."""
        self.visit(tree)

    def visit(self, node):
        """Visit a node and assign it an ID."""
        if isinstance(node, ast.Module):
            comp_key = self.source[:-3]
        elif hasattr(node, "name"):
            comp_key = node.name
        else:
            entity = ".".join(self.path)
            comp_key = str(self.comp_counts.setdefault(entity, 0))
            self.comp_counts[entity] += 1

        node.comp_key = comp_key
        self.path.append(comp_key)
        self.generic_visit(node)
        self.path.pop()


class ComponentExtractor(ast.NodeVisitor):
    """Extracts components from AST nodes with assigned IDs."""

    def __init__(
        self,
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
        self.path = []
        self.entities = []
        self.entity_types = tuple(getattr(ast, t) for t in entity_types)
        self.field_types = tuple(getattr(ast, t) for t in field_types)

    def extract_components(self, tree: ast.AST) -> list[dict]:
        """Extract components from the AST."""
        self.entities = []
        self.path = []
        self.visit(tree)
        return self.entities

    def get_node_id(self, node):
        """Get the entity and component key for a node."""
        entity = ".".join(self.path)
        comp_key = getattr(node, "comp_key", "unknown")
        return entity, comp_key

    def get_node_path(self, node):
        """Get the full path for a node."""
        entity, comp_key = self.get_node_id(node)
        return f"{entity}.{comp_key}"

    def visit(self, node):
        """Visit a node and extract component if it's an entity type."""
        if not isinstance(node, self.entity_types):
            self.generic_visit(node)
            return

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
        self.generic_visit(node)

        # Move back up the path
        self.path.pop()

    def parse_field(self, field_value):
        """Parse a field value, handling different types appropriately."""
        # For lists and dicts, recursively parse their contents
        if isinstance(field_value, list):
            return [self.parse_field(item) for item in field_value]
        if isinstance(field_value, dict):
            return {key: self.parse_field(value) for key, value in field_value.items()}
        # For primitives, return the value directly
        if not hasattr(field_value, "__dict__"):
            return field_value
        # For AST nodes, convert to a dict of fields or a reference
        if isinstance(field_value, self.field_types):
            return dict(ast.iter_fields(field_value))
        if isinstance(field_value, ast.AST):
            return self.get_node_path(field_value)
        raise ValueError(f"Unsupported field type: {type(field_value)}")


class PythonExtractor:
    """Main class that orchestrates ID assignment and component extraction."""

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
        self.id_assigner = IdAssigner(source)
        self.component_extractor = ComponentExtractor(entity_types, field_types)

    def extract_from_input(self, input_python: str) -> pd.DataFrame:
        """Extract components from Python code."""
        tree = ast.parse(input_python)
        
        # First pass: assign IDs
        self.id_assigner.assign_ids(tree)
        
        # Second pass: extract components
        entities = self.component_extractor.extract_components(tree)
        
        return pd.DataFrame(entities)