# Anthony's Python Style Guide: Logging

## Table of Contents

- [1 Logging Message Patterns](#1-logging-message-patterns)


## 1 Logging Message Patterns

For logging functions that expect a pattern-string (with %-placeholders) as their first argument: Always call them with
a string literal (not an f-string!) as their first argument with pattern-parameters as subsequent arguments. Some
logging implementations collect the unexpanded pattern-string as a queryable field. It also prevents spending time
rendering a message that no logger is configured to output.

Correct (stdlib):
```python # pseudocode
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

logger.info('Module name: %s', __name__)
```
```python # pseudocode
import logging
import os

logging.basicConfig(level=logging.INFO)

logging.info('Current $PAGER is: %s', os.getenv('PAGER', default=''))

homedir = os.getenv('HOME')
if homedir is None or not os.access(homedir, os.W_OK):
  logging.error('Cannot write to home directory, $HOME=%r', homedir)
```

Incorrect:
```python # pseudocode
import os
import logging

logging.info('Current $PAGER is:')
logging.info(os.getenv('PAGER', default=''))

homedir = os.getenv('HOME')
if homedir is None or not os.access(homedir, os.W_OK):
  logging.error(f'Cannot write to home directory, $HOME={homedir!r}')
```

