"""
ETL workflow for registry processing, based on base_manifest/etl.yaml.
"""

import yaml
import pandas as pd
from typing import List, Dict, Callable, Any
from . import data
import glob
import os


# Extraction system: handles reading and parsing entities from YAML
class ExtractSystem:
    def extract_entities(self, filename_patterns: str | List[str]) -> data.Registry:

        if isinstance(filename_patterns, str):
            filename_patterns = [filename_patterns]

        # Always include all YAML files in the base_manifest directory (one level up from this file)
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        base_manifest_pattern = f"{base_dir}/base_manifest/*"
        filename_patterns.append(base_manifest_pattern)

        entities = []
        for pattern in filename_patterns:
            for filename in glob.glob(pattern):
                with open(filename, "r", encoding="utf-8") as f:
                    entities_i = self.extract_entities_from_yaml(f)
                # Assemble a metadata component for each entity
                metadata_i = entities_i["entity"].value_counts()
                metadata_i.name = "comp_ind"
                metadata_i = metadata_i.reset_index()
                metadata_i["metadata"] = metadata_i.apply(
                    lambda row: {
                        "source_file": filename,
                        "n_comps": row["comp_ind"] + 1,
                    },
                    axis="columns",
                )

                entities_i["metadata"]["source_file"] = filename
                entities.append(entities_i)

        entities = pd.concat(entities, ignore_index=True)

        return self.load_entities_to_registry(entities)

    def extract_entities_from_yaml(self, input_yaml: str) -> pd.DataFrame:
        input_yaml = yaml.safe_load(input_yaml)
        entities = []
        for entity, comps in input_yaml.items():
            # Check if the entity already exists
            if entity in entities:
                raise KeyError(f"Entity {entity} is defined in multiple files.")
            # Get a list containing each component
            entity_comps = self.parse_components_list(entity, comps)
            entities += entity_comps

        return pd.DataFrame(entities)

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

        # Convert to a registry
        registry = data.Registry(
            {
                key: df.drop(columns="component_entity")
                for key, df in entities.groupby("component_entity")
            }
        )
        return registry


# Transform system: handles all transforms on the registry
class TransformSystem:
    def __init__(self):
        pass

    def apply_preprocess_transforms(self, registry: data.Registry) -> data.Registry:
        pass

    def apply_system_transforms(self, registry: data.Registry) -> data.Registry:
        pass

    def apply_transforms(
        self,
        registry: data.Registry,
        transforms: List[Callable[[data.Registry], data.Registry]],
    ) -> data.Registry:
        pass

    def get_transform_order(self, dependencies: Dict[str, List[str]]) -> List[str]:
        pass

    def apply_transform(
        self, registry: data.Registry, source: str, target: str, mode: str = "append"
    ) -> data.Registry:
        pass
