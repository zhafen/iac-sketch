"""
ETL workflow for registry processing, based on base_manifest/etl.yaml.
"""

import copy
from typing import List, Dict, Callable
import glob
import os

import networkx as nx
import pandas as pd

from . import data
from . import transform
from .extract import YAMLExtractor, PythonExtractor


# Extraction system: handles reading and parsing entities from YAML
class ExtractSystem:

    def __init__(self):
        self.yaml_extractor = YAMLExtractor()
        self.python_extractor = PythonExtractor()

    def extract_entities(
        self,
        filename_patterns: str | List[str] = [],
        root_dir: str = None,
        input_yaml: str = None,
    ) -> data.Registry:

        if root_dir is None:
            root_dir = os.getcwd()

        # Ensure we don't modify the original list
        filename_patterns = copy.copy(filename_patterns)

        if isinstance(filename_patterns, str):
            filename_patterns = [filename_patterns]

        # Always include base manifest and source files
        source_dir = os.path.dirname(os.path.abspath(__file__))
        # Patterns relative to the source dir.
        system_filename_patterns = [
            "../base_manifest/*.yaml",
            "../base_manifest/*.yml",
            "./**/*.py",
        ]
        filename_patterns += [
            os.path.abspath(f"{source_dir}/{pattern}")
            for pattern in system_filename_patterns
        ]

        # Resolve paths relative to root
        filename_patterns = [
            (
                pattern
                if os.path.isabs(pattern)
                else os.path.abspath(f"{root_dir}/{pattern}")
            )
            for pattern in filename_patterns
        ]

        # Iterate over the files
        entities = []
        self.filenames = []
        for pattern in filename_patterns:
            filenames = glob.glob(pattern, recursive=True)
            for filename in filenames:
                self.filenames.append(filename)

                # Choose extractor based on file type
                if filename.endswith((".yaml", ".yml")):
                    extractor = YAMLExtractor()
                elif filename.endswith(".py"):
                    extractor = PythonExtractor()
                else:
                    continue

                # Perform extraction
                entities_i = extractor.extract(filename, root_dir=root_dir)
                entities += entities_i

        # Add direct input YAML if provided
        if input_yaml is not None:
            entities_i = self.yaml_extractor.extract_from_input(
                input_yaml, source="input"
            )
            entities += entities_i

        entities = pd.DataFrame(entities)

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
            ["entity", "comp_key", "component_type"]
        ].set_index(["entity", "comp_key"])

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
            except Exception as e:
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
                "compdef": data.View(["component", "fields"], join_how="outer")
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

        # Analyze requirements
        registry = self.apply_transform(
            registry,
            transform.RequirementAnalyzer(),
            components_mapping={"requirement": data.View("requirement")},
            mode="overwrite",
        )

        return registry

    def build_graph_from_links(self, registry: data.Registry) -> data.Registry:
        """
        Metadata
        ----------
        - todo: >
            Probably delete this, because it makes more sense to just make graphs as
            needed because the filtering is much more powerful *before* it's turned
            into a graph.
        """

        # Build a graph from the links
        registry.graph = nx.from_pandas_edgelist(
            registry.view("link"),
            source="source",
            target="target",
            edge_key="link_type",
            create_using=nx.MultiDiGraph,
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
