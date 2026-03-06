"""concretehierarchytestsuite.py
Template module demonstrating a test suite for the ConcreteHierarchy class.

This module provides the `ConcreteHierarchyTestSuite` class which inherits from `BaseHierarchyTestSuite` to test the
functionality of the concrete implementation.
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

# Local Packages #
from ...hierarchy.concrete_hierarchy import ConcreteHierarchy
from .basehierarchytestsuite import BaseHierarchyTestSuite


# Definitions #
# Classes #
class ConcreteHierarchyTestSuite(BaseHierarchyTestSuite):
    """A test suite for the ConcreteHierarchy class.

    This suite inherits from `BaseHierarchyTestSuite` to reuse basic tests and adds tests for concrete-specific
    functionality, including abstract method implementations and mixin usage.
    """

    # Attributes #
    UnitTestClass: type[ConcreteHierarchy] = ConcreteHierarchy

    # Instance Methods #
    # Fixtures
    @pytest.fixture
    def test_object(self, *args: Any, **kwargs: Any) -> ConcreteHierarchy:
        """Creates a test object for ConcreteHierarchy.

        Args:
            *args: Positional arguments to pass to the class constructor.
            **kwargs: Keyword arguments to pass to the class constructor.

        Returns:
            ConcreteHierarchy: A ConcreteHierarchy instance for testing.
        """
        kwargs.setdefault("name", "TestConcrete")
        return self.UnitTestClass(*args, **kwargs)

    # Tests
    def test_perform_action(self, test_object: ConcreteHierarchy) -> None:
        """Tests the perform_action method, ensuring it uses the mixin.

        Args:
            test_object: The object to test.
        """
        result = test_object.perform_action("input")
        assert "Processed: input" in result
        assert "TestConcrete" in result

    def test_get_status(self, test_object: ConcreteHierarchy) -> None:
        """Tests the get_status method.

        Args:
            test_object: The object to test.
        """
        assert test_object.get_status() is True

    def test_mixin_functionality(self, test_object: ConcreteHierarchy) -> None:
        """Tests functionality provided by the HierarchyMixin.

        Args:
            test_object: The object to test.
        """
        assert test_object.get_mixin_info() == "HierarchyMixin is present."


# Main #
if __name__ == "__main__":
    pytest.main(["-v", "-s"])
