#!/usr/bin/env python
"""unit_test_template.py
Template module demonstrating the structure of a unit test file using pytest.

This module provides a template for writing unit tests, including test fixtures, test classes, and parameterized tests.
It demonstrates how to test the functionality of the package_template modules ensuring code correctness. Normally, the
name of this script should match the name of the module it contains, but it is named unit_test_template to make it
easier to find when browsing the templates directory.
"""

# Header #
__package_name__ = "package_template"

__author__ = "Author Name"
__credits__ = ["Author Name"]
__copyright__ = "Copyright 2021, Author Name"
__license__ = "License"

__version__ = "0.1.0"


# Imports #
# Standard Libraries #
from typing import Final
import copy

# Third-Party Packages #
import pytest

# Local Packages #
from templates.src.package_template.class_template import User
from templates.src.package_template.module_template import UserRegistry


# Definitions #
# Constants and Test Data #
_SECTION_LINE: Final[str] = "-" * 72

# Tests #
class TestRegistryBehaviors:
    """Tests UserRegistry."""

    # Fixtures #
    @pytest.fixture(scope="module")
    def sample_users(self) -> list[User]:
        """Provides reusable test data."""
        return [User(user_id="1", name="Alice"), User(user_id="2", name="Bob")]

    @pytest.fixture()
    def registry(self, sample_users: list[User]) -> UserRegistry:
        """Yields a fresh registry."""
        # Create a fresh registry with copies of users to avoid side effects
        users_copy = [copy.copy(u) for u in sample_users]
        return UserRegistry(users=users_copy)

    # Tests #
    def test_initial_state(self, registry: UserRegistry) -> None:
        """Verifies initial state of the registry.

        Args:
            registry: The registry to test.
        """
        assert len(registry.users) == 2
        assert "alice" in registry.get_all_names()

    def test_add_user(self, registry: UserRegistry) -> None:
        """Tests adding a user.

        Args:
            registry: The registry to test.
        """
        u = User(user_id="3", name="Charlie")
        registry.add_user(u)
        assert len(registry.users) == 3
        assert "charlie" in registry.get_all_names()

    @pytest.mark.parametrize("name, expected", [
        ("Alice", "alice"),
        ("  Bob  ", "bob"),
    ])
    def test_normalization(self, name: str, expected: str) -> None:
        """Verifies normalization logic via helper.

        Args:
            name: Username to normalize.
            expected: Expected normalized name.
        """
        u = User(user_id="temp", name=name)
        reg = UserRegistry(users=[u])
        assert reg.get_all_names() == [expected]


# Main #
if __name__ == "__main__":
    pytest.main(["-v", "-s"])
