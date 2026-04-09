# Anthony's Python Style Guide: Performance Tests

Use performance tests to measure execution time, memory usage, and other efficiency metrics of individual components.

### Rationale
Performance testing is required to identify regressions, validate optimizations, and ensure that implementations meet efficiency requirements.

Directives:
- Follow general style guidelines (naming, layout, docstrings) in all performance test code.
- Create performance tests for any module or class with a significant performance impact.
- Compare custom implementations against standard library equivalents or previous versions.

## Table of Contents

- [1 Directory Hierarchy](#1-directory-hierarchy)
- [2 Performance Test Structure](#2-performance-test-structure)
    - [2.1 Performance Test Classes](#21-performance-test-classes)
    - [2.2 Performance Test Methods](#22-performance-test-methods)
    - [2.3 Performance Test Suites](#23-performance-test-suites)
        - [2.3.1 Base Performance Test Suites](#231-base-performance-test-suites)
        - [2.3.2 Concrete Performance Test Suites](#232-concrete-performance-test-suites)
- [3 Performance Test Semantics and Syntax](#3-performance-test-semantics-and-syntax)
    - [3.1 Benchmarking](#31-benchmarking)
    - [3.2 Comparison Methodology](#32-comparison-methodology)
    - [3.3 Measurement and Reporting](#33-measurement-and-reporting)
- [4 Common Patterns](#4-common-patterns)
    - [4.1 Comparing with Standard Library](#41-comparing-with-standard-library)
    - [4.2 Comparing Implementation Variants](#42-comparing-implementation-variants)
    - [4.3 Measuring Overhead](#43-measuring-overhead)


## 1 Directory Hierarchy

Organize performance tests within a structure that separates them from functional unit tests.

### Rationale
A dedicated performance directory is required to prevent performance-heavy tests from slowing down the primary unit test suite.

Directives:
- Place performance base suites in the package source under `testsuite/`.
- Organize concrete performance tests in a `performance/` subdirectory within the corresponding module's test directory.
- Name performance test files with a `_performance.py` suffix.

Example:
```
src/
+-- baseobjects/                # The main source package
    +-- testsuite/
    �   +-- bases/
    �   �   +-- __init__.py
    �   �   +-- basetestsuite.py
    �   �   +-- baseperformancetestsuite.py
    �   �   +-- ...
    �   +-- __init__.py
    �   +-- objecttestsuite.py
    �   +-- objectperformancetestsuite.py
    �   +-- ...
    +-- ...
```

Ensure Concrete Performance Tests and performance tests for individual or specific components follow a specific directory structure to separate them from regular unit tests:

- Create a corresponding `performance` directory in the `tests` directory for each module.
- Place performance tests for a module in the corresponding `performance` directory.
- Start filenames with a descriptive name followed by `_performance` (e.g., `name_performance.py`).
- Use additional files to contain fixtures, test doubles, performance base classes, or other performance-specific code.

Example:
```
tests/
+-- bases/                          # Tests for the bases package
�   +-- performance/                # Performance tests for the bases package
�   �   +-- baseobject_performance.py
�   �   +-- basecallable_performance.py
�   �   +-- ...
�   +-- ...
+-- cachingtools/
    +-- performance/
    �   +-- ...
    +-- ...
```


## 2 Performance Test Structure

Follow the structure established in [Unit Tests](unit_tests.md) for performance tests.

### 2.1 Performance Test Classes

Use classes to group related performance benchmarks.

### Rationale
Structured performance classes are required to manage benchmark parameters, such as iteration counts and speed tolerances, consistently across multiple tests.

Directives:
- Define comparison objects from the standard library or alternative implementations.
- Set performance-specific attributes (e.g., `timeit_runs`, `speed_tolerance`) at the class level.

### 2.2 Performance Test Methods

Design methods to measure a specific performance metric.

### Rationale
Granular measurement methods are required to isolate bottlenecks and provide clear, actionable feedback on performance changes.

Directives:
- Focus on a single aspect (e.g., speed, memory).
- Include assertions that verify metrics against defined thresholds.
- Provide detailed reporting for analysis upon failure.

Example:
```python # pseudocode
def test_copy_speed(self, test_object: BaseObject) -> None:
    """Test the performance of the copy method of BaseObject.

    This test compares the speed of BaseObject.copy() with the standard copy.copy() function.

    Args:
        test_object: A fixture providing a BaseObject instance.
    """
    normal = self.NormalObject()

    def normal_copy() -> None:
        copy.copy(normal)

    # Calculate the mean time in microseconds for the new implementation
    new_time = timeit.timeit(test_object.copy, number=self.timeit_runs)
    mean_new = new_time / self.timeit_runs * 1000000

    # Calculate the mean time in microseconds for the old implementation
    old_time = timeit.timeit(normal_copy, number=self.timeit_runs)
    mean_old = old_time / self.timeit_runs * 1000000
    percent = (mean_new / mean_old) * 100

    # Print the performance comparison
    print(f"\nNew: {mean_new:.3f} �s ({percent:.3f}% of old function time)")
    assert percent < self.speed_tolerance
```

### 2.3 Performance Test Suites

Use performance test suites to group related tests that evaluate the efficiency of a specific component or feature.

### Rationale
Hierarchical test suites are required to maintain a consistent testing pattern while building complex, scalable performance validation logic.

Directives:
- Inherit from general base suites to share common benchmarks.
- Use `BasePerformanceTestSuite` as the foundation for all performance suites.
- Follow naming conventions: `Base<Component>PerformanceTestSuite` for generic suites and `<Component>PerformanceTestSuite` for specific implementations.

#### 2.3.1 Base Performance Test Suites

Define abstract and concrete methods in base suites to establish mandatory performance benchmarks.

### Rationale
Base suites are required to enforce that all subclasses implement essential performance checks and use consistent measurement techniques.

Directives:
- Use abstract methods when implementation details depend on the specific target.
- Use concrete methods for benchmarks shared across all subclasses.
- Establish a clear test target (e.g., `UnitTestClass`).

Example:
```python # pseudocode
class WrapperPerformanceTestSuite(BasePerformanceTestSuite, BaseClassTestSuite):
    """A base test suite which assays the performance of wrapper classes.

    This is a base test suite that concrete subclasses implement abstract methods and assign attributes.

    Attributes:
        ConcreteOne: A class which the wrapper class will wrap.
        ConcreteTwo: A another class which the wrapper class will wrap.
        _base_time: The time it takes to run a simple function call for a baseline of 100 million iterations.
        call_speed: The baseline speed of a simple function call in microseconds.
        timeit_runs: The number of runs to use for timeit measurements.
        speed_tolerance: The maximum percentage of time a new implementation can take compared to the old one.
        UnitTestClass: The main wrapper class to be assayed.
    """
     # Class Definitions #
    class ExampleOne:
        """An example class for testing wrappers.

        This class has attributes and methods that can be wrapped by wrapper classes.
        """
        def __init__(self) -> None:
            """Initializes with attributes."""
            self.one = "one"
            self.two = "one"
            self.common = "example_one"

        def __eq__(self, other: Any) -> bool:
            """Always returns True for equality comparison."""
            return True

        def method(self) -> str:
            """Returns a string identifying this class.

            Returns:
                A string identifying this class.
            """
            return "one"

        def __str__(self) -> str:
            """Returns a string representation of this class."""
            return "ConcreteOne"

    class ExampleTwo:
        """Another example class for testing wrappers.

        This class has different attributes and methods than ConcreteOne.
        """
        def __init__(self) -> None:
            """Initializes with attributes."""
            self.one = "two"
            self.three = "two"
            self.common = "example_two"

        def function(self) -> str:
            """Returns a string identifying this class.

            Returns:
                A string identifying this class.
            """
            return "two"

        def __str__(self) -> str:
            """Returns a string representation of this class."""
            return "ConcreteTwo"

    # Attributes #
    speed_tolerance: int = 150

    UnitTestClass: Any = None

    # Instance Methods #
    # Fixtures
    @abstractmethod
    @pytest.fixture
    def test_object(self) -> Any:
        """Creates a test object.

        Returns:
            A wrapper object with ConcreteOne and ConcreteTwo objects.
        """
        # This is abstract because each subclass needs to create a specific instance
        # of the wrapper class being tested, which requires knowledge of that specific class.

    @pytest.fixture
    def test_example_one(self) -> ExampleOne:
        """Creates a test ConcreteOne object.

        Returns:
            An ConcreteOne object.
        """
        # This is concrete because it can be implemented in a general way that works
        # for all subclasses. The ConcreteOne class is defined in this test suite.
        return self.ExampleOne()

    @pytest.fixture
    def test_example_two(self) -> ExampleTwo:
        """Creates a test ConcreteTwo object.

        Returns:
            An ConcreteTwo object.
        """
        # This is concrete because it can be implemented in a general way that works
        # for all subclasses. The ConcreteTwo class is defined in this test suite.
        return self.ExampleTwo()

    # Tests
    @abstractmethod
    def test_instance_creation(self, *args: Any, **kwargs: Any) -> None:
        """Tests that instances of the class can be created.

        This is an abstract method that must be implemented by subclasses.

        Args:
            *args: Positional arguments list to pass to the class constructor.
            **kwargs: Keyword arguments to pass to the class constructor.
        """
        # This is abstract because different wrapper classes have different constructor
        # signatures and initialization requirements.

    def test_attribute_access_speed(self, test_wrapper: Any, test_example_one: ExampleOne) -> None:
        """Tests the performance of attribute access through DynamicWrapper.

        This test compares the speed of accessing attributes through DynamicWrapper with direct attribute access.

        Args:
            test_wrapper: A fixture providing a DynamicWrapperTestObject.
            test_example_one: A fixture providing an ConcreteOne object.
        """
        # This is concrete because the attribute access performance test can be implemented
        # in a general way that works for all wrapper classes. The test measures the overhead
        # of accessing attributes through the wrapper compared to direct access, which is a
        # common performance concern for all wrapper classes.
        def wrapper_access() -> None:
            _ = test_wrapper.one
            _ = test_wrapper.two
            _ = test_wrapper.common

        def direct_access() -> None:
            _ = test_example_one.one
            _ = test_example_one.two
            _ = test_example_one.common

        # Calculate the mean time in microseconds for the wrapper access
        new_time = timeit.timeit(wrapper_access, number=self.timeit_runs)
        mean_new = new_time / self.timeit_runs * 1000000

        # Calculate the mean time in microseconds for direct access
        old_time = timeit.timeit(direct_access, number=self.timeit_runs)
        mean_old = old_time / self.timeit_runs * 1000000
        percent = (mean_new / mean_old) * 100

        # Print the performance comparison
        print(f"\n{self.UnitTestClass.__name__} attribute access: {mean_new:.3f} �s ({percent:.3f}% of direct access time)")
        assert percent < self.speed_tolerance

```

#### 2.3.2 Concrete Performance Test Suites

Concrete Performance Test Suites are subclasses of Base Performance Test Suites and focus on validating tests defined by the Base Performance Test Suite and creating tests that pertain only to a specific test target. Ensure Concrete Performance Test Suites follow the general test suite guidelines in [Unit Tests](unit_tests.md).

Guidelines:
- Inherit from a Base Performance Test Suite.
- Name with a `Performance` suffix.

Example:

```python # pseudocode
# Classes #
ExampleOne = WrapperPerformanceTestSuite.ConcreteOne
ExampleTwo = WrapperPerformanceTestSuite.ConcreteTwo


class DynamicWrapperTestObject(DynamicWrapper):
    """A test class that inherits from DynamicWrapper.

    This class uses DynamicWrapper to wrap ConcreteOne and ConcreteTwo objects.
    """
    _wrapped = ["_first", "_second"]

    def __init__(self, first: ExampleOne | None = None, second: ExampleTwo | None = None) -> None:
        """Initializes with wrapped objects.

        Args:
            first: The first object to wrap.
            second: The second object to wrap.
        """
        self._first = first
        self._second = second
        self.two = "wrapper"
        self.four = "wrapper"

    def wrap(self) -> str:
        """Returns a string identifying this class.

        Returns:
            A string identifying this class.
        """
        return "wrapper"


class TestDynamicWrapperPerformance(WrapperPerformanceTestSuite):
    """A base test suite which assays the performance of wrapper classes.

    This is a base test suite that concrete subclasses implement abstract methods and assign attributes.

    Attributes:
        ConcreteOne: A class which the wrapper class will wrap.
        ConcreteTwo: A another class which the wrapper class will wrap.
        _base_time: The time it takes to run a simple function call for a baseline of 100 million iterations.
        call_speed: The baseline speed of a simple function call in microseconds.
        timeit_runs: The number of runs to use for timeit measurements.
        speed_tolerance: The maximum percentage of time a new implementation can take compared to the old one.
        UnitTestClass: The main wrapper class to be assayed.
    """

    # Attributes #
    speed_tolerance: int = 150
    UnitTestClass: Any = DynamicWrapperTestObject

    # Instance Methods #
    # Fixtures
    @pytest.fixture
    def test_object(self) -> Any:
        """Creates a test object.

        Returns:
            A wrapper object with ConcreteOne and ConcreteTwo objects.
        """
        # This concrete implementation satisfies the abstract fixture requirement from the parent class.
        # It provides a specific implementation for creating a DynamicWrapperTestObject instance.
        # The implementation is specific to this test suite because it knows how to create and
        # initialize a DynamicWrapperTestObject with the appropriate wrapped objects.
        first = self.ExampleOne()
        second = self.ExampleTwo()
        return self.DynamicWrapperTestObject(first, second)

    # Tests
    def test_instance_creation(self, *args: Any, **kwargs: Any) -> None:
        """Tests that instances of the class can be created.

        Args:
            *args: Positional arguments list to pass to the class constructor.
            **kwargs: Keyword arguments to pass to the class constructor.
        """
        # This concrete implementation satisfies the abstract method requirement from the parent class.
        # It provides a specific implementation for testing DynamicWrapperTestObject instance creation.
        # The implementation is specific to this test suite because it knows the constructor signature
        # and initialization requirements of the DynamicWrapperTestObject class.
        instance = self.UnitTestClass()
        assert isinstance(instance, self.UnitTestClass)

    def test_setattr_vs_normal_set_speed(self, test_wrapper: DynamicWrapperTestObject) -> None:
        """Tests the performance difference between _setattr and normal attribute setting.

        This test compares the speed of setting attributes using _setattr with normal attribute setting.

        Args:
            test_wrapper: A fixture providing a DynamicWrapperTestObject.
        """

        # This is a concrete method that is specific to this test suite and not required by the parent class.
        # It tests a specific feature of the DynamicWrapperTestObject class (_setattr method) that may not
        # be present in all wrapper classes. This shows how concrete test suites can add additional tests
        # that are specific to the class being tested.
        def setattr_method() -> None:
            test_wrapper._setattr("one", "test")

        def normal_set() -> None:
            test_wrapper.one = "test"

        # Calculate the mean time in microseconds for _setattr
        new_time = timeit.timeit(setattr_method, number=self.timeit_runs)
        mean_new = new_time / self.timeit_runs * 1000000

        # Calculate the mean time in microseconds for normal set
        old_time = timeit.timeit(normal_set, number=self.timeit_runs)
        mean_old = old_time / self.timeit_runs * 1000000
        percent = (mean_new / mean_old) * 100

        # Print the performance comparison
        print(f"\n_setattr method: {mean_new:.3f} �s ({percent:.3f}% of normal set time)")
        # No assertion here, just measuring relative performance

```


## 3 Performance Test Semantics and Syntax

Follow established patterns for benchmarking and comparison to ensure reliable results.

### Rationale
Accurate benchmarking is required to identify minor performance variations that could indicate regressions or successful optimizations.

### 3.1 Benchmarking

Use the `timeit` module for high-precision timing of small code snippets.

### Rationale
High-precision timing is required to accurately detect performance changes.

Directives:
- Use a sufficient number of iterations (defined in `timeit_runs`).
- Report times in microseconds.
- Calculate and report percentage comparisons between implementations.

### 3.2 Comparison Methodology

Compare custom implementations against standard library baselines or previous versions.

### Rationale
Relative comparisons are recommended to account for hardware differences and provide a clear measure of impact.

Directives:
- Ensure compared operations are truly equivalent.
- Use identical input data for all implementations.
- Isolate the specific operation being tested.

Example:
```python # pseudocode
def normal_copy() -> None:
    copy.copy(normal)

# vs.

test_object.copy()
```

### 3.3 Measurement and Reporting

Ensure that performance metrics are reported clearly.

### Rationale
Standardized reporting is required to facilitate the analysis of performance data across different environments and test runs.

Directives:
- Print the mean execution time in microseconds.
- Include the percentage comparison to the reference implementation.
- Use `speed_tolerance` to define the maximum acceptable performance degradation.
- Provide detailed performance information for debugging.

Example:
```python # pseudocode
# Calculate the mean time in microseconds for the new implementation
new_time = timeit.timeit(test_object.copy, number=self.timeit_runs)
mean_new = new_time / self.timeit_runs * 1000000

# Calculate the mean time in microseconds for the old implementation
old_time = timeit.timeit(normal_copy, number=self.timeit_runs)
mean_old = old_time / self.timeit_runs * 1000000
percent = (mean_new / mean_old) * 100

# Print the performance comparison
print(f"\nNew: {mean_new:.3f} �s ({percent:.3f}% of old function time)")
```


## 4 Common Patterns

Use established patterns for common performance testing scenarios.

### Rationale
Consistent testing patterns are required to ensure that benchmarks are comparable and that common pitfalls are avoided.

### 4.1 Comparing with Standard Library

Benchmark custom implementations against their standard library counterparts.

### Rationale
This comparison is recommended to justify the existence of custom code and ensure it provides a tangible performance benefit.

```python # pseudocode
def test_copy_speed(self, test_object):
    """Tests the performance of the copy method of BaseObject."""
    normal = self.NormalObject()

    def normal_copy():
        copy.copy(normal)

    # Compare custom implementation with standard library
    new_time = timeit.timeit(test_object.copy, number=self.timeit_runs)
    old_time = timeit.timeit(normal_copy, number=self.timeit_runs)
    # ...
```

### 4.2 Comparing Implementation Variants

Evaluate the performance of different internal implementations.

### Rationale
Comparing variants is required to select the most efficient implementation for a specific use case.

```python # pseudocode
def test_copy_vs_dunder_copy(self, test_object):
    """Tests the performance difference between copy() and __copy__() methods."""
    # Compare two different implementations
    copy_time = timeit.timeit(test_object.copy, number=self.timeit_runs)
    dunder_time = timeit.timeit(test_object.__copy__, number=self.timeit_runs)
    # ...
```

### 4.3 Measuring Overhead

Measure the overhead introduced by wrappers, decorators, or other abstractions.

### Rationale
Quantifying overhead is recommended to ensure that abstractions do not unacceptably degrade performance.

```python # pseudocode
def test_attribute_access_speed(self, test_object):
    """Tests the performance of attribute access in BaseObject."""
    normal = self.NormalObject()

    def access_base_attr():
        _ = test_object.immutable
        _ = test_object.mutable

    def access_normal_attr():
        _ = normal.immutable
        _ = normal.mutable

    # Measure overhead of BaseObject attribute access
    base_time = timeit.timeit(access_base_attr, number=self.timeit_runs)
    normal_time = timeit.timeit(access_normal_attr, number=self.timeit_runs)
    # ...
```

Following these guidelines ensures that developers create effective performance tests that help maintain the efficiency and reliability of the codebase.
