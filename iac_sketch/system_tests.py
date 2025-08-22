import pandas as pd

from iac_sketch import data


def test_designed(registry: data.Registry) -> pd.DataFrame:
    """
    Parameters
    ----------
    registry : data.Registry
        The registry containing the components to test.

    Returns
    -------
    pd.DataFrame
        A DataFrame containing the test results.

    Components
    ----------
    - test
    - satisfies: fully_designed
    """

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
    """
    Parameters
    ----------
    registry : data.Registry
        The registry containing the components to test.

    Returns
    -------
    pd.DataFrame
        A DataFrame containing the test results.

    Components
    ----------
    - test
    - satisfies: fully_implemented
    """

    # All requirements where the satisfies component status is not 'done'
    reqs = registry.view("requirement").reset_index()
    links = registry.view(["link", "status"]).query("`link.link_type` == 'satisfies'")
    return reqs.merge(
        links, left_on="entity", right_on="link.target", how="left"
    ).query("`status.value` != 'done'")

def test_defined(registry: data.Registry) -> pd.DataFrame:
    """
    Parameters
    ----------
    registry : data.Registry
        The registry containing the components to test.

    Returns
    -------
    pd.DataFrame
        A DataFrame containing the test results.

    Components
    ----------
    - test
    - satisfies: fully_defined
    """

    # All compdefs that are invalid
    return registry.view("compdef").query("~is_valid")

def test_connected(registry: data.Registry) -> pd.DataFrame:
    """
    Parameters
    ----------
    registry : data.Registry
        The registry containing the components to test.

    Returns
    -------
    pd.DataFrame
        A DataFrame containing the test results.

    Components
    ----------
    - test
    - satisfies: fully_connected
    """

    return registry.view("node").query("connected_component_group != 0")

def test_no_forbidden_components(
    registry: data.Registry,
    forbidden_components: list[str] = ["todo", "error"],
) -> pd.DataFrame:
    """
    Parameters
    ----------
    registry : data.Registry
        The registry containing the components to test.
    forbidden_components : list[str], optional
        A list of component types that should not exist if the system
        is fully functional.

    Returns
    -------
    pd.DataFrame
        A DataFrame containing the test results.

    Components
    ----------
    - test
    - satisfies: no_forbidden_components
    """

    compinst = registry.view("compinst")
    return compinst.loc[compinst["component_type"].isin(forbidden_components)]
