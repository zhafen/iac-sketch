from dataclasses import dataclass
import re

import pandas as pd


class Entity(str):
    """Subclass of str to represent entities."""


@dataclass
class Field:
    name: str
    type: str
    description: str = ""
    multiplicity: str = "0..*"
    default: str = ""

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

@dataclass
class Registry:
    entities: pd.DataFrame
    components: dict[str, pd.DataFrame]
