import glob

import pandas as pd
import yaml

from . import data


class ParseSystem:

    ignored_components = []

    def parse(self, input_dir: str) -> data.Registry:
        """
        Parse the input directory and return a dictionary of DataFrames.
        """

        # Extract the entities from the YAML files
        registry = self.extract(input_dir)

        # Transform the entities into a dictionary of DataFrames
        registry = self.transform(registry)

        return registry

    def extract(self, input_dir: str) -> data.Registry:

        registry = data.Registry({})
        for filename in glob.glob(f"{input_dir}/*.yaml"):
            with open(filename, "r", encoding="utf-8") as f:
                registry_i = self.extract_from_stream(f)
            registry.components.update(registry_i.components)
            # Mark the file as the source of the data
            registry["metadata"]["source_file"] = filename

        return registry

    def extract_from_stream(self, input_file: str) -> data.Registry:

        input_file = yaml.safe_load(input_file)

        entities = []
        for entity, comps in input_file.items():

            # Check if the entity already exists
            if entity in entities:
                raise KeyError(f"Entity {entity} is defined in multiple files.")

            # Get a list containing each component
            entity_comps = self.extract_entity(entity, comps)

            # Add a component indicating the file the entity was found in
            entity_comps.append(
                {
                    "entity": entity,
                    "comp_ind": len(entity_comps),
                    "component_entity": "metadata",
                    "component": {
                        # Increase by one to account for the metadata component
                        "n_comps": len(entity_comps)
                        + 1,
                    },
                }
            )

            entities += entity_comps

        # Convert to a registry
        entities = pd.DataFrame(entities)
        registry = data.Registry(
            {key: df for key, df in entities.groupby("component_entity")}
        )

        return registry

    def extract_entity(self, entity: str, comps: list) -> list:

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

    def transform(self, registry: data.Registry) -> data.Registry:

        comps = {}
        for comp_key in registry.keys():

            # Look for the function to parse the entity
            parse_fn = f"parsecomp_{comp_key}"
            if hasattr(self, parse_fn):
                comps[comp_key] = getattr(self, parse_fn)(registry)
            # If the component is ignored, skip it
            elif comp_key in self.ignored_components:
                continue
            # Default to the cleaned version
            else:
                comps[comp_key] = self.general_parsecomp(comp_key, registry)

        return comps

    def general_parsecomp(
        self, group_key: str, registry: data.Registry
    ) -> pd.DataFrame:

        # Get the data, slightly cleaned
        group = registry[group_key].reset_index(drop=True)

        # Try parsing the component column
        comp_data = pd.json_normalize(group["component"])

        # If there wasn't a dictionary to parse
        if len(comp_data.columns) == 0:
            group = group.rename(columns={"component": group_key})
            if group[group_key].isna().all():
                group = group.drop(columns=[group_key])
        # If the component column was parsed successfully
        else:

            # For the rows that were not parsed because they were not dictionaries
            # try setting the group_key column to the component value.
            not_parsed = comp_data.isna().all(axis="columns")
            if group_key not in comp_data.columns and not_parsed.any():
                comp_data[group_key] = pd.NA
            comp_data.loc[not_parsed, group_key] = group.loc[not_parsed, "component"]

            # Clean and join
            group = group.drop(columns=["component"])
            group = group.join(comp_data)

        return group

    # These components are handled as part of the component component
    ignored_components += [
        "data",
    ]

    def parsecomp_component(
        self,
        registry: data.Registry,
    ) -> pd.DataFrame:

        components = self.build_components_dataframe(registry)
        components = self.parse_fields(components)

        return components

    def build_components_dataframe(self, registry: data.Registry) -> pd.DataFrame:

        # Get the entities with the components flag
        components = registry["component"]
        components = components[["entity", "comp_ind"]]

        # Get the entities with the data component
        data_comp = registry["data"]
        data_comp = data_comp.rename(
            columns={"comp_ind": "data_comp_ind", "component": "data"}
        ).drop(columns=["component_entity"])

        # Join the components with the data component
        components = components.set_index("entity").join(
            data_comp.set_index("entity"), how="outer"
        )

        # Identify the components that are defined vs implicitly included
        components["defined"] = True
        comps_created = pd.DataFrame({"entity": registry.keys()})
        components = components.merge(comps_created, how="outer", on="entity")
        components.loc[components["defined"].isna(), "defined"] = False
        components["defined"] = components["defined"].astype(bool)

        return components

    def parse_fields(self, components: pd.DataFrame) -> pd.DataFrame:

        # Make a copy of the data column so we can refer to the unparsed data as well
        components["unparsed_data"] = components["data"]

        valids = []
        valid_messages = []
        fields = []
        for _, comp in components.query("defined").iterrows():
            fields_i = {}

            if comp.notna()["data"]:

                # Parse the fields
                valid_fields = True
                valid_message = ""
                for field_key, field_value in comp["data"].items():
                    try:
                        field = data.Field.from_kv_pair(field_key, field_value)
                        fields_i[field.name] = field
                    except ValueError:
                        valid_fields = False
                        valid_message = (
                            f"field {field_key} is incorrectly formatted: {field_value}"
                        )
                        break

                if not valid_fields:
                    valids.append(False)
                    valid_messages.append(valid_message)
                    fields.append(pd.NA)
                    continue

            # If we got this far the component is valid
            fields.append(fields_i)
            valids.append(True)
            valid_messages.append("")

        # Defaults
        components["valid"] = False
        components["valid_message"] = "undefined"
        # Then override
        components.loc[components["defined"], "valid"] = valids
        components.loc[components["defined"], "valid_message"] = valid_messages
        components.loc[components["defined"], "data"] = fields

        return components

    def parsecomp_links(
        self,
        registry: data.Registry,
    ) -> pd.DataFrame:

        # Pass the entities to the general parse function first
        links = self.general_parsecomp("links", registry)

        # Parse the links column
        exploded_links = (
            links["links"]
            # Split on newlines
            .str.strip()
            .str.split("\n")
            .explode()
            # Split on arrows
            .str.strip()
            .str.split("-->", expand=True)
            # Rename columns
            .rename(columns={0: "source", 1: "target"})
        )
        if len(exploded_links.columns) > 2:
            raise ValueError(
                "Links column is not formatted correctly. Did you use | or >? "
            )
        # Add the parsed results back to the original DataFrame
        links = (
            links.join(exploded_links).drop(columns=["links"]).reset_index(drop=True)
        )

        # Get the new comp index, using the metadata
        links["comp_ind"] = links.groupby("entity").cumcount()
        links["comp_ind"] += links.merge(registry["metadata"], on="entity", how="left")[
            "n_comps"
        ]

        # Add these links to the link component
        link_comp = registry.get("link", pd.DataFrame())
        registry.components["link"] = pd.concat([link_comp, links], ignore_index=True)

        return links
