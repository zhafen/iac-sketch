"""
ETL workflow for registry processing, based on base_manifest/etl.yaml.
"""
import yaml
import pandas as pd
from typing import List, Dict, Callable, Any
from . import data


# Extraction system: handles reading and parsing entities from YAML
class ExtractSystem:
    def extract_entities(self, input_dir: str) -> data.Registry:
        registry = data.Registry({})
        for filename in glob.glob(f"{input_dir}/*.yaml"):
            with open(filename, "r", encoding="utf-8") as f:
                registry_i = self.read_entities(f)
            # Mark the file as the source of the data
            registry_i["metadata"]["source_file"] = filename
            registry.update(registry_i)
        return registry

    def extract_entities_from_yaml(self, input_file: str) -> data.Registry:
        input_file = yaml.safe_load(input_file)
        entities = []
        for entity, comps in input_file.items():
            # Check if the entity already exists
            if entity in entities:
                raise KeyError(f"Entity {entity} is defined in multiple files.")
            # Get a list containing each component
            entity_comps = self.parse_components_list(entity, comps)
            # Add a component indicating the file the entity was found in
            entity_comps.append(
                {
                    "entity": entity,
                    "comp_ind": len(entity_comps),
                    "component_entity": "metadata",
                    "component": {
                        # Increase by one to account for the metadata component
                        "n_comps": len(entity_comps) + 1,
                    },
                }
            )
            entities += entity_comps
        # Convert to a registry
        registry = data.Registry(
            {
                key: df.drop(columns="component_entity")
                for key, df in pd.DataFrame(entities).groupby("component_entity")
            }
        )
        return registry

    def parse_components_list(self, entity: str, comps: list) -> list:
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
            # We should only have dictionaries or strings
            else:
                raise format_error
            row = {
                "entity": entity,
                "comp_ind": i,
                "component_entity": comp_entity,
                "component": comp,
            }
            extracted_comps.append(row)
        return extracted_comps

    def load_entities_to_registry(self, entities: pd.DataFrame) -> data.Registry:
        pass


# Transform system: handles all transforms on the registry
class TransformSystem:
    def __init__(self):
        pass

    def apply_preprocess_transforms(self, registry: data.Registry) -> data.Registry:
        pass

    def apply_system_transforms(self, registry: data.Registry) -> data.Registry:
        pass

    def apply_transforms(self, registry: data.Registry, transforms: List[Callable[[data.Registry], data.Registry]]) -> data.Registry:
        pass

    def get_transform_order(self, dependencies: Dict[str, List[str]]) -> List[str]:
        pass

    def apply_transform(self, registry: data.Registry, transform: Callable[[data.Registry], data.Registry]) -> data.Registry:
        pass



