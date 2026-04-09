# Anthony's Python Style Guide: Logging

Use standardized logging patterns to ensure that log messages are efficient, queryable, and consistent.

### Rationale
Structured logging is required to support automated log analysis and to optimize performance by avoiding unnecessary string rendering.

## Table of Contents

- [1 Logging Message Patterns](#1-logging-message-patterns)


## 1 Logging Message Patterns

Use string literals with %-placeholders for logging functions that expect a pattern-string.

### Rationale
Using pattern-strings with subsequent arguments is required because many logging implementations collect the unexpanded pattern as a queryable field. This practice also prevents rendering overhead for messages below the active logging level.

Directives:
- Store the logging pattern in a local variable named `msg` before calling logging functions.
- Use string literals with %-placeholders for the `msg` variable to support lazy evaluation.
- Do not use f-strings for the `msg` variable in logging calls.
- Provide pattern parameters as subsequent arguments to the logging function.

Compliant:
```python # pseudocode
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

msg = 'Module name: %s'
logger.info(msg, __name__)
```
```python # pseudocode
import logging
import os

logging.basicConfig(level=logging.INFO)

msg = 'Current $PAGER is: %s'
logging.info(msg, os.getenv('PAGER', default=''))

homedir = os.getenv('HOME')
if homedir is None or not os.access(homedir, os.W_OK):
  msg = 'Cannot write to home directory, $HOME=%r'
  logging.error(msg, homedir)
```

Non-Compliant:
```python # pseudocode
import os
import logging

# PROBLEM: Not using a 'msg' variable
logging.info('Current $PAGER is: %s', os.getenv('PAGER', default=''))

# PROBLEM: Message split across multiple calls
logging.info('Current $PAGER is:')
logging.info(os.getenv('PAGER', default=''))

# PROBLEM: Using f-string for logging (prevents lazy evaluation)
homedir = os.getenv('HOME')
if homedir is None or not os.access(homedir, os.W_OK):
  msg = f'Cannot write to home directory, $HOME={homedir!r}'
  logging.error(msg)
```

