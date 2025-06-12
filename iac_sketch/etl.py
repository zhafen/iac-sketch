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
        self,
        registry: data.Registry,
        transformer,
        apply_components: None | str | list[str] | dict[str, str | list[str]] = None,
        fit_components: str | list[str] = None,
    ) -> data.Registry:
        """
        Apply a scikit-learn style transformer to registry components.
        - transformer: must implement transform and, if fit_components is provided, fit methods.
        - apply_components: str or list of str, registry keys to transform.
        - fit_components: str or list of str, registry keys to fit on.
        Returns a new Registry with transformed components.
        """

        # Format the arguments for transformation
        # Full form is a dictionary mapping target component keys
        # to source component keys
        if not isinstance(apply_components, dict):
            if apply_components is not None:
                if isinstance(apply_components, str):
                    apply_components = [apply_components]
            else:
                apply_components = registry.keys()
            apply_components = {comp: comp for comp in apply_components}
        if isinstance(fit_components, str):
            fit_components = [fit_components]

        # Fit transformer on concatenated fit_components
        if fit_components is not None:
            fit_data = registry.view(fit_components)
            transformer.fit(fit_data)

        # Copy registry to avoid mutation
        new_registry = registry.copy()
        for target_comp, source_comp in apply_components.items():
            input_data = registry.view(source_comp)
            try:
                new_registry[target_comp] = transformer.transform(input_data)
            except AssertionError as e:
                raise ValueError(
                    f"Transformer {transformer} failed to transform component "
                    f"'{target_comp}' with source '{source_comp}'"
                ) from e
        return new_registry
