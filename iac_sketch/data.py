import copy
import re
from dataclasses import dataclass
from typing import Optional, Any, Type

import pandas as pd
import pandera.pandas as pa
from pandera.backends.pandas.components import ColumnBackend
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
        "dtype",
        "multiplicity",
    ]

    def __init__(
        self,
        *args,
        dtype=None,
        checks=None,
        parsers=None,
        nullable=True,
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
        categories: list[str] = None,
        **kwargs,
    ):

        # Try to parse the dtype as a known dtype, and if not set it to None.
        # This is likely to change if we want to do something with entity data types.
        self.dtype_str = dtype
        try:
            dtype = pandas_engine.Engine.dtype(dtype)
        except TypeError:
            dtype = None

        # Override the dtype if provided categories
        if categories is not None:
            dtype = pd.CategoricalDtype(categories=categories)

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
    def get_backend(
        cls, check_obj: Optional[Any] = None, check_type: Optional[Type] = None
    ):
        """Override to use pandas backend for Field instances."""
        return ColumnBackend()

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


class Registry:
    """
    Entity-Component-System registry implementation using pandas DataFrames.

    The Registry manages a collection of component DataFrames, where each DataFrame
    represents components of a specific type. Each entity can have multiple components
    associated with it, and each component is uniquely identified by an entity and
    component index (comp_ind) pair.

    Two special components are supported:
    - 'compinsts': Master index tracking all components across all DataFrames
    - 'compdefs': Contains definitions per component type

    Parameters
    ----------
    components : dict[str, pd.DataFrame]
        Dictionary mapping component type names to their respective DataFrames.
        Each DataFrame should be indexed by ('entity', 'comp_ind') multi-index.

    Attributes
    ----------
    components : dict[str, pd.DataFrame]
        Dictionary storing all component DataFrames by type name.
    """

    def __init__(self, components: dict[str, pd.DataFrame] = None):
        self.components = {}
        if components:
            for key, value in components.items():
                self.set(key, value)

    def __getitem__(self, key: str):
        """
        Retrieve a component DataFrame by its type name.

        Parameters
        ----------
        key : str
            The component type name to retrieve.

        Returns
        -------
        pd.DataFrame
            The DataFrame containing components of the specified type.
        """

        if key not in self.components:
            raise KeyError(f"Component '{key}' not found in registry.")

        return self.components[key]

    def __setitem__(self, key: str, value: pd.DataFrame):
        """
        Set a component DataFrame using dictionary-style assignment.

        This method delegates to the `set` method with 'overwrite' mode.

        Parameters
        ----------
        key : str
            The component type name.
        value : pd.DataFrame
            The DataFrame to store for this component type.
        """
        self.set(key, value, mode="overwrite")

    def __contains__(self, key: str) -> bool:
        """
        Check if a component type exists in the registry.

        Parameters
        ----------
        key : str
            The component type name to check.

        Returns
        -------
        bool
            True if the component type exists, False otherwise.
        """
        return key in self.components

    def keys(self):
        """
        Return the component type names in the registry.

        Returns
        -------
        dict_keys
            A view of the component type names.
        """
        return self.components.keys()

    def items(self):
        """
        Return key-value pairs of component types and their DataFrames.

        Returns
        -------
        dict_items
            A view of (component_type, DataFrame) pairs.
        """
        return self.components.items()

    def update(self, other: "Registry", mode: str = "upsert"):
        """
        Update this registry with components from another registry.

        Parameters
        ----------
        other : Registry
            Another Registry instance to update from.
        mode : str, default 'upsert'
            The update mode to use. Can be 'upsert' or 'overwrite'.
            - 'upsert': Merge new data with existing, keeping latest duplicates
            - 'overwrite': Replace existing component DataFrames entirely
        """

        for key, comp_df in other.items():
            self.set(key, comp_df, mode)

    def set(self, key: str, value: pd.DataFrame, mode: str = "upsert"):
        """
        Validate the index of a component DataFrame and update compinsts.

        The 'compinsts' component serves as a master index tracking all components
        across all DataFrames and their relationship to entities.

        Parameters
        ----------
        key : str
            The component type name being updated.
        comp_df : pd.DataFrame
            The component DataFrame with 'entity' and 'comp_ind' columns.
        mode : str, default 'upsert'
            The update mode:
            - 'upsert': Merge with existing compinsts, keeping latest duplicates
            - 'overwrite': Remove existing entries for this component type,
              then add new ones

        Notes
        -----
        The method assumes comp_df has 'entity' and 'comp_ind' columns and creates
        new rows in compinsts with these values plus the component_type.
        """

        if mode not in ["upsert", "overwrite"]:
            raise ValueError(f"Invalid mode '{mode}'. Use 'overwrite' or 'upsert'.")

        # We'll be messing with the indices, so we reset them for now
        value = self.reset_index(value)

        # Incorporate the existing component if mode is 'upsert'
        if mode == "upsert" and key in self.components:
            existing = self.reset_index(self[key])
            value = pd.concat(
                [existing, value],
            )

        # Sync component indices with compinsts
        value = self.sync_comp_inds(key, value, mode)

        # Add indices
        value = self.set_index(key, value)

        # Store
        self.components[key] = value

    def sync_comp_inds(
        self, key: str, value: pd.DataFrame, mode: str = "upsert"
    ) -> pd.DataFrame:

        # Just in case, we reset the index of value
        # This should already be done in set, but if we're using this method
        # independently, we want to ensure the index is reset.
        value = self.reset_index(value)

        # Skip if compinst is not created yet
        if "compinst" not in self.components:
            return value

        # Get compinst, with fresh indices so we can modify them
        compinst = self.reset_index(self["compinst"])

        # Prepare new rows from comp_df for compinst
        # Store the original index to map back to comp_df later
        new_rows = value[["entity", "comp_ind"]].copy()
        new_rows["component_type"] = key
        new_rows["original_index"] = value.index  # Track original comp_df row indices

        # If mode is 'overwrite', remove existing entries for this component type
        if mode == "overwrite":
            compinst = compinst[~(compinst["component_type"] == key)]

        # Concatenate new rows to compinst
        compinst = pd.concat([compinst, new_rows])

        # Replace nan comp_inds with a monotonic index, starting from the largest
        # existing comp_ind value for a given entity
        if compinst["comp_ind"].isna().any():

            # Group by entity to handle each entity separately
            def fill_comp_ind(group):
                # Find rows with NaN comp_ind
                nan_mask = group["comp_ind"].isna()
                if nan_mask.any():
                    # Get the maximum existing comp_ind for this entity
                    max_comp_ind = group["comp_ind"].dropna().max()
                    # If no existing comp_ind, start from 0
                    if pd.isna(max_comp_ind):
                        max_comp_ind = -1
                    # Fill NaN values with monotonic sequence starting from max + 1
                    nan_count = nan_mask.sum()
                    new_indices = range(
                        int(max_comp_ind) + 1, int(max_comp_ind) + 1 + nan_count
                    )
                    group.loc[nan_mask, "comp_ind"] = new_indices
                return group

            compinst = compinst.groupby("entity", group_keys=False).apply(fill_comp_ind)

            # Propagate filled comp_ind values back to comp_df
            # Filter for rows that were just added (those with original_index values)
            new_rows_mask = compinst["original_index"].notna()
            new_rows = compinst[new_rows_mask].copy()
            # Update comp_df using vectorized assignment
            value.loc[new_rows["original_index"], "comp_ind"] = new_rows["comp_ind"]

        # Clean up: drop duplicates, indices, and ensure comp_ind is of type int
        # There's probably a better way to do this than calling drop_duplicates twice
        value = value.drop_duplicates(
            subset=["entity", "comp_ind"],
            keep="last",
        ).reset_index(drop=True)
        value["comp_ind"] = value["comp_ind"].astype(int)
        compinst = compinst.drop_duplicates(
            subset=["entity", "comp_ind"],
            keep="last",
        ).reset_index(drop=True)
        compinst["comp_ind"] = compinst["comp_ind"].astype(int)

        # Return compinst to the original format and set it
        compinst = compinst.set_index(["entity", "comp_ind"])
        compinst = compinst[["component_type"]]
        compinst = compinst.sort_index()
        self.components["compinst"] = compinst

        # Indices for value are handled later
        return value

    def reset_index(self, value: pd.DataFrame) -> pd.DataFrame:
        """We have a special reset_index method because we want to drop the index only
        when it's not set to 'entity' or ['entity', 'comp_ind'].

        Parameters
        ----------
        value : pd.DataFrame
            The DataFrame to reset the index for.

        Returns
        -------
        pd.DataFrame
            The DataFrame with the index reset.
        """

        drop = (
            list(value.index.names) != ["entity", "comp_ind"]
        ) and value.index.name != "entity"
        return value.reset_index(drop=drop)

    def set_index(self, key: str, value: pd.DataFrame):

        # Check component multiplicity to determine indexing strategy
        try:
            multiplicity_str = self.components["compdef"].loc[key, "multiplicity"]
            # Parse multiplicity string (format: "min..max")
            _, upper_bound = multiplicity_str.split("..", 1)
        except (KeyError, ValueError):
            # If compdef doesn't exist, key not found, or parsing fails,
            # default to multi-index behavior
            upper_bound = "*"

        # Ensure the DataFrame has the proper indexing
        if upper_bound == "1":
            # For components with multiplicity upper bound of 1, index by entity only
            value = value.set_index("entity")
        else:
            # For components with multiplicity > 1, use multi-index (entity, comp_ind)
            value = value.set_index(["entity", "comp_ind"])

        return value.sort_index()

    def copy(self):
        """
        Create a deep copy of the registry.

        Returns
        -------
        Registry
            A deep copy of this Registry instance, including all component
            DataFrames.
        """
        return copy.deepcopy(self)

    def resolve_view(
        self,
        view: View,
    ) -> pd.DataFrame:
        """
        Resolve a View specification into a concrete DataFrame.

        This method takes a View instance and creates a DataFrame by either
        retrieving a single component or joining multiple components together.

        Parameters
        ----------
        view : View
            A View instance specifying which components to include and how
            to join them.

        Returns
        -------
        pd.DataFrame
            The resulting DataFrame containing the requested view of components.
            The DataFrame's attrs will contain 'view_components' indicating
            which components were used to create the view.

        Notes
        -----
        When joining multiple components:
        - If join_on is None, components must be indexed by 'entity' or
          ['entity', 'comp_ind']
        - If join_on is specified, components are merged on that column
        - Column name conflicts are resolved with suffixes
        """

        if isinstance(view.components, str):
            view_df = self[view.components].copy()
        elif isinstance(view.components, list):
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
                        rsuffix=f"_{key}",
                        on="entity",
                    )
                else:
                    view_df = view_df.merge(
                        df_i,
                        how=view.join_how,
                        left_on=view.join_on,
                        right_on=view.join_on,
                        suffixes=("", f"_{key}"),
                    )
        else:
            raise TypeError("View.keys must be a string or a list of strings.")

        # Store the view components in the DataFrame attributes
        view_df.attrs["view_components"] = view.components
        return view_df

    def view(self, *args, **kwargs) -> pd.DataFrame:
        """
        Get a component or view of components.

        This is a convenience method that creates a View instance from the
        provided arguments and then delegates to resolve_view.

        Parameters
        ----------
        *args : tuple
            Positional arguments passed to View constructor.
        **kwargs : dict
            Keyword arguments passed to View constructor.

        Returns
        -------
        pd.DataFrame
            The resulting DataFrame containing the requested view of components.
        """
        view = View(*args, **kwargs)
        return self.resolve_view(view)
