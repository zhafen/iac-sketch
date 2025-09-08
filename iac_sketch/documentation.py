"""Module for generating documentation from infrastructure-as-code manifests."""

import pandas as pd

from . import data


class DocumentationSystem:

    def generate_documentation(
        self,
        output_dir: str,
        registry: data.Registry,
        excluded_sources: list[str] = ["system"],
    ) -> str:
        """
        Generates markdown documentation for the infrastructure-as-code manifests.

        Parameters
        ----------
        registry : data.Registry
            The registry containing the extracted entities.

        Returns
        -------
        None
        """

        # Entities to document
        entity_sources = registry.view("entity_source")

        # Drop duplicate entity/source pairs
        entities = entity_sources.index.get_level_values("entity")
        is_duplicated = entities.duplicated(keep="first")
        entity_sources = registry.reset_index(entity_sources.loc[~is_duplicated])

        # Write out one file per source
        for source, entity_sources_i in entity_sources.groupby("source"):
            # Skip excluded sources, e.g. system
            if source in excluded_sources:
                continue

            # Generate the markdown representation
            entity_sources_repr = self.generate_markdown(
                entity_sources_i["entity"],
                registry,
            )

            # Write to file
            with open(f"{output_dir}/{source}.md", "w", encoding="utf-8") as f:
                f.write(entity_sources_repr)

    def generate_markdown(self, entities: pd.Series, registry: data.Registry) -> str:

        compinsts = registry.view("compinst")

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
