import pandas as pd

from . import data

def test_designed(registry: data.Registry) -> pd.DataFrame:

    # Get the requirements and join with the entities that satisfy them
    requirements = registry.view(["requirement", "description"])
    satisfies = registry.view("satisfies")
    requirements = requirements.merge(
        satisfies,
        left_on="entity",
        right_on="value",
        how="left",
    )

    return requirements.query("satisfies.isna()")

def test_implemented(registry: data.Registry) -> pd.DataFrame:

    assert False

def test_defined(registry: data.Registry) -> pd.DataFrame:

    assert False

def test_connected(registry: data.Registry) -> pd.DataFrame:

    assert False