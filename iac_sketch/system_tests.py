import pandas as pd

from iac_sketch import data


def test_designed(
    registry: data.Registry,
    allowed_infrastructure: list[str] = None,
    min_priority: float = 0.2,
    link_types: list[str] = ["satisfies", "parent"],
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
    reqs = test_implemented(
        registry,
        allowed_infrastructure=allowed_infrastructure,
        min_priority=min_priority,
        link_types=link_types,
    )

    # Then we just select those that don't even have a satisfies link yet
    reqs = reqs.query("`link.link_type`.isna()")

    return reqs


def test_implemented(
    registry: data.Registry,
    allowed_statuses: list[str] = ["in production"],
    allowed_infrastructure: list[str] = None,
    min_priority: float = 0.3,
    link_types: list[str] = ["satisfies", "parent"],
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
    # Rename columns for clarity
    reqs = reqs.rename(
        columns={col: f"requirement.{col}" for col in reqs.columns}
    )

    # Get entities with [requirement] components and any entities linked with
    # a [satisfies]/[satisfied_by] or [parent]/[child] link.
    # Entities without either have nan values, which will be among those returned.
    reqs = reqs.reset_index().merge(
        (links := registry.view(["link", "status", "test"])).loc[
            links["link.link_type"].isin(link_types)
        ],
        left_on="entity",
        right_on="link.target",
        how="left",
    )

    # Drop the requirements that meet one of the below conditions
    # - that have children
    # - have an allowed status
    # - have a low priority
    # - are satisfied by a test component (because the tests themselves check that)
    is_dropped = (
        (reqs["link.link_type"] == "parent")
        | (reqs["status.value"].isin(allowed_statuses))
        | (reqs["requirement.priority"] < min_priority)
        | (reqs["test.comp_key"].notna())
    )
    reqs = reqs.loc[~is_dropped]

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
    forbidden_components: list[str] = ["todo", "issue"],
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
