#!/usr/bin/env python
"""performance_test_template.py
Starter template for creating runnable performance tests under the examples/ directory.

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
from typing import Final
import timeit

# Third-Party Packages #
from baseobjects.testsuite import BasePerformanceTestSuite
import pytest

# Source Packages #
# Import from the project under test. Keep imports local to tests where reasonable.
# Example targets (replace with your actual targets):
# from src.baseobjects.bases import BaseObject


# Definitions #
# Constants #
_SECTION_LINE: Final[str] = "-" * 72


# Tests #
class TestMyFeaturePerformance(BasePerformanceTestSuite):
    """Concrete performance test suite for <MyFeature>.

    The placeholder <MyFeature> represents the object/module intended for benchmarking.

    Common attributes used in repository performance tests:
    - timeit_runs: number of iterations per timing sample
    - speed_tolerance: acceptable percent-of-baseline overhead (lower is faster)
    """

    # Attributes #
    timeit_runs: int = 100000  # Adjust based on the cost of the operation
    speed_tolerance: float = 200.0  # Allow up to 2x of baseline unless stricter

    # Fixtures #
    @pytest.fixture()
    def sample_input(self) -> int:
        """Provides a small, deterministic input for micro-benchmarks."""

        return 42

    # Example benchmark comparing new vs baseline approaches
    def test_operation_performance(self, sample_input: int) -> None:
        """Benchmarks <operation> against a simple baseline.

        The inner functions below act as stand-ins for the concrete operations being measured. They remain minimal and
        self-contained so that timeit can invoke them directly.
        """

        # Define benchmarked callables (replace with real work)
        def new_impl() -> int:
            # Simulate the new or target implementation
            return (sample_input + 1) * 2

        def baseline_impl() -> int:
            # Simulate a baseline (e.g., stdlib or simpler approach)
            return (sample_input << 1) + 2

        # Measure mean time in microseconds
        new_total = timeit.timeit(new_impl, number=self.timeit_runs)
        baseline_total = timeit.timeit(baseline_impl, number=self.timeit_runs)

        mean_new_us = new_total / self.timeit_runs * 1_000_000
        mean_base_us = baseline_total / self.timeit_runs * 1_000_000

        percent_of_baseline = (mean_new_us / mean_base_us) * 100 if mean_base_us else float("inf")

        # Report (prints are common in repo perf tests for quick inspection)
        print(
            f"\n{_SECTION_LINE}\n"
            f"<MyFeature> operation vs baseline\n"
            f"mean_new:   {mean_new_us:10.3f} µs\n"
            f"mean_base:  {mean_base_us:10.3f} µs\n"
            f"percent:    {percent_of_baseline:10.3f}% of baseline\n"
            f"tolerance:  {self.speed_tolerance:10.3f} (percent ceiling)\n"
            f"{_SECTION_LINE}\n"
        )

        # Assertion: new implementation should be within tolerance of baseline
        assert percent_of_baseline < self.speed_tolerance


# Main #
if __name__ == "__main__":
    pytest.main(["-v", "-s"])
