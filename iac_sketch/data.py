import copy
import re
from dataclasses import dataclass

import pandas as pd
import pandera.pandas as pa
from pandera.engines import pandas_engine


# --- Registry class ---


class Entity(str):
    """Subclass of str to represent entities."""


class Field(pa.Column):
    """
    Field extends pandera's Column to represent a DataFrame column with additional metadata.

    Parameters
    ----------
    dtype : str, type, DataType, Type, ExtensionDtype, or numpy.dtype, optional
        Datatype of the column for type-checking.
    checks : Check, List[Check | Hypothesis], or None, optional
        Checks to verify validity of the column.
    parsers : Parser, List[Parser], or None, optional
        Parsers to preprocess or validate the column.
    nullable : bool, default False
        Whether the column can contain null values.
    unique : bool, default False
        Whether column values should be unique.
    report_duplicates : {'exclude_first', 'exclude_last', 'all'}, default 'all'
        How to report unique errors.
    coerce : bool, default False
        If True, coerce the column to the specified dtype during validation.
    required : bool, default True
        Whether the column must be present in the DataFrame.
    name : str, tuple of str, or None, optional
        Name of the column in the DataFrame.
    regex : bool, default False
        Whether the name should be treated as a regex pattern.
    title : str, optional
        Human-readable label for the column.
    description : str, optional
        Textual description of the column.
    default : Any, optional
        Default value for missing values in the column.
    metadata : dict, optional
        Optional key-value metadata for the column.
    drop_invalid_rows : bool, default False
        If True, drop invalid rows during validation.
    multiplicity : str, default "0..*"
        Custom field for additional multiplicity metadata.
    *args, **kwargs :
        Additional positional and keyword arguments passed to pa.Column.
    """
    field_def_order = [
        "dtype", "multiplicity",
    ]
    def __init__(
        self,
        *args,
        dtype=None,
        checks=None,
        parsers=None,
        nullable=False,
        unique=False,
        report_duplicates="all",
        coerce=False,
        required=True,
        name=None,
        regex=False,
        title=None,
        description=None,
        default=None,
        metadata=None,
        drop_invalid_rows=False,
        multiplicity: str = "0..*",
        **kwargs,
    ):

        # Try to parse the dtype as a known dtype, and if not set it to None.
        # This is likely to change if we want to do something with entity data types.
        self.dtype_str = dtype
        try:
            dtype = pandas_engine.Engine.dtype(dtype)
        except TypeError:
            dtype = None

        super().__init__(
            *args,
            dtype=dtype,
            checks=checks,
            parsers=parsers,
            nullable=nullable,
            unique=unique,
            report_duplicates=report_duplicates,
            coerce=coerce,
            required=required,
            name=name,
            regex=regex,
            title=title,
            description=description,
            default=default,
            metadata=metadata,
            drop_invalid_rows=drop_invalid_rows,
            **kwargs,
        )
        self.multiplicity = multiplicity

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
class View:
    """Encapsulates the specification for a registry view."""

    components: str | list[str]
    join_on: str = None
    join_how: str = "left"


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

    def resolve_view(
        self,
        view: View,
    ) -> pd.DataFrame:
        """Get a component or view of components, using a View instance only."""

        if isinstance(view.components, str):
            return self[view.components]
        if isinstance(view.components, list):
            for i, key in enumerate(view.components):
                df_i = self[key]
                if i == 0:
                    view_df = df_i
                    continue
                if view.join_on is None:
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
                        how=view.join_how,
                        rsuffix=f".{key}",
                        on="entity",
                    )
                else:
                    view_df = view_df.merge(
                        df_i,
                        how=view.join_how,
                        left_on=view.join_on,
                        right_on=view.join_on,
                        suffixes=("", f".{key}"),
                    )
            return view_df
        raise TypeError("View.keys must be a string or a list of strings.")

    def view(self, *args, **kwargs) -> pd.DataFrame:
        """Get a component or view of components. Accepts arguments to
        construct a View, then delegates to resolve_view."""
        view = View(*args, **kwargs)
        return self.resolve_view(view)

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
