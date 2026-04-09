# Anthony's Python Style Guide: Docstrings

Use docstrings to document packages, modules, classes, and functions. A docstring is a string that must be the first statement in the entity. Docstrings follow the Google style by default, with specific requirements detailed below.

### Rationale
High-quality docstrings are required to ensure that code is self-documenting and to support automated documentation generation and IDE features.

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

Write all docstrings in the third-person.

### Rationale
Using a consistent third-person perspective is required to maintain a professional and objective tone across all documentation.

Directives:
- Use the third-person declarative mood for summary lines and feature descriptions (e.g., "Returns the name").
- Use the third-person imperative mood when providing instructions or requirements (e.g., "The user must call this method"). Instructions must be active and issued as commands.

Compliant (Declarative):
```python # pseudocode
def get_name(self) -> str:
    """Returns the name of the object."""
    return self.name
```

Compliant (Imperative):
```python # pseudocode
def setup(self) -> None:
    """Sets up the object.

    The user must call this method before using any other methods of this object.
    """
    ...
```


## 2 Modules

Include a docstring at the beginning of every module.

### Rationale
Module-level documentation is required to provide an immediate overview of a file's purpose and contents.

Directives:
- Include license boilerplate as the first section if required.
- Set the first line of the docstring to the exact file name.
- Provide a one-line summary on the second line, terminated by a period.
- Leave the third line blank.
- Include a detailed description starting from the fourth line.

Compliant:
```python # pseudocode
"""file_name.py
One-line summary of the module or program, terminated by a period.

Detailed description of the module or program. Logical sections should be separated 
by blank lines.
"""
```


## 3 Classes

Provide a docstring below the class definition describing the class. Document all attributes (excluding properties) in an `Attributes:` section and follow the same formatting as a function's `Args:` section.

### Rationale
Class docstrings are required to define the responsibility of a class and document its attributes for clear usage.

Directives:
- Start all class docstrings with a one-line summary.
- Describe what the class instance represents.
- Ensure subclasses of `Exception` describe what the exception represents, not the context in which it occurs.
- Avoid repeating unnecessary information, such as stating that the class is a class.

Compliant:
```python # pseudocode
class CheeseShopAddress:
    """The address of a cheese shop."""

class OutOfCheeseError(Exception):
    """No more cheese is available."""
```

Non-Compliant:
```python # pseudocode
class CheeseShopAddress:
    """Class that describes the address of a cheese shop."""

class OutOfCheeseError(Exception):
    """Raised when no more cheese is available."""
```


## 4 Functions and Methods

In this section, "function" refers to a method, function, generator, or property.

### Rationale
Function docstrings are required to specify the interface, including parameters, return values, and potential exceptions, enabling developers to use the function without reading its implementation.

Directives:
- Include a mandatory docstring for every function that is part of the public API, has a nontrivial size, or contains non-obvious logic.
- Provide enough information to write a call to the function. Describe calling syntax and semantics.
- Avoid implementation details unless they are relevant to how the function is used.
- Use the third-person declarative voice for summaries and return descriptions.
- Use the same style for a `@property` docstring as for an attribute.
- Document specific aspects in sections: `Args:`, `Returns:`, `Yields:`, and `Raises:`.
- Maintain a hanging indent of four spaces for all sections.

**Args:**
List each parameter by name. Follow the name with a description, separated by a colon.

**Returns:** (or **Yields:** for generators)
Describe the semantics of the return value. This section is not required if the function only returns `None`.

**Raises:**
List all exceptions relevant to the interface followed by a description.

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
                msg = f"Required key {key} not found"
                raise IOError(msg)
        except Exception as e:
            msg = f"Error accessing table: {e}"
            raise IOError(msg)
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
            msg = f"Required key {k!r} not found"
            raise IOError(msg)
    return result
```

### 4.1 Overridden Methods

A method that overrides a base class method does not require a docstring if it is decorated with `@override`.

### Rationale
Reducing documentation redundancy is recommended when the base class docstring already accurately describes the method's contract.

Directives:
- Use the `@override` decorator for overridden methods.
- Provide a docstring if the overriding method materially refines the contract or has additional side effects.

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

Use a docstring and omit the `pass` statement when defining empty classes, methods, or functions.

### Rationale
Using a docstring instead of `pass` is recommended to provide context for why the entity is empty.

Compliant:
```python # pseudocode
class EmptyClass:
    """An empty class."""


def empty_function():
    """An empty function."""
```

Non-Compliant:
```python # pseudocode
class EmptyClass:
    pass


def empty_function():
    pass
```

## 6 Standard Templates

Use the following templates for common methods and structures to ensure consistency across the codebase.

### Rationale
Standardized templates are required to maintain a uniform documentation style and quality.

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
