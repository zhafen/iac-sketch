"""
ETL workflow for registry processing, based on base_manifest/etl.yaml.
"""

import yaml
import pandas as pd
from typing import List, Dict, Callable
from . import data
import glob
import os

from . import transform


# Extraction system: handles reading and parsing entities from YAML
class ExtractSystem:

    def extract_entities(
        self, filename_patterns: str | List[str] = [], input: str = None
    ) -> data.Registry:

        if isinstance(filename_patterns, str):
            filename_patterns = [filename_patterns]

        # Always include all YAML files in the base_manifest directory
        # (one level up from this file)
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        base_manifest_pattern = f"{base_dir}/base_manifest/*.yaml"
        filename_patterns.append(base_manifest_pattern)

        # Iterate over the files
        entities = []
        for pattern in filename_patterns:
            for filename in glob.glob(pattern):
                with open(filename, "r", encoding="utf-8") as f:
                    entities_i = self.extract_entities_from_yaml(f, source=filename)
                entities.append(entities_i)

        # Add direct input YAML if provided
        if input is not None:
            entities_i = self.extract_entities_from_yaml(input, source="input")
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

    def apply_transforms(
        self,
        registry: data.Registry,
        transforms: List[Callable[[data.Registry], data.Registry]],
    ) -> data.Registry:
        # TODO: Delete?
        pass

    def get_transform_order(self, dependencies: Dict[str, List[str]]) -> List[str]:
        # TODO: Delete?
        pass

    def apply_transform(
        self,
        registry: data.Registry,
        transformer,
        components_mapping: dict[str, data.View],
        transform_kwargs: dict = {},
    ) -> data.Registry:

        # Copy registry to avoid mutation
        new_registry = registry.copy()
        for target_comp, source_view in components_mapping.items():
            # We make a kwargs dictionary so we can easily include the registry
            try:
                new_registry[target_comp] = transformer.transform(
                    registry.resolve_view(source_view),
                    **transform_kwargs,
                )
            except AssertionError as e:
                raise ValueError(
                    f"Transformer {transformer} failed to transform component "
                    f"'{target_comp}' with source '{source_view}'"
                ) from e
        return new_registry

    def apply_preprocess_transforms(self, registry: data.Registry) -> data.Registry:

        registry = self.normalize_components(registry)
        registry = self.extract_component_definitions(registry)
        registry = self.validate_components(registry)

        return registry

    def normalize_components(self, registry: data.Registry) -> data.Registry:

        return self.apply_transform(
            registry,
            transform.ComponentNormalizer(),
            # The components are transformed individually,
            # but we leave out the "fields" component
            # because it will be handled during the component definition extraction.
            components_mapping={
                comp: data.View(comp) for comp in registry.keys() if comp != "fields"
            },
        )

    def extract_component_definitions(self, registry: data.Registry) -> data.Registry:

        return self.apply_transform(
            registry,
            transform.ComponentDefExtractor(),
            # We only transform a single component, "component",
            # and it receives a view that joins the "component" and "fields"
            # components.
            components_mapping={
                "component": data.View(
                    ["component", "fields"], join_on="entity", join_how="outer"
                )
            },
            transform_kwargs={"registry_keys": list(registry.keys())},
        )

    def validate_components(self, registry: data.Registry) -> data.Registry:

        # First we validate the component definitions, since they'll be used
        # to validate the components themselves.
        registry = self.apply_transform(
            registry,
            transform.ComponentValidator(),
            components_mapping={
                "component": data.View("component")
            },
            transform_kwargs={"component_defs": registry.view("component")},
        )

        return self.apply_transform(
            registry,
            transform.ComponentValidator(),
            components_mapping={
                comp: data.View(comp) for comp in registry.keys() if comp != "component"
            },
            transform_kwargs={"component_defs": registry.view("component")},
        )

    def apply_system_transforms(self, registry: data.Registry) -> data.Registry:

        return registry

