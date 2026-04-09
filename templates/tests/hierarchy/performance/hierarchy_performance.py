#!/usr/bin/env python
"""hierarchy_performance.py
Template module demonstrating performance tests for a complex class hierarchy.

This module provides a template for measuring the performance of methods within a class hierarchy, focusing on the
overhead of various class levels and mixins.
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
import timeit
from typing import Final

# Third-Party Packages #
import pytest
from baseobjects.testsuite import BasePerformanceTestSuite

# Source Packages #
from templatepackage.hierarchy import BaseHierarchy, ConcreteHierarchy


# Definitions #
# Constants #
_SECTION_LINE: Final[str] = "-" * 72


# Tests #
class TestHierarchyPerformance(BasePerformanceTestSuite):
    """Benchmarks ConcreteHierarchy against BaseHierarchy.

    Attributes:
        timeit_runs: Number of iterations per timing sample.
        speed_tolerance: Acceptable percent-of-baseline overhead.
    """

    # Attributes #
    timeit_runs: int = 1000
    speed_tolerance: float = 150.0

    # Instance Methods #
    # Tests
    def test_description_performance(self) -> None:
        """Benchmarks the performance of description retrieval across hierarchy levels."""
        base_obj = BaseHierarchy(name="Base")
        concrete_obj = ConcreteHierarchy(name="Concrete")

        def test_concrete() -> None:
            """Calls description on the concrete object."""
            concrete_obj.get_description()

        def test_base() -> None:
            """Calls description on the base object (baseline)."""
            base_obj.get_description()

        # Measure mean time in microseconds
        concrete_total = timeit.timeit(test_concrete, number=self.timeit_runs)
        base_total = timeit.timeit(test_base, number=self.timeit_runs)

        mean_concrete_us = concrete_total / self.timeit_runs * 1_000_000
        mean_base_us = base_total / self.timeit_runs * 1_000_000

        percent_of_baseline = (mean_concrete_us / mean_base_us) * 100 if mean_base_us else float("inf")

        # Report
        print(
            f"\n{_SECTION_LINE}\n"
            f"Concrete vs Base description performance\n"
            f"mean_concrete: {mean_concrete_us:10.3f} μs\n"
            f"mean_base:     {mean_base_us:10.3f} μs\n"
            f"percent:       {percent_of_baseline:10.3f}% of baseline\n"
            f"tolerance:     {self.speed_tolerance:10.3f} (percent ceiling)\n"
            f"{_SECTION_LINE}\n"
        )

        # Assertion: performance should be within tolerance
        assert percent_of_baseline < self.speed_tolerance


# Main #
if __name__ == "__main__":
    pytest.main(["-v", "-s"])
