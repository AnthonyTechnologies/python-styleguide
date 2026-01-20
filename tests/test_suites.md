# Anthony's Python Style Guide: Test Suites

Test suites provide a structured way to test components by grouping common test logic and ensuring consistency across the codebase. This project uses a hierarchy of test suite classes to facilitate testing of components.

Test suites are collections of related tests that validate a specific component, feature, or functionality of the software. They help organize tests logically and provide a structured way to verify multiple aspects of the code. Test suites can inherit from base test suites to provide consistent testing patterns across similar components.

The test suite system allows you to:
- Reuse common tests (e.g., for copying, pickling, and inheritance validation).
- Standardize test setup and teardown.
- Easily extend tests for subclasses.
- Group related test cases together.
- Share fixtures and utility methods.
- Enable test parameterization.

Test suites are typically located in `src/baseobjects/testsuite` (or package equivalent) and its subpackages. When writing tests in the `tests/` directory, you should inherit from the appropriate test suite class.

## Table of Contents

- [1 pytest](#1-pytest)
- [2 Base Test Suites](#2-base-test-suites)
- [3 Concrete Test Suites](#3-concrete-test-suites)
- [4 Creating a Test Suite](#4-creating-a-test-suite)
- [5 Fixtures](#5-fixtures)
- [6 Directory Structure](#6-directory-structure)

## 1 pytest

**pytest** is the testing framework used for creating test suites in this project. Although `pytest` is widely known for its support of functional tests, it also provides robust support for class-based tests, which serves as the foundation for the test suites described in this document.

Using `pytest` allows test suites to benefit from features such as fixtures, parameterization, and powerful assertion introspection. When creating a new test suite, ensure that it is compatible with `pytest` execution and conventions.

## 2 Base Test Suites

Base Test Suites are test suites contain a collection of tests for validating a component, feature, or functionality of
the software with a focus on testing general aspects of the component, feature, or functionality.

Typically, a Base Test Suites have a target to test such as `UnitTestClass` or `test_target` and will be composed of
abstract and concrete methods which test the target against various unit tests which the target must pass. Establishing
a test target allows subclassed test suites to interchange test targets to validate. The concrete tests defined in a
Base Test Suite ensure that test targets are tested similarly, while the abstract tests enforce that certain test must
be done, but the implementation of the test can be defined in a more test suite.

Base test suites should be created for common testing patterns, such as:
- Class testing (verifying class instantiation and behavior)
- Performance testing (benchmarking and profiling)
- Integration testing (testing component interactions)
- API testing (verifying interface contracts)

It is not required, but the `templatepackage` package (and this project) provides base test suites which serve as a great foundation for test suites. These classes provide common functionality and ensure consistency across tests.

- `BaseTestSuite`: The abstract base class for all test suites
- `BaseClassTestSuite`: For testing Classes
- `BaseFunctionTestSuite`: For testing Functions
- `BasePerformanceTestSuite`: For testing performance

### Guidelines

- Inherit from test suites which are related to the target
- If there are multiple relevant test suites, then multiple inherit and/or mixin classes should be used
- If there is no relevant test suite to inherit from, then inherit a base test suite
- Ensure there is an attribute that will be the target for testing; it may be defined in a parent test suite
- Ensure the annotations for the test target match what will be tested
- Abstract methods should be used when:
  - The implementation details depend on the specific class or function being tested
  - The test is required for all subclasses, but the implementation varies
  - The test requires specific knowledge about the class or function being tested that can't be generalized
  - The test suite wants to enforce that certain tests must be implemented by subclasses
- Concrete methods should be used when:
  - The implementation can be shared across all subclasses
  - The test behavior is consistent regardless of the specific class or function being tested
  - The test can be implemented in a general way that works for all subclasses
  - The test suite wants to provide a default implementation that subclasses can optionally override
- Generic test suites can be named similar to `BaseOjectTestSuite` where the component being validated should be
  inserted between Base and TestSuite
- Specific test suites which define most of the suite's implementation can be named similar to `ObjectTestSuite` where
  the component being tested is before TestSuite

### Example

```python # pseudocode
# Classes #
class BaseObjectTestSuite(BaseClassTestSuite):
    """Base test suite for children of BaseObject.

    This class provides common test functionality for child class of BaseObject, including tests for copying and
    pickling. Subclasses should set the UnitTestClass attribute and may override or extend the test methods.

    Attributes:
        UnitTestClass: The class that the test suite is testing.
    """

    # Attributes #
    UnitTestClass: Type[BaseObject] | None = None

    # Instance Methods #
    # Fixtures
    @abstractmethod
    @pytest.fixture
    def test_object(self) -> BaseObject:
        """Creates a test object."""
        # This is abstract because each subclass needs to create a specific instance
        # of the class being tested, which requires knowledge of that specific class.

    # Tests
    @abstractmethod
    def test_instance_creation(self, *args: Any, **kwargs: Any) -> None:
        """Tests that instances of the class can be created.

        This is an abstract method that must be implemented by subclasses.

        Args:
            *args: Positional arguments list to pass to the class constructor.
            **kwargs: Keyword arguments to pass to the class constructor.
        """
        # This is abstract because different classes have different constructor
        # signatures and initialization requirements.

    def test_copy(self, test_object: BaseObject) -> None:
        """Tests the copy behavior of the object.

        This test verifies that copy creates a new object with the same attributes.

        Args:
            test_object: A fixture providing a test object instance.
        """
        # This is a concrete implementation because the copy behavior is consistent
        # across all BaseObject subclasses.
        obj_copy = copy.copy(test_object)
        assert obj_copy is not test_object
        assert isinstance(obj_copy, type(test_object))
        # Additional assertions specific to the BaseObject copy behavior
```

### Common Base Test Suites

#### `BaseObjectTestSuite`

This is the most commonly used test suite for this project. It includes built-in tests for:
- **Instance Creation**: Verifies that instances can be created.
- **Copying**: Verifies `copy()` and `__copy__` behavior.
- **Deep Copying**: Verifies `deepcopy()` and `__deepcopy__` behavior.
- **Pickling**: Verifies that the object can be pickled and unpickled.

When using `BaseObjectTestSuite`, ensure your class supports these operations or override the corresponding test methods to skip them if strictly necessary (though `BaseObject` subclasses should generally support them).

## 3 Concrete Test Suites

Concrete Test Suites are subclasses of Base Test Suites and focus on validating tests defined by the Base Test Suite and
creating tests which may pertain only to a specific test target.

### Guidelines

- Should inherit from a Base Test Suite
- Should be named with a `Test` prefix followed by the name of the class or component being tested
- Test classes should contain most of their resources within their scope so the resource may be changed to suit different test variations.
  - Test involving defining classes should either be defined as inner classes or defined elsewhere and assigned to a class attribute.
  - Test involving defining functions should either be defined as inner functions or defined elsewhere and assigned to a class attribute.
- Test classes should define a test target attribute that points to the class being tested such that the tested class
  can interchanged with other similar classes which will be tested using the same test suite.

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
    templatepackage package. It creates a test subclass of BaseObject to test with.
    """

    # Attributes #
    UnitTestClass: Type[BaseObject] | None = TestBaseObject

    # Instance Methods #
    # Fixtures
    @pytest.fixture
    def test_object(self) -> BaseObject:
        """Creates a test object."""
        return self.UnitTestClass(10)

    # Tests
    def test_instance_creation(self, *args: Any, **kwargs: Any) -> None:
        """Tests that instances of the class can be created.

        This is an abstract method that must be implemented by subclasses.

        Args:
            *args: Positional arguments list to pass to the class constructor.
            **kwargs: Keyword arguments to pass to the class constructor.
        """
        instance = self.UnitTestClass()
        assert isinstance(instance, self.UnitTestClass)

    def test_copy(self, test_object: BaseObject) -> None:
        """Tests the copy behavior of the object.

        This test verifies that copy creates a new object with the same attributes.

        Args:
            test_object: A fixture providing a test object instance.
        """
        obj_copy = copy.copy(test_object)
        assert obj_copy.x == 10
```

## 4 Creating a Test Suite

To create a new test suite, follow these steps:

1.  **Inherit from a Base Test Suite**: Choose the base test suite that matches the type of object you are testing. Common base suites include:
    - `BaseTestSuite`: The foundational class for all test suites.
    - `BaseClassTestSuite`: For testing generic classes.
    - `BaseObjectTestSuite`: For testing subclasses of `BaseObject`.

2.  **Define the `UnitTestClass` Attribute**: Set the `UnitTestClass` class attribute to the class you intend to test. This tells the test suite which class to instantiate for fixtures.

3.  **Implement or Override Tests**: Add methods starting with `test_` to define new tests or override existing ones from the base class.

### Example

Here is an example of how to create a test suite for a custom class `MyObject` that inherits from `BaseObject`.

```python
import pytest
from src.baseobjects.bases import BaseObject
from src.baseobjects.testsuite import BaseObjectTestSuite

# The class to be tested
class MyObject(BaseObject):
    def do_something(self):
        return True

# The test suite
class TestMyObject(BaseObjectTestSuite):
    UnitTestClass = MyObject

    def test_do_something(self, test_object):
        """Test the do_something method."""
        assert test_object.do_something() is True
```

## 5 Fixtures

Base test suites often provide Pytest fixtures to simplify test methods.

- **`test_object`**: Provided by `BaseObjectTestSuite` (and others). It creates and returns an instance of `UnitTestClass`. You can pass constructor arguments by overriding the `test_object` fixture or by using indirect parametrization if supported.

## 6 Directory Structure

Tests are typically located in the `tests/` directory, mirroring the structure of the `src/` directory.

```
project_root/
├── src/
│   └── mypackage/
│       └── mymodule.py
└── tests/
    └── mypackage/
        └── mymodule_test.py
```

In `mymodule_test.py`, you would define the test suite class.
