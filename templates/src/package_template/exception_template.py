"""exception_template.py
Template module demonstrating the structure and style of custom exceptions.

This module provides a template for defining custom exceptions. It demonstrates the inheritance from built-in Exception
classes and the organization of exception classes within a module. Normally, the name of this module should match the
name of the exception it contains or be named `exceptions.py` if it contains multiple related exceptions.
"""

# Header #
__package_name__ = "package_template"

__author__ = "Author Name"
__credits__ = ["Author Name"]
__copyright__ = "Copyright 2021, Author Name"
__license__ = "License"

__version__ = "0.1.0"


# Definitions #
# Classes #
class TemplateError(Exception):
    """Base exception for the package_template package.

    This exception serves as a base class for all other exceptions in this package, allowing users to catch all
    package-specific errors with a single except block.

    Args:
        message: The error message.
        *args: Additional arguments.
    """
    
    # Magic Methods #
    # Construction/Destruction
    def __init__(self, message: str, *args: object) -> None:
        super().__init__(message, *args)


class ValidationError(TemplateError):
    """Raised when validation fails for an object or input.

    Attributes:
        value: The invalid value that caused the error.
    """

    # Attributes #
    value: object

    # Magic Methods #
    # Construction/Destruction
    def __init__(self, message: str, value: object, *args: object) -> None:
        """Initializes the ValidationError.

        Args:
            message: The error message.
            value: The invalid value.
            *args: Additional arguments.
        """
        super().__init__(message, *args)
        self.value = value
