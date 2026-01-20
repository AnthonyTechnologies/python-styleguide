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
import copy
from typing import Any, Final

# Third-Party Packages #
import pytest

# Source Packages #
from baseobjects.testsuite import BaseClassTestSuite

# Local Packages #
from ..src.package_template import User, UserRegistry
from ..src.package_template.testsuite import UserTestSuite


# Definitions #
# Constants and Test Data #
_SECTION_LINE: Final[str] = "-" * 72


# Tests #
class TestUser(UserTestSuite):
    """Tests User using UserTestSuite."""
    pass


class TestUserRegistry(BaseClassTestSuite):
    """Tests UserRegistry."""

    # Attributes #
    UnitTestClass = UserRegistry

    # Fixtures #
    @pytest.fixture(scope="module")
    def sample_users(self) -> list[User]:
        """Provides reusable test data."""
        return [User(user_id="1", name="Alice"), User(user_id="2", name="Bob")]

    @pytest.fixture
    def test_object(self, sample_users: list[User]) -> UserRegistry:
        """Yields a fresh registry."""
        # Create a fresh registry with copies of users to avoid side effects
        users_copy = [copy.copy(u) for u in sample_users]
        return UserRegistry(users=users_copy)

    # Tests #
    def test_instance_creation(self, *args: Any, **kwargs: Any) -> None:
        """Tests that instances of the class can be created.

        Args:
            *args: Positional arguments list to pass to the class constructor.
            **kwargs: Keyword arguments to pass to the class constructor.
        """
        users = [User(user_id="1", name="Alice")]
        obj = self.UnitTestClass(users=users, *args, **kwargs)
        assert isinstance(obj, self.UnitTestClass)
        assert len(obj.users) == 1

    def test_initial_state(self, test_object: UserRegistry) -> None:
        """Verifies initial state of the registry.

        Args:
            test_object: The registry to test.
        """
        assert len(test_object.users) == 2
        assert "alice" in test_object.get_all_names()

    def test_add_user(self, test_object: UserRegistry) -> None:
        """Tests adding a user.

        Args:
            test_object: The registry to test.
        """
        u = User(user_id="3", name="Charlie")
        test_object.add_user(u)
        assert len(test_object.users) == 3
        assert "charlie" in test_object.get_all_names()

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
