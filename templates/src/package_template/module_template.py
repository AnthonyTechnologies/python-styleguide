"""module_template.py
Template module demonstrating the overall structure of a general Python module file.

This module provides a template for a general-purpose Python module, including imports, constants, function
definitions, and class definitions. It serves as a guide for organizing code within a module to ensure consistency
and readability. Typically, in a project a module file will either be a class definition or a function definition,
but this template can be used for any type of module or a complex module containing multiple components.
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
from dataclasses import dataclass

# Local Packages #
from .class_template import User
from .function_template import normalize_names


# Definitions #
# Constants #
EXAMPLE_CONSTANT: int = 42  # The canonical answer for demonstration purposes.


# Functions #
def create_registry(names: list[str]) -> "UserRegistry":
    """Creates a registry from a list of names.

    Args:
        names: List of usernames.

    Returns:
        A new UserRegistry containing users with the given names.
    """
    users = [User(user_id=name.lower(), name=name) for name in names]
    return UserRegistry(users=users)


# Classes #
@dataclass(slots=True)
class UserRegistry:
    """Manages a collection of users.

    Attributes:
        users: The list of managed users.
    """

    # Attributes #
    users: list[User]

    # Instance Methods #
    def get_all_names(self) -> list[str]:
        """Returns normalized names of all users.

        Returns:
            A list of normalized names.
        """
        return normalize_names(u.name for u in self.users)

    def add_user(self, user: User) -> None:
        """Adds a user to the registry.

        Args:
            user: The user to add.
        """
        self.users.append(user)


# Additional Definitions #
# Circular References #
# Note: Use this section for forward references that cannot be resolved earlier.
# Example:
# OtherType = "PublicClass"  # type: ignore[assignment]

# Registration #
# Note: Use this section to register classes/functions to external registries.
# Example:
# registry.register("public_class", PublicClass)
