"""base_template.py
Template module demonstrating the structure and style of an abstract base class.

This module provides a template for defining abstract base classes (ABCs) using the `abc` module. It demonstrates the
use of `@abstractmethod` to enforce implementation in subclasses and organization of the base class.
"""

# Header #
__package_name__ = "package_template"

__author__ = "Author Name"
__credits__ = ["Author Name"]
__copyright__ = "Copyright 2021, Author Name"
__license__ = "License"

__version__ = "0.1.0"


# Imports #
# Standard Libraries #
from abc import ABC, abstractmethod


# Definitions #
# Classes #
class BaseUser(ABC):
    """Abstract base class for a User.

    This class defines the interface that all User-like objects must implement.
    """

    # Class Magic Methods #
    # Construction/Destruction
    def __init__(self) -> None:
        """Initializes the BaseUser."""
        super().__init__()

    # Instance Methods #
    # Operations
    @abstractmethod
    def get_id(self) -> str:
        """Returns the unique identifier for the user.

        Returns:
            The user ID as a string.
        """
        pass

    @abstractmethod
    def is_active(self) -> bool:
        """Checks if the user is currently active.

        Returns:
            True if active, False otherwise.
        """
        pass

    # Utility
    def display_info(self) -> str:
        """Returns a formatted string with user information.

        This is a concrete method providing common functionality calling abstract methods.

        Returns:
            Formatted string.
        """
        status = "Active" if self.is_active() else "Inactive"
        return f"User[{self.get_id()}]: {status}"
