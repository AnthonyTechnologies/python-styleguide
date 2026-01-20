"""__init__.py
Test suites for the package_template package.

Contains test suites for the package_template package. It provides a structured testing framework to ensure the
functionality and reliability of the package_template components and is a basis for creating tests for hierarchies of
components.
"""

# Header #
__package_name__ = "package_template"

__author__ = "Author Name"
__credits__ = ["Author Name"]
__copyright__ = "Copyright 2021, Author Name"
__license__ = "License"

__version__ = "0.1.0"


# Imports #
# Local Packages #
from .test_suite_template import UserTestSuite

__all__ = ["UserTestSuite"]
