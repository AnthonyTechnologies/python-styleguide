#!/usr/bin/env python
"""hierarchy_example.py
Template module demonstrating how to write example scripts for a subpackage hierarchy.
"""

# Header #
__package_name__ = "templatepackage"

__author__ = "Author Name"
__credits__ = ["Author Name"]
__copyright__ = "Copyright 2021, Author Name"
__license__ = "License"

__version__ = "0.1.0"


# Imports #
# Third-Party Packages #
from templatepackage.hierarchy.concrete_hierarchy import ConcreteHierarchy


# Definitions #
# Example Sections #
def hierarchy_usage_example() -> None:
    """Demonstrates the usage of a concrete hierarchy implementation."""
    print(f"\nHierarchy Usage\n{'-' * 72}")

    # Setup
    hierarchy = ConcreteHierarchy(name="ExampleHierarchy")
    print(f"Created hierarchy: {hierarchy}")

    # Action
    print(f"Hierarchy name: {hierarchy.name}")


# Main #
if __name__ == "__main__":  # pragma: no cover - examples are user-run
    hierarchy_usage_example()
