import glob

import pandas as pd
import yaml

from . import data


class ParseSystem:

    def parse(self, input_dir: str) -> data.Registry:
        """
        Parse the input directory and return a dictionary of DataFrames.
        """

        # Extract the entities from the YAML files
        registry = self.extract_entities(input_dir)

        # Transform the entities into a dictionary of DataFrames
        registry = self.transform(registry)

        return registry

    def extract_entities(self, input_dir: str) -> data.Registry:

        registry = data.Registry({})
        for filename in glob.glob(f"{input_dir}/*.yaml"):
            with open(filename, "r", encoding="utf-8") as f:
                registry_i = self.read_entities(f)
            # Mark the file as the source of the data
            registry_i["metadata"]["source_file"] = filename
            registry.update(registry_i)

        return registry

    def extract_entities_from_yaml(self, input_file: str) -> data.Registry:

        input_file = yaml.safe_load(input_file)

        entities = []
        for entity, comps in input_file.items():

            # Check if the entity already exists
            if entity in entities:
                raise KeyError(f"Entity {entity} is defined in multiple files.")

            # Get a list containing each component
            entity_comps = self.read_entity(entity, comps)

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
        registry = data.Registry(
            {
                key: df.drop(columns="component_entity")
                for key, df in pd.DataFrame(entities).groupby("component_entity")
            }
        )

        return registry

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

    def transform(self, registry: data.Registry) -> data.Registry:

        # Do a regular pass-through first
        registry = self.base_transform(registry)

        # Now do the customized parsing
        for comp_key in list(registry.keys()):

            if comp_key in registry.parsed_components:
                continue

            # Look for the function to parse the entity
            parse_fn = f"parsecomp_{comp_key}"
            if hasattr(self, parse_fn):
                getattr(self, parse_fn)(registry)

        # Validate again after the transformation
        registry.validate()

        return registry

    def base_transform(self, registry: data.Registry) -> data.Registry:

        # Pass through with base_parsecomp
        registry.components = {
            comp_key: (
                self.base_parsecomp(comp_key, registry)
                if comp_key not in registry.parsed_components
                else registry[comp_key]
            )
            for comp_key in registry.keys()
        }

        # Further parse the components component
        self.parsecomp_component(registry)
        registry.validate_component("component")
        registry.parsed_components.append("component")

        # With the components component parsed, we can validate the registry
        registry.validate()

        return registry

    def base_parsecomp(self, comp_key: str, registry: data.Registry) -> pd.DataFrame:

        # Get the data, slightly cleaned
        comp_df = registry[comp_key].reset_index(drop=True)

        # Try parsing the component column
        comp_data = pd.json_normalize(comp_df["component"])

        # If there wasn't a dictionary to parse
        if len(comp_data.columns) == 0:
            comp_df = comp_df.rename(columns={"component": comp_key})
            if comp_df[comp_key].isna().all():
                comp_df = comp_df.drop(columns=[comp_key])
        # If the component column was parsed successfully
        else:

            # For the rows that were not parsed because they were not dictionaries
            # try setting the comp_key column to the component value.
            not_parsed = comp_data.isna().all(axis="columns")
            if comp_key not in comp_data.columns and not_parsed.any():
                comp_data[comp_key] = pd.NA
            comp_data.loc[not_parsed, comp_key] = comp_df.loc[not_parsed, "component"]

            # Clean and join
            comp_df = comp_df.drop(columns=["component"])
            comp_df = comp_df.join(comp_data)

        return comp_df

    def parsecomp_component(
        self,
        registry: data.Registry,
    ) -> pd.DataFrame:

        comps_df = self.build_components_dataframe(registry)
        comps_df = self.parse_fields(comps_df)
        comps_df = comps_df.set_index("entity")
        registry["component"] = comps_df

        return comps_df

    def build_components_dataframe(self, registry: data.Registry) -> pd.DataFrame:

        # Get the components component
        # We drop the component column because it is not meaningful,
        # but is added by default by the base_parsecomp method
        comp_df = registry["component"].drop(columns=["component"])

        # Get the entities with the data component
        data_comp = registry["fields"]
        data_comp = data_comp.rename(
            columns={"comp_ind": "fields_comp_ind", "component": "fields"}
        )

        # Join the components with the data component
        comp_df = comp_df.set_index("entity").join(
            data_comp.set_index("entity"), how="outer"
        )

        # Identify the components that are defined vs implicitly included
        comp_df["defined"] = True
        comps_created = pd.DataFrame({"entity": registry.keys()})
        comp_df = comp_df.merge(comps_created, how="outer", on="entity")
        comp_df.loc[comp_df["defined"].isna(), "defined"] = False
        comp_df["defined"] = comp_df["defined"].astype(bool)

        return comp_df

    def parse_fields(self, components: pd.DataFrame) -> pd.DataFrame:

        # Make a copy of the data column so we can refer to the unparsed data as well
        components["unparsed_fields"] = components["fields"]

        valids = []
        valid_messages = []
        fields = []
        for _, comp in components.query("defined").iterrows():
            fields_i = {}

            if comp.notna()["fields"]:

                # Parse the fields
                valid_fields = True
                valid_message = ""
                for field_key, field_value in comp["fields"].items():
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
        components["valid_def"] = False
        components["valid_def_message"] = "undefined"
        # Then override
        components.loc[components["defined"], "valid_def"] = valids
        components.loc[components["defined"], "valid_def_message"] = valid_messages
        components.loc[components["defined"], "fields"] = fields

        return components

    def parsecomp_links(
        self,
        registry: data.Registry,
    ) -> pd.DataFrame:

        links_df = registry["links"]

        # Parse the links column
        exploded_links = (
            links_df["links"]
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
        # Strip whitespace
        for col in exploded_links.columns:
            exploded_links[col] = exploded_links[col].str.strip()
        if len(exploded_links.columns) > 2:
            raise ValueError(
                "Links column is not formatted correctly. Did you use | or >? "
            )
        # Add the parsed results back to the original DataFrame
        link_df = (
            links_df.join(exploded_links).drop(columns=["links"]).reset_index(drop=True)
        )

        # Get the new comp index, using the metadata
        link_df["comp_ind"] = link_df.groupby("entity").cumcount()
        merged_links = link_df.merge(registry["metadata"], on="entity", how="left")
        link_df["comp_ind"] += merged_links["n_comps"]

        # Also update the metadata
        n_new_comps = link_df.reset_index()["entity"].value_counts()
        metadata_df = registry["metadata"].set_index("entity")
        metadata_df.loc[n_new_comps.index, "n_comps"] += n_new_comps
        registry["metadata"] = metadata_df.reset_index()

        # Add these links to the link component
        link_comp = registry.components.get("link", pd.DataFrame())
        registry["link"] = pd.concat([link_comp, link_df], ignore_index=True)

        return link_df
