"""enums.py
Template module demonstrating the structure and style of enumerations.

This module provides a template for defining enumerations using the `enum` module. It demonstrates standard `Enum` usage
as well as `IntEnum` or `StrEnum` (Python 3.11+) where appropriate.
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
import sys
from enum import Enum, auto

if sys.version_info >= (3, 11):
    from enum import StrEnum
else:
    # Fallback for Python < 3.11
    class StrEnum(str, Enum):
        """A string enumeration fallback for Python < 3.11."""


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


class Color(StrEnum):
    """Enumeration of supported colors.

    Attributes:
        RED: 'red'
        GREEN: 'green'
        BLUE: 'blue'
    """
    RED = "red"
    GREEN = "green"
    BLUE = "blue"
