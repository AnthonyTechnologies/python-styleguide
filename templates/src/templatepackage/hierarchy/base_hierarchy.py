"""base_hierarchy.py
Template module demonstrating a base class within a complex hierarchy.

This module provides a base class that serves as the root for a more complex class hierarchy, demonstrating common
attributes and methods shared across all related classes.
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


# Definitions #
# Classes #
class BaseHierarchy:
    """The root class for the hierarchy.

    This class provides basic functionality and attributes that are common to all classes in this submodule's hierarchy.
    In a real project, this might inherit from `baseobjects.bases.BaseObject`.

    Attributes:
        name: A name for the hierarchy object.
    """

    # Class Magic Methods #
    # Construction/Destruction
    def __init__(self, name: str) -> None:
        """Initializes the BaseHierarchy object.

        Args:
            name: The name of the object.
        """
        self.name: str = name

    # Representation
    def __repr__(self) -> str:
        """Returns a string representation of the object.

        Returns:
            A string representation.
        """
        return f"<{self.__class__.__name__}(name={self.name!r})>"

    # Instance Methods #
    # Information
    def get_description(self) -> str:
        """Returns a description of the object.

        Returns:
            A string description.
        """
        return f"Hierarchy object named {self.name}"
