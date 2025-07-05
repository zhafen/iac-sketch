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
        "dtype", "multiplicity",
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
    def get_backend(cls, check_obj: Optional[Any] = None, check_type: Optional[Type] = None):
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


@dataclass(repr=False)
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
    
    Examples
    --------
    >>> import pandas as pd
    >>> registry = Registry(components={})
    >>> df = pd.DataFrame({'entity': ['A', 'B'], 'comp_ind': [0, 0], 'value': [1, 2]})
    >>> registry['positions'] = df
    """
    components: dict[str, pd.DataFrame]

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
        
        Raises
        ------
        KeyError
            If the component type is not found in the registry.
        
        Examples
        --------
        >>> positions_df = registry['positions']
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
        
        Examples
        --------
        >>> registry['positions'] = positions_df
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
        
        Examples
        --------
        >>> 'positions' in registry
        True
        """
        return key in self.components

    def keys(self):
        """
        Return the component type names in the registry.
        
        Returns
        -------
        dict_keys
            A view of the component type names.
        
        Examples
        --------
        >>> list(registry.keys())
        ['positions', 'velocities', 'compinsts']
        """
        return self.components.keys()

    def items(self):
        """
        Return key-value pairs of component types and their DataFrames.
        
        Returns
        -------
        dict_items
            A view of (component_type, DataFrame) pairs.
        
        Examples
        --------
        >>> for comp_type, df in registry.items():
        ...     print(f"{comp_type}: {len(df)} components")
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
        
        Examples
        --------
        >>> registry1.update(registry2, mode='upsert')
        """

        for key, comp_df in other.items():
            self.set(key, comp_df, mode)

    def set(self, key: str, value: pd.DataFrame, mode: str = "upsert"):
        """
        Update or add a component DataFrame to the registry.
        
        Parameters
        ----------
        key : str
            The component type name.
        value : pd.DataFrame
            The DataFrame containing components of this type. Must contain
            'entity' and 'comp_ind' columns for proper indexing.
        mode : str, default 'upsert'
            The update mode to use:
            - 'upsert': Merge with existing data, keeping latest duplicates
            - 'overwrite': Replace existing DataFrame entirely
        
        Raises
        ------
        TypeError
            If value is not a pandas DataFrame.
        ValueError
            If mode is not 'upsert' or 'overwrite'.
        
        Notes
        -----
        If 'compinsts' component exists in the registry, it will be automatically
        updated to reflect the new or modified components.
        
        Examples
        --------
        >>> registry.set('positions', positions_df, mode='upsert')
        """
        if not isinstance(value, pd.DataFrame):
            raise TypeError("Value must be a pandas DataFrame.")

        if key not in self.components:
            self.components[key] = value
        else:
            if mode == "overwrite":
                self.components[key] = value
            elif mode == "upsert":
                self.components[key] = pd.concat(
                    [self.components[key], value]
                ).drop_duplicates(subset=["entity", "comp_ind"], keep="last")
            else:
                raise ValueError(
                    f"Invalid mode '{mode}'. Use 'overwrite' or 'upsert'."
                )

        if "compinst" in self.components:
            self.update_compinsts(key, value, mode=mode)

    def update_compinsts(self, key: str, comp_df: pd.DataFrame, mode: str = "upsert"):
        """
        Update the component instances master index.
        
        This method maintains the 'compinsts' component, which serves as a master
        index tracking all components across all DataFrames and their relationship
        to entities.
        
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
        
        Raises
        ------
        ValueError
            If mode is not 'upsert' or 'overwrite'.
        
        Notes
        -----
        The method assumes comp_df has 'entity' and 'comp_ind' columns and creates
        new rows in compinsts with these values plus the component_type.
        
        Examples
        --------
        >>> registry.update_compinsts('positions', positions_df, mode='upsert')
        """
        compinst = self["compinst"].copy()

        # Prepare new rows from comp_df for compinst
        # Assume comp_df has columns 'entity' and 'comp_ind'
        new_rows = comp_df[["entity", "comp_ind"]].copy()
        new_rows["component_type"] = key
        new_rows = new_rows.set_index(["entity", "comp_ind"], drop=False)

        # Update compinst based on the mode
        if mode == "overwrite":
            compinst = compinst[~(compinst["component_type"] == key)]
            compinst = pd.concat([compinst, new_rows])
        elif mode == "upsert":
            compinst = pd.concat([compinst, new_rows])
            compinst = compinst[~compinst.index.duplicated(keep="last")]
        else:
            raise ValueError(
                f"Invalid mode '{mode}'. Use 'overwrite' or 'upsert'."
            )

        # TODO: Check if comp_df has duplicate non-nan comp_inds
        # TODO: We also need to check on the indices of comp_df and update them.

        # Store
        self.components["compinst"] = compinst

    def copy(self):
        """
        Create a deep copy of the registry.
        
        Returns
        -------
        Registry
            A deep copy of this Registry instance, including all component
            DataFrames.
        
        Examples
        --------
        >>> registry_copy = registry.copy()
        >>> registry_copy is registry
        False
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
        
        Raises
        ------
        TypeError
            If view.components is not a string or list of strings.
        ValueError
            If joining components that are not properly indexed and no join_on
            is specified.
        
        Notes
        -----
        When joining multiple components:
        - If join_on is None, components must be indexed by 'entity' or 
          ['entity', 'comp_ind']
        - If join_on is specified, components are merged on that column
        - Column name conflicts are resolved with suffixes
        
        Examples
        --------
        >>> view = View(components=['positions', 'velocities'])
        >>> combined_df = registry.resolve_view(view)
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
        
        Examples
        --------
        >>> # Get a single component
        >>> positions = registry.view('positions')
        
        >>> # Join multiple components
        >>> combined = registry.view(['positions', 'velocities'], join_how='inner')
        
        >>> # Join on specific column
        >>> result = registry.view(['comp1', 'comp2'], join_on='custom_id')
        """
        view = View(*args, **kwargs)
        return self.resolve_view(view)
