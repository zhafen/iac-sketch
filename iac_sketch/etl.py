"""
ETL workflow for registry processing, based on base_manifest/etl.yaml.
"""

import copy
import networkx as nx
import pandas as pd
from typing import List, Dict, Callable
import glob
import os

from . import data
from . import transform
from .extract import YAMLExtractor


# Extraction system: handles reading and parsing entities from YAML
class ExtractSystem:

    def __init__(self):
        self.yaml_extractor = YAMLExtractor()

    def extract_entities(
        self, filename_patterns: str | List[str] = [], input_yaml: str = None
    ) -> data.Registry:

        # Ensure we don't modify the original list
        filename_patterns = copy.copy(filename_patterns)

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
                    entities_i = self.yaml_extractor.extract_entities_from_yaml(f, source=filename)
                entities.append(entities_i)

        # Add direct input YAML if provided
        if input_yaml is not None:
            entities_i = self.yaml_extractor.extract_entities_from_yaml(input_yaml, source="input")
            entities.append(entities_i)

        entities = pd.concat(entities, ignore_index=True)

        return self.load_entities_to_registry(entities)

    def load_entities_to_registry(self, entities: pd.DataFrame) -> data.Registry:

        # Convert to a registry
        registry = data.Registry(
            {
                # We don't want the component_type column in the final registry
                # since it was just used to group the components.
                # We also don't care about the index, so reset it.
                key: df.drop(columns="component_type")
                for key, df in entities.groupby("component_type")
            }
        )

        # We also record the mapping of components to entities in the "compinst"
        # component. We take the time to use the same format as the other components.
        registry["compinst"] = entities[
            ["entity", "comp_ind", "component_type"]
        ].set_index(["entity", "comp_ind"])

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
        mode: str = "overwrite",
    ) -> data.Registry:

        # Copy registry to avoid mutation
        new_registry = registry.copy()
        for target_comp, source_view in components_mapping.items():
            # We make a kwargs dictionary so we can easily include the registry
            try:
                result = transformer.transform(
                    registry.resolve_view(source_view),
                    registry,
                )
                new_registry.set(
                    target_comp,
                    result,
                    mode=mode,
                )
            except AssertionError as e:
                raise ValueError(
                    f"Transformer {transformer} failed to transform component "
                    f"'{target_comp}' with source '{source_view}'"
                ) from e
        return new_registry

    def apply_preprocess_transforms(self, registry: data.Registry) -> data.Registry:

        registry = self.normalize_components(registry)
        registry = self.extract_compdefs(registry)
        registry = self.validate_compdefs(registry)

        return registry

    def normalize_components(self, registry: data.Registry) -> data.Registry:

        return self.apply_transform(
            registry,
            transform.ComponentNormalizer(),
            # The components are transformed individually, with a few exceptions.
            components_mapping={
                comp: data.View(comp)
                for comp in registry.keys()
                if comp not in ["compinst", "fields"]
            },
        )

    def extract_compdefs(self, registry: data.Registry) -> data.Registry:

        return self.apply_transform(
            registry,
            transform.ComponentDefExtractor(),
            # We only transform a single component, "component",
            # and it receives a view that joins the "component" and "fields"
            # components.
            components_mapping={
                "compdef": data.View(
                    ["component", "fields"], join_how="outer"
                )
            },
        )

    def validate_compdefs(self, registry: data.Registry) -> data.Registry:
        """First we validate the component definitions, since they'll be used
        to validate the components themselves.
        We also do this in postprocessing.
        """

        registry = self.apply_transform(
            registry,
            transform.ComponentValidator(),
            components_mapping={"compdef": data.View("compdef")},
        )

        return self.apply_transform(
            registry,
            transform.ComponentValidator(),
            components_mapping={
                comp: data.View(comp) for comp in registry.keys() if comp != "compdef"
            },
        )

    def apply_system_transforms(self, registry: data.Registry) -> data.Registry:

        # Parse links components into link components
        registry = self.apply_transform(
            registry,
            transform.LinksParser(),
            components_mapping={"link": data.View("links")},
            mode="upsert",
        )

        # Collect components with link_type tags into the link component df
        registry = self.apply_transform(
            registry,
            transform.LinkCollector(),
            components_mapping={"link": data.View("link")},
            mode="upsert",
        )

        registry = self.build_graph_from_links(registry)

        return registry

    def build_graph_from_links(self, registry: data.Registry) -> data.Registry:

        # Build a graph from the links
        registry.graph = nx.from_pandas_edgelist(
            registry.view("link"),
            source="source",
            target="target",
            edge_key="link_type",
            create_using=nx.DiGraph,
        )
        registry.graph.add_nodes_from(registry.entities)
        registry = self.apply_transform(
            registry,
            transform.GraphAnalyzer(),
            components_mapping={"node": data.View("link")},
            mode="overwrite",
        )

        return registry

    def apply_postprocess_transforms(self, registry: data.Registry) -> data.Registry:

        registry = self.validate_compdefs(registry)

        return registry