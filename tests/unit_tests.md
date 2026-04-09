# Anthony's Python Style Guide: Unit Tests

Use unit tests to verify the correctness of individual components and ensure that code behaves as expected.

### Rationale
A comprehensive unit test suite is required to maintain code quality, prevent regressions, and enable confident refactoring.

Directives:
- Follow general style guidelines (naming, layout, docstrings) in all test code.
- Prioritize "Project Consistency" across all test modules. Once a project-wide standard is established, it must be applied uniformly to all tests.
- Refer to [Code File Layout](../code_file_layout.md) and [Syntactic Guidelines](../syntax/) for baseline standards.

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

Use the **pytest** framework for all Python projects.

### Rationale
Pytest is required because it provides superior features, flexibility, and a more concise syntax than the standard `unittest` library.

Directives:
- Create tests by defining functions with a `test_` prefix.
- Use the pytest API and command-line interface to manage run conditions and diagnostics.


## 2 Directory Hierarchy

Organize tests into a hierarchy that mirrors the package source code.

### Rationale
A mirrored directory structure is required to make test discovery intuitive and to maintain a clear mapping between code and its corresponding tests.

Directives:
- Place base test suites in the package source under `testsuite/`.
- Organize concrete tests in a `tests/` directory at the repository root.
- Mirror the `src/` package structure within the `tests/` directory.
- Create a directory for each major package under the `tests/` directory.
- Use subdirectories for subpackages and functional groupings.
- Name test files with a `_test.py` suffix (e.g., `name_test.py`).
- Use additional files for fixtures, test doubles, and base classes.

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

Structure tests to verify implementation correctness and provide tools for extension.

### Rationale
Well-structured tests are required to ensure that functionality is verified comprehensively and that test code is reusable for future enhancements.

Directives:
- Organize tests into classes and subclasses to support parameterization and reuse.
- Follow the [Docstrings](../syntax/docstrings.md) guidelines for all test modules and classes.
- Ensure test code verifies implementation even for functionality not yet fully realized.

### 3.1 Test Classes

Use test classes to group related test methods and create test suites.

### Rationale
Test classes are required to maintain an organized and scalable test structure, allowing for shared setup and parameterization.

Directives:
- Inherit from appropriate base test classes or suites to ensure consistency.
- Include descriptive docstrings explaining the scope of the test class.
- Define a `UnitTestClass` attribute to specify the target of the tests.
- Keep resources within the class scope to allow for variation in subclasses.

For test method naming and organization, follow the general method guidelines in the Syntax topics �
[Formatting](../syntax/formatting.md), [Docstrings](../syntax/docstrings.md), and [Comments](../syntax/comments.md) �
and [Code File Layout](../code_file_layout.md).

### 3.2 Test Methods

Design test methods to verify a specific aspect of behavior.

### Rationale
Focused test methods are required to provide clear feedback and simplify debugging when a failure occurs.

Directives:
- Use the `test_` prefix for all test method names.
- Provide a descriptive docstring for every test method.
- Ensure methods are independent and do not rely on side effects from other tests.
- Verify expected behavior with explicit assertions.
- Use parameterized tests to avoid duplication when testing similar functionality.

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

Use test suites to validate complex components or features. Refer to [Test Suites](test_suites.md) for detailed guidelines.

### 3.4 Main

Include a `if __name__ == "__main__":` block to enable direct execution of test files.

### Rationale
Providing a direct entry point is recommended for quick validation of individual test files during development.

Example:
```python # pseudocode
# Main #
if __name__ == "__main__":
    pytest.main(["-v", "-s"])
```

## 4 Test Semantics and Syntax

Follow the general [Semantics Guidelines](../semantics.md) and Syntax topics, but prioritize the test-specific rules below when they conflict.

### 4.1 Assertions

Use plain `assert` statements as the primary verification mechanism.

### Rationale
Pytest leverages standard Python `assert` statements to provide detailed failure diagnostics, making them the preferred choice for unit testing.

Directives:
- Include at least one assertion per test.
- Use specific, non-composite assertions.
- Provide descriptive error messages for complex checks.

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

Use fixtures to manage test dependencies and state.

### Rationale
Fixtures are required to ensure that test setup and teardown are consistent, reusable, and isolated from the tests themselves.

Directives:
- Use `pytest` fixtures for setting up environments and creating test objects.
- Use `@pytest.fixture()` with parentheses.
- Define fixtures at the appropriate scope (e.g., `function`, `module`, `session`).
- Include descriptive docstrings and type hints for all fixtures.
- Define common fixtures in base test modules or `conftest.py`.
- Organize fixtures under a `# Fixtures` header comment.

Example:
```python # pseudocode
# Fixtures
@pytest.fixture()
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

Use mocks, stubs, and fakes to isolate the code under test.

### Rationale
Test doubles are recommended to prevent unit tests from depending on external systems, improve test speed, and enable verification of edge cases.

Directives:
- Use the appropriate type of test double (Stub, Mock, Fake, Spy) for the situation.
- Use `pytest`'s `monkeypatch` fixture for simple patching.
- Use `unittest.mock` for creating complex mock objects and verifying interactions.
- Ensure test doubles are reset or torn down after use.

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

Use `@pytest.mark.parametrize` to run a test with multiple sets of data.

### Rationale
Parameterization is required to reduce code duplication and ensure that a wide range of inputs is verified systematically.

Directives:
- Use the `ids` parameter to provide descriptive names for each test case.
- Apply parameterization for data-driven tests, edge case validation, and cross-implementation testing.

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

Use `pytest-asyncio` for testing asynchronous code.

### Rationale
Asynchronous tests are required to ensure that `async` functions and event loops are handled correctly.

Directives:
- Mark async tests with `@pytest.mark.asyncio`.
- Handle `NotImplementedError` or `AttributeError` by skipping the test if the functionality is not applicable to the target.

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

Use markers to skip tests that cannot be run in certain environments.

### Rationale
Explicitly skipping tests is required to prevent build failures due to environment-specific limitations while still tracking test coverage.

Directives:
- Use `pytest.skip` within a test or fixture when execution is impossible.
- Provide a clear, descriptive reason for skipping.

Example:
```python # pseudocode
def test_conditional_feature(self, test_object: BaseObject) -> None:
    """Tests a feature that may not be present."""
    if not hasattr(test_object, "special_feature"):
        pytest.skip("Test object does not have the special feature.")

    assert test_object.special_feature() == "success"
```

### 4.7 Testing Exceptions

Use `pytest.raises()` to verify that the correct exceptions are raised.

### Rationale
Explicit exception verification is required to ensure that error handling logic behaves as expected.

Directives:
- Use `pytest.raises` as a context manager.
- Specify the most specific exception type possible.
- Use the `match` parameter to verify the exception message.

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

Execute tests using the `pytest` command or through Nox.

### Rationale
Standardizing test execution is required to ensure that all developers and CI systems run the same set of tests in a consistent environment.

Directives:
- Ensure tests are runnable using `pytest` and provide clear feedback.
- Verify that tests clean up resources and do not depend on execution order.
- Use `nox -s tests` for automated multi-environment testing.

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
