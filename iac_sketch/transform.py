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

    def transform(self, X: pd.DataFrame, _registry: data.Registry = None) -> pd.DataFrame:
        X = X.copy()
        if "errors" not in X.columns:
            X["errors"] = ""
        if "valid" not in X.columns:
            X["valid"] = True
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
        X["defined"] = True
        registry_comps = pd.DataFrame({"entity": registry.keys()})
        X = X.merge(registry_comps, how="outer", on="entity")
        X.loc[X["defined"].isna(), "defined"] = False
        X["defined"] = X["defined"].astype(bool)

        # Parse the fields
        X = X.apply(self._parse_fields, axis="columns")

        # Rename
        X = X.rename({"component": "unparsed_fields"}, axis="columns")

        # All component definitions include an "entity" column and a "comp_ind" column
        # We pull the definitions from a "default_fields" component.
        default_fields = X.loc[X["entity"] == "default_fields", "fields"].iloc[0]
        X["fields"] = X["fields"].apply(lambda d: {**default_fields, **d})

        # Update validity with whether or not the component is defined
        X.loc[~X["defined"], "valid"] = False
        X.loc[~X["defined"], "errors"] += "Component definition does not exist. "

        return X

    def _parse_fields(
        self,
        row,
    ) -> pd.Series:
        # If not given any fields then this is just a flag component
        if pd.isna(row["component"]):
            row["component"] = {}
            row["fields"] = {}
            row["valid"] = True
            row["errors"] = ""
            return row

        fields_i = {}
        valid_fields = True
        valid_message = ""
        for field_key, field_value in row["component"].items():
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
        row["valid"] = valid_fields
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
        X.attrs["valid"] = component_def["valid"]
        X.attrs["errors"] = component_def["errors"]

        # The fields in the component definition are the schema for the DataFrame
        dataframe_schema = pa.DataFrameSchema(component_def["fields"])

        # Validate X against the schema
        try:
            X = dataframe_schema.validate(X)
        except pa.errors.SchemaError as exc:
            X.attrs["valid"] = False
            X.attrs["errors"] += str(exc) + " "

        return X

class LinksParser(BaseEstimator, TransformerMixin):
    """TODO: Facing an instance of the newest problem with the framework, which is: how to handle comp_inds when we're generating new components post-yaml?
    """

    def fit(self, _X, _y=None):
        return self

    def transform(self, X: pd.DataFrame, _registry: data.Registry = None) -> pd.DataFrame:
        X = X.copy()

        # Parse the links column
        exploded_links = (
            X["links"]
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
        X_out = (
            X.join(exploded_links).drop(columns=["links"]).reset_index(drop=True)
        )

        # Ensure we have the right index
        X_out = X_out.set_index(["entity", "comp_ind"], drop=False)

        return X_out
