"""module_template.py
A one-line summary of the module or program, terminated by a period.

Leave one blank line. The rest of this docstring should contain an overall description of the module or program. The
description can be broken up into multiple paragraphs to present the functionality into logical sections. Bullet-point
and numerical lists may be used as well, but only add them if they are needed.
"""

# Header #
__package_name__ = "package_name"

__author__ = "Author Name"
__credits__ = ["Author Name"]
__copyright__ = "Copyright 2021, Author Name"
__license__ = "License"

__version__ = "0.1.0"


# Imports #
# Standard Libraries #
from dataclasses import dataclass
from typing import ClassVar

# Third-Party Libraries #
# import requests

# Project Libraries #
# from . import helpers


# Definitions #
# Constants #
EXAMPLE_CONSTANT: int = 42  # The canonical answer for demonstration purposes.


# Functions #
def _validate_inputs(x: int) -> None:
    """Validates inputs for public API functions in this module.

    Args:
        x: A non-negative integer.

    Raises:
        ValueError: If the input is invalid.
    """
    if x < 0:
        raise ValueError("x must be non-negative")


def public_function(x: int) -> str:
    """Example public function.

    Args:
        x: A non-negative integer.

    Returns:
        A human‑readable message for the given input.

    Raises:
        ValueError: If ``x`` is negative.
    """
    _validate_inputs(x)
    return f"value={x}"


# Classes #
@dataclass(slots=True)
class PublicClass:
    """Example class.

    Attributes:
        name: The display name.
        count: Number of items managed by this instance.
    """

    name: str
    count: int = 0

    def increment(self, n: int = 1) -> int:
        """Increases count by n.

        Args:
            n: Amount to increment.

        Returns:
            The updated count.
        """
        self.count += n
        return self.count


# Additional Definitions #
# Circular References #
# Note: Use this section for forward references that cannot be resolved earlier.
# Example:
# OtherType = "PublicClass"  # type: ignore[assignment]

# Registration #
# Note: Use this section to register classes/functions to external registries.
# Example:
# registry.register("public_class", PublicClass)
