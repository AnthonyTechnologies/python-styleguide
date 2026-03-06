# Anthony's Python Style Guide: Exceptions and Error Messages

## Table of Contents

- [1 Exceptions](#1-exceptions)
- [2 Error Messages](#2-error-messages)


## 1 Exceptions

Ensure exceptions follow these conditions:

Use built-in exception classes when appropriate. For example, raise a `ValueError` to indicate a programming mistake like a violated precondition, such as when validating function arguments.

Do not use `assert` statements in place of conditionals or for validating preconditions. Ensure they are not critical to the application logic. A litmus test is that the `assert` can be removed without breaking the code. Remember that `assert` conditionals are not guaranteed to be evaluated. For `pytest` based tests, `assert` is permitted and expected to verify expectations.

Examples:

Correct:
```python # pseudocode
# Setup minimal context so this snippet runs
import logging
import os
logging.basicConfig(level=logging.INFO)

def connect_to_next_port(self, minimum: int) -> int:
    """Connects to the next available port.

    Args:
        minimum: A port value greater or equal to 1024.

    Returns:
        The new minimum port.

    Raises:
        ConnectionError: If no available port is found.
    """
    if minimum < 1024:
      # Note that this raising of ValueError is not mentioned in the doc
      # string's "Raises:" section because it is not appropriate to
      # guarantee this specific behavioral reaction to API misuse.
      raise ValueError(f'Min. port must be at least 1024, not {minimum}.')
    port = self._find_next_open_port(minimum)
    if port is None:
        raise ConnectionError(
            f'Could not connect to service on port {minimum} or higher.')
    # The code does not depend on the result of this assert.
    assert port >= minimum, (f'Unexpected port {port} when minimum was {minimum}.')
    return port
```

Incorrect:
```python # pseudocode
# Setup minimal context so this snippet runs
import logging
import os

def connect_to_next_port(self, minimum: int) -> int:
    """Connects to the next available port.

    Args:
        minimum: A port value greater or equal to 1024.

    Returns:
        The new minimum port.
    """
    assert minimum >= 1024, 'Minimum port must be at least 1024.'
    # The following code depends on the previous assert.
    port = self._find_next_open_port(minimum)
    assert port is not None
    # The type checking of the return statement relies on the assert.
    return port
```

Libraries or packages may define their own exceptions. When doing so, inherit from an existing exception class. End exception names in `Error` and avoid introducing repetition (e.g., use `FooError` not `foo.FooError` if the package name is already `foo`).

Never use catch-all `except:` statements, and avoid catching `Exception` or `StandardError` except in the following cases:
- Re-raising the exception.
- Creating an isolation point in the program where exceptions are recorded and suppressed rather than propagated, such as protecting a thread from crashing by guarding its outermost block.

Python's tolerance means `except:` catches everything, including misspelled names, `sys.exit()` calls, Ctrl+C interrupts, and `unittest` failures; avoid catching these unexpectedly.

Minimize the amount of code in a `try`/`except` block. The larger the body of the `try`, the more likely an exception will be raised by a line of code that was not expected to raise one, potentially hiding a real error.

Use the `finally` clause to execute code whether or not an exception is raised in the `try` block. This is useful for cleanup, such as closing a file.

## 2 Error Messages
Follow these guidelines for error messages (such as message strings on exceptions like `ValueError` or messages shown to the user):

1. Match the message precisely to the actual error condition.
2. Ensure interpolated pieces are always clearly identifiable.
3. Ensure they allow simple automated processing (e.g., grepping).

Correct:
```python # pseudocode
# Minimal context
import os
import logging
logging.basicConfig(level=logging.INFO)
p = 0.5
workdir = "."

if not 0 <= p <= 1:
    raise ValueError(f'Not a probability: {p}')

try:
    os.rmdir(workdir)
except OSError as error:
    logging.warning('Could not remove directory (reason: %r): %r', error, workdir)
```

Incorrect:
```python # pseudocode
import os
import logging
p = 0.5
workdir = "."

if p < 0 or p > 1:  # PROBLEM: also false for float('nan')!
    raise ValueError(f'Not a probability: {p}')

try:
    os.rmdir(workdir)
except OSError:
    # PROBLEM: Message makes an assumption that might not be true:
    # Deletion might have failed for some other reason, misleading
    # whoever has to debug this.
    logging.warning('Directory already was deleted: %s', workdir)

try:
    os.rmdir(workdir)
except OSError:
    # PROBLEM: The message is harder to grep for than necessary, and
    # not universally non-confusing for all possible values of `workdir`.
    # Imagine someone calling a library function with such code
    # using a name such as workdir = 'deleted'. The warning would read:
    # "The deleted directory could not be deleted."
    logging.warning('The %s directory could not be deleted.', workdir)
```

