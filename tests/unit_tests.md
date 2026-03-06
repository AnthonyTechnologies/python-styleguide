# Anthony's Python Style Guide: Unit Tests

Unit tests are used to verify the correctness of the code being tested to ensure that it is working as expected.
Typically, unit tests are written to verify individual components of the code.

Test suites are collections of related tests that validate a specific component, feature, or functionality of the
software. They help organize tests logically and provide a structured way to verify multiple aspects of the code. Test
suites can inherit from base test suites to provide consistent testing patterns across similar components.

Ensure unit tests and test suites follow the guidelines set forth by the general styleguide such as the code
organization, file structure, naming conventions, docstrings, and other standard practices in:

- [Code File Layout](../code_file_layout.md) - For file organization and structure
- Syntax topics � [Formatting](../syntax/formatting.md), [Naming](../syntax/naming.md), [Typing](../syntax/typing.md), [Docstrings](../syntax/docstrings.md), [Comments](../syntax/comments.md), [Strings](../syntax/strings.md), [Exceptions & Error Messages](../syntax/exceptions_error_messages.md), [Logging](../syntax/logging.md), and [Resources](../syntax/resources.md) � for naming conventions, docstrings, and code formatting
- [Semantics Guidelines](../semantics.md) - For general code organization principles

The guidelines in this document are supplemental to the general guidelines and focus on test-specific code to ensure
consistency, maintainability, and effectiveness of the test suite across the project.

## Table of Contents

- [1 pytest](#1-pytest)
- [2 Directory Hierarchy](#2-directory-hierarchy)
- [3 Test Structure](#3-test-structure)
    - [3.1 Test Classes](#31-test-classes)
    - [3.2 Test Methods](#32-test-methods)
    - [3.3 Test Suites](#33-test-suites)
    - [3.4 Main](#34-main)
- [4 Test Semantics and Syntax](#4-test-semantics-and-syntax)
    - [4.1 Assertions](#41-assertions)
    - [4.2 Fixtures](#42-fixtures)
    - [4.3 Test Doubles](#43-test-doubles)
    - [4.4 Parameterization](#44-parameterization)
    - [4.5 Async Testing](#45-async-testing)
    - [4.6 Skipping Tests](#46-skipping-tests)
    - [4.7 Testing Exceptions](#47-testing-exceptions)
    - [5 Test Execution](#5-test-execution)


## 1 pytest

**pytest** testing framework is the preferred framework for Python projects, as it provides more features and
flexibility than python's unittest library.

In pytest, tests can be created by defining a test function with a `test_` prefix. pytest can then run the tests using
its Python or command line interface and display diagnostics about the tests. Additionally, the pytest API offers an
extensive array of options for customizing the run conditions and diagnostic information of these tests. For more
information on pytest, see the [pytest documentation](https://docs.pytest.org/en/latest/).

The pytest package has many features, and this styleguide will offer guidance on how to use them.


## 2 Directory Hierarchy

Place Base Test Suites or test suites that cover general implementations in the package source code under `testsuite`. Under normal circumstances, do not place test suites in the project source as only developers need them. However, given that PyPI currently does not support alternate package installations, include these test suites in the source to allow developers using PyPI to expand or create their own.

Example:
```
src/
+-- baseobjects/                # The main source package
    +-- bases/
    +-- testsuite/
    �   +-- bases/
    �   �   +-- __init__.py
    �   �   +-- basetestsuite.py
    �   �   +-- ...
    �   +-- __init__.py
    �   +-- objecttestsuite.py
    �   +-- ...
    +-- ...
```

Organize Concrete Test Suites and unit tests for individual or specific components in a directory structure outside the source code that mirrors the package structure. This makes it easy to find tests relevant to specific components and allows `pytest` to automatically discover tests when running with the `pytest` command.

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
+-- bases/                      # Tests for the bases package
�   +-- collections/            # Tests for the bases.collections subpackage
�   �   +-- baseobject_test.py
�   +-- basecallable_test.py
�   +-- sentinelobject_test.py
�   +-- ...
+-- cachingtools/               # Tests for the cachingtools package
    +-- caches/                 # Tests for the cachingtools.caches subpackage
    +-- cachingobject_test.py
    +-- ...
```


## 3 Test Structure

Use test code to not only verify that the code works as expected but also to provide a set of tools for testing extensions. For example, even if a class outlines functionality not yet implemented, the test code must verify that the class works as expected.

In `pytest`, organize tests into classes and subclasses to parameterize tests or create test suites to verify different implementations.

Follow the general docstring guidelines in [Docstrings](../syntax/docstrings.md), particularly the module and test module subsections, for creating documentation.

### 3.1 Test Classes

Use test classes to group related test methods and create test suites. Create base test classes to provide consistent testing patterns across the project.

Ensure test classes inherit from appropriate base test classes/suites to maintain consistency.

Guidelines:
- Inherit test classes from an appropriate base test class/suite.
- Include a descriptive docstring in test classes explaining what is being tested.
- Define a `UnitTestClass` class attribute to specify the class or function being tested. This allows generic test suites to interchange test targets.
- Ensure test classes contain most of their resources within their scope so the resource may be changed to suit different test variations.
  - Define classes involved in tests either as inner classes or define them elsewhere and assign them to a class attribute.
  - Define functions involved in tests either as inner functions or define them elsewhere and assign them to a class attribute.

For test method naming and organization, follow the general method guidelines in the Syntax topics �
[Formatting](../syntax/formatting.md), [Docstrings](../syntax/docstrings.md), and [Comments](../syntax/comments.md) �
and [Code File Layout](../code_file_layout.md).

### 3.2 Test Methods

Design test methods to test a specific aspect of the class or function. Ensure each test method is focused, independent, and provides clear feedback upon failure.

Guidelines:
- Name test methods with a `test_` prefix followed by a descriptive name.
- Include a descriptive docstring in test methods explaining what is being tested.
- Use type hints for test method parameters and return values.
- Ensure test methods are independent and do not rely on state from other tests.
- Focus test methods on testing a single aspect of behavior.
- Include assertions in test methods to verify expected behavior.
- Handle both normal and edge cases in test methods.
- Use attributes provided by the test class (this allows more options when used as a test suite).

Example:
```python # pseudocode
def test_deepcopy(self, test_object: BaseObject) -> None:
    """Tests the deep copy behavior of BaseObject.

    This test verifies that deepcopy creates a new object with new mutable attributes
    but the same immutable attributes.

    Args:
        test_object: A fixture providing a BaseObject instance.
    """
    # Perform the operation being tested
    new = copy.deepcopy(test_object)

    # Assert the expected behavior
    assert new is not test_object
    assert id(new.immutable) == id(test_object.immutable)
    assert id(new.mutable) != id(test_object.mutable)
    assert new.mutable == test_object.mutable
```

When creating test methods that test similar functionality across different implementations, consider using
[parameterized tests](#44-parameterization) to reduce code duplication and ensure consistent testing.

### 3.3 Test Suites

Test suites are collections of related tests that validate a specific component, feature, or functionality of the
software. For detailed guidelines on creating and using test suites, see [Test Suites](test_suites.md).

### 3.4 Main

Include a `__main__` block in test files for running the tests directly. Mainly it sets the run options for pytest
for the tests in the file.

Example:
```python # pseudocode
# Main #
if __name__ == "__main__":
    pytest.main(["-v", "-s"])
```

## 4 Test Semantics and Syntax

Ensure tests conform to the semantics and syntax described in [Semantics Guidelines](../semantics.md) and the Syntax topics:
[Formatting](../syntax/formatting.md), [Naming](../syntax/naming.md), [Typing](../syntax/typing.md), [Docstrings](../syntax/docstrings.md),
[Comments](../syntax/comments.md), [Strings](../syntax/strings.md), [Exceptions & Error Messages](../syntax/exceptions_error_messages.md),
[Logging](../syntax/logging.md), and [Resources](../syntax/resources.md) � but in some cases it may be necessary to deviate from the general
guidelines. The following sections describe semantics and syntax which take precedence over the general styleguide.

### 4.1 Assertions

Assertions are a base Python feature that allows for checking the state of a program at runtime and are used by pytest
as the primary means of verifying test conditions. Assertions are discouraged in source code because they do not conform
to Python's error handling principles. However, assertions are permitted for debugging, testing, examples, and tutorials
because assertions are good for explaining the behavior of a program, and in these scenarios error handling
is managed by the user rather than the program.

Guidelines:
- Include at least one assertion in each test
- Ensure assertions are specific and verify a single aspect of behavior
- Use appropriate assertion methods for the type of comparison being made
- Include descriptive error messages in assertions to make test failures more informative

Example:
```python # pseudocode
# Simple assertions
assert result == expected
assert instance is not None

# More complex assertions
assert id(new.immutable) == id(test_object.immutable)
assert id(new.mutable) != id(test_object.mutable)
assert unpickled.immutable == test_object.immutable
assert unpickled.mutable == test_object.mutable
assert unpickled is not test_object
```

### 4.2 Fixtures

Use `pytest` fixtures to provide a setup and teardown of test environments and create test objects.

Guidelines:
- Use fixtures for setting up test environments and creating test objects.
- Define fixtures at the appropriate scope (function, class, module, or session).
- Include a descriptive docstring in fixtures explaining their purpose and return value.
- Use type hints for fixture parameters and return values.
- Define common fixtures in base test modules.
- Organize fixtures under a `# Fixtures` comment.

Example:
```python # pseudocode
# Fixtures
@pytest.fixture
def test_object(self, *args: Any, **kwargs: Any) -> BaseObject:
    """Creates a test object instance for use in tests.

    Args:
        *args: Positional arguments to pass to the class constructor.
        **kwargs: Keyword arguments to pass to the class constructor.

    Returns:
        BaseObject: An instance of the test class.
    """
    return self.UnitTestClass(*args, **kwargs)

@pytest.fixture
def tmp_dir(tmpdir: Any) -> Path:
    """A pytest fixture that turns the tmpdir into a Path object.

    Args:
        tmpdir: A pytest tmpdir fixture.

    Returns:
        Path: A pathlib.Path object representing the temporary directory.
    """
    return Path(tmpdir)
```

### 4.3 Test Doubles

Use test doubles (mocks, stubs, fakes, etc.) to isolate the code being tested from its dependencies.

Guidelines:
- Use test doubles to isolate the code being tested from its dependencies.
- Use the appropriate type of test double for the situation:
  - Stubs: return predefined values.
  - Mocks: verify interactions.
  - Fakes: simplified implementations.
  - Spies: record interactions.
- Use `pytest`'s `monkeypatch` fixture for patching functions and methods.
- Use `unittest.mock` for creating mock objects.
- Reset or tear down test doubles after use.

Example:
```python # pseudocode
def test_with_mock(self, monkeypatch: pytest.MonkeyPatch) -> None:
    """Tests with a mock object.

    This test uses a mock object to verify that the correct method is called.

    Args:
        monkeypatch: A pytest fixture for patching functions and methods.
    """
    # Create a mock object
    mock = unittest.mock.Mock()

    # Patch a method to use the mock
    monkeypatch.setattr(self.class_, "some_method", mock)

    # Call the method that uses the patched method
    instance = self.class_()
    instance.method_under_test()

    # Verify the mock was called correctly
    mock.assert_called_once_with(expected_args)
```

### 4.4 Parameterization

Use `pytest` parameterization to run a test function or method multiple times with different sets of arguments. This
reduces code duplication and ensures consistent testing across multiple scenarios.

Guidelines:
- Use `@pytest.mark.parametrize` for function-level parameterization.
- Use the `ids` parameter to provide descriptive names for each test case, which helps in identifying failures.
- When testing similar functionality across different implementations, consider using parameterized tests to reduce
  code duplication and ensure consistent testing.

#### When to Use Parameterization

- **Data-Driven Tests**: When the same test logic is applied to multiple inputs and expected results.
- **Edge Case Validation**: When testing multiple boundary conditions or edge cases for a single function or method.
- **Equivalent Operations**: When verifying that different ways of performing an operation (e.g., a function call vs. a
  method call) yield the same results.
- **Cross-Implementation Testing**: When testing that different subclasses or implementations of an interface behave
  identically under the same conditions.

#### When Not to Use Parameterization

- **Complex Test Logic**: If different parameters require significantly different test logic, leading to complex
  conditional branching (`if/else`) within the test method. In such cases, separate test methods are clearer.
- **Unrelated Scenarios**: Avoid grouping unrelated test cases just because they share a similar signature. Each test
  method represents a distinct logical scenario.
- **Obscure Failures**: If parameterization makes it difficult to understand which specific case failed or why, use
  individual test methods instead.
- **Too Many Parameters**: If a test requires a large number of parameters (e.g., more than 4 or 5), it can become
  difficult to read and maintain. Consider using a different testing strategy or breaking down the test.

Example:
```python # pseudocode
# Parameterized test method
@pytest.mark.parametrize(
    "input_val, expected_output",
    [
        (1, 2),
        (5, 10),
        (0, 0),
        (-1, -2),
    ],
    ids=["small_positive", "large_positive", "zero", "negative"]
)
def test_multiply_by_two(self, input_val: int, expected_output: int) -> None:
    """Tests the multiplication of an integer by two.

    Args:
        input_val: The input value to multiply.
        expected_output: The expected result of the multiplication.
    """
    assert input_val * 2 == expected_output
```

### 4.5 Async Testing

Use `@pytest.mark.asyncio` for asynchronous test methods. If a method might not be implemented in a specific test target, handle the `NotImplementedError` and skip the test using `pytest.skip`.

Guidelines:
- Use `@pytest.mark.asyncio` to decorate asynchronous test methods.
- Handle `NotImplementedError` or `AttributeError` by skipping the test with `pytest.skip` when the functionality is not implemented or not applicable for the current test target.

Example:
```python # pseudocode
@pytest.mark.asyncio
async def test_async_method(self, test_object: BaseObject) -> None:
    """Tests an asynchronous method.

    Args:
        test_object: A fixture providing a test object instance.
    """
    try:
        result = await test_object.some_async_method()
        assert result is True
    except NotImplementedError:
        pytest.skip("Async method not implemented for this object.")
```

### 4.6 Skipping Tests

Use `pytest.skip` to skip tests that are not applicable to the current test target or environment. Provide a clear reason for skipping to help with maintenance.

Guidelines:
- Call `pytest.skip` within a test method or fixture when the test cannot be executed.
- Provide a descriptive message explaining why the test is being skipped.

Example:
```python # pseudocode
def test_conditional_feature(self, test_object: BaseObject) -> None:
    """Tests a feature that may not be present."""
    if not hasattr(test_object, "special_feature"):
        pytest.skip("Test object does not have the special feature.")

    assert test_object.special_feature() == "success"
```

### 4.7 Testing Exceptions

Use `pytest.raises` to verify that the code raises the expected exception under specific conditions.

Guidelines:
- Use `pytest.raises` as a context manager.
- Specify the expected exception type.
- Use the `match` parameter to verify the error message when appropriate.

Example:
```python # pseudocode
def test_invalid_input(self, test_object: BaseObject) -> None:
    """Tests that an invalid input raises a ValueError.

    Args:
        test_object: A fixture providing a test object instance.
    """
    with pytest.raises(ValueError, match="Invalid input value"):
        test_object.method_requiring_valid_input(invalid_value)
```

## 5 Test Execution

Ensure tests are easy to run and provide clear feedback on failures.

Guidelines:
- Ensure tests are runnable using `pytest`.
- Ensure tests are runnable individually or as part of a test suite.
- Ensure tests provide clear error messages on failure.
- Ensure tests clean up after themselves.
- Ensure tests do not depend on the order of execution.

Running tests:
```bash
# Run all tests
pytest

# Run tests in a specific file
pytest tests/bases/test_baseobject.py

# Run a specific test
pytest tests/bases/test_baseobject.py::TestBaseObject::test_deepcopy

# Run tests with verbose output
pytest -v

# Run tests with output capturing disabled
pytest -s
```
