#!/usr/bin/env python
"""concrete_hierarchy_test.py
Template module demonstrating unit tests for the ConcreteHierarchy class.

This module provides a template for writing unit tests for the `ConcreteHierarchy` class using the
`concrete_hierarchy_test`, ensuring it is correctly tested.
"""

# Header #
__package_name__ = "templatepackage"

__author__ = "Author Name"
__credits__ = ["Author Name"]
__copyright__ = "Copyright 2021, Author Name"
__license__ = "License"

__version__ = "0.1.0"


# Imports #
# Third-Party Packages #
import pytest

# Source Packages #
from templatepackage.hierarchy import ConcreteHierarchy
from templatepackage.testsuite.hierarchy import ConcreteHierarchyTestSuite


# Definitions #
# Tests #
class TestConcreteHierarchy(ConcreteHierarchyTestSuite):
    """Tests ConcreteHierarchy using the corresponding test suite."""

    # Attributes #
    UnitTestClass: type[ConcreteHierarchy] = ConcreteHierarchy


# Main #
if __name__ == "__main__":
    pytest.main(["-v", "-s"])
