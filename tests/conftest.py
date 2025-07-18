import pandas as pd
import pytest


@pytest.fixture(scope="session", autouse=True)
def configure_pandas():
    """Configure pandas display options for all tests."""
    pd.set_option('display.width', 250)
    pd.set_option('display.max_columns', None)
