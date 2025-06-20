import pandas as pd
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

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        X = X.copy()
        if 'errors' not in X.columns:
            X['errors'] = ""
        if 'valid' not in X.columns:
            X['valid'] = True
        return X

class ComponentNormalizer(BaseEstimator, TransformerMixin):
    """
    Expands a 'component' column in a DataFrame into separate columns using pandas.json_normalize.
    If the component is not a dict, the value is placed in a column named after the component key.
    """
    def fit(self, _X, _y=None):
        return self

    def transform(self, X):

        X = X.copy()

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

    def __init__(self, registry: data.Registry):
        self.registry = registry

    def fit(self, _X, _y=None):
        return self

    def transform(self, X):

        X = X.copy()

        # Add in all components defined in the registry
        # and mark the ones that are not defined
        X["defined"] = True
        registry_comps = pd.DataFrame({"entity": self.registry.keys()})
        X = X.merge(registry_comps, how="outer", on="entity")
        X.loc[X["defined"].isna(), "defined"] = False
        X["defined"] = X["defined"].astype(bool)

        # Parse the fields
        X = X.apply(self._parse_fields, axis="columns")

        # Rename
        X = X.rename({"component": "unparsed_fields"}, axis="columns")

        return X


    def _parse_fields(self, row):
        # If not given any fields then this is just a flag component
        if pd.isna(row["component"]):
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
