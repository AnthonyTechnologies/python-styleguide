"""logger.py
Template module demonstrating standardized logging patterns.

This module provides a template for setting up and using a module-level logger following the project's style guide,
including the use of the `msg` variable pattern and pattern-strings with %-placeholders.
"""

# Header #
__package_name__ = "templatepackage"

__author__ = "Author Name"
__credits__ = ["Author Name"]
__copyright__ = "Copyright 2026, Author Name"
__license__ = "License"

__version__ = "0.1.0"


# Imports #
# Standard Libraries #
import logging
from typing import Any


# Definitions #
# Global Variables #
# Module-level logger is the preferred pattern.
logger = logging.getLogger(__name__)


# Functions #
def log_user_action(user_id: str, action: str, details: dict[str, Any] | None = None) -> None:
    """Logs a user action with metadata.

    This function demonstrates the `msg` variable pattern and the use of %-placeholders for logging.

    Args:
        user_id: The ID of the user performing the action.
        action: The action performed.
        details: Optional additional metadata.
    """
    msg = "User %s performed action: %s"
    logger.info(msg, user_id, action)

    if details:
        msg = "Action details for user %s: %r"
        logger.debug(msg, user_id, details)


def handle_error(user_id: str, error: Exception) -> None:
    """Handles and logs an error.

    Args:
        user_id: The user ID associated with the error.
        error: The caught exception.
    """
    msg = "An error occurred for user %s: %s"
    logger.error(msg, user_id, error, exc_info=True)


# Main #
if __name__ == "__main__":
    # Basic configuration for demonstration (normally configured at the application root)
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    log_user_action("user_123", "login")
    log_user_action("user_123", "update_profile", details={"field": "email"})

    try:
        msg = "Invalid configuration"
        raise ValueError(msg)
    except ValueError as e:
        handle_error("user_123", e)
