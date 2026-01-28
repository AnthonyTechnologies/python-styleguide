#!/usr/bin/env python
"""example_template.py
Template module demonstrating how to write example scripts.

This module provides a template for creating example scripts that demonstrate the usage of the package. It includes
basic, advanced, and edge-case usage examples to guide users on how to effectively use the library. Normally, the name
of this script should match the name of the function it contains, but it is named example_template to make it easier to
find when browsing the templates directory.
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
from typing import Final

# Third-Party Packages #
from package_template.class_template import User
from package_template.module_template import UserRegistry, create_registry


# Utilities #
_SECTION_LINE: Final[str] = "-" * 72


def _print_heading(title: str) -> None:
    """Pretty prints a section heading for example output."""
    print(f"\n{title}\n{_SECTION_LINE}")


# Example Sections #
def basic_usage_example() -> None:
    """Demonstrates the most common, happy‑path usage in a few lines."""
    _print_heading("Basic Usage")

    # Setup
    registry = create_registry(["Alice", "Bob"])
    print(f"Created registry: {registry}")

    # Action
    names = registry.get_all_names()
    print(f"Normalized names: {names}")

    # Simple verification
    assert "alice" in names
    assert "bob" in names


def advanced_usage_example() -> None:
    """Demonstrates a slightly more advanced or less common pattern."""
    _print_heading("Advanced Usage")

    # Manually creating and adding users
    registry = UserRegistry(users=[])
    u1 = User(user_id="u1", name="Charlie", active=True)
    u2 = User(user_id="u2", name="Dave", active=False)

    registry.add_user(u1)
    registry.add_user(u2)

    print(f"Registry users: {registry.users}")
    print(f"Normalized names: {registry.get_all_names()}")


def edge_cases_example() -> None:
    """Highlights noteworthy edge cases succinctly."""
    _print_heading("Edge Cases")

    # Empty registry
    registry = create_registry([])
    print(f"Empty registry names: {registry.get_all_names()}")

    # User with weird name
    u = User(user_id="u3", name="   Eve   ")
    registry.add_user(u)
    print(f"Names with whitespace: {registry.get_all_names()}")


# Main #
if __name__ == "__main__":  # pragma: no cover - examples are user‑run
    basic_usage_example()
    advanced_usage_example()
    edge_cases_example()
