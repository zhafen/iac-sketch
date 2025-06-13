

import copy
import re
from dataclasses import dataclass
from typing import Optional, Union
import pandas as pd



# --- Registry class ---


class Entity(str):
    """Subclass of str to represent entities."""


@dataclass
class Field:
    name: str
    type: str
    description: str = ""
    multiplicity: str = "0..*"
    default: str = ""
    categories: list[str] = None

    field_def_order = ["type", "multiplicity"]

    @classmethod
    def from_kv_pair(cls, field_key: str, field_value: str | dict[str, str]) -> "Field":

        # Parse the overall field definition
        # The awful regex expression is to match the field name and balance brackets
        # It was spat out by copilot, but it works...
        pattern = (
            r"(?P<name>\w+)\s*"
            + r"\[(?P<bracket>[^\[\]]*(?:\[[^\[\]]*\][^\[\]]*)*)]"
            + r"(?:\s*=\s*(?P<default>.+))?"
        )
        match = re.match(pattern, field_key)

        # Check results
        if match is None:
            raise ValueError(f"field key {field_key} is not formatted correctly.")
        field_name = match.group("name")
        if field_name is None:
            raise ValueError(f"field key {field_key} is not formatted correctly.")
        bracket_contents = match.group("bracket")

        # Convert into keyword arguments
        kwargs = {
            "name": field_name,
            "default": match.group("default"),
        }
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


class View:
    """Encapsulates the specification for a registry view."""
    def __init__(
        self,
        keys: Union[str, list[str]],
        join_on: Optional[str] = None,
        join_how: str = "left",
    ):
        self.keys = keys
        self.join_on = join_on
        self.join_how = join_how

    def __repr__(self):
        return (
            f"View(keys={self.keys!r}, join_on={self.join_on!r}, join_how={self.join_how!r})"
        )

@dataclass(repr=False)
class Registry:
    components: dict[str, pd.DataFrame]

    def __getitem__(self, key: str):

        if key not in self.components:
            raise KeyError(f"Component '{key}' not found in registry.")

        return self.components[key]

    def __setitem__(self, key: str, value: pd.DataFrame):
        if not isinstance(value, pd.DataFrame):
            raise TypeError("Value must be a pandas DataFrame.")
        self.components[key] = value

    def __contains__(self, key: str) -> bool:
        return key in self.components

    def keys(self):
        return self.components.keys()

    def items(self):
        return self.components.items()

    def update(self, other: "Registry"):

        for comp_key, comp_df in other.items():
            if comp_key not in self.components:
                self.components[comp_key] = comp_df
            else:
                self.components[comp_key] = pd.concat(
                    [self.components[comp_key], comp_df]
                )

    def copy(self):
        return copy.deepcopy(self)


    def view(
        self,
        view: Union[View, str, list[str]],
        join_on: Optional[str] = None,
        join_how: str = "left",
    ) -> pd.DataFrame:
        """Get a component or view of components. Accepts a View instance or legacy arguments."""
        # If a View instance is provided, use its attributes
        if isinstance(view, View):
            keys = view.keys
            join_on = view.join_on
            join_how = view.join_how
        else:
            keys = view
        # Legacy behavior for string or list
        if isinstance(keys, str):
            return self[keys]
        if isinstance(keys, list):
            for i, key in enumerate(keys):
                df_i = self[key]
                if i == 0:
                    view_df = df_i
                    continue
                if join_on is None:
                    # If join_on is not specified we join on the entity
                    if df_i.index.name != "entity" and df_i.index.name != [
                        "entity",
                        "comp_ind",
                    ]:
                        raise ValueError(
                            f"Component {key} is not indexed by 'entity' or "
                            "['entity', 'comp_ind']. Must provide join_on."
                        )
                    view_df = view_df.join(
                        df_i,
                        how=join_how,
                        rsuffix=f".{key}",
                        on="entity",
                    )
                else:
                    view_df = view_df.merge(
                        df_i,
                        how=join_how,
                        left_on=join_on,
                        right_on=join_on,
                        suffixes=("", f".{key}"),
                    )
            return view_df
        # If we got here, keys is not a string or a list of strings
        raise TypeError("view must be a View, string, or list of strings.")

    def validate(self):
        """Validate the data in the registry. This only validates that the data
        is correctly consistent with the component definition. It does not perform the
        level of checks that Validator does."""

        for comp_key in self.keys():

            self.validate_component(comp_key)

    def validate_component(self, comp_key: str) -> tuple[pd.Series, pd.DataFrame]:
        """Validate the component table. This only validates that the data
        is correctly consistent with the component definition. It does not perform the
        level of checks that Validator does."""

        comp_df = self[comp_key].copy()

        # Get the settings according to the component definition,
        # stored in the component row
        comp_def: pd.Series = self["component"].loc[comp_key].copy()

        # After this we check for matching with component definition, so if
        # the component definition is not valid then the component table is not valid
        if not comp_def["valid_def"]:
            comp_def["valid_data"] = False
            comp_def["valid_data_message"] = "Invalid component definition."
            return comp_def, comp_df

        # Validate fields
        for field_name, field_obj in comp_def["fields"].items():
            if field_name not in comp_df.columns:
                comp_df[field_name] = field_obj.default

        # If the index is not set, we check the multiplicity and set the index
        if comp_df.index.name != "entity":
            if comp_def["multiplicity"] == "1":
                comp_df = comp_df.set_index("entity")

                # Check for duplicates
                if comp_df.index.has_duplicates:
                    comp_def["valid_data"] = False
                    comp_def["valid_data_message"] = (
                        "Multiplicity is 1, but there are duplicates: "
                        f"{list(comp_df.index[comp_df.index.duplicated()].values)}"
                    )
                    return comp_def, comp_df
            else:
                comp_df = comp_df.set_index(["entity", "comp_ind"])

        # If we got this far, the component table is valid
        comp_def["valid_data"] = True
        comp_def["valid_data_message"] = ""

        # Store changes to the registry
        self["component"].loc[comp_key] = comp_def
        self[comp_key] = comp_df

        return comp_def, comp_df
