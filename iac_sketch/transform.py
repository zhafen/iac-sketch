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

# Transformer to extract and validate component definitions (bottom of file)
class ComponentDefExtractor(BaseEstimator, TransformerMixin):
    """
    Extracts and validates component definitions from a registry, mimicking parsecomp_component.
    """
    def fit(self, _X, _y=None):
        return self

    def transform(self, registry):
        comps_df = self._build_components_dataframe(registry)
        comps_df = self._parse_fields(comps_df)
        comps_df = comps_df.set_index("entity")
        registry["component"] = comps_df
        return registry

    def _build_components_dataframe(self, registry: data.Registry) -> pd.DataFrame:
        comp_df = registry["component"].drop(columns=["component"])
        data_comp = registry["fields"]
        data_comp = data_comp.rename(
            columns={"comp_ind": "fields_comp_ind", "component": "fields"}
        )
        comp_df = comp_df.set_index("entity").join(
            data_comp.set_index("entity"), how="outer"
        )
        comp_df["defined"] = True
        comps_created = pd.DataFrame({"entity": registry.keys()})
        comp_df = comp_df.merge(comps_created, how="outer", on="entity")
        comp_df.loc[comp_df["defined"].isna(), "defined"] = False
        comp_df["defined"] = comp_df["defined"].astype(bool)
        return comp_df

    def _parse_fields(self, components: pd.DataFrame) -> pd.DataFrame:
        components["unparsed_fields"] = components["fields"]
        valids = []
        valid_messages = []
        fields = []
        for _, comp in components.query("defined").iterrows():
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
        components["valid_def"] = False
        components["valid_def_message"] = "undefined"
        components.loc[components["defined"], "valid_def"] = valids
        components.loc[components["defined"], "valid_def_message"] = valid_messages
        components.loc[components["defined"], "fields"] = fields
        return components
