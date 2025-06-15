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
        base_manifest_pattern = f"{base_dir}/base_manifest/*.yaml"
        filename_patterns.append(base_manifest_pattern)

        entities = []
        for pattern in filename_patterns:
            for filename in glob.glob(pattern):
                with open(filename, "r", encoding="utf-8") as f:
                    entities_i = self.extract_entities_from_yaml(f, source=filename)
                entities.append(entities_i)

        entities = pd.concat(entities, ignore_index=True)

        return self.load_entities_to_registry(entities)

    def extract_entities_from_yaml(
        self,
        input_yaml: str,
        source: str = None,
    ) -> pd.DataFrame:
        input_yaml = yaml.safe_load(input_yaml)
        entities = []
        for entity, comps in input_yaml.items():
            # Check if the entity already exists
            if entity in entities:
                raise KeyError(f"Entity {entity} is defined in multiple files.")
            # Get a list containing each component
            entity_comps = self.parse_components_list(entity, comps, source=source)
            entities += entity_comps

        return pd.DataFrame(entities)

    def parse_components_list(
        self, entity: str, comps: list, source: str = None
    ) -> list:
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
                "comp_ind": i,
                "component_entity": comp_entity,
                "component": comp,
            }
            extracted_comps.append(row)
        # Metadata component
        extracted_comps.append(
            {
                "entity": entity,
                "comp_ind": len(extracted_comps),
                "component_entity": "metadata",
                "component": {
                    "source": source,
                    # Increase by one to account for the metadata component
                    "n_comps": len(extracted_comps) + 1,
                },
            }
        )
        return extracted_comps

    def load_entities_to_registry(self, entities: pd.DataFrame) -> data.Registry:

        # Convert to a registry
        registry = data.Registry(
            {
                # We don't want the component_entity column in the final registry
                # since it was just used to group the components.
                # We also don't care about the index, so reset it.
                key: df.drop(columns="component_entity").reset_index(drop=True)
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
        self,
        registry: data.Registry,
        transformer,
        apply_components: dict[str, data.View],
        fit_components: data.View = None,
    ) -> data.Registry:

        # Fit transformer on concatenated fit_components
        if fit_components is not None:
            fit_data = registry.resolve_view(fit_components)
            transformer.fit(fit_data)

        # Copy registry to avoid mutation
        new_registry = registry.copy()
        for target_comp, source_comp in apply_components.items():
            input_data = registry.resolve_view(source_comp)
            try:
                new_registry[target_comp] = transformer.transform(input_data)
            except AssertionError as e:
                raise ValueError(
                    f"Transformer {transformer} failed to transform component "
                    f"'{target_comp}' with source '{source_comp}'"
                ) from e
        return new_registry

    def apply_one_to_one_transform(
        self,
        registry: data.Registry,
        transformer,
        apply_components: str | list[str] = None,
    ) -> data.Registry:

        # Format the arguments to then call apply_transform
        if apply_components is None:
            apply_components = registry.keys()
        elif isinstance(apply_components, str):
            apply_components = [apply_components]

        apply_components = {comp: data.View(comp) for comp in apply_components}

        return self.apply_transform(
            registry,
            transformer,
            apply_components=apply_components,
        )
