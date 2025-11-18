#!/usr/bin/env python
"""example_template.py
Starter template for creating runnable examples under the examples/ directory.

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
from contextlib import suppress
from dataclasses import dataclass
from typing import Final

# Third‑Party Packages #
# (Examples import project packages as "Source Packages" below; usually no third‑party here.)

# Source Packages #
# Import from the project under demonstration here (treat as third‑party for examples)
# from baseobjects.<area> import <Thing>


# Utilities #
_SECTION_LINE: Final[str] = "-" * 72


def _print_heading(title: str) -> None:
    """Pretty prints a section heading for example output."""
    print(f"\n{title}\n{_SECTION_LINE}")


# Example Domain Fixtures (replace or remove as needed) #
@dataclass(slots=True)
class DemoItem:
    """Tiny domain object used by the example code.

    In real examples, this class would be replaced with objects from the
    package under demonstration.
    """

    name: str
    value: int = 0

    def bump(self, n: int = 1) -> int:
        self.value += n
        return self.value


# Example Sections #
def basic_usage_example() -> None:
    """The most common, happy‑path usage is shown in a few lines."""
    _print_heading("Basic Usage")

    # Setup
    item = DemoItem(name="demo", value=1)
    print(f"Created: {item!r}")

    # Action
    new_value = item.bump()
    print(f"After bump: {new_value}")

    # Simple verification (examples may use light assertions)
    assert new_value == 2, "Expected value to increment by 1"


def advanced_usage_example() -> None:
    """A slightly more advanced or less common pattern is demonstrated."""
    _print_heading("Advanced Usage")

    item = DemoItem(name="demo-advanced", value=10)
    print(f"Start: value={item.value}")

    # Multiple operations
    for step in (1, 2, 3):
        print(f" bump(+{step}) -> {item.bump(step)}")

    # Optional: demonstrate a controlled error for learning
    print("\nIntentional error demonstration (caught):")
    with suppress(AssertionError):
        assert item.value == 10, "This will fail and be suppressed"
        # The above is suppressed to keep the example runnable and readable


def edge_cases_example() -> None:
    """Noteworthy edge cases are highlighted succinctly."""
    _print_heading("Edge Cases")

    item = DemoItem(name="edge", value=0)
    print(f"Initial: {item}")

    # Example edge: zero/negative increments
    for step in (0, -1):
        before = item.value
        after = item.bump(step)
        print(f" bump({step:+}) from {before} -> {after}")


# Main #
if __name__ == "__main__":  # pragma: no cover - examples are user‑run
    basic_usage_example()
    advanced_usage_example()
    edge_cases_example()
