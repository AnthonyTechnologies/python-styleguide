"""enum_template.py
Template module demonstrating the structure and style of enumerations.

This module provides a template for defining enumerations using the `enum` module. It demonstrates standard `Enum` usage
as well as `IntEnum` or `StrEnum` (Python 3.11+) where appropriate.
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
from enum import Enum, auto


# Definitions #
# Classes #
class UserRole(Enum):
    """Enumeration of User roles in the system.

    Attributes:
        ADMIN: Administrator with full access.
        EDITOR: Can edit content.
        VIEWER: Read-only access.
    """
    ADMIN = auto()
    EDITOR = auto()
    VIEWER = auto()


class Color(str, Enum):
    """Enumeration of supported colors (String implementation).

    Attributes:
        RED: 'red'
        GREEN: 'green'
        BLUE: 'blue'
    """
    RED = "red"
    GREEN = "green"
    BLUE = "blue"
