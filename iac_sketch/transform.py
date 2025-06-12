# Custom transformer for adding error and validity metadata columns
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

class AddErrorTrackingTransformer(BaseEstimator, TransformerMixin):
    """
    Transformer that adds two columns to a DataFrame:
    - 'errors': for tracking errors on a per-row basis (default: empty string)
    - 'valid': for indicating if a row is valid (default: True)
    """
    def fit(self, X, y=None):
        # Stateless transformer, nothing to fit
        return self

    def transform(self, X):
        X = X.copy()
        if 'errors' not in X.columns:
            X['errors'] = ""
        if 'valid' not in X.columns:
            X['valid'] = True
        return X
