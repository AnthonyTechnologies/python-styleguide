# Anthony's Python Style Guide: Files, Sockets, and Stateful Resources

Explicitly manage the lifecycle of files, sockets, and other stateful resources.

### Rationale
Proper resource management is required to prevent resource exhaustion, avoid filesystem locks, and ensure that I/O operations are predictable and safe.

## Table of Contents

- [1 Rationale](#1-rationale)
- [2 Preferred Pattern](#2-preferred-pattern)
- [3 Alternatives](#3-alternatives)
- [4 Documentation Requirement](#4-documentation-requirement)
- [5 System and Environment](#5-system-and-environment)
- [6 Dates and Time](#6-dates-and-time)
- [7 Path Management](#7-path-management)


## 1 Resource Management Patterns

Manage files and similar resources using the `with` statement.

### Rationale
Context-based resource management is required to guarantee that resources are closed correctly, even when exceptions occur. Relying on `__del__` or finalizers is unsafe because their execution is not guaranteed by the Python runtime.

Directives:
- Use the `with` statement for all resources that support it.
- Use `contextlib.closing()` for objects that provide a `close()` method but do not support the context manager protocol.
- Do not couple the lifetime of an object to the state of a resource.
- Document the resource management strategy clearly if context-based management is infeasible.

Compliant:
```python # pseudocode
with open("hello.txt") as hello_file:
    for line in hello_file:
        print(line)
```

Compliant:
```python # pseudocode
import contextlib
import urllib.request

with contextlib.closing(urllib.request.urlopen("https://www.python.org/")) as front_page:
    for line in front_page:
        print(line)
```


## 2 System and Environment

### 2.1 Python Version Checking

Use `sys.version_info` for version checks.

### Rationale
Structured version info is required for reliable comparisons across different Python versions and implementations.

Directives:
- Avoid relying on `sys.version` string comparisons.

Compliant:
```python # pseudocode
import sys
if sys.version_info >= (3, 10):
    # logic for Python 3.14+
```

Non-Compliant:
```python # pseudocode
import sys
if sys.version.startswith("3.14"):
    # logic for Python 3.14+
```

## 3 Dates and Time

### 3.1 Timezone-Aware Datetimes

Use timezone-aware datetime objects for all specific points in time.

### Rationale
Timezone awareness is required to prevent ambiguity and errors when handling multiple timezones or Daylight Saving Time transitions.

Compliant:
```python # pseudocode
from datetime import datetime, UTC
now = datetime.now(UTC)
```

Non-Compliant:
```python # pseudocode
from datetime import datetime
now = datetime.now()  # PROBLEM: Returns a naive datetime
```


## 4 Path Management

### 4.1 Pathlib

Use the `pathlib` module for all filesystem path manipulations and access.

### Rationale
`pathlib` is recommended over `os.path` because it provides an intuitive, object-oriented API that is more robust and readable.

Compliant:
```python # pseudocode
from pathlib import Path
workdir = Path("/tmp") / "project"
if workdir.exists():
    for file in workdir.glob("*.txt"):
        print(file.name)
```

Non-Compliant:
```python # pseudocode
import os
workdir = os.path.join("/tmp", "project")
if os.path.exists(workdir):
    for file in os.listdir(workdir):
        if file.endswith(".txt"):
            print(file)
```

