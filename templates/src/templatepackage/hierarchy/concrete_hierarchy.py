"""concrete_hierarchy.py
Template module demonstrating a concrete class within a complex hierarchy.

This module provides a concrete implementation that combines multiple aspects of the hierarchy, including base classes,
abstract classes, and mixins.
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
from .abstract_hierarchy import AbstractHierarchy
from .hierarchy_mixin import HierarchyMixin


# Definitions #
# Classes #
class ConcreteHierarchy(AbstractHierarchy, HierarchyMixin):
    """A concrete implementation in the hierarchy.

    This class provides the final implementation for all abstract methods and uses mixin functionality to provide a
    complete hierarchy object.

    Attributes:
        is_ready: Indicates if the concrete object is ready.
    """

    # Class Magic Methods #
    # Construction/Destruction
    def __init__(self, name: str, is_ready: bool = True) -> None:
        """Initializes the ConcreteHierarchy object.

        Args:
            name: The name of the object.
            is_ready: Whether the object is ready. Defaults to True.
        """
        super().__init__(name=name)
        self.is_ready: bool = is_ready

    # Instance Methods #
    # Operations
    def perform_action(self, action_input: str) -> str:
        """Performs a specific action on the concrete object.

        Args:
            action_input: The input for the action.

        Returns:
            The result of the action, incorporating the mixin.
        """
        processed = self.process_data(action_input)
        return f"Action '{processed}' performed by {self.name}."

    def get_status(self) -> bool:
        """Returns the status of the concrete object.

        Returns:
            True if the object is ready, False otherwise.
        """
        return self.is_ready

    # Information
    def get_description(self) -> str:
        """Returns an enhanced description including status.

        Returns:
            A string description.
        """
        base_desc = super().get_description()
        status = "Ready" if self.get_status() else "Not Ready"
        return f"{base_desc} - Status: {status}"
