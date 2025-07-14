import pandas as pd

from . import data

def validate_designed(registry: data.Registry) -> pd.DataFrame:

    # Get the requirements and join with the entities that satisfy them
    requirements = registry.view(["requirement", "description"])
    satisfies = registry.view("satisfies")
    requirements = requirements.merge(
        satisfies,
        left_on="entity",
        right_on="value",
        how="left",
    )

    return requirements.query("value_satisfies.isna()")

def validate_implemented(registry: data.Registry) -> pd.DataFrame:

    assert False

def validate_defined(registry: data.Registry) -> pd.DataFrame:

    assert False

def validate_connected(registry: data.Registry) -> pd.DataFrame:

    assert False