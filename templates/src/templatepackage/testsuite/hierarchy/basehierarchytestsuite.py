"""basehierarchytestsuite.py
Template module demonstrating a test suite for the BaseHierarchy class.

This module provides the `BaseHierarchyTestSuite` class which serves as a foundation for testing classes that inherit
from `BaseHierarchy`. It includes basic tests for initialization and description.
"""

# Header #
__package_name__ = "templatepackage"

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
from ...hierarchy.base_hierarchy import BaseHierarchy


# Definitions #
# Classes #
class BaseHierarchyTestSuite(BaseClassTestSuite):
    """A test suite for the BaseHierarchy class.

    This suite tests the basic functionality provided by the root class of the hierarchy.
    """

    # Attributes #
    UnitTestClass: type[BaseHierarchy] = BaseHierarchy

    # Instance Methods #
    # Fixtures
    @pytest.fixture
    def test_object(self, *args: Any, **kwargs: Any) -> BaseHierarchy:
        """Creates a test object for BaseHierarchy.

        Args:
            *args: Positional arguments to pass to the class constructor.
            **kwargs: Keyword arguments to pass to the class constructor.

        Returns:
            BaseHierarchy: A BaseHierarchy instance for testing.
        """
        kwargs.setdefault("name", "TestBase")
        return self.UnitTestClass(*args, **kwargs)

    # Tests
    def test_name_assignment(self, test_object: BaseHierarchy) -> None:
        """Tests that the name is correctly assigned during initialization.

        Args:
            test_object: The object to test.
        """
        assert test_object.name == "TestBase"

    def test_get_description(self, test_object: BaseHierarchy) -> None:
        """Tests the get_description method.

        Args:
            test_object: The object to test.
        """
        assert "TestBase" in test_object.get_description()


# Main #
if __name__ == "__main__":
    pytest.main(["-v", "-s"])
