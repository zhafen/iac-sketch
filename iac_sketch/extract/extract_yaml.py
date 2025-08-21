"""
YAML extraction functionality for parsing component definitions from YAML files.
"""

import yaml
import pandas as pd


class YAMLExtractor:
    """Main class that orchestrates YAML parsing and component extraction."""

    def __init__(self):
        pass

    def extract(self, filepath: str) -> pd.DataFrame:
        """Extract components from a YAML file."""
        with open(filepath, "r", encoding="utf-8") as file:
            input_yaml = file.read()

        return self.extract_from_input(input_yaml, source=filepath)

    def extract_from_input(
        self, input_yaml: str, source: str = "input"
    ) -> list[dict]:
        """Extract components from YAML content.
        
        Args:
            input_yaml: YAML content as string
            source: Source identifier for the YAML (filename, "input", etc.)
            
        Returns:
            DataFrame with extracted entities and components
        """
        try:
            parsed_yaml = yaml.safe_load(input_yaml)
        except (yaml.parser.ParserError, yaml.scanner.ScannerError) as e:
            raise ValueError(f"Error parsing YAML from {source}") from e

        if parsed_yaml is None:
            return []

        entities = []
        for entity, comps in parsed_yaml.items():
            # Check if the entity already exists
            if entity in entities:
                raise KeyError(f"Entity {entity} is defined in multiple files.")
            # Get a list containing each component
            entity_comps = self.parse_components_list(entity, comps, source=source)
            entities += entity_comps

        return entities

    def parse_components_list(
        self, entity: str, comps: list, source: str = None
    ) -> list:
        """Parse a list of components for an entity.
        
        Args:
            entity: Entity name
            comps: List of component definitions
            source: Source identifier
            
        Returns:
            List of component dictionaries
        """
        extracted_comps = []
        for i, entry in enumerate(comps):
            format_error = ValueError(
                f"Entity component {entity}.{i} is not formatted correctly."
            )
            # When just given a flag
            if isinstance(entry, str):
                comp_entity = entry
                comp = pd.NA
            # When given values for a component
            elif isinstance(entry, dict):
                # Check formatting
                if len(entry) != 1:
                    raise format_error
                comp_entity, comp = list(entry.items())[0]

                # Format the component itself
                # If comp is just a value, wrap it in a dictionary
                if not isinstance(comp, dict):
                    comp = {"value": comp}

                # If the component has a key that is the same as the entity,
                # we assume that is the value for the component.
                if comp_entity in comp:
                    # Can't have both though
                    if "value" in comp:
                        raise format_error
                    # Rename the key to "value"
                    comp["value"] = comp.pop(comp_entity)

            # We should only have dictionaries or strings
            else:
                raise format_error
            row = {
                "entity": entity,
                "comp_key": str(i),
                "component_type": comp_entity,
                "component": comp,
            }
            extracted_comps.append(row)
        # Metadata component
        extracted_comps.append(
            {
                "entity": entity,
                "comp_key": str(len(extracted_comps)),
                "component_type": "metadata",
                "component": {
                    "source": source,
                    # Increase by one to account for the metadata component
                    "n_comps": len(extracted_comps) + 1,
                },
            }
        )
        return extracted_comps
