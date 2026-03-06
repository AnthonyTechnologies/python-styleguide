# Anthony's Python Style Guide: Docstrings

Python uses docstrings to document code. A docstring is a string that is the first statement in a package, module,
class, or function. These strings can be extracted automatically through the `__doc__` member of the object and are used
by pydoc. (For example, run pydoc on a module to preview the output.) Always use the three-double-quote `"""` format for
docstrings (per PEP 257). A docstring should be organized as a summary line (one physical line not exceeding 120
characters) terminated by a period, question mark, or exclamation point. When writing more (encouraged), this must be
followed by a blank line, followed by the rest of the docstring starting at the same cursor position as the first quote
of the first line. There are more formatting guidelines for docstrings below. Be sure to use the right style for module,
function, method docstrings, and inline comments.

All docstrings and comments should be written in the third-person and use the Google style docstrings throughout the
project.

## Table of Contents

- [1 Writing Style](#1-writing-style)
- [2 Modules](#2-modules)
- [3 Classes](#3-classes)
- [4 Functions and Methods](#4-functions-and-methods)
    - [4.1 Overridden Methods](#41-overridden-methods)
- [5 Empty Classes, Methods, and Functions](#5-empty-classes-methods-and-functions)
- [6 Standard Templates](#6-standard-templates)
    - [6.1 Module Level](#61-module-level)
    - [6.2 Class Level](#62-class-level)
    - [6.3 Method Templates](#63-method-templates)
    - [6.4 Common Argument Descriptions](#64-common-argument-descriptions)


## 1 Writing Style

The writing style should be in the third-person. When explaining features and how things work, use the
third-person descriptive voice. When instructing users on how to use things, use the third-person imperative voice
that is active and issued as commands.

### 1.1 Third-Person Descriptive Voice

Use the third-person descriptive voice to explain the behavior of functions, classes, and other features. This typically
involves using the third-person singular present tense.

Example:
```python # pseudocode
def get_name(self) -> str:
    """Returns the name of the object."""
    return self.name
```

### 1.2 Third-Person Imperative Voice

Use the third-person imperative voice when providing instructions or requirements to the user or subclasses. The
voice should be active and be issued as commands. This typically involves using words like "must," "should," or "shall"
with a third-person subject.

Example:
```python # pseudocode
def setup(self) -> None:
    """Sets up the object.

    The user must call this method before using any other methods of this object.
    """
    ...
```


## 2 Modules

Include license boilerplate in every file. Choose the appropriate boilerplate for the license used by the project (for example, Apache 2.0, BSD, LGPL, GPL).

Guidelines:
- Set the first line of the module to the file name exactly as it is in the file system (typically lowercase).
- Set the second line to a one-line summary of the module or program, terminated by a period.
- Leave the third line blank.
- Include a detailed description of the module or program starting from the fourth line.

```python # pseudocode
"""file_name.py
A one-line summary of the module or program, terminated by a period.

Leave one blank line. The rest of this docstring should contain an overall description of the module or program. The
description can be broken up into multiple paragraphs to present the functionality into logical sections. Bullet-point
and numerical lists may be used as well, but only add them if they are needed.
"""
```


## 3 Classes
Provide a docstring below the class definition describing the class. Document all attributes (excluding properties) in an Attributes section and follow the same formatting as a function's Args section.

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

Start all class docstrings with a one-line summary that describes what the class instance represents. Ensure subclasses of `Exception` also describe what the exception represents, not the context in which it might occur. Avoid repeating unnecessary information in the class docstring, such as stating that the class is a class.

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


## 4 Functions and Methods

In this section, "function" means a method, function, generator, or property.

Include a mandatory docstring for every function that has one or more of the following properties:

- being part of the public API
- nontrivial size
- non-obvious logic

Provide enough information in the docstring to write a call to the function without reading the function's code. Describe the function's calling syntax and its semantics, but generally avoid implementation details unless they are relevant to how the function is used. For example, if a function mutates one of its arguments as a side effect, note that in its docstring. Otherwise, express subtle but important implementation details not relevant to the caller as comments alongside the code rather than within the docstring.

Use descriptive-style docstrings (e.g., `"""Fetches rows from a Bigtable."""`). Use the same style for a `@property` data descriptor's docstring as the docstring for an attribute or a function argument (e.g., `"""The Bigtable path."""`, rather than `"""Returns the Bigtable path."""`).

Document certain aspects of a function in special sections, listed below. End each section heading line with a colon. Maintain a hanging indent of four spaces for all sections other than the heading. Omit these sections if the function's name and signature are informative enough to be aptly described using a one-line docstring.

**Args:**
List each parameter by name. Follow the name with a description, separated by a colon and either a space or newline. Use a hanging indent of 4 spaces more than the parameter name if the description is too long to fit on a single 120-character line. Include required type(s) if the code does not contain a corresponding type annotation. List variable length argument lists (`*foo`) and arbitrary keyword arguments (`**bar`) if the function accepts them.

**Returns:** (or **Yields:** for generators)
Describe the semantics of the return value, including any type information that the type annotation does not provide. This section is not required if the function only returns `None`. Also, omit it if the docstring starts with "Return", "Returns", "Yield", or "Yields" (e.g., `"""Returns row from Bigtable as a tuple of strings."""`) and the opening sentence is sufficient to describe the return value. Do not imitate older 'NumPy style', which frequently documents a tuple return value as multiple return values with individual names. Instead, describe such a return value as: "Returns: A tuple (mat_a, mat_b), where mat_a is ..., and ...". Ensure auxiliary names in the docstring do not necessarily correspond to internal names used in the function body. For generators, use the `Yields:` section to document the object returned by `next()`, instead of the generator object itself.

**Raises:**
List all exceptions relevant to the interface followed by a description. Use a similar exception name + colon + space or newline and hanging indent style as described in `Args:`. Do not document exceptions if the API specified in the docstring is violated.

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

### 4.1 Overridden Methods
A method that overrides a method from a base class does not need a docstring if it is explicitly decorated with
`@override` (from typing_extensions or typing modules), unless the overriding method's behavior materially refines the
base method's contract, or details need to be provided (e.g., documenting additional side effects), in which case a
docstring with at least those differences is required on the overriding method.

```python # pseudocode
# Portable no-op `override` decorator so this snippet runs without third-party deps.
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

## 5 Empty Classes, Methods, and Functions

When defining an empty class, method, or function, use a docstring to define it and omit the `pass` statement.

Correct:
```python # pseudocode
class EmptyClass:
    """An empty class."""


def empty_function():
    """An empty function."""
```

Incorrect:
```python # pseudocode
class EmptyClass:
    pass


def empty_function():
    pass
```

## 6 Standard Templates

To ensure consistency across the codebase, the following templates should be used for common methods and structures.

### 6.1 Module Level

#### Module File Header
```python
"""[filename.py]
[Short Module Summary]

[Extended Description of module contents and purpose]
"""
```

### 6.2 Class Level

#### Standard Class
```python
class [ClassName]:
    """[Short Class Summary]

    [Extended Description]

    Attributes:
        [attribute_name]: [Description]
    """
```

### 6.3 Method Templates

#### Constructor (`__init__`)
```python
    def __init__(self, *args, **kwargs) -> None:
        """Initializes a new [ClassName] instance.

        Args:
            *args: [Description of positional arguments]
            **kwargs: [Description of keyword arguments]
        """
```

#### Constructor (`construct`)
```python
    def construct(self, *args, **kwargs) -> None:
        """Constructs this object with the given arguments.

        Args:
            *args: [Description of positional arguments]
            **kwargs: [Description of keyword arguments]
        """
```

#### Shallow Copy (`copy` or `__copy__`)
```python
    def copy(self) -> Any:
        """Creates a shallow copy of this object.

        Returns:
            A shallow copy of this object.
        """
```

#### Deep Copy (`deepcopy` or `__deepcopy__`)
```python
    def deepcopy(self, memo: dict | None = None) -> Any:
        """Creates a deep copy of this object.

        Args:
            memo: A dictionary that maps object IDs to their copies.

        Returns:
            A deep copy of this object.
        """
```

#### Pickle State Getter (`__getstate__`)
```python
    def __getstate__(self) -> dict[str, Any]:
        """Gets the object's state for pickling.

        Returns:
            The state of the object.
        """
```

#### Pickle State Setter (`__setstate__`)
```python
    def __setstate__(self, state: Any) -> None:
        """Sets the object's state from a pickled state.

        Args:
            state: An object which can be used to set the state of this object.
        """
```

#### Property Getter
```python
    @property
    def [property_name](self) -> [Type]:
        """The [noun phrase description of the property]."""
```

#### Property Setter
```python
    @[property_name].setter
    def [property_name](self, value: [Type]) -> None:
        self._[property_name] = value
```
*(Note: Setters often do not have docstrings in this codebase if the getter is documented, or they simply implement the logic. If one is needed, usage of "Sets the [property name]..." is appropriate.)*

#### Clear Method
```python
    def clear(self) -> None:
        """Clears the contents of the [object type]."""
```

#### Representation (`__repr__`)
```python
    def __repr__(self) -> str:
        """Returns the string representation of this object.

        Returns:
            The string representation of this object.
        """
```

### 6.4 Common Argument Descriptions

*   `*args`: "Arguments for inheritance." (common in mixins/bases)
*   `**kwargs`: "Keyword arguments for inheritance." (common in mixins/bases)
*   `func`: "The function to wrap." (for decorators)
*   `instance`: "The object to bind to." (for descriptors)
*   `owner`: "The class of the object." (for descriptors)
