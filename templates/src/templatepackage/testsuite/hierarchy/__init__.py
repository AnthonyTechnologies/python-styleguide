"""__init__.py
Package initialization for the testsuite of the hierarchy.
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
from .basehierarchytestsuite import BaseHierarchyTestSuite
from .concretehierarchytestsuite import ConcreteHierarchyTestSuite

__all__ = ["BaseHierarchyTestSuite", "ConcreteHierarchyTestSuite"]
