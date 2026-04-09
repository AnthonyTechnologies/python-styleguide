# Anthony's Python Style Guide: Exceptions and Error Messages

Use exceptions to handle error conditions and provide meaningful feedback.

### Rationale
Clear and consistent exception handling is required to ensure that errors are predictable, easy to debug, and do not lead to silent failures.

## Table of Contents

- [1 Exceptions](#1-exceptions)
- [2 Error Messages](#2-error-messages)
- [3 Exception Message Formatting](#3-exception-message-formatting)


## 1 Exceptions

Follow these directives for using and defining exceptions.

### Rationale
Proper exception usage is required to maintain the integrity of application logic and to provide clear signals when a program enters an invalid state.

Directives:
- Use built-in exception classes when appropriate (e.g., `ValueError` for invalid arguments).
- Do not use `assert` statements for critical application logic or precondition validation. `assert` must be limited to tests and non-critical checks.
- Suffix custom exception names with `Error`.
- Inherit custom exceptions from existing exception classes.
- Avoid catch-all `except:` statements. Do not catch `Exception` unless re-raising or creating a documented isolation point.
- Keep `try` blocks as small as possible to avoid hiding unrelated errors.
- Use `finally` for required cleanup operations.

Compliant:
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
      msg = f'Min. port must be at least 1024, not {minimum}.'
      raise ValueError(msg)
    port = self._find_next_open_port(minimum)
    if port is None:
        msg = f'Could not connect to service on port {minimum} or higher.'
        raise ConnectionError(msg)
    # The code does not depend on the result of this assert.
    msg = f'Unexpected port {port} when minimum was {minimum}.'
    assert port >= minimum, msg
    return port
```

Non-Compliant:
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

Directives:
- Suffix custom exception names with `Error`.
- Inherit custom exceptions from existing exception classes.
- Avoid introducing repetition in the name (e.g., use `FooError` not `foo.FooError` if the package name is `foo`).
- Avoid catch-all `except:` statements. Do not catch `Exception` unless re-raising or creating a documented isolation point.
- Keep `try` blocks as small as possible to avoid hiding unrelated errors.
- Use `finally` for required cleanup operations.

## 2 Error Messages

Follow these directives for formatting and content of error messages.

### Rationale
Clear and specific error messages are required to provide actionable information to developers and users.

Directives:
- Match the message precisely to the actual error condition.
- Store the error message in a local variable named `msg` before passing to the exception or warning.
- Use f-strings within the `msg` variable for clarity and consistency.
- Avoid redundant information already present in the traceback.
- Be specific about what was expected and what was received.
- Start with a capital letter and avoid a period for short, single-sentence messages.

Compliant:
```python # pseudocode
msg = f"Expected a positive integer, got {value}"
raise ValueError(msg)

msg = f"Expected str, got {type(value).__name__}"
raise TypeError(msg)
```

Non-Compliant:
```python # pseudocode
# PROBLEM: Message not stored in 'msg' variable
raise ValueError(f"Expected a positive integer, got {value}")

# PROBLEM: Non-specific and not using 'msg' variable
raise ValueError("Value must be positive.")
```

Compliant:
```python # pseudocode
# Minimal context
import os
import logging
logging.basicConfig(level=logging.INFO)
p = 0.5
workdir = "."

if not 0 <= p <= 1:
    msg = f'Not a probability: {p}'
    raise ValueError(msg)

try:
    os.rmdir(workdir)
except OSError as error:
    msg = 'Could not remove directory (reason: %r): %r'
    logging.warning(msg, error, workdir)
```

Non-Compliant:
```python # pseudocode
import os
import logging
p = 0.5
workdir = "."

if p < 0 or p > 1:  # PROBLEM: also false for float('nan')!
    msg = f'Not a probability: {p}'
    raise ValueError(msg)

try:
    os.rmdir(workdir)
except OSError:
    # PROBLEM: Message makes an assumption that might not be true.
    # PROBLEM: Not using 'msg' variable
    logging.warning('Directory already was deleted: %s', workdir)
```

