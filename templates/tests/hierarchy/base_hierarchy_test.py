#!/usr/bin/env python
"""base_hierarchy_test.py
Template module demonstrating unit tests for the base_hierarchy class.

This module provides a template for writing unit tests for the `base_hierarchy` class using the `base_hierarchyTestSuite`,
ensuring it is correctly tested.
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

# Local Packages #
from templatepackage.hierarchy import BaseHierarchy
from templatepackage.testsuite.hierarchy import BaseHierarchyTestSuite


# Definitions #
# Tests #
class TestBaseHierarchy(BaseHierarchyTestSuite):
    """Tests BaseHierarchy using the corresponding test suite."""

    # Attributes #
    UnitTestClass: type[BaseHierarchy] = BaseHierarchy


# Main #
if __name__ == "__main__":
    pytest.main(["-v", "-s"])
