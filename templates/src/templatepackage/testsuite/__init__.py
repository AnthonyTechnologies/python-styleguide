"""__init__.py
Test suites for the templatepackage package.

Contains test suites for the templatepackage package. It provides a structured testing framework to ensure the
functionality and reliability of the templatepackage components and is a basis for creating tests for hierarchies of
components.
"""

# Header #
__package_name__ = "templatepackage"

__author__ = "Author Name"
__credits__ = ["Author Name"]
__copyright__ = "Copyright 2021, Author Name"
__license__ = "License"

__version__ = "0.1.0"


# Imports #
# Local Packages #
from .usertestsuite import UserTestSuite
from .hierarchy import *

__all__ = ["UserTestSuite", "BaseHierarchyTestSuite", "ConcreteHierarchyTestSuite"]
