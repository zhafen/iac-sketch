"""
Metadata
--------
- parameterization:
    name: documentation
    value:
        output_dir [str]: >
            Directory to output generated documentation files, relative to root_dir.
        excluded_sources [list[str]]: >
            List of sources to exclude from documentation generation. Default is
            ["system"] to avoid generating documentation for system-added components.
"""
from abc import abstractmethod
import os

import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from .. import data


class DocsGeneratorPreparer(BaseEstimator, TransformerMixin):

    def fit(self, _X, _y=None):
        return self

    def transform(
        self, X: pd.DataFrame, registry: data.Registry = None
    ) -> pd.DataFrame:

        # Validate and get an index-less copy
        if X.attrs["view_components"] != "documentation":
            raise ValueError(
                "The input component for preparing documents should be"
                f"[documentation]. Got: {X.attrs['view_components']}"
            )

        # Add a documentation component for every entity,
        # in addition to whatever already exists.
        X_generated = pd.DataFrame(
            {"entity": registry.entities, "comp_key": pd.NA, "value": pd.NA}
        )
        X_out = pd.concat([X, X_generated], ignore_index=True)

        return X_out


class DocsGenerator(BaseEstimator, TransformerMixin):

    def fit(self, _X, _y=None):
        return self

    def transform(
        self,
        X: pd.DataFrame,
        registry: data.Registry,
    ) -> pd.DataFrame:

        # Validate and get an index-less copy
        if X.attrs["view_components"] != "documentation":
            raise ValueError(
                "The input component for generating documents should be"
                f"[documentation]. Got: {X.attrs['view_components']}"
            )

        # Drop duplicate entity/source pairs
        entities = X.index.get_level_values("entity")
        is_duplicated = entities.duplicated(keep="first")
        X = registry.reset_index(X.loc[~is_duplicated])

        # Write out one file per source
        os.makedirs(output_dir, exist_ok=True)
        for source, entity_sources_i in X.groupby("source"):
            # Skip excluded sources, e.g. system
            if source in excluded_sources:
                continue

            # Generate the markdown representation
            entity_sources_repr = self.generate_docs(
                entity_sources_i["entity"],
                registry,
            )

            # Write to file
            with open(f"{output_dir}/{source}.md", "w", encoding="utf-8") as f:
                f.write(entity_sources_repr)

    @abstractmethod
    def generate_docs(self, entities: pd.Index, registry: data.Registry) -> str:
        pass


class DefaultMarkdownGenerator(DocsGenerator):

    def generate_docs(
        self, entities: pd.Index, registry: data.Registry
    ) -> pd.DataFrame:

        # Loop over all entities
        output = ""
        for entity_i in entities:

            # One header per entity
            output += f"#### {entity_i}\n\n"

            # Component instances for this entity
            compinsts_i = compinsts.loc[entity_i].sort_values("component_type")

            # Loop over component instances
            for comp_key_j, compinst_j in compinsts_i.iterrows():

                # Get the actual component
                comptype_j_comps = registry.view(compinst_j["component_type"])

                # Handle single-level and multi-level indices
                if comptype_j_comps.index.nlevels == 2:
                    comp_j = comptype_j_comps.loc[(entity_i, comp_key_j)]
                else:
                    comp_j = comptype_j_comps.loc[entity_i]

                # Generate the markdown representation
                output += self.generate_component_markdown(
                    comp_j, compinst_j["component_type"]
                )
                output += "\n"
            output += "\n"
        return output

    def generate_component_markdown(
        self,
        comp: pd.Series,
        comp_type: str,
        skipped_fields: list[str] = ["comp_key", "value"],
    ) -> str:

        output = f"**{comp_type}:**"

        # If there's a value, we put it right after the component type
        # The "__iter__" check is to avoid treating lists/dicts as values
        if ("value" in comp) and (
            hasattr(comp["value"], "__iter__") or (not pd.isna(comp["value"]))
        ):
            output += f" {comp['value']}\n"
        else:
            output += "\n"

        # The other fields we list as bullet points
        n_bullets = 0
        for field, val in comp.items():
            if field in skipped_fields:
                continue

            # Skip null values
            if not hasattr(val, "__iter__") and pd.isna(val):
                continue

            output += f"- {field}: {val}\n"
            n_bullets += 1

        # Revert to simpler output if there are no fields to list
        if n_bullets == 0:
            output = f"**{comp_type}**\n"

        return output
