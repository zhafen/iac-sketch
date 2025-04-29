import glob

import numpy as np
import pandas as pd
import yaml
import re


class Entity(str):
    """Subclass of str to represent entities."""

    pass


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

                    self.entities += self.extract_entity(entity, comps)

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

        self.components = {}
        for group_key in entities_by_comp.groups.keys():

            # Look for the function to parse the entity
            parse_fn = f"parse_component_{group_key}"
            if hasattr(self, parse_fn):
                self.components[group_key] = getattr(self, parse_fn)(entities_by_comp)
            # If the component is ignored, skip it
            elif group_key in self.ignored_components:
                continue
            # Default to the cleaned version
            else:
                self.components[group_key] = self.get_cleaned_component_group(
                    group_key, entities_by_comp
                )

        return self.components

    def validate(self):

        # Get the component table for easy access
        comps = self.components["component"].copy()

        self.components["component"] = comps

        return comps

    # These components are handled as part of the component component
    ignored_components += ["data", "value"]

    def parse_component_component(
        self,
        entities_by_comp: pd.core.groupby.DataFrameGroupBy,
    ) -> pd.DataFrame:

        components = self.build_components_dataframe(entities_by_comp)
        components = self.validate_components(components)

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

        # Get the entities with the value component
        values = entities_by_comp.get_group("value")
        values = values.rename(
            columns={"comp_ind": "value_comp_ind", "component": "value_type"}
        ).drop(columns=["component_entity"])

        # Join the components with the data and value components
        components = components.set_index("entity").join(
            [data.set_index("entity"), values.set_index("entity")], how="outer"
        )

        return components

    def validate_components(self, components: pd.DataFrame) -> pd.DataFrame:

        # Identify the components that are defined vs implicitly included
        components["defined"] = True
        comps_created = pd.DataFrame({"entity": self.components.keys()})
        components = components.merge(comps_created, how="outer", on="entity")
        components.loc[components["defined"].isna(), "defined"] = False

        valid = []
        valid_message = []
        for i, comp in components.query("defined").iterrows():

            comp_key = comp["entity"]
            comp_not_na = comp.notna()

            # When there's a value, we check it's valid
            if comp_not_na["value_type"]:

                # Check if we only have one or the other
                if comp_not_na["data"]:
                    valid.append(False)
                    valid_message.append("has both a value_type and data")
                    continue

                # If we have a value type we turn the data into that
                try:
                    # Among the components, the column with the name of the component
                    # is where values are stored if the component is a single value
                    self.components[comp_key][comp_key] = self.components[comp_key][
                        comp_key
                    ].astype(comp["value_type"])
                except (TypeError, KeyError):
                    valid.append(False)
                    valid_message.append(
                        f"cannot convert {comp_key} to {comp['value_type']}"
                    )
                    continue

            if comp_not_na["data"]:

                for field_key, field_descr in comp["data"].items():
                    assert False

            # If we got this far the component is valid
            valid.append(False)
            valid_message.append("validate function incomplete")

        # Defaults
        components["valid"] = False
        components["valid_message"] = "undefined"
        # Then override
        components.loc[components["defined"], "valid"] = valid
        components.loc[components["defined"], "valid_message"] = valid_message

        return components

    def parse_field_definition(
        self, field_key: str, field_value: str | dict[str, str]
    ) -> dict[str, str]:


        # Regex to parse the field definition
        pattern = (
            r"(?P<name>\w+)\s*"
            + r"\[(?P<type>\w+)?"
            + r"(?:\|(?P<multiplicity>[01\*]\.\.[01\*]))?\]"
        )

        match = re.match(pattern, field_key)

        # Parse the multiplicity
        field_multiplicity = match.group("multiplicity")
        if field_multiplicity is None:
            # Default multiplicity
            field_multiplicity = "1..*"

        # Set up the field definition
        field_definition = {
            "field": match.group("name"),
            "type": match.group("type"),
            "multiplicity": field_multiplicity,
        }

        if isinstance(field_value, str):
            field_definition["description"] = field_value
        elif isinstance(field_value, dict):
            field_definition.update(field_value)
        else:
            raise TypeError(
                f"Field value must be a string or a dictionary, got {type(field_value)}"
            )

        return field_definition
