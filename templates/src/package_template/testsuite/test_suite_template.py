"""test_suite_template.py
Template module demonstrating the structure of a test suite using the project's base test suites.

This module provides a template for creating a test suite that inherits from a base test suite (e.g., BaseClassTestSuite,
BaseObjectTestSuite). It demonstrates how to set the TestClass, define fixtures, and implement tests. Normally, the name
of this script should match the name of the class or module it tests, appended with _test.
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
from typing import Any

# Third-Party Packages #
import pytest
from baseobjects.testsuite import BaseClassTestSuite

# Local Packages #
from ..class_template import User


# Definitions #
# Classes #
class UserTestSuite(BaseClassTestSuite):
    """A Testsuite for the User class.

    This class tests the functionality of the User class. It inherits from BaseClassTestSuite to leverage common testing
    functionality.
    """

    # Attributes #
    TestClass = User

    # Fixtures #
    @pytest.fixture
    def test_object(self) -> User:
        """Creates a test object.

        Returns:
            User: A User instance for testing.
        """
        return User(user_id="test_id", name="Test User")

    # Tests #
    def test_instance_creation(self, *args: Any, **kwargs: Any) -> None:
        """Tests that instances of the class can be created.

        Args:
            *args: Positional arguments list to pass to the class constructor.
            **kwargs: Keyword arguments to pass to the class constructor.
        """
        obj = self.TestClass(user_id="1", name="Name", *args, **kwargs)
        assert isinstance(obj, self.TestClass)
        assert obj.user_id == "1"

    def test_get_display_name(self, test_object: User) -> None:
        """Tests the get_display_name method.

        Args:
            test_object: A fixture providing a test object instance.
        """
        assert test_object.get_display_name() == "Test User"


# Main #
if __name__ == "__main__":
    pytest.main(["-v", "-s"])
