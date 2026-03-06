# Anthony's Python Style Guide: Files, Sockets, and Similar Stateful Resources

## Table of Contents

- [1 Rationale](#1-rationale)
- [2 Preferred Pattern](#2-preferred-pattern)
- [3 Alternatives](#3-alternatives)
- [4 Documentation Requirement](#4-documentation-requirement)


## 1 Rationale

Explicitly close files and sockets when done with them. This rule extends to closeable resources that internally use sockets, such as database connections, and other resources that need to be closed. Examples include `mmap` mappings, `h5py` File objects, and `matplotlib.pyplot` figure windows.

Avoid leaving files, sockets, or other stateful objects open unnecessarily to prevent the following:

- Exhausting limited system resources, such as file descriptors.
- Preventing actions such as moving or deleting files, or unmounting a filesystem.
- Inadvertent reading or writing after logically closing the resource. Actual closing ensures exceptions are raised for such attempts, making the problem known sooner.

Furthermore, do not couple the lifetime of the object to the state of the resource, even if they are automatically closed upon destruction:

- Runtime invocation of the `__del__` method is not guaranteed. Different Python implementations use various memory management techniques, which may increase the object's lifetime indefinitely.
- Unexpected references, such as in globals or exception tracebacks, may keep the resource open longer than intended.
- Avoid relying on finalizers for automatic cleanup with observable side effects, as this often leads to major problems across various languages.

## 2 Preferred Pattern

Manage files and similar resources using the `with` statement:

```python # pseudocode
with open("hello.txt") as hello_file:
    for line in hello_file:
        print(line)
```

## 3 Alternatives

For file-like objects that do not support the `with` statement, use `contextlib.closing()`:

```python # pseudocode
import contextlib
import urllib.request

with contextlib.closing(urllib.request.urlopen("https://www.python.org/")) as front_page:
    for line in front_page:
        print(line)
```

## 4 Documentation Requirement

In rare cases where context-based resource management is infeasible, ensure code documentation explains clearly how resource lifetime is managed.

