# Anthony's Python Style Guide: Performance Tests

Performance testing is a critical aspect of software development that ensures code not only functions correctly but also
executes efficiently. These tests help identify performance regressions, validate optimizations, and ensure that
implementations meet performance requirements.

The performance tests in this guide are designed around the unit testing framework described in
[Unit Tests](unit_tests.md) as test performance against individual components of the code similar to
unit tests.

Unlike unit tests that verify functional correctness, performance tests measure execution time, memory usage, and other
performance metrics. They often compare the performance of custom implementations against standard library equivalents
or previous versions to ensure that optimizations are effective and that new features don't introduce performance
regressions.

Performance tests are not required for all modules and classes, but create them for any that may have a
significant performance impact.

This document focuses on performance test-specific aspects. For general code organization, file structure, naming
conventions, docstrings, and other standard practices, please refer to:

- [Code File Layout](../code_file_layout.md) - For file organization and structure
- Syntax topics â€” [Formatting](../syntax/formatting.md), [Naming](../syntax/naming.md), [Typing](../syntax/typing.md), [Docstrings](../syntax/docstrings.md), [Comments](../syntax/comments.md), [Strings](../syntax/strings.md), [Exceptions & Error Messages](../syntax/exceptions_error_messages.md), [Logging](../syntax/logging.md), and [Resources](../syntax/resources.md) â€” for naming conventions, docstrings, and code formatting
- [Semantics Guidelines](../semantics.md) - For general code organization principles
- [Unit Tests](unit_tests.md) - For general testing practices and patterns

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

Performance tests mostly follow the Unit Test Directory Hierarchy with some differences.

Place Performance Base Test Suites or performance test suites that cover general implementations in the package source code under `testsuite`, along with other unit test suites. Under normal circumstances, do not place test suites in the project source as only developers need them. However, given that PyPI currently does not support alternate package installations, include these test suites in the source to allow developers using PyPI to expand or create their own.

Example:
```
src/
+-- baseobjects/                # The main source package
    +-- testsuite/
    ¦   +-- bases/
    ¦   ¦   +-- __init__.py
    ¦   ¦   +-- basetestsuite.py
    ¦   ¦   +-- baseperformancetestsuite.py
    ¦   ¦   +-- ...
    ¦   +-- __init__.py
    ¦   +-- objecttestsuite.py
    ¦   +-- objectperformancetestsuite.py
    ¦   +-- ...
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
¦   +-- performance/                # Performance tests for the bases package
¦   ¦   +-- baseobject_performance.py
¦   ¦   +-- basecallable_performance.py
¦   ¦   +-- ...
¦   +-- ...
+-- cachingtools/
    +-- performance/
    ¦   +-- ...
    +-- ...
```


## 2 Performance Test Structure

Use performance tests to measure the performance components of the code and provide a set of tools for measuring the performance of extensions. Ensure the structure of performance tests follows the structure described in [Unit Tests](unit_tests.md).

### 2.1 Performance Test Classes

Use performance test classes to group related test methods and create test suites as described in [Unit Tests](unit_tests.md), section 4.1. Follow these additional requirements specific to performance testing:

- Define comparison objects in test classes that match the functionality of the test objects but use standard library or alternative implementations.
- Define performance-specific attributes like `timeit_runs` and `speed_tolerance` in test classes.

### 2.2 Performance Test Methods

Ensure performance test methods follow the general test method guidelines in [Unit Tests](unit_tests.md). Follow these additional requirements specific to performance testing:

- Focus test methods on measuring a specific performance aspect (speed, memory usage, etc.).
- Include performance-specific assertions in test methods that verify metrics meet requirements.
- Include detailed performance reporting in test methods for analysis.
- Assert that the percentage comparison is below the threshold.
- Use different thresholds for different types of operations if necessary.

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
    print(f"\nNew: {mean_new:.3f} µs ({percent:.3f}% of old function time)")
    assert percent < self.speed_tolerance
```

### 2.3 Performance Test Suites

Performance Test Suites are Test Classes designed to function as collections of related tests that assay the performance of a specific component, feature, or functionality. Ensure Performance Test Suites follow the general test suite guidelines in [Unit Tests](unit_tests.md).

Organize test suites hierarchically, with more specific test suites inheriting from more general base test suites to build up complex testing functionality while maintaining consistent testing patterns. The base hierarchy consists of Base Performance Test Suites and Concrete Test Suites.

#### 2.3.1 Base Performance Test Suites

Base Performance Test Suites contain a collection of tests assaying the performance of a component, feature, or functionality with a focus on testing general aspects. Generally, follow the guidelines for Base Performance Test Suites in [Unit Tests](unit_tests.md).

As in [Unit Tests](unit_tests.md), ensure a Base Performance Test Suite has a target to test such as `UnitTestClass` or `test_target`. Compose it of abstract and concrete methods which test the target against various unit tests which the target must pass. Establishing a test target allows subclassed test suites to interchange test targets to assay performance.

Use concrete performance tests in a Base Performance Test Suite to ensure that test targets are tested similarly, and use abstract tests to enforce that certain tests must be performed, with implementation details defined in more specific test suites.

Use abstract methods when:
- The implementation details depend on the specific class or function being tested.
- The test is required for all subclasses, but the implementation varies.
- The test requires specific knowledge about the class or function being tested that cannot be generalized.
- The test suite needs to enforce that certain tests are implemented by subclasses.

Use concrete methods when:
- The implementation can be shared across all subclasses.
- The test behavior is consistent regardless of the specific class or function being tested.
- The test can be implemented in a general way that works for all subclasses.
- The test suite provides a default implementation that subclasses may optionally override.

Use the base performance test suites provided by the `baseobjects` package as a foundation. These classes provide common functionality and ensure consistency across performance tests.

- `BasePerformanceTestSuite`: The abstract base class for performance tests.


Guidelines:
- Name generic test suites similarly to `BaseObjectPerformanceTestSuite`, where the component being validated is inserted between "Base" and "PerformanceTestSuite".
- Name specific test suites that define most of the implementation similarly to `ObjectPerformanceTestSuite`, where the component being tested precedes "PerformanceTestSuite".

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
        print(f"\n{self.UnitTestClass.__name__} attribute access: {mean_new:.3f} µs ({percent:.3f}% of direct access time)")
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
        print(f"\n_setattr method: {mean_new:.3f} µs ({percent:.3f}% of normal set time)")
        # No assertion here, just measuring relative performance

```


## 3 Performance Test Semantics and Syntax

Ensure performance tests conform to the semantics and syntax described in [Semantics Guidelines](../semantics.md) and the Syntax topics, but in some cases deviate from the general guidelines. The following sections describe semantics and syntax which take precedence over the general style guide.

### 3.1 Benchmarking

Use the `timeit` module for benchmarking performance tests. Follow these guidelines:

- Use the `timeit` module for measuring execution time.
- Use a sufficient number of iterations to get reliable measurements (defined in `timeit_runs`).
- Report times in microseconds for better readability.
- Calculate and report the percentage comparison between implementations.

### 3.2 Comparison Methodology

Compare the performance of custom implementations against standard library equivalents or other reference implementations:

- Define functions that perform equivalent operations using different implementations.
- Ensure that the compared operations are truly equivalent.
- Use the same input data for all implementations.
- Isolate the specific operation being tested.

Example:
```python # pseudocode
def normal_copy() -> None:
    copy.copy(normal)

# vs.

test_object.copy()
```

### 3.3 Measurement and Reporting

Ensure performance measurements are accurate, consistent, and informative:

- Use the `timeit` module with a sufficient number of iterations.
- Calculate mean execution time per operation.
- Convert times to microseconds for better readability.
- Calculate and report the percentage comparison between implementations.
- Print detailed performance information for debugging.

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
print(f"\nNew: {mean_new:.3f} µs ({percent:.3f}% of old function time)")
```


## 4 Common Patterns

### 4.1 Comparing with Standard Library

Use this common pattern to compare the performance of custom implementations against standard library equivalents:

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

Use this pattern to compare different implementation variants:

```python # pseudocode
def test_copy_vs_dunder_copy(self, test_object):
    """Tests the performance difference between copy() and __copy__() methods."""
    # Compare two different implementations
    copy_time = timeit.timeit(test_object.copy, number=self.timeit_runs)
    dunder_time = timeit.timeit(test_object.__copy__, number=self.timeit_runs)
    # ...
```

### 4.3 Measuring Overhead

Use performance tests to measure the overhead of additional functionality:

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
