"""abstract_hierarchy.py
Template module demonstrating an abstract class within a hierarchy.

This module provides an abstract base class that defines the required interface for subclasses, demonstrating the use of
abstract methods and properties.
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
from abc import ABC, abstractmethod

# Local Packages #
from .base_hierarchy import BaseHierarchy


# Definitions #
# Classes #
class AbstractHierarchy(BaseHierarchy, ABC):
    """An abstract class in the hierarchy.

    This class defines abstract methods that must be implemented by concrete subclasses, ensuring a consistent
    interface.
    """

    # Instance Methods #
    # Operations
    @abstractmethod
    def perform_action(self, action_input: str) -> str:
        """Performs a specific action on the hierarchy object.

        Args:
            action_input: The input for the action.

        Returns:
            The result of the action.
        """

    @abstractmethod
    def get_status(self) -> bool:
        """Returns the status of the object.

        Returns:
            True if operational, False otherwise.
        """
