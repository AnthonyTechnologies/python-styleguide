# Python Style Guide: Test Suites

Test suites provide a structured way to test components by grouping common test logic and ensuring consistency across the codebase. This guide acts as a neutral arbiter of quality, prioritizing clarity and explaining the rationale behind rules. Adhere to these standards to maintain a professional and consistent codebase.

Prioritize project consistency within the project. Once a project-wide standard is established, it must be applied uniformly across all files and modules within that project.

Test suites enable:
- Reusing common tests (e.g., for copying, pickling, and inheritance validation).
- Standardizing test setup and teardown.
- Extending tests for subclasses.
- Grouping related test cases.
- Sharing fixtures and utility methods.
- Enabling [test parameterization](unit_tests.md#44-parameterization).

Locate test suites in `src/[package name]/testsuite`. When writing tests in the `tests/` directory, inherit from the appropriate test suite class.

## Table of Contents

- [1 pytest](#1-pytest)
- [2 Directory Hierarchy](#2-directory-hierarchy)
- [3 Base Test Suites](#3-base-test-suites)
- [4 Concrete Test Suites](#4-concrete-test-suites)
- [5 Creating a Test Suite](#5-creating-a-test-suite)
- [6 Fixtures](#6-fixtures)

## 1 pytest

Use **pytest** as the testing framework for creating test suites. Although `pytest` is widely known for supporting functional tests, it also provides robust support for class-based tests, which serves as the foundation for the test suites described in this document.

### Rationale
Adopting `pytest` is required to benefit from modern testing features such as fixtures, [parameterization](unit_tests.md#44-parameterization), and powerful assertion introspection. Consistency in the testing framework is recommended to simplify development and onboarding.

Directives:
- Ensure that all new test suites are compatible with `pytest` execution and conventions.
- Prefer class-based tests for complex components to leverage inheritance and shared logic.

## 2 Directory Hierarchy

Place base test suites or test suites that cover general implementations in the package source code under `testsuite`. Under normal circumstances, do not place test suites in the project source as only developers require these suites. However, if the package must support developers using PyPI to expand or create new suites, include these test suites in the source to circumvent current PyPI limitations regarding alternate package installations.

### Rationale
A clear directory hierarchy is required for automated test discovery and component mapping. Placing general test suites in the source package ensures accessibility for downstream developers, while keeping specific tests in a separate directory minimizes the package's footprint for end-users.

Directives:
- Organize concrete test suites and unit tests for specific components in a directory structure that mirrors the package structure.
- Define multiple test suite classes in a single test file for related components (e.g., a class and its decorators).
- Create a directory for each major package under the `tests/` directory.
- Use subdirectories to group tests by subpackage or functionality.
- Start filenames with a descriptive name followed by `_test` (e.g., `name_test.py`).
- Use additional files for fixtures, test doubles, or test base classes to maintain separation of concerns.

Compliant:
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

Compliant:
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

Define the concrete test suite classes in `*_test.py` files.

## 3 Base Test Suites

Base test suites provide a collection of tests for validating a component, feature, or functionality with a focus on testing general aspects. Use a `UnitTestClass` or `test_target` as the test target and compose the suite of abstract and concrete methods. Establish a clear test target to allow subclassed test suites to interchange the validation target.

### Rationale
Base test suites are recommended to ensure that similar components are tested consistently across the project. They reduce duplication by providing common tests for standard operations like copying, pickling, and instantiation.

Directives:
- Use concrete tests in a base test suite to ensure that test targets are validated using standardized patterns.
- Use abstract tests to enforce that specific tests must be performed, with the implementation defined in a more specific test suite or concrete test class.
- Create base test suites for common testing patterns:
    - **Class testing**: Verifying class instantiation and behavior.
    - **Performance testing**: Benchmarking and profiling.
    - **Integration testing**: Testing component interactions.
    - **API testing**: Verifying interface contracts.

### Guidelines

- Inherit from test suites related to the target.
    - Check the inheritance hierarchy of the target to determine the appropriate base suites.
    - Use multiple inheritance or mixin classes if multiple test suites are relevant.
    - Inherit a foundational base test suite if no specialized suite exists.
- Define a `UnitTestClass` class attribute to serve as the test target.
- Ensure annotations for the test target match the object being tested.
- Use abstract methods when:
    - Implementation details depend on the specific class or function.
    - The test is required for all subclasses, but the implementation varies.
    - The test requires specific knowledge that cannot be generalized.
    - Subclasses must be enforced to implement specific tests.
- Use concrete methods when:
    - The implementation can be shared across all subclasses.
    - Test behavior is consistent regardless of the target.
    - A default implementation is provided that subclasses may optionally override.
- Name generic test suites using the `Base[Component]TestSuite` pattern (e.g., `BaseObjectTestSuite`).
- Name specific test suites that define most of the implementation using the `[Component]TestSuite` pattern (e.g., `ObjectTestSuite`).

Compliant:

```python # pseudocode
# Classes #
class BaseObjectTestSuite(BaseClassTestSuite):
    """A base test suite for children of BaseObject.

    Provides common test functionality for child classes of BaseObject, including tests for copying and pickling. 
    Define the UnitTestClass attribute in subclasses.
    """

    # Attributes #
    UnitTestClass: type[BaseObject]

    # Instance Methods #
    # Fixtures
    @pytest.fixture
    def test_object(self, *args: Any, **kwargs: Any) -> BaseObject:
        """Creates a test object.

        Args:
            *args: Positional arguments for the class constructor.
            **kwargs: Keyword arguments for the class constructor.

        Returns:
            A test object instance.
        """
        return self.UnitTestClass(*args, **kwargs)

    # Tests
    # Instantiation
    def test_instance_creation(self, *args: Any, **kwargs: Any) -> None:
        """Tests that instances of the class can be created.

        Subclasses may override this method to perform additional tests on the instance.

        Args:
            *args: Positional arguments for the class constructor.
            **kwargs: Keyword arguments for the class constructor.
        """
        # Create Object
        obj = self.UnitTestClass(*args, **kwargs)

        # Validate
        assert isinstance(obj, self.UnitTestClass)

    @pytest.mark.parametrize("method", ["copy", "method"])
    def test_copy_operations(self, test_object: BaseObject, method: str) -> None:
        """Tests the copy behavior of the object.

        Verifies that copy creates a new object with the same attributes.

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

This is the most commonly used test suite in this project. Use this suite for objects requiring verification of:
- **Instance Creation**: Verifies that instances are created correctly.
- **Copying**: Verifies `copy()` and `__copy__` behavior.
- **Deep Copying**: Verifies `deepcopy()` and `__deepcopy__` behavior.
- **Pickling**: Verifies that the object can be pickled and unpickled.

When using `BaseObjectTestSuite`, ensure the target class supports these operations. Override corresponding test methods to skip tests if strictly necessary.

## 4 Concrete Test Suites

Concrete test suites are subclasses of base test suites that validate specific test targets. These suites focus on implementing the tests defined by the base suite and creating additional tests unique to the target component.

### Rationale
Concrete test suites are required to bridge the gap between general testing patterns and specific component behavior. Isolating resources and targets within these suites is recommended to allow for flexible test variations and to maintain clear separation between test logic and the code under test.

Directives:
- Inherit from a relevant base test suite.
- Use the `Test` prefix followed by the name of the class or component being tested (e.g., `TestBaseObject`).
- Contain test resources (inner classes, inner functions, or class attributes) within the suite's scope to facilitate resource swapping.
- Define a test target attribute that points to the class being tested, enabling the suite to be reused for similar classes.

Compliant:

```python # pseudocode
# Classes #
class BaseTestObject(BaseObject):
    """A subclass of BaseObject for testing purposes."""
    def __init__(self, x: int = 5):
        self.x = x

# Test Suite #
class TestBaseObject(BaseObjectTestSuite):
    """A test suite for the BaseObject class.

    Tests the functionality of the BaseObject class using a test subclass.
    """

    # Attributes #
    UnitTestClass: type[BaseObject] = BaseTestObject

    # Instance Methods #
    # Fixtures
    @pytest.fixture
    def test_object(self, *args: Any, **kwargs: Any) -> BaseObject:
        """Creates a test object.

        Args:
            *args: Positional arguments for the class constructor.
            **kwargs: Keyword arguments for the class constructor.

        Returns:
            A test object instance.
        """
        return self.UnitTestClass(10, *args, **kwargs)

    # Tests
    def test_instance_creation(self, *args: Any, **kwargs: Any) -> None:
        """Tests that instances of the class can be created.

        Args:
            *args: Positional arguments for the class constructor.
            **kwargs: Keyword arguments for the class constructor.
        """
        instance = self.UnitTestClass(*args, **kwargs)
        assert isinstance(instance, self.UnitTestClass)

    def test_copy_operations(self, test_object: BaseObject, method: str) -> None:
        """Tests the copy behavior of the object.

        Verifies that copy creates a new object with the same attributes.

        Args:
            test_object: A fixture providing a test object instance.
            method: The method to use for copying ('copy' or 'method').
        """
        obj_copy = copy.copy(test_object)
        assert obj_copy.x == 10
```

## 5 Creating a Test Suite

Follow these steps to create a new test suite:

1.  **Inherit from a Base Test Suite**: Select a base test suite matching the object type. Verify the inheritance of the test target to ensure all relevant test suites are inherited.
2.  **Define the `UnitTestClass` Attribute**: Set the `UnitTestClass` class attribute to the target class or function.
3.  **Define or Override Fixtures**: Implement required fixtures. Base test suites typically provide a `test_object` fixture using `UnitTestClass`. Override this fixture if specific constructor arguments are required.
4.  **Implement or Override Tests**: Define methods starting with `test_` for new validations or override base class tests.

### Rationale
A standardized creation process is recommended to maintain consistency across the test suite hierarchy. Clear steps help ensure that the `UnitTestClass` is correctly targeted and that fixtures are appropriately managed.

Compliant:

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
        """Tests the do_something method."""
        assert test_object.do_something() is True
```

## 6 Fixtures

Base test suites provide Pytest fixtures to simplify test methods.

### Rationale
Using shared fixtures is required to reduce boilerplate and ensure that objects are instantiated consistently across different tests.

Directives:
- **`test_object`**: Use this fixture (provided by `BaseObjectTestSuite` and others) to obtain an instance of `UnitTestClass`. Pass constructor arguments by overriding the fixture or using indirect parametrization.
- **`io_object`**: Use this fixture in I/O related test suites for the object under test.
- **`test_function_object`**: Use this fixture in function or decorator test suites.
