import networkx as nx
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from .. import data


class LinksParser(BaseEstimator, TransformerMixin):

    def fit(self, _X, _y=None):
        return self

    def transform(
        self, X: pd.DataFrame, registry: data.Registry = None
    ) -> pd.DataFrame:

        # This transformer produces new components,
        # so we indicate that with nan comp_keys
        X = registry.reset_index(X)
        X["comp_key"] = pd.NA

        # Parse and check formatting
        parsed_links = X["value"].str.strip().str.split("\n").explode()
        correctly_formatted = parsed_links.str.match(r"^\w+\s*-->\s*\w+$")
        if not correctly_formatted.all():
            bad_parsed_links = parsed_links.loc[~correctly_formatted]
            first_entity = X.loc[bad_parsed_links.index[0], "entity"]
            raise ValueError(
                "Found malformed 'links' components. All components should be one or "
                "more lines of the form 'source --> target'.\n"
                f"First error is for entity {first_entity}: "
                f'"{bad_parsed_links.iloc[0]}"'
            )

        # Split into columns
        split_links = parsed_links.str.split("-->", expand=True).rename(
            columns={0: "source", 1: "target"}
        )
        # Strip whitespace
        for col in split_links.columns:
            split_links[col] = split_links[col].str.strip()
        # Add the parsed results back to the original DataFrame
        X_out = X.join(split_links).reset_index(drop=True).drop(columns="value")

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

        # Set up parent-child links for all components with a "child_component" flag
        child_compinsts = registry.reset_index(registry.view("compinst")).merge(
            registry.reset_index(registry.view("child_component")),
            left_on="component_type",
            right_on="entity",
            how="inner",
            suffixes=("", "_child"),
        )
        child_compinsts = child_compinsts.rename(
            columns={"entity": "target", "comp_key": "source"}
        )[["source", "target"]]
        child_compinsts["link_type"] = "parent"

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
            # and a multiindex of entity, comp_key. We massage those into a DataFrame
            # with multiindex (with nan comp_key) and a source and target column.
            df_i = df_i.reset_index()
            df_i = df_i.rename(columns={"value": "target"})
            df_i["source"] = df_i["entity"]
            # This will get filled in to an appropriate value later
            df_i["comp_key"] = pd.NA
            df_i["link_type"] = link_type
            df_i = df_i[["entity", "comp_key", "source", "target", "link_type"]]

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
        assert hasattr(
            registry, "graph"
        ), "GraphBuilder expects the registry to have a 'graph' attribute."

        # Build a nodes dataframe with information about connectivity
        connected_components = [
            _ for _ in nx.connected_components(registry.graph.to_undirected())
        ]
        X_out = pd.DataFrame({"entity": list(registry.graph.nodes())}).set_index(
            "entity"
        )
        X_out["connected_component_group"] = -1
        for i, comps in enumerate(connected_components):
            X_out.loc[list(comps), "connected_component_group"] = i

        return X_out


class RequirementAnalyzer(BaseEstimator, TransformerMixin):
    """
    Transformer that analyzes requirements in the registry.
    """

    def fit(self, _X, _y=None):
        return self

    def transform(
        self, X: pd.DataFrame, registry: data.Registry = None
    ) -> pd.DataFrame:

        # Filter to only parent-child relationships
        subgraph = nx.subgraph_view(
            registry.graph, filter_edge=lambda u, v, k: k == "parent"
        )

        # Propagate requirement values down the parent-child hierarchy
        reqs_with_values = X.dropna(subset="value")
        for idx, req in reqs_with_values.iterrows():
            for d in nx.ancestors(subgraph, idx):
                X.loc[d, "value"] = req["value"]

        return X
