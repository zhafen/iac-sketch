"""
ETL workflow for registry processing, based on base_manifest/etl.yaml.
"""
import yaml
import pandas as pd
from typing import List, Dict, Callable, Any
from . import data


# Extraction system: handles reading and parsing entities from YAML
class ExtractSystem:
    def extract_entities(self, input_paths: List[str]) -> pd.DataFrame:
        """
        Load the entities from yaml files.
        """
        all_entities = []
        for path in input_paths:
            with open(path, 'r', encoding='utf-8') as f:
                yaml_str = f.read()
            entities = self.extract_entities_from_yaml(yaml_str)
            all_entities.extend(entities)
        return pd.DataFrame(all_entities)

    def extract_entities_from_yaml(self, yaml_str: str) -> List[Dict[str, Any]]:
        """
        Read the entities from a yaml string or stream.
        """
        yaml_data = yaml.safe_load(yaml_str)
        if not isinstance(yaml_data, dict):
            return []
        return self.parse_components_list(yaml_data)

    def parse_components_list(self, components_dict: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Convert a dictionary containing components into a list of components.
        """
        entities = []
        for entity, comps in components_dict.items():
            if isinstance(comps, list):
                for comp in comps:
                    entities.append({'entity': entity, **comp})
            elif isinstance(comps, dict):
                entities.append({'entity': entity, **comps})
            else:
                entities.append({'entity': entity, 'component': comps})
        return entities

    def load_entities_to_registry(self, entities: pd.DataFrame) -> data.Registry:
        """
        Convert entities DataFrame to a Registry object.
        """
        # This is a placeholder; actual implementation may differ
        return data.Registry.from_entities_df(entities)


# Transform system: handles all transforms on the registry
class TransformSystem:
    def __init__(self):
        self.preprocess_transforms: List[Callable[[data.Registry], data.Registry]] = []
        self.system_transforms: List[Callable[[data.Registry], data.Registry]] = []
        self.user_transforms: List[Callable[[data.Registry], data.Registry]] = []

    def apply_preprocess_transforms(self, registry: data.Registry) -> data.Registry:
        """
        Applies a set of required transforms to components that must always occur before any other transforms.
        """
        for transform in self.preprocess_transforms:
            registry = transform(registry)
        return registry

    def apply_system_transforms(self, registry: data.Registry) -> data.Registry:
        """
        Applies a set of system-defined transforms.
        """
        return self.apply_transforms(registry, self.system_transforms)

    def apply_transforms(self, registry: data.Registry, transforms: List[Callable[[data.Registry], data.Registry]]) -> data.Registry:
        """
        Applies a list of transforms to the registry in order.
        """
        for transform in transforms:
            registry = transform(registry)
        return registry

    def get_transform_order(self, dependencies: Dict[str, List[str]]) -> List[str]:
        """
        Given a dependency dict, return a list of transform names in topological order.
        """
        import networkx as nx
        G = nx.DiGraph()
        for t, deps in dependencies.items():
            for dep in deps:
                G.add_edge(dep, t)
        return list(nx.topological_sort(G))

    def apply_transform(self, registry: data.Registry, transform: Callable[[data.Registry], data.Registry]) -> data.Registry:
        """
        Apply a single transform to the registry.
        """
        return transform(registry)



