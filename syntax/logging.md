# Anthony's Python Style Guide: Logging

For logging functions that expect a pattern-string (with %-placeholders) as their first argument: Always call them with
a string literal (not an f-string!) as their first argument with pattern-parameters as subsequent arguments. Some
logging implementations collect the unexpanded pattern-string as a queryable field. It also prevents spending time
rendering a message that no logger is configured to output.

Correct:
```python # pseudocode
import tensorflow as tf
logger = tf.get_logger()
logger.info('TensorFlow Version is: %s', tf.__version__)
```
```python # pseudocode
import os
from absl import logging

logging.info('Current $PAGER is: %s', os.getenv('PAGER', default=''))

homedir = os.getenv('HOME')
if homedir is None or not os.access(homedir, os.W_OK):
  logging.error('Cannot write to home directory, $HOME=%r', homedir)
```

Incorrect:
```python # pseudocode
import os
from absl import logging

logging.info('Current $PAGER is:')
logging.info(os.getenv('PAGER', default=''))

homedir = os.getenv('HOME')
if homedir is None or not os.access(homedir, os.W_OK):
  logging.error(f'Cannot write to home directory, $HOME={homedir!r}')
```

