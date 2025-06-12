
# Custom transformer for adding error and validity metadata columns
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

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

class ComponentDictNormalizer(BaseEstimator, TransformerMixin):
    """
    Expands a 'component' column in a DataFrame into separate columns using pandas.json_normalize.
    If the component is not a dict, the value is placed in a column named after the component key.
    """
    def fit(self, _X, _y=None):
        return self

    def transform(self, X):

        X = X.copy()

        comp_data = pd.json_normalize(X["component"])
        if len(comp_data.columns) == 0:
            if not X["component"].isna().all():
                X = X.rename(columns={"component": "value"})
            else:
                X = X.drop(columns=["component"])
        else:
            not_parsed = comp_data.isna().all(axis="columns")
            if not_parsed.any():
                if "value" not in comp_data.columns and not_parsed.any():
                    comp_data["value"] = pd.NA
                comp_data.loc[not_parsed, "value"] = X.loc[not_parsed, "component"]
            X = X.drop(columns=["component"])
            X = X.join(comp_data)

        return X