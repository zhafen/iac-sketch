import glob

import pandas as pd
import yaml

from .data import Field, Registry


class ParseSystem:

    ignored_components = []

    def parse(self, input_dir: str) -> Registry:
        """
        Parse the input directory and return a dictionary of DataFrames.
        """

        # Extract the entities from the YAML files
        entities = self.extract(input_dir)

        # Transform the entities into a dictionary of DataFrames
        comps = self.transform(entities)

        return Registry(entities=entities, components=comps)

    def extract(self, input_dir: str) -> pd.DataFrame:

        entities = []
        for filename in glob.glob(f"{input_dir}/*.yaml"):
            with open(filename, "r", encoding="utf-8") as file:
                file_entities = yaml.safe_load(file)

                for entity, comps in file_entities.items():

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
                                "source_file": filename,
                                # Increase by one to account for the metadata component
                                "n_comps": len(entity_comps) + 1,
                            }
                        }
                    )

                    entities += entity_comps

        # Convert to a DataFrame
        entities = pd.DataFrame(entities)

        return entities

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

    def transform(self, entities: pd.DataFrame) -> dict[str, pd.DataFrame]:

        entities_by_comp = entities.groupby("component_entity")

        comps = {}
        for group_key in entities_by_comp.groups.keys():

            # Look for the function to parse the entity
            parse_fn = f"parsecomp_{group_key}"
            if hasattr(self, parse_fn):
                comps[group_key] = getattr(self, parse_fn)(entities_by_comp)
            # If the component is ignored, skip it
            elif group_key in self.ignored_components:
                continue
            # Default to the cleaned version
            else:
                comps[group_key] = self.general_parsecomp(
                    group_key, entities_by_comp
                )

        return comps

    def general_parsecomp(
        self, group_key: str, entities_by_comp: pd.core.groupby.DataFrameGroupBy
    ) -> pd.DataFrame:

        # Get the data, slightly cleaned
        group = entities_by_comp.get_group(group_key).reset_index(drop=True)
        group = group.drop(columns=["component_entity"])

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
        entities_by_comp: pd.core.groupby.DataFrameGroupBy,
    ) -> pd.DataFrame:

        components = self.build_components_dataframe(entities_by_comp)
        components = self.parse_fields(components)

        return components

    def build_components_dataframe(
        self, entities_by_comp: pd.core.groupby.DataFrameGroupBy
    ) -> pd.DataFrame:
        group_key = "component"

        # Get the entities with the components flag
        components = entities_by_comp.get_group(group_key)
        components = components[["entity", "comp_ind"]]

        # Get the entities with the data component
        data = entities_by_comp.get_group("data")
        data = data.rename(
            columns={"comp_ind": "data_comp_ind", "component": "data"}
        ).drop(columns=["component_entity"])

        # Join the components with the data component
        components = components.set_index("entity").join(
            data.set_index("entity"), how="outer"
        )

        # Identify the components that are defined vs implicitly included
        components["defined"] = True
        comps_created = pd.DataFrame({"entity": entities_by_comp.groups.keys()})
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
                        field = Field.from_kv_pair(field_key, field_value)
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
        entities_by_comp: pd.core.groupby.DataFrameGroupBy,
    ) -> pd.DataFrame:

        # Pass the entities to the general parse function first
        links = self.general_parsecomp("links", entities_by_comp)

        # Now parse the edges, etc.
        return links