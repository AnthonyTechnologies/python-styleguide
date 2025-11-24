# Anthony's Python Style Guide: Docstrings

Python uses docstrings to document code. A docstring is a string that is the first statement in a package, module,
class, or function. These strings can be extracted automatically through the `__doc__` member of the object and are used
by pydoc. (For example, run pydoc on a module to preview the output.) Always use the three-double-quote `"""` format for
docstrings (per PEP 257). A docstring should be organized as a summary line (one physical line not exceeding 120
characters) terminated by a period, question mark, or exclamation point. When writing more (encouraged), this must be
followed by a blank line, followed by the rest of the docstring starting at the same cursor position as the first quote
of the first line. There are more formatting guidelines for docstrings below. Be sure to use the right style for module,
function, method docstrings, and inline comments.

All docstrings should be written in the declarative voice, not imperative and use the Google style docstrings throughout
the project.

## Table of Contents

- [1 Modules](#1-modules)
- [2 Classes](#2-classes)
- [3 Functions and Methods](#3-functions-and-methods)
    - [3.1 Overridden Methods](#31-overridden-methods)


## 1 Modules

Every file should contain license boilerplate. Choose the appropriate boilerplate for the license used by the project
(for example, Apache 2.0, BSD, LGPL, GPL).

Guidelines:
- The first line of the module should be file name exactly as it is in the file system (typically lowercase)
- The second line should be a one-line summary of the module or program, terminated by a period
- The third line should be blank
- Starting from the fourth line, the rest of docstring should include a detailed description of the module or program

```python # pseudocode
"""file_name.py
A one-line summary of the module or program, terminated by a period.

Leave one blank line. The rest of this docstring should contain an overall description of the module or program. The
description can be broken up into multiple paragraphs to present the functionality into logical sections. Bullet-point
and numerical lists may be used as well, but only add them if they are needed.
"""
```


## 2 Classes
Classes should have a docstring below the class definition describing the class. All attributes, excluding
properties, should be documented here in an Attributes section and follow the same formatting as a function's Args
section.

```python # pseudocode
from typing import ClassVar

class ExampleClass:
    """An example class.

    This example class outlines how a class should be formatted and structured. It provides examples of how attributes,
    methods, and docstrings should be implemented. Furthermore, it demonstrates the class's implementation structure.
    Particularly, the grouping of attributes and methods into different sections.

    Attributes:
        _protected: A protected attribute.
        integer: An integer to track.
        floating_point: A floating point number to track.
    """
    # Class Attributes #
    class_attribute: ClassVar[int] = 10

    # Class Methods #
    @classmethod
    def class_method(cls) -> None:
        """Prints the class attribute."""
        print(cls.class_attribute)

    # Attributes #
    _protected: bool
    integer: int
    floating_point: float = 1.0

    # Properties #
    @property
    def floating_point_inverse(self) -> float:
        """The inverse of the floating point number."""
        return 1 / self.floating_point

    # Magic Methods #
    # Construction/Destruction #
    def __init__(self, is_protected: bool = True):
        """Initializes the instance based on spam preference.

        Args:
            is_protected: Determines if the attribute is protected.
        """
        self._protected = is_protected
```

All class docstrings should start with a one-line summary that describes what the class instance represents. This
implies that subclasses of Exception should also describe what the exception represents, and not the context in which it
might occur. The class docstring should not repeat unnecessary information, such as that the class is a class.

Correct:
```python # pseudocode
class CheeseShopAddress:
    """The address of a cheese shop.

    ...
    """

class OutOfCheeseError(Exception):
    """No more cheese is available."""
```

Incorrect:
```python # pseudocode
class CheeseShopAddress:
    """Class that describes the address of a cheese shop.

    ...
    """

class OutOfCheeseError(Exception):
    """Raised when no more cheese is available."""
```


## 3 Functions and Methods

In this section, "function" means a method, function, generator, or property.

A docstring is mandatory for every function that has one or more of the following properties:

- being part of the public API
- nontrivial size
- non-obvious logic

A docstring should give enough information to write a call to the function without reading the function's code. The
docstring should describe the function's calling syntax and its semantics, but generally not its implementation details,
unless those details are relevant to how the function is to be used. For example, a function that mutates one of its
arguments as a side effect should note that in its docstring. Otherwise, subtle but important details of a function's
implementation that are not relevant to the caller are better expressed as comments alongside the code than within the
function's docstring.

The docstring may be descriptive-style (`"""Fetches rows from a Bigtable."""`). The docstring for a `@property` data
descriptor should use the same style as the docstring for an attribute or a function argument
(`"""The Bigtable path."""`, rather than `"""Returns the Bigtable path."""`).

Certain aspects of a function should be documented in special sections, listed below. Each section begins with a heading
line, which ends with a colon. All sections other than the heading should maintain a hanging indent of two or four
spaces (be consistent within a file). These sections can be omitted in cases where the function's name and signature are
informative enough that it can be aptly described using a one-line docstring.

**Args:**
List each parameter by name. A description should follow the name, and be separated by a colon followed by either a
space or newline. If the description is too long to fit on a single 120-character line, use a hanging indent of 2 or 4
spaces more than the parameter name (be consistent with the rest of the docstrings in the file). The description should
include required type(s) if the code does not contain a corresponding type annotation. If a function accepts `*foo`
(variable length argument lists) and/or `**bar` (arbitrary keyword arguments), they should be listed as `*foo` and
`**bar`.

**Returns:** (or **Yields:** for generators)
Describe the semantics of the return value, including any type information that the type annotation does not provide. If
the function only returns None, this section is not required. It may also be omitted if the docstring starts with
"Return", "Returns", "Yield", or "Yields" (e.g. `"""Returns row from Bigtable as a tuple of strings."""`) and the
opening sentence is sufficient to describe the return value. Do not imitate older 'NumPy style' (example), which
frequently documented a tuple return value as if it were multiple return values with individual names (never mentioning
the tuple). Instead, describe such a return value as: "Returns: A tuple (mat_a, mat_b), where mat_a is …, and …". The
auxiliary names in the docstring need not necessarily correspond to any internal names used in the function body (as
those are not part of the API). If the function uses yield (is a generator), the Yields: section should document the
object returned by next(), instead of the generator object itself that the call evaluates to.

**Raises:**
List all exceptions that are relevant to the interface followed by a description. Use a similar exception name + colon +
space or newline and hanging indent style as described in Args:. Exceptions should not be documented if
the API specified in the docstring is violated (because this would paradoxically make behavior under violation of the
API part of the API).

```python # pseudocode
from typing import Mapping, Sequence


class Table:
    """A table data structure for storing and retrieving rows of data.

    Attributes:
        name: The name of the table.
        rows: Dictionary storing the table data.
    """

    # Class Attributes #
    name: str
    rows: Mapping[bytes, tuple[str, ...]]

    # Magic Methods #
    # Construction/Destruction #
    def __init__(self, name: str):
        self.name = name
        self.rows = {}


def fetch_table_rows(
    table_handle: Table,
    keys: Sequence[bytes | str],
    require_all_keys: bool = False,
) -> Mapping[bytes, tuple[str, ...]]:
    """Fetches rows from a Smalltable.

    Retrieves rows pertaining to the given keys from the Table instance represented by table_handle. String keys will be
    UTF-8 encoded.

    Args:
        table_handle: An open Table instance.
        keys: A sequence of strings representing the key of each table row to fetch. String keys will be UTF-8 encoded.
        require_all_keys: If True only rows with values set for all keys will be returned.

    Returns:
        A dict mapping keys to the corresponding table row data fetched. Each row is represented as a tuple of strings.
        For example:

        {b'Serak': ('Rigel VII', 'Preparer'),
         b'Zim': ('Irk', 'Invader'),
         b'Lrrr': ('Omicron Persei 8', 'Emperor')}

        Returned keys are always bytes.  If a key from the keys argument is missing from the dictionary, then that row
        was not found in the table (and require_all_keys must have been False).

    Raises:
        IOError: An error occurred accessing the smalltable.
    """
    result = {}
    for key in keys:
        if isinstance(key, str):
            key = key.encode('utf-8')
        try:
            row = table_handle.rows.get(key)
            if row is not None:
                result[key] = row
            elif require_all_keys:
                raise IOError(f"Required key {key} not found")
        except Exception as e:
            raise IOError(f"Error accessing table: {e}")
    return result
```

Similarly, this variation on Args: with a line break is also allowed:

```python # pseudocode
from typing import Mapping, Sequence


class SmallTable:
    def __init__(self) -> None:
        """Initializes a SmallTable instance."""
        self.rows: dict[bytes, tuple[str, ...]] = {}


def fetch_smalltable_rows(
    table_handle: SmallTable,
    keys: Sequence[bytes | str],
    require_all_keys: bool = False,
) -> Mapping[bytes, tuple[str, ...]]:
    """Fetches rows from a Smalltable.

    Retrieves rows pertaining to the given keys from the Table instance represented by table_handle. String keys will be
    UTF-8 encoded.

    Args:
        table_handle:
        An open SmallTable instance.
        keys:
        A sequence of strings representing the key of each table row to fetch. String keys will be UTF-8 encoded.
        require_all_keys:
        If True only rows with values set for all keys will be returned.

    Returns:
        A dict mapping keys to the corresponding table row data fetched. Each row is represented as a tuple of strings.
        For example:

        {b'Serak': ('Rigel VII', 'Preparer'),
            b'Zim': ('Irk', 'Invader'),
            b'Lrrr': ('Omicron Persei 8', 'Emperor')}

        Returned keys are always bytes.  If a key from the keys argument is missing from the dictionary, then that row was
        not found in the table (and require_all_keys must have been False).

    Raises:
        IOError: An error occurred accessing the smalltable.
    """

    result: dict[bytes, tuple[str, ...]] = {}
    for key in keys:
        k = key.encode("utf-8") if isinstance(key, str) else key
        row = table_handle.rows.get(k)
        if row is not None:
            result[k] = row
        elif require_all_keys:
            raise IOError(f"Required key {k!r} not found")
    return result
```

### 3.1 Overridden Methods
A method that overrides a method from a base class does not need a docstring if it is explicitly decorated with
`@override` (from typing_extensions or typing modules), unless the overriding method's behavior materially refines the
base method's contract, or details need to be provided (e.g., documenting additional side effects), in which case a
docstring with at least those differences is required on the overriding method.

```python # pseudocode
# Portable no-op `override` decorator so this snippet runs without third‑party deps.
def override(func):
    return func

class Parent:
    def do_something(self):
        """Parent method, includes docstring."""
        print("Parent doing something")


# Child class, method annotated with override.
class Child1(Parent):
    @override
    def do_something(self):
        print("Child1 doing something")


# Child class, but without @override decorator, a docstring is required.
class Child2(Parent):
    def do_something(self):
        """Overrides parent's do_something with modified behavior."""
        print("Child2 doing something differently")


# Docstring is trivial, @override is sufficient to indicate that docs can be found in the base class.
class Child3(Parent):
    @override
    def do_something(self):
        """See base class."""
        super().do_something()
        print("Child3 doing additional things")
```
