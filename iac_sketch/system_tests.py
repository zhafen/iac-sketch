import pandas as pd

from . import data

def test_designed(registry: data.Registry) -> pd.DataFrame:

    # Get all requirements that are not satisfied by any component
    return registry.view("requirement").reset_index().merge(
        registry.view("link").query("link_type == 'satisfies'"),
        left_on="entity",
        right_on="target",
        how="left",
    ).query("source.isna()")

def test_implemented(registry: data.Registry) -> pd.DataFrame:

    assert False

def test_defined(registry: data.Registry) -> pd.DataFrame:

    assert False

def test_connected(registry: data.Registry) -> pd.DataFrame:

    assert False