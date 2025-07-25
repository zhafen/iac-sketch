import pandas as pd

from . import data


def test_designed(registry: data.Registry) -> pd.DataFrame:

    # Get all requirements that are not satisfied by any component
    return (
        registry.view("requirement")
        .reset_index()
        .merge(
            registry.view("link").query("link_type == 'satisfies'"),
            left_on="entity",
            right_on="target",
            how="left",
        )
        .query("source.isna()")
    )


def test_implemented(registry: data.Registry) -> pd.DataFrame:

    # All requirements where the satisfies component status is not 'done'
    reqs = registry.view("requirement").reset_index()
    links = registry.view(["link", "status"]).query("`link.link_type` == 'satisfies'")
    return reqs.merge(
        links, left_on="entity", right_on="link.target", how="left"
    ).query("`status.value` != 'done'")

def test_defined(registry: data.Registry) -> pd.DataFrame:

    # All compdefs that are invalid
    return registry.view("compdef").query("~is_valid")

def test_connected(registry: data.Registry) -> pd.DataFrame:

    return registry.view("node").query("connected_component_group != 0")