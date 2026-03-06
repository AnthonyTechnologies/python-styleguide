"""__init__.py
Package initialization for the hierarchy submodule.
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
from .base_hierarchy import BaseHierarchy
from .hierarchy_mixin import HierarchyMixin
from .abstract_hierarchy import AbstractHierarchy
from .concrete_hierarchy import ConcreteHierarchy

__all__ = ["BaseHierarchy", "HierarchyMixin", "AbstractHierarchy", "ConcreteHierarchy"]
