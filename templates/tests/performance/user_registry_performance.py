#!/usr/bin/env python
"""registry_performance.py
Starter template for creating runnable performance tests.

This module provides a template for creating performance tests that can be run using pytest. It includes a basic test
case that measures the performance of creating a registry against a baseline (e.g., list comprehension).
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
from templatepackage.user_registry import create_registry


# Definitions #
# Constants #
_SECTION_LINE: Final[str] = "-" * 72


# Tests #
class TestRegistryPerformance(BasePerformanceTestSuite):
    """Benchmarks UserRegistry.

    Attributes:
        timeit_runs: Number of iterations per timing sample.
        speed_tolerance: Acceptable percent-of-baseline overhead.
    """

    # Attributes #
    timeit_runs: int = 100  # Adjust based on the cost of the operation.
    speed_tolerance: float = 200.0

    # Instance Methods #
    # Tests
    def test_registry_creation_performance(self) -> None:
        """Benchmarks registry creation against a baseline (e.g., list comprehension)."""
        names = [f"user_{i}" for i in range(1000)]

        def new_impl() -> None:
            """Creates a registry."""
            create_registry(names)

        def baseline_impl() -> None:
            """Just creates User objects in a list."""
            # Simulating overhead of just creating User objects without Registry wrapper
            # Source Packages #
            from templatepackage.user import User
            [User(user_id=n, name=n) for n in names]

        # Measure mean time in microseconds
        new_total = timeit.timeit(new_impl, number=self.timeit_runs)
        baseline_total = timeit.timeit(baseline_impl, number=self.timeit_runs)

        mean_new_us = new_total / self.timeit_runs * 1_000_000
        mean_base_us = baseline_total / self.timeit_runs * 1_000_000

        percent_of_baseline = (mean_new_us / mean_base_us) * 100 if mean_base_us else float("inf")

        # Report
        print(
            f"\n{_SECTION_LINE}\n"
            f"UserRegistry creation vs raw list\n"
            f"mean_new:   {mean_new_us:10.3f} μs\n"
            f"mean_base:  {mean_base_us:10.3f} μs\n"
            f"percent:    {percent_of_baseline:10.3f}% of baseline\n"
            f"tolerance:  {self.speed_tolerance:10.3f} (percent ceiling)\n"
            f"{_SECTION_LINE}\n"
        )

        # Assertion: creation shouldn't be vastly slower than just list creation
        assert percent_of_baseline < self.speed_tolerance


# Main #
if __name__ == "__main__":
    pytest.main(["-v", "-s"])
