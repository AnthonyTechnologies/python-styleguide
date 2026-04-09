"""conftest.py
Template module demonstrating shared pytest fixtures.

This module provides a template for centralizing shared fixtures in a `conftest.py` file, demonstrating fixture scoping
and the use of the project's custom classes within tests.
"""

# Header #
__package_name__ = "templatepackage"

__author__ = "Author Name"
__credits__ = ["Author Name"]
__copyright__ = "Copyright 2026, Author Name"
__license__ = "License"

__version__ = "0.1.0"


# Imports #
# Standard Libraries #
import shutil
from collections.abc import AsyncIterator, Generator
from pathlib import Path
from typing import Any

# Third-Party Packages #
import pytest
import pytest_asyncio

# Source Packages #
from templatepackage.async_client import MockAsyncClient


# Definitions #
# Fixtures #
@pytest.fixture(scope="session")
def mock_db() -> Generator[dict[str, Any], None, None]:
    """Provides a session-scoped mock database connection.

    Yields:
        dict[str, Any]: A simulated database dictionary.
    """
    db: dict[str, Any] = {"users": {}, "settings": {}}
    yield db
    db.clear()


@pytest.fixture
def user_data() -> dict[str, Any]:
    """Provides a fresh set of user data for each test.

    Returns:
        dict[str, Any]: A dictionary containing sample user attributes.
    """
    return {
        "user_id": "user_456",
        "name": "Jane Smith",
        "active": True,
    }


@pytest_asyncio.fixture
async def async_client() -> AsyncIterator[MockAsyncClient]:
    """Provides a connected MockAsyncClient.

    This fixture demonstrates how to manage async resources using `async with`.

    Yields:
        MockAsyncClient: A connected client instance.
    """
    async with MockAsyncClient("https://api.test.com") as client:
        yield client


@pytest.fixture
def temp_dir(tmp_path: Path) -> Generator[Path, None, None]:
    """Demonstrates usage of the built-in `tmp_path` fixture with custom cleanup.

    Args:
        tmp_path: The built-in pytest fixture for a temporary directory.

    Yields:
        Path: The path to a temporary directory created for the test.
    """
    d = tmp_path / "test_run"
    d.mkdir()
    yield d
    shutil.rmtree(d, ignore_errors=True)
