from dataclasses import dataclass
import glob

import numpy as np
import pandas as pd
import yaml
import re


class Entity(str):
    """Subclass of str to represent entities."""


@dataclass
class Field:
    name: str
    type: str
    description: str = ""
    multiplicity: str = "0..*"

    field_def_order = ["type", "multiplicity"]

    @classmethod
    def from_kv_pair(cls, field_key: str, field_value: str | dict[str, str]) -> "Field":

        # Parse the overall field definition
        # The awful regex expression is to match the field name and balance brackets
        # It was spat out by copilot, but it works...
        pattern = r"(?P<name>\w+)\s*\[(?P<bracket>[^\[\]]*(?:\[[^\[\]]*\][^\[\]]*)*)]"
        match = re.match(pattern, field_key)

        # Check results
        if match is None:
            raise ValueError(f"field key {field_key} is not formatted correctly.")
        field_name = match.group("name")
        if field_name is None:
            raise ValueError(f"field key {field_key} is not formatted correctly.")
        bracket_contents = match.group("bracket")

        # Convert into keyword arguments
        kwargs = {"name": field_name}
        for i, field_attr_value in enumerate(bracket_contents.split("|")):
            field_attr = cls.field_def_order[i]
            kwargs[field_attr] = field_attr_value

        if isinstance(field_value, str):
            kwargs["description"] = field_value
        elif isinstance(field_value, dict):
            kwargs.update(field_value)
        elif field_value is None:
            pass
        else:
            raise ValueError(f"field key {field_key} is not formatted correctly.")

        return cls(**kwargs)


class Parser:

    ignored_components = []

    def __init__(self, input_dir: str):
        self.input_dir = input_dir

    def extract(self) -> pd.DataFrame:

        self.entities = []
        for filename in glob.glob(f"{self.input_dir}/*.yaml"):
            with open(filename, "r", encoding="utf-8") as file:
                file_entities = yaml.safe_load(file)

                for entity, comps in file_entities.items():

                    # Check if the entity already exists
                    if entity in self.entities:
                        raise KeyError(f"Entity {entity} is defined in multiple files.")

                    # Get a list containing each component
                    entity_comps = self.extract_entity(entity, comps)

                    # Add a component indicating the file the entity was found in
                    entity_comps.append(
                        {
                            "entity": entity,
                            "comp_ind": len(entity_comps),
                            "component_entity": "source_file",
                            "component": filename,
                        }
                    )

                    self.entities += entity_comps

        # Convert to a DataFrame
        self.entities = pd.DataFrame(self.entities)

        return self.entities

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

    def get_cleaned_component_group(
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
            group = group.drop(columns=["component"])
            group = group.join(comp_data)

        return group

    def transform(self) -> dict[str, pd.DataFrame]:

        entities_by_comp = self.entities.groupby("component_entity")

        self.comps = {}
        for group_key in entities_by_comp.groups.keys():

            # Look for the function to parse the entity
            parse_fn = f"parse_component_{group_key}"
            if hasattr(self, parse_fn):
                self.comps[group_key] = getattr(self, parse_fn)(entities_by_comp)
            # If the component is ignored, skip it
            elif group_key in self.ignored_components:
                continue
            # Default to the cleaned version
            else:
                self.comps[group_key] = self.get_cleaned_component_group(
                    group_key, entities_by_comp
                )

        return self.comps

    def validate(self):

        # Get the component table for easy access
        comps = self.comps["component"].copy()

        self.comps["component"] = comps

        return comps

    # These components are handled as part of the component component
    ignored_components += [
        "data",
    ]

    def parse_component_component(
        self,
        entities_by_comp: pd.core.groupby.DataFrameGroupBy,
    ) -> pd.DataFrame:

        components = self.build_components_dataframe(entities_by_comp)
        components = self.validate_components(components)

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

        return components

    def validate_components(self, components: pd.DataFrame) -> pd.DataFrame:

        # Identify the components that are defined vs implicitly included
        components["defined"] = True
        comps_created = pd.DataFrame({"entity": self.comps.keys()})
        components = components.merge(comps_created, how="outer", on="entity")
        components.loc[components["defined"].isna(), "defined"] = False

        # Make a copy of the data column so we can refer to the unparsed data as well
        components["unparsed_data"] = components["data"]

        valids = []
        valid_messages = []
        fields = []
        for i, comp in components.query("defined").iterrows():
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
