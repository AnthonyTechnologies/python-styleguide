#!/usr/bin/env python
"""unit_test_template.py
Starter template for creating runnable unit tests under the examples/ directory.

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
from typing import Any, Final, Protocol
import copy

# Third-Party Packages #
from baseobjects.testsuite import BaseObjectTestSuite
import pytest

# Local Packages #
# Import from the project under test. Keep imports local to tests where reasonable.
# Example (replace with your targets):
# from src.package.bases import PackageObject
# from src.package.testsuite import PackageObjectTestSuite


# Definitions #
# Constants and Test Data #
_SECTION_LINE: Final[str] = "-" * 72


# Local Test Utilities (Optional) #
@dataclass(slots=True)
class _Sample:
    """Small helper object for illustrative tests. This helper may be replaced or removed as needed."""

    name: str
    value: int = 0

    def bump(self, n: int = 1) -> int:
        """Increase value by n and return the new value."""
        self.value += n
        return self.value


class _SupportsCopy(Protocol):  # Example Protocol for typing in tests
    """Protocol specifying shallow and deep copy support for types used in tests."""

    def __copy__(self) -> Any:
        """Return a shallow copy of the object."""
        ...

    def __deepcopy__(self, memo: dict[int, Any]) -> Any:
        """Return a deep copy of the object, using memo to avoid recursion."""
        ...


# Fixtures #
@pytest.fixture(scope="module")
def sample_items() -> list[_Sample]:
    """Module-scoped fixture providing reusable test data.

    Returns:
        A list of _Sample items.
    """

    return [_Sample("a", 1), _Sample("b", 2)]


@pytest.fixture()
def fresh_sample() -> _Sample:
    """Function-scoped fixture yielding a fresh _Sample each time."""

    return _Sample("fresh", 0)


# Tests #
class TestModuleLevelBehaviors:
    """Free-form tests that don't require a test suite base class.

    For projects using custom Base Test Suites (see src/.../testsuite), prefer subclassing an appropriate base class as
    shown in the next example class.
    """

    def test_basic_assertions(self, fresh_sample: _Sample) -> None:
        """Demonstrates a simple, focused test."""

        before = fresh_sample.value
        after = fresh_sample.bump()

        assert after == before + 1

    @pytest.mark.parametrize("delta", [0, 1, 2])
    def test_parametrized_behavior(self, delta: int, fresh_sample: _Sample) -> None:
        """Shows pytest parametrization for concise coverage."""

        result = fresh_sample.bump(delta)
        assert result == delta


# Example of a Test Suite derived from a base testsuite
class TestMyType(BaseObjectTestSuite):
    """Concrete Test Suite for <MyType>, extending a Base Test Suite.

    In practice, BaseObjectTestSuite is replaced with the domain‑appropriate base suite from src/.../testsuite, and
    TestClass is set to the class under test.
    """

    # Target type under test
    TestClass: type[BaseObject] = MyType  # noqa: F821  # replace MyType

    # Optionally override or extend specific tests defined by the base suite
    def test_copy(self, test_object: BaseObject) -> None:  # noqa: F821
        """Ensures that copy.copy creates a distinct instance of the correct type."""
        obj_copy = copy.copy(test_object)
        assert obj_copy is not test_object
        assert isinstance(obj_copy, self.TestClass)

    # Add new tests specific to this implementation
    def test_special_case(self, test_object: BaseObject) -> None:  # noqa: F821
        """Validates an implementation-specific edge case behavior."""
        # Implement validation for an implementation-specific edge case
        assert True


# Main #
if __name__ == "__main__":
    pytest.main(["-v", "-s"])
