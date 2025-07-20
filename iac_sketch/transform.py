import networkx as nx
import pandas as pd
import pandera.pandas as pa
from sklearn.base import BaseEstimator, TransformerMixin
from . import data


# Custom transformer for adding error and validity metadata columns
class LogPrepper(BaseEstimator, TransformerMixin):
    """
    Transformer that adds two columns to a DataFrame:
    - 'errors': for tracking errors on a per-row basis (default: empty string)
    - 'valid': for indicating if a row is valid (default: True)
    """

    def fit(self, _X, _y=None):
        # Stateless transformer, nothing to fit
        return self

    def transform(
        self, X: pd.DataFrame, _registry: data.Registry = None
    ) -> pd.DataFrame:
        X = X.copy()
        if "errors" not in X.columns:
            X["errors"] = ""
        if "is_valid" not in X.columns:
            X["is_valid"] = True
        return X


class ComponentNormalizer(BaseEstimator, TransformerMixin):

    def fit(self, _X, _y=None):
        return self

    def transform(self, X, registry: data.Registry = None):

        # This transform operates on unindexed DataFrames.
        # They'll be reindexed when they're returned to the registry.
        X = registry.reset_index(X)

        # Start by unpacking the 'component' column
        comp_data = pd.json_normalize(X["component"])

        # If there was nothing to unpack, we just use the values in the column
        if len(comp_data.columns) == 0:
            # If there are any non-null values we rename the column to 'value'
            if X["component"].isna().any():
                X = X.rename(columns={"component": "value"})
            # Otherwise, we just drop the column
            else:
                X = X.drop(columns=["component"])

        # If there was something to unpack, we need to handle it
        else:
            # Find rows that were not parsed
            not_parsed = comp_data.isna().all(axis="columns")
            # If we both have unparsed rows and non-null values in the same rows,
            # we add them to a value column
            if not_parsed.any() and X.loc[not_parsed, "component"].notna().any():
                # Ensure there's a value column to hold unparsed components
                if "value" not in comp_data.columns:
                    comp_data["value"] = pd.NA

                # Move unparsed components to the 'value' column
                comp_data.loc[not_parsed, "value"] = X.loc[not_parsed, "component"]

            # With everything unpacked, we can drop the original 'component' column
            # and join the new columns
            X = X.drop(columns=["component"])
            X = X.join(comp_data)

        return X


# Transformer to extract and validate component definitions (bottom of file)
class ComponentDefExtractor(BaseEstimator, TransformerMixin):

    def fit(self, _X, _y=None, registry: data.Registry = None):
        self.registry = registry
        return self

    def transform(self, X, registry: data.Registry = None):

        X = X.copy()

        # Add in all components defined in the registry
        # and mark the ones that are not defined
        X["is_defined"] = True
        registry_comps = pd.DataFrame({"entity": registry.keys()})
        X = X.merge(registry_comps, how="outer", on="entity")
        X.loc[X["is_defined"].isna(), "is_defined"] = False
        X["is_defined"] = X["is_defined"].astype(bool)

        # Parse the fields
        X = X.apply(self._parse_fields, axis="columns")

        # All component definitions include an "entity" column and a "comp_ind" column
        # We pull the definitions from a "default_fields" component.
        default_fields = X.loc[X["entity"] == "default_fields", "fields"].iloc[0]
        X["fields"] = X["fields"].apply(lambda d: {**default_fields, **d})

        # Update validity with whether or not the component is defined
        X.loc[~X["is_defined"], "is_valid"] = False
        X.loc[~X["is_defined"], "errors"] += "Component definition does not exist. "

        # Reorganize and rename
        X = X.rename(
            columns={
                "fields.component": "unparsed_fields",
                "component.multiplicity": "multiplicity",
            }
        ).drop(columns=["component.value"])

        return X

    def _parse_fields(
        self,
        row,
    ) -> pd.Series:
        # If not given any fields then this is just a flag component
        if pd.isna(row["fields.component"]):
            row["fields.component"] = {}
            row["fields"] = {}
            row["is_valid"] = True
            row["errors"] = ""
            return row

        fields_i = {}
        valid_fields = True
        valid_message = ""
        for field_key, field_value in row["fields.component"].items():
            try:
                field = data.Field.from_kv_pair(field_key, field_value)
                fields_i[field.name] = field
            except (ValueError, TypeError) as e:
                valid_fields = False
                valid_message += (
                    f"Field {field_key} is incorrectly formatted: {field_value}. "
                    f"Error: {e}"
                )

        row["fields"] = fields_i
        row["is_valid"] = valid_fields
        row["errors"] = valid_message

        return row


class ComponentValidator(BaseEstimator, TransformerMixin):

    def fit(self, _X, _y=None):
        return self

    def transform(self, X, registry: data.Registry = None):

        # This is another transform operation that operates on unindexed DataFrames.
        X = registry.reset_index(X)

        # Since X is the input view, which is what we're validating,
        # we can use the view_components attribute to get the name of the component
        key = X.attrs["view_components"]

        # Get the component definition
        # If we're validating compdef we have to handle it specially,
        # because X is not yet in the format it should be.
        if key == "compdef":
            component_def = X.loc[X["entity"] == "compdef"]
            if len(component_def) > 1:
                raise ValueError(
                    f"Multiple component definitions found for key '{key}'. "
                    "This should not happen, please check your registry."
                )
            component_def = component_def.iloc[0]
        else:
            component_def = registry["compdef"].loc[key]

        # Set the attributes for validity and errors
        X.attrs["is_valid"] = component_def["is_valid"]
        X.attrs["errors"] = component_def["errors"]

        # Validate X against the schema
        try:
            # The fields in the component definition are the schema for the DataFrame
            dataframe_schema = pa.DataFrameSchema(component_def["fields"])
            X = dataframe_schema.validate(X)
        except (AttributeError, pa.errors.SchemaError) as e:
            X.attrs["is_valid"] = False
            X.attrs["errors"] += str(e) + " "

        return X


class LinksParser(BaseEstimator, TransformerMixin):

    def fit(self, _X, _y=None):
        return self

    def transform(
        self, X: pd.DataFrame, registry: data.Registry = None
    ) -> pd.DataFrame:

        # This transformer produces new components,
        # so we indicate that with nan comp_inds
        X = registry.reset_index(X)
        X["comp_ind"] = pd.NA

        # Parse the links column
        exploded_links = (
            X["value"]
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
                "Links column is not formatted correctly. Did you use a pipe, |? "
            )
        # Add the parsed results back to the original DataFrame
        X_out = X.join(exploded_links).reset_index(drop=True).drop(columns="value")

        return X_out


class LinkCollector(BaseEstimator, TransformerMixin):

    def fit(self, _X, _y=None):
        return self

    def transform(
        self, X: pd.DataFrame, registry: data.Registry = None
    ) -> pd.DataFrame:

        # Validate and get an index-less copy
        if X.attrs["view_components"] != "link":
            raise ValueError(
                "LinkCollector should only be used on the 'link' view. "
                f"Got: {X.attrs['view_components']}"
            )
        X = X.reset_index()

        # Check that link_types has the right index
        link_types = registry.view("link_type")
        assert link_types.index.names == [
            "entity",
        ], "link_types should have a single index level 'entity'."

        def format_links(link_type: str) -> pd.DataFrame:
            """
            Formats links for a given link_type, setting owner as source or target.

            Parameters
            ----------
            link_type : str
                The link type to format.
            owner_is_source : bool
                If True, owner is source; otherwise, owner is target.

            Returns
            -------
            pd.DataFrame
                DataFrame of formatted links.
            """

            df_i = registry.view(link_type)

            # Every component flagged as a link_type should have a 'value' column
            # and a multiindex of entity, comp_ind. We massage those into a DataFrame
            # with multiindex (with nan comp_ind) and a source and target column.
            df_i = df_i.reset_index()
            df_i = df_i.rename(columns={"value": "target"})
            df_i["source"] = df_i["entity"]
            # This will get filled in to an appropriate value later
            df_i["comp_ind"] = pd.NA
            df_i["link_type"] = link_type
            df_i = df_i[["entity", "comp_ind", "source", "target", "link_type"]]

            return df_i

        # Loop through and gather the links from the components tagged with link_type
        dfs = []
        for _, row in link_types.iterrows():

            # Collect the links from the component
            link_type = row.name

            # Sometimes there aren't links of that type yet, at least as components
            if link_type in registry:
                df_i = format_links(link_type)
                dfs.append(df_i)

            # Collect the links from the reverse component
            if row.isna()["reverse"]:
                continue
            reverse_link_type = row["reverse"]
            if reverse_link_type in registry:
                df_i = format_links(reverse_link_type)
                # We use the non-reverse link type as the link_type, since we want to treat
                # them as the same type of link
                dfs.append(df_i)

        # Add the links to the original DataFrame
        X = pd.concat([X] + dfs, ignore_index=True)

        # Change reversed link types to the original link type
        for _, row in link_types.iterrows():

            # Get the relevant rows
            is_reverse_link_type = X["link_type"] == row["reverse"]
            df_i = X.loc[is_reverse_link_type].copy()

            # If there are no links of this type, skip
            if df_i.empty:
                continue

            # Reverse the source and target columns and change the link_type
            df_i = df_i.rename(columns={"source": "target", "target": "source"})
            df_i["link_type"] = row.name

            # Put the data back
            X.loc[is_reverse_link_type] = df_i

        # De-duplicate
        X = X.drop_duplicates(subset=["source", "target", "link_type"])

        return X


class GraphAnalyzer(BaseEstimator, TransformerMixin):
    """
    Transformer that builds a graph from the links in the registry.
    It doesn't modify the link component, but adds a node component.
    """

    def fit(self, _X, _y=None):
        return self

    def transform(
        self, X: pd.DataFrame, registry: data.Registry = None
    ) -> pd.DataFrame:

        assert X.attrs["view_components"] == "link", (
            "GraphBuilder should only be used on the 'link' view. "
            f"Got: {X.attrs['view_components']}"
        )
        assert hasattr(registry, "graph"), (
            "GraphBuilder expects the registry to have a 'graph' attribute."
        )

        # Build a nodes dataframe with information about connectivity
        connected_components = [
            _ for _ in nx.connected_components(registry.graph.to_undirected())
        ]
        X_out = pd.DataFrame({"entity": list(registry.graph.nodes())}).set_index("entity")
        X_out["connected_component_group"] = -1
        for i, comps in enumerate(connected_components):
            X_out.loc[list(comps), "connected_component_group"] = i

        return X_out
