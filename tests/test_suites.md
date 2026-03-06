# Anthony's Python Style Guide: Test Suites

Test suites provide a structured way to test components by grouping common test logic and ensuring consistency across
the codebase. This project uses a hierarchy of test suite classes to facilitate testing of components.

Test suites are collections of related tests that validate a specific component, feature, or functionality of the
software. They help organize tests logically and provide a structured way to verify multiple aspects of the code. Test
suites can inherit from base test suites to provide consistent testing patterns across similar components.

The test suites allow:
- Reuse common tests (e.g., for copying, pickling, and inheritance validation).
- Standardize test setup and teardown.
- Easily extend tests for subclasses.
- Group related test cases together.
- Share fixtures and utility methods.
- Enable [test parameterization](unit_tests.md#44-parameterization).

Test suites are typically located in `src/[package name]/testsuite`. When writing tests in the `tests/` directory,
inherit from the appropriate test suite class.

## Table of Contents

- [1 pytest](#1-pytest)
- [2 Directory Hierarchy](#2-directory-hierarchy)
- [3 Base Test Suites](#3-base-test-suites)
- [4 Concrete Test Suites](#4-concrete-test-suites)
- [5 Creating a Test Suite](#5-creating-a-test-suite)
- [6 Fixtures](#6-fixtures)

## 1 pytest

**pytest** is the testing framework used for creating test suites in this style guide. Although `pytest` is widely known
for its support of functional tests, it also provides robust support for class-based tests, which serves as the
foundation for the test suites described in this document.

Using `pytest` allows test suites to benefit from features such as fixtures,
[parameterization](unit_tests.md#44-parameterization), and powerful assertion introspection. When creating a new test
suite, ensure that it is compatible with `pytest` execution and conventions.

## 2 Directory Hierarchy

Place Base Test Suites or test suites that cover general implementations in the package source code under `testsuite`.
Under normal circumstances, do not place test suites in the project source as only developers need them. However, given
that PyPI currently does not support alternate package installations, include these test suites in the source to allow
developers using PyPI to expand or create their own.

Example:
```
src/
└── baseobjects/                # The main source package
    ├── bases/
    ├── testsuite/
    │   ├── bases/
    │   │   ├── __init__.py
    │   │   ├── basetestsuite.py
    │   │   └── ...
    │   ├── __init__.py
    │   ├── objecttestsuite.py
    │   └── ...
    └── ...
```

Organize Concrete Test Suites and unit tests for individual or specific components in a directory structure outside the
source code that mirrors the package structure. This makes it easy to find tests relevant to specific components and
allows `pytest` to automatically discover tests when running with the `pytest` command. For related components (like a
class and its decorators), multiple test suite classes can be defined in a single test file.

Guidelines:
- Create a directory for each major package under the `tests/` directory.
- Use subdirectories for subpackages when they contain multiple components.
- Use additional subdirectories to group tests by functionality.
- Group related tests together in the same directory.
- Start filenames with a descriptive name followed by `_test` (e.g., `name_test.py`).
- Use additional files to contain fixtures, test doubles, test base classes, or other test-specific code.

Example:
```
tests/
├── bases/                      # Tests for the bases package
│   ├── collections/            # Tests for the bases.collections subpackage
│   │   └── baseobject_test.py
│   ├── basecallable_test.py
│   ├── sentinelobject_test.py
│   └── ...
└── cachingtools/               # Tests for the cachingtools package
    ├── caches/                 # Tests for the cachingtools.caches subpackage
    ├── cachingobject_test.py
    └── ...
```

In `*_test.py` files, define the Concrete Test Suite classes.

## 3 Base Test Suites

Base Test Suites contain a collection of tests for validating a component, feature, or functionality with a focus on
testing general aspects.

Typically, a Base Test Suite has a target to test such as `UnitTestClass` or `test_target` and is composed of abstract
and concrete methods which test the target against various unit tests which the target must pass. Establish a test
target to allow subclassed test suites to interchange test targets to validate. Use concrete tests in a Base Test Suite
to ensure that test targets are tested similarly. Use abstract tests to enforce that certain tests must be performed,
with the implementation defined in a more specific test suite or the concrete test classes.

Create base test suites for common testing patterns, such as:
- Class testing (verifying class instantiation and behavior).
- Performance testing (benchmarking and profiling).
- Integration testing (testing component interactions).
- API testing (verifying interface contracts).

The `baseobjects` package offers foundational base test suites. These classes provide common functionality and ensure
consistency across tests.

- `BaseTestSuite`: The abstract base class for all test suites.
- `BaseClassTestSuite`: For testing Classes.
- `BaseFunctionTestSuite`: For testing Functions.
- `BasePerformanceTestSuite`: For testing performance.

### Guidelines

- Inherit from test suites related to the target.
  - Check the target's inheritance hierarchy to determine the appropriate test suites to inherit from.
  - If there are multiple relevant test suites, use multiple inheritance and/or mixin classes.
  - If there is no relevant test suite to inherit from, inherit a base test suite.
- Define a `UnitTestClass` class attribute that serves as the target for testing; it may be defined in a parent test suite.
- Ensure annotations for the test target match what will be tested.
- Use abstract methods when:
  - The implementation details depend on the specific class or function being tested.
  - The test is required for all subclasses, but the implementation varies.
  - The test requires specific knowledge about the class or function being tested that cannot be generalized.
- The test suite needs to enforce that certain tests are implemented by subclasses.
- Use concrete methods when:
  - The implementation can be shared across all subclasses.
  - The test behavior is consistent regardless of the specific class or function being tested.
  - The test can be implemented in a general way that works for all subclasses.
  - The test suite provides a default implementation that subclasses may optionally override.
- Name generic test suites similarly to `BaseObjectTestSuite`, where the component being validated is inserted between "Base" and "TestSuite".
- Name specific test suites that define most of the implementation similarly to `ObjectTestSuite`, where the component being tested precedes "TestSuite".

### Example

```python # pseudocode
# Classes #
class BaseObjectTestSuite(BaseClassTestSuite):
    """Base test suite for children of BaseObject.

    This class provides common test functionality for child class of BaseObject, including tests for copying and
    pickling. Set the UnitTestClass attribute in subclasses and may override or extend the test methods.

    Attributes:
        UnitTestClass: The class that the test suite is testing.
    """

    # Attributes #
    UnitTestClass: type[BaseObject]

    # Instance Methods #
    # Fixtures
    @pytest.fixture
    def test_object(self, *args: Any, **kwargs: Any) -> BaseObject:
        """Creates a test object.

        Args:
            *args: Positional arguments to pass to the class constructor.
            **kwargs: Keyword arguments to pass to the class constructor.

        Returns:
            BaseObject: A test object instance.
        """
        return self.UnitTestClass(*args, **kwargs)

    # Tests
    # Instantiation
    def test_instance_creation(self, *args: Any, **kwargs: Any) -> None:
        """Tests that instances of the class can be created.

        This method can be overridden by subclasses to perform additional tests on the instance.

        Args:
            *args: Positional arguments list to pass to the class constructor.
            **kwargs: Keyword arguments to pass to the class constructor.
        """
        # Create Object
        obj = self.UnitTestClass(*args, **kwargs)

        # Validate
        assert isinstance(obj, self.UnitTestClass)

    @pytest.mark.parametrize("method", ["copy", "method"])
    def test_copy_operations(self, test_object: BaseObject, method: str) -> None:
        """Tests the copy behavior of the object.

        This test verifies that copy creates a new object with the same attributes.

        Args:
            test_object: A fixture providing a test object instance.
            method: The method to use for copying ('copy' or 'method').

        Raises:
            ValueError: If the method is invalid.
        """
        # Copy Object
        if method == "copy":
            obj_copy = copy.copy(test_object)
        elif method == "method":
            obj_copy = test_object.copy()
        else:
            msg = f"Invalid method: {method}"
            raise ValueError(msg)

        # Validate
        assert obj_copy is not test_object
```

### Common Base Test Suites

#### `BaseObjectTestSuite`

This is the most commonly used test suite for this project. It includes built-in tests for:
- **Instance Creation**: Verifies that instances can be created.
- **Copying**: Verifies `copy()` and `__copy__` behavior.
- **Deep Copying**: Verifies `deepcopy()` and `__deepcopy__` behavior.
- **Pickling**: Verifies that the object can be pickled and unpickled.

When using `BaseObjectTestSuite`, ensure the class supports these operations or override the corresponding test methods
to skip them if strictly necessary (though `BaseObject` subclasses generally support them).

## 4 Concrete Test Suites

Concrete Test Suites are subclasses of Base Test Suites and focus on validating tests defined by the Base Test Suite and
creating tests that pertain only to a specific test target.

### Guidelines

- Inherit from a Base Test Suite.
- Name with a `Test` prefix followed by the name of the class or component being tested.
- Ensure test classes contain most of their resources within their scope so the resource may be changed to suit different test variations.
  - Define classes involved in tests either as inner classes or define them elsewhere and assign them to a class attribute.
  - Define functions involved in tests either as inner functions or define them elsewhere and assign them to a class attribute.
- Ensure test classes define a test target attribute that points to the class being tested such that the tested class can be interchanged with other similar classes which will be tested using the same test suite.

### Example

```python # pseudocode
# Classes #
class BaseTestObject(BaseObject):
    """A subclass of BaseObject for testing purposes."""
    def __init__(self, x: int = 5):
        self.x = x

# Test Suite #
class TestBaseObject(BaseObjectTestSuite):
    """A Testsuite for the BaseObject class.

    This class tests the functionality of the BaseObject class, which is the base class for all objects in the
    baseobjects package. It creates a test subclass of BaseObject to test with.
    """

    # Attributes #
    UnitTestClass: type[BaseObject] = BaseTestObject

    # Instance Methods #
    # Fixtures
    @pytest.fixture
    def test_object(self, *args: Any, **kwargs: Any) -> BaseObject:
        """Creates a test object.

        Args:
            *args: Positional arguments to pass to the class constructor.
            **kwargs: Keyword arguments to pass to the class constructor.

        Returns:
            BaseObject: A test object instance.
        """
        return self.UnitTestClass(10, *args, **kwargs)

    # Tests
    def test_instance_creation(self, *args: Any, **kwargs: Any) -> None:
        """Tests that instances of the class can be created.

        Args:
            *args: Positional arguments list to pass to the class constructor.
            **kwargs: Keyword arguments to pass to the class constructor.
        """
        instance = self.UnitTestClass(*args, **kwargs)
        assert isinstance(instance, self.UnitTestClass)

    def test_copy_operations(self, test_object: BaseObject, method: str) -> None:
        """Tests the copy behavior of the object.

        This test verifies that copy creates a new object with the same attributes.

        Args:
            test_object: A fixture providing a test object instance.
            method: The method to use for copying ('copy' or 'method').
        """
        obj_copy = copy.copy(test_object)
        assert obj_copy.x == 10
```

## 5 Creating a Test Suite

To create a new test suite, follow these steps:

1.  **Inherit from a Base Test Suite**: Choose the base test suite that matches the type of object being tested. Cross-reference the inheritance of the test target to ensure that relevant test suites are inherited.

2.  **Define the `UnitTestClass` Attribute**: Set the `UnitTestClass` class attribute to the class or function being tested. This tells the test suite which class to instantiate for fixtures and is used by test methods.

3.  **Define or Override Fixtures**: Implement fixtures required for the tests. Base test suites often provide a `test_object` fixture that uses `UnitTestClass`. Override this fixture if specific constructor arguments are needed.

4.  **Implement or Override Tests**: Add methods starting with `test_` to define new tests or override existing ones from the base class.

### Example

Here is an example of how to create a test suite for a custom class `MyObject` that inherits from `BaseObject`.

```python
import pytest
from baseobjects.bases import BaseObject
from baseobjects.testsuite import BaseObjectTestSuite

# The class to be tested
class MyObject(BaseObject):
    def do_something(self) -> bool:
        return True

# The test suite
class TestMyObject(BaseObjectTestSuite):
    UnitTestClass = MyObject

    def test_do_something(self, test_object: MyObject) -> None:
        """Test the do_something method."""
        assert test_object.do_something() is True
```

## 6 Fixtures

Base test suites often provide Pytest fixtures to simplify test methods.

- **`test_object`**: Provided by `BaseObjectTestSuite` (and others). It creates and returns an instance of `UnitTestClass`. Pass constructor arguments by overriding the `test_object` fixture or by using indirect parametrization if supported.
- **`io_object`**: Often used in I/O related test suites as a fixture for the object under test.
- **`test_function_object`**: Used in function or decorator test suites.
