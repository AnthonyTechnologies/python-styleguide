# Anthony's Python Style Guide: Exceptions and Error Messages

## Table of Contents

- [1 Exceptions](#1-exceptions)
- [2 Error Messages](#2-error-messages)


## 1 Exceptions

Exceptions must follow certain conditions:

Make use of built-in exception classes when it makes sense. For example, raise a ValueError to indicate a programming
mistake like a violated precondition, such as may happen when validating function arguments.

Do not use assert statements in place of conditionals or validating preconditions. They must not be critical to the
application logic. A litmus test would be that the assert could be removed without breaking the code. assert
conditionals are not guaranteed to be evaluated. For pytest based tests, assert is okay and expected to verify
expectations.

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

Libraries or packages may define their own exceptions. When doing so they must inherit from an existing exception class.
Exception names should end in Error and should not introduce repetition (foo.FooError).

Never use catch-all `except:` statements, or catch `Exception` or `StandardError`, unless any of the following apply:
- re-raising the exception, or
- creating an isolation point in the program where exceptions are not propagated but are recorded and suppressed instead, such as protecting a thread from crashing by guarding its outermost block.

Python is very tolerant in this regard and `except:` will really catch everything including misspelled names, sys.exit()
calls, Ctrl+C interrupts, unittest failures and all kinds of other exceptions that should not be caught.

Minimize the amount of code in a try/except block. The larger the body of the try, the more likely that an exception
will be raised by a line of code that was not expected to raise an exception. In those cases, the try/except block
hides a real error.

Use the `finally` clause to execute code whether or not an exception is raised in the try block. This is often useful
for cleanup, i.e., closing a file.

## 2 Error Messages
Error messages (such as: message strings on exceptions like ValueError, or messages shown to the user) should follow
three guidelines:

1. The message needs to precisely match the actual error condition.
2. Interpolated pieces need to always be clearly identifiable as such.
3. They should allow simple automated processing (e.g. grepping).

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

