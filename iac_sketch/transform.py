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
    """
    Extracts and validates component definitions from a registry, mimicking parsecomp_component.
    """
    def fit(self, _X, _y=None):
        return self

    def transform(self, X):

        X = X.copy()

        comps_df = self._parse_fields(comps_df)
        comps_df = comps_df.set_index("entity")
        X["component"] = comps_df
        return X

    def _parse_fields(self, X: pd.DataFrame) -> pd.DataFrame:

        X["defined"] = True
        comps_created = pd.DataFrame({"entity": X.keys()})
        X = X.merge(comps_created, how="outer", on="entity")
        X.loc[X["defined"].isna(), "defined"] = False
        X["defined"] = X["defined"].astype(bool)

        X["unparsed_fields"] = X["fields"]
        valids = []
        valid_messages = []
        fields = []
        for _, comp in X.query("defined").iterrows():
            fields_i = {}
            if comp.notna()["fields"]:
                valid_fields = True
                valid_message = ""
                for field_key, field_value in comp["fields"].items():
                    try:
                        field = data.Field.from_kv_pair(field_key, field_value)
                        fields_i[field.name] = field
                    except ValueError:
                        valid_fields = False
                        valid_message = (
                            f"field {field_key} is incorrectly formatted: {field_value}"
                        )
                        break
                if not valid_fields:
                    valids.append(False)
                    valid_messages.append(valid_message)
                    fields.append(pd.NA)
                    continue
            fields.append(fields_i)
            valids.append(True)
            valid_messages.append("")
        X["valid_def"] = False
        X["valid_def_message"] = "undefined"
        X.loc[X["defined"], "valid_def"] = valids
        X.loc[X["defined"], "valid_def_message"] = valid_messages
        X.loc[X["defined"], "fields"] = fields
        return X
