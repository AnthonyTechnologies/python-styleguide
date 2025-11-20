# Anthony's Python Style Guide: Files, Sockets, and Similar Stateful Resources

## Table of Contents

- [1 Rationale](#1-rationale)
- [2 Preferred Pattern](#2-preferred-pattern)
- [3 Alternatives](#3-alternatives)
- [4 Documentation Requirement](#4-documentation-requirement)


## 1 Rationale

Explicitly close files and sockets when done with them. This rule naturally extends to closeable resources that
internally use sockets, such as database connections, and also other resources that need to be closed down in a similar
fashion. To name only a few examples, this also includes mmap mappings, h5py File objects, and matplotlib.pyplot figure
windows.

Leaving files, sockets or other such stateful objects open unnecessarily has many downsides:

- They may consume limited system resources, such as file descriptors. Code that deals with many such objects may exhaust those resources unnecessarily if they're not returned to the system promptly after use.
- Holding files open may prevent other actions such as moving or deleting them, or unmounting a filesystem.
- Files and sockets that are shared throughout a program may inadvertently be read from or written to after logically being closed. If they are actually closed, attempts to read or write from them will raise exceptions, making the problem known sooner.

Furthermore, while files and sockets (and some similarly behaving resources) are automatically closed when the object is
destructed, coupling the lifetime of the object to the state of the resource is poor practice:

- There are no guarantees as to when the runtime will actually invoke the `__del__` method. Different Python implementations use different memory management techniques, such as delayed garbage collection, which may increase the object's lifetime arbitrarily and indefinitely.
- Unexpected references to the file, e.g. in globals or exception tracebacks, may keep it around longer than intended.
- Relying on finalizers to do automatic cleanup that has observable side effects has been rediscovered over and over again to lead to major problems, across many decades and multiple languages (see e.g. this article for Java).

## 2 Preferred Pattern

The preferred way to manage files and similar resources is using the `with` statement:

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

In rare cases where context-based resource management is infeasible, code documentation must explain clearly how
resource lifetime is managed.

