import pandas as pd

from iac_sketch import data


def test_designed(
    registry: data.Registry, allowed_infrastructure: list[str] = None
) -> pd.DataFrame:
    """
    Parameters
    ----------
    registry : data.Registry
        The registry containing the components to test.

    Returns
    -------
    pd.DataFrame
        A DataFrame containing the test results.

    Metadata
    ----------
    - test
    - satisfies: fully_designed
    """

    # We start with the requirements that are not implemented
    reqs = test_implemented(registry, allowed_infrastructure=allowed_infrastructure)

    # Then we just select those that don't even have a satisfies link yet
    reqs = reqs.query("`link.link_type`.isna()")

    return reqs


def test_implemented(
    registry: data.Registry,
    allowed_statuses: list[str] = ["in production"],
    allowed_infrastructure: list[str] = None,
) -> pd.DataFrame:
    """
    Parameters
    ----------
    registry : data.Registry
        The registry containing the components to test.

    Returns
    -------
    pd.DataFrame
        A DataFrame containing the invalid entities.

    Metadata
    ----------
    - test
    - satisfies: fully_implemented
    - todo: Add code that identifies parent nodes with unsatisfied child nodes.
    """

    reqs = registry.view("requirement")
    if allowed_infrastructure is not None:
        is_allowed = reqs["value"].isin(allowed_infrastructure) | reqs["value"].isna()
        reqs = reqs.loc[is_allowed]

    # Get entities with [requirement] components and any entities linked with
    # a [satisfies]/[satisfied_by] or [parent]/[child] link.
    # Entities without either have nan values, which will be among those returned.
    reqs = reqs.reset_index().merge(
        registry.view(["link", "status"]).query(
            "`link.link_type` in ['satisfies', 'parent']"
        ),
        left_on="entity",
        right_on="link.target",
        how="left",
    )

    # Drop the requirements that have children
    reqs = reqs.query("`link.link_type` != 'parent'")
    # Drop the requirements that have a valid status
    reqs = reqs[~reqs["status.value"].isin(allowed_statuses)]

    return reqs


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

    Metadata
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

    Metadata
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

    Metadata
    ----------
    - test
    - satisfies: no_forbidden_components
    - todo: Add priority cutoff.
    """

    result_dfs = []
    for comp_type in forbidden_components:
        if comp_type not in registry:
            continue
        result_df = registry.view(comp_type).reset_index()
        result_dfs.append(result_df[["entity", "comp_key", "value"]])

    if len(result_dfs) > 0:
        result_df = pd.concat(result_dfs, ignore_index=True)
    else:
        result_df = pd.DataFrame()

    return result_df
