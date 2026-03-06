"""hierarchy_mixin.py
Template module demonstrating a mixin class within a hierarchy.

This module provides a mixin class that can be added to hierarchy classes to provide additional common functionality.
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
from typing import Any


# Definitions #
# Classes #
class HierarchyMixin:
    """A mixin for the hierarchy.

    This mixin provides utility methods that can be shared across multiple concrete implementations in the hierarchy.
    """

    # Instance Methods #
    # Processing
    def process_data(self, data: Any) -> Any:
        """Processes data using a generic mixin method.

        Args:
            data: The data to process.

        Returns:
            The processed data.
        """
        return f"Processed: {data}"

    # Utility
    def get_mixin_info(self) -> str:
        """Returns information about this mixin.

        Returns:
            A string indicating the mixin's presence.
        """
        return "HierarchyMixin is present."
