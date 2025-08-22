import ast
import os
import re

import pandas as pd

from .extract_yaml import YAMLExtractor


class PythonExtractor:
    """Main class that orchestrates ID assignment and component extraction.

    Components
    ----------
    - satisfies: minimizes_structure_repetition
    - status: in production
    """

    def __init__(
        self,
        entity_types: list[str] = [
            "FunctionDef",
            "ClassDef",
            "Module",
            "Import",
            "ImportFrom",
            "Call",
        ],
        field_types: list[str] = [
            "alias",
        ],
        docstring_yaml_delimiter: str = r"Components\n-+\n",
    ):
        self.id_assigner = IdAssigner()
        self.component_extractor = ComponentExtractor(
            entity_types=entity_types,
            field_types=field_types,
            docstring_yaml_delimiter=docstring_yaml_delimiter,
        )

    def extract(self, filepath: str, root_dir: str) -> list[dict]:
        """Extract components from a Python file."""
        with open(filepath, "r", encoding="utf-8") as file:
            input_python = file.read()

        root_entity = os.path.relpath(filepath, root_dir)[:-3]
        return self.extract_from_input(input_python, root_entity)

    def extract_from_input(
        self,
        input_python: str,
        root_entity: str = "direct_input/module",
    ) -> list[dict]:
        """Extract components from Python code."""
        module_node = ast.parse(input_python)

        # First pass: assign IDs
        module_node = self.id_assigner.assign_ids(
            module_node,
            root_path=root_entity,
        )

        # Second pass: extract components
        entities = self.component_extractor.extract_components(module_node)

        return entities


class IdAssigner(ast.NodeTransformer):
    """Assigns unique identifiers to AST nodes."""

    def __init__(
        self,
        entity_types: list[str] = [
            "FunctionDef",
            "ClassDef",
            "Module",
            "Import",
            "ImportFrom",
            "Call",
        ],
    ):
        self.entity_types = tuple(getattr(ast, t) for t in entity_types)

    def assign_ids(
        self, module_node: ast.Module, root_path: str = "direct_input/module"
    ) -> ast.Module:
        """Assign IDs to all nodes in the AST."""

        if not isinstance(module_node, ast.Module):
            raise TypeError("assign_ids only takes objects of type ast.Module as input")
        self.root_entity, self.root_comp_key = os.path.split(root_path)

        # Variables modified while iterating
        self.entity = self.root_entity
        self.comp_key = self.root_comp_key
        self.path = [self.root_entity]
        self.comp_counts = {}

        # Actually assign the ids
        module_node = self.visit(module_node)
        return module_node

    def visit(self, node):
        """Visit a node and assign it an ID."""

        if not isinstance(node, self.entity_types):
            node.entity = self.entity
            node.comp_key = self.comp_key
            node = self.generic_visit(node)
            return node

        self.entity = ".".join(self.path)

        # Get the component key based on the node type
        if isinstance(node, ast.Module):
            self.entity = self.root_entity
            self.comp_key = self.root_comp_key
        elif hasattr(node, "name"):
            self.comp_key = node.name
        else:
            self.comp_key = str(self.comp_counts.setdefault(self.entity, 0))
            self.comp_counts[self.entity] += 1

        # Set the attributes for the node
        node.entity = self.entity
        node.comp_key = self.comp_key

        self.path.append(self.comp_key)
        node = self.generic_visit(node)
        self.path.pop()

        return node


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
            "Call",
        ],
        field_types: list[str] = [
            "alias",
        ],
        docstring_yaml_delimiter: str = r"Components\n-+\n",
    ):
        self.entity_types = tuple(getattr(ast, t) for t in entity_types)
        self.field_types = tuple(getattr(ast, t) for t in field_types)
        self.yaml_extractor = YAMLExtractor()
        self.docstring_yaml_delimiter = docstring_yaml_delimiter

    def extract_components(self, tree: ast.AST) -> list[dict]:
        """Extract components from the AST."""
        self.entities = []
        self.visit(tree)
        return self.entities

    def get_node_id(self, node):
        """Get the entity and component key for a node."""

        if not hasattr(node, "entity") or not hasattr(node, "comp_key"):
            raise ValueError(
                "Node must have 'entity' and 'comp_key' attributes. "
                "Run IdAssigner first."
            )

        return node.entity, node.comp_key

    def get_node_path(self, node):
        """Get the full path for a node."""
        entity, comp_key = self.get_node_id(node)
        node_path = f"{entity}.{comp_key}"
        return node_path

    def visit(self, node):
        """Visit a node and extract component if it's an entity type."""
        if not isinstance(node, self.entity_types):
            self.generic_visit(node)
            return

        # Get the entity and component key
        entity, comp_key = self.get_node_id(node)

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

        # Get the docstring as a component
        try:
            docstring = ast.get_docstring(node)
        except TypeError:
            docstring = None
        if docstring is not None:
            comp["docstring"] = docstring
            component = {
                "entity": f"{entity}.{comp_key}",
                "comp_key": "docstring",
                "component_type": "docstring",
                "component": {"value": docstring},
            }
            self.entities.append(component)

            # Parse the docstring yaml, if it exists.
            docstring_yaml = re.split(
                self.docstring_yaml_delimiter, docstring, maxsplit=1
            )
            if len(docstring_yaml) > 1:
                input_yaml = f"{entity}.{comp_key}:\n{docstring_yaml[1]}"
                try:
                    yaml_entities = self.yaml_extractor.extract_from_input(
                        input_yaml,
                        source="docstring",
                    )
                    self.entities += yaml_entities
                except Exception as e:  # pylint: disable=W0718
                    component = {
                        "entity": f"{entity}.{comp_key}",
                        "comp_key": "docstring_error",
                        "component_type": "error",
                        "component": {"value": str(e)},
                    }
                    self.entities.append(component)

        # Visit children
        self.generic_visit(node)

    def parse_field(self, field_value):
        """Parse a field value, handling different types appropriately."""
        # For lists and dicts, recursively parse their contents
        if isinstance(field_value, list):
            field_value = [self.parse_field(item) for item in field_value]
        elif isinstance(field_value, dict):
            field_value = {
                key: self.parse_field(value) for key, value in field_value.items()
            }
        # For primitives, return the value directly
        elif not hasattr(field_value, "__dict__"):
            pass
        # For Name AST nodes, return the name
        elif isinstance(field_value, ast.Name):
            field_value = field_value.id
        # For Attribute AST nodes, recurse
        elif isinstance(field_value, ast.Attribute):
            field_value = self.parse_field(field_value.value) + f".{field_value.attr}"
        # For other AST nodes, convert to a dict of fields or a reference
        elif isinstance(field_value, self.field_types):
            field_value = {
                k: self.parse_field(v) for k, v in ast.iter_fields(field_value)
            }
        elif isinstance(field_value, ast.AST):
            field_value = self.get_node_path(field_value)
        else:
            raise ValueError(f"Unsupported field type: {type(field_value)}")

        return field_value
