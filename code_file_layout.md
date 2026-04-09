# Anthony's Python Style Guide: Code and File Layout

This document establishes the standard structure and layout for Python files. Following these guidelines is required to ensure consistency, making the codebase easier to navigate and maintain.

### Rationale
A uniform file layout reduces cognitive load and allows developers to quickly locate specific sections of a module, such as imports, constants, or class definitions.

## Table of Contents

- [1 General Python File Layout](#1-general-python-file-layout)
    - [1.1 Shebang Line](#11-shebang-line)
    - [1.2 Future Imports](#12-future-imports)
    - [1.3 Module Docstring](#13-module-docstring)
    - [1.4 Header Section](#14-header-section)
    - [1.5 Imports](#15-imports)
    - [1.6 Definitions Section](#16-definitions-section)
        - [1.6.1 Constants](#161-constants)
        - [1.6.2 Functions](#162-functions)
        - [1.6.3 Classes](#163-classes)
            - [1.6.3.1 Static Methods](#1631-static-methods)
            - [1.6.3.2 Class Attributes](#1632-class-attributes)
            - [1.6.3.3 Class Magic Methods](#1633-class-magic-methods)
            - [1.6.3.4 Class Methods](#1634-class-methods)
            - [1.6.3.5 Attributes](#1635-attributes)
            - [1.6.3.6 Properties](#1636-properties)
            - [1.6.3.7 Magic Methods](#1637-magic-methods)
                - [1.6.3.7.1 Magic Method Subcategories](#16371-magic-method-subcategories)
            - [1.6.3.8 Instance Methods](#1638-instance-methods)
                - [1.6.3.8.1 Instance Method Subcategories](#16381-instance-method-subcategories)
            - [1.6.3.9 Getters and Setters](#1639-getters-and-setters)
            - [1.6.3.10 Additional Definitions](#16310-additional-definitions)
    - [1.7 Main](#17-main)
- [2 \_\_init__.py File Layout](#2-__init__py-file-layout)


## 1 General Python File Layout

Follow this structure for all Python files:

1. Shebang Line (if applicable)
2. Module Docstring
3. Future Imports
4. Header Section
5. Imports Section
6. Definitions Section (constants, functions, classes)
7. Main Section

### Rationale
A standardized ordering of sections is required to provide a predictable environment for both developers and automated tools.

Directives:
- Always include a blank line at the end of the file.

### 1.1 Shebang Line

Omit the `#!` line for most `.py` files. Files intended for direct execution must start with `#!/usr/bin/env python3`.

### Rationale
The shebang line is required for the kernel to identify the correct interpreter for executable scripts.

### 1.2 Future Imports

Use `from __future__ import` statements to enable modern Python syntax features in older runtimes.

### Rationale
Future imports should be used to ensure forward compatibility and to leverage improvements in the Python language as early as possible.

Directives:
- Keep future imports in place until it is certain that the code will only be executed in environments where the features are standard.
- Place the Future Imports section before the Header section to comply with Python's syntax requirements.
- Omit this section if no future imports are required.

### 1.3 Module Docstring

Describe the contents and usage of the module in the docstring.

### Rationale
High-quality module documentation is required to help developers understand the purpose and interface of a file without reading the entire source code.

Directives:
- Start every file with a module docstring.
- Use the exact filename as the first line of the docstring.
- Provide a one-line summary on the second line, terminated by a period.
- Leave the third line blank.
- Include a detailed description starting from the fourth line.
- Use the third-person declarative voice for all descriptions (e.g., "Provides...").

Compliant:
```python # pseudocode
"""file_name.py
One-line summary of the module, terminated by a period.

Detailed description of the module or program. The description may be broken into 
multiple paragraphs to present functionality in logical sections.
"""
```

### 1.4 Header Section

Include metadata about the file and the package in the header section.

### Rationale
Standardized metadata is required for tracking authorship and credits within the codebase.

Directives:
- Include the `# Header #` comment.
- Specify `__package_name__`, `__author__`, and `__credits__`.
- Ensure credits are a list of strings.
- Include copyright information as `__copyright__` in the Header section.
- Include license information as `__license__` in the Header section.
- Include version information as `__version__` in the Header section.

Example:
```python # pseudocode
# Header #
__package_name__ = "templatepackage"

__author__ = "Anthony Fong"
__credits__ = ["Anthony Fong"]
__copyright__ = "Copyright 2021, Anthony Fong"
__license__ = "MIT"

__version__ = "1.12.0"
```

### 1.5 Imports

Group and order imports logically to make dependencies clear.

### Rationale
Standardized import organization is required to avoid circular dependencies and to quickly identify where a module's dependencies originate.

Directives:
- Place imports at the top of the file, after the module docstring and before definitions.
- Include the `# Imports #` header comment.
- Group imports into the following categories, in order:
  1. Standard Libraries (`# Standard Libraries #`)
  2. Third-Party Packages (`# Third-Party Packages #`)
  3. Source Project Packages (`# Source Packages #`)
  4. Local Package Modules (`# Local Packages #`)
- Separate groups with a single blank line.
- Sort imports lexicographically within each group.
- Put package and module imports on separate lines.
- Use `from x import y` for individual types, classes, or functions.
- Avoid wildcard imports (`from module import *`).
- Use aliases (`import y as z`) for name conflicts, excessively long names, or standard abbreviations (e.g., `import numpy as np`).

Compliant:
```python # pseudocode
# Imports #
# Standard Libraries #
from collections.abc import Mapping, Sequence
import os
import sys
from typing import Any, List, Optional, NewType

# Third-Party Packages #
import numpy as np
import pandas as pd

# Source Packages #
from proxyarrays.bases import BaseObject

# Local Packages #
from .utils import helper_function
```

Non-Compliant:
```python # pseudocode
import os, sys
```

### 1.6 Definitions Section

The definitions section contains constants, functions, and classes.

### Rationale
A consistent ordering of definitions is required to provide a predictable structure for reading and navigating source code.

Directives:
- Include the `# Definitions #` header comment.
- Organize definitions into the following subsections, in order:
  1. Constants (`# Constants #`)
  2. Functions (`# Functions #`)
  3. Classes (`# Classes #`)
  4. Additional Definitions
- Omit subsections if they contain no definitions.

#### 1.6.1 Constants

Define constants at the module level.

### Rationale
Constants should be grouped together to provide a single point of reference for fixed values used throughout the module.

Directives:
- Include the `# Constants #` header comment.
- Name constants using `ALL_CAPS_WITH_UNDERSCORES`.
- Place constants before function and class definitions.
- Use clear, descriptive names.
- Provide a comment for complex constants explaining their derivation.

Compliant:
```python # pseudocode
# Constants #
EXCEL_INIT_DATE = datetime(1899, 12, 30)  # The initial date of Excel's date system
```

#### 1.6.2 Functions

Define reusable blocks of code as functions at the module level.

### Rationale
Consistent function organization is required to maintain a logical flow within the module.

Directives:
- Place functions after constants and before class definitions.
- Include the `# Functions #` header comment.
- Provide a descriptive docstring for every function.
- Use `snake_case` for function names.
- Include type hints for all parameters and return values.
- Place decorator functions before the functions they decorate.

Compliant:
```python # pseudocode
# Functions #
@singledispatch
def excel_date_to_datetime(timestamp: int | float | str | bytes, tzinfo: tzinfo | None = timezone.utc) -> datetime:
    """Converts a filetime to a datetime object.

    Args:
        timestamp: The filetime to convert to a datetime.
        tzinfo: The timezone of the datetime.

    Returns:
        The datetime of the filetime.
    """
    msg = f"{timestamp.__class__} cannot be converted to a datetime"
    raise TypeError(msg)
```

#### 1.6.3 Classes

Define blueprints for objects as classes at the module level.

### Rationale
A standardized internal class organization is required to ensure that members are easily discoverable.

Directives:
- Place classes after constants and functions.
- Include the `# Classes #` header comment.
- Use `CapWords` (PascalCase) for class names.
- Provide a descriptive docstring for every class.
- Follow a consistent internal organization for methods and attributes.
- Define base classes before derived classes.

Compliant:
```python # pseudocode
# Classes #
class BaseObject(ABC):
    """An abstract class that implements basic functions for all objects."""

    # Class structure follows...
```

Organize class members into the following sections, in order:
1. Docstring
2. Static Methods (`# Static Methods #`)
3. Class Attributes (`# Class Attributes #`)
4. Class Magic Methods (`# Class Magic Methods #`)
5. Class Methods (`# Class Methods #`)
6. Attributes (`# Attributes #`)
7. Properties (`# Properties #`)
8. Magic Methods (`# Magic Methods #`)
9. Instance Methods (`# Instance Methods #`)

Omit sections if they contain no members.

##### 1.6.3.1 Static Methods

Define methods that do not operate on instance data as static methods.

### Rationale
Static methods are recommended for functionality that is logically related to a class but does not require access to class or instance state.

Directives:
- Define at the beginning of the class, before class attributes.
- Group under the `# Static Methods #` header comment.
- Decorate with `@staticmethod`.
- Use `snake_case` for names.
- Provide a descriptive docstring and include type hints for parameters and return values.

Compliant:
```python # pseudocode
# Static Methods #
@staticmethod
def create_from_data(data: dict) -> "MyClass":
    """Creates a new instance from a data dictionary.

    Args:
        data: Dictionary containing initialization data.

    Returns:
        A new instance of MyClass.
    """
    return MyClass(**data)
```

##### 1.6.3.2 Class Attributes

Define variables shared by all instances as class attributes.

### Rationale
Class attributes are required for storing state that is common across all instances of a class.

Directives:
- Define after static methods and before class magic methods.
- Group under the `# Class Attributes #` header comment.
- Use `snake_case` for names.
- Use `ClassVar` for type hints to distinguish from instance attributes.
- Prefix private class attributes with an underscore.

Compliant:
```python # pseudocode
# Class Attributes #
method_type: ClassVar[type[DynamicMethod]] = singlekwargdispatchmethod
_bind_method: ClassVar[str] = "bind_method_dispatcher"

_kwarg: ClassVar[str | None] = None
_parse_method: ClassVar[str] = "parse_first"
```

##### 1.6.3.3 Class Magic Methods

Define special methods that operate on the class itself as class magic methods.

### Rationale
Class magic methods (e.g., `__new__`) are required for controlling class-level behavior like object creation.

Directives:
- Define after class attributes and before class methods.
- Group under the `# Class Magic Methods #` header comment.
- Use double underscores (e.g., `__new__`).
- Provide descriptive docstrings and type hints.

Compliant:
```python # pseudocode
# Class Magic Methods #
def __new__(cls, *args: Any, **kwargs: Any) -> Any:
    """Creates a new instance of the class.

    Args:
        *args: Arguments for initialization.
        **kwargs: Keyword arguments for initialization.

    Returns:
        A new instance of the class.
    """
    return super().__new__(cls)
```

##### 1.6.3.4 Class Methods

Define methods that operate on the class itself as class methods.

### Rationale
Class methods are recommended for factory methods and operations that require access to class state.

Directives:
- Define after class magic methods and before instance attributes.
- Group under the `# Class Methods #` header comment.
- Decorate with `@classmethod`.
- Provide descriptive docstrings and type hints.

Compliant:
```python # pseudocode
# Class Methods #
@classmethod
def from_dict(cls, data: dict) -> "MyClass":
    """Creates a new instance from a dictionary.

    Args:
        data: Dictionary containing initialization data.

    Returns:
        A new instance of the class.
    """
    return cls(**data)
```

##### 1.6.3.5 Attributes

Define variables specific to each instance as instance attributes.

### Rationale
Instance attributes are required for maintaining the unique state of each object.

Directives:
- Define at the class level, after class methods and before properties.
- Group under the `# Attributes #` header comment.
- Do not use `ClassVar` for type hints.
- Prefix private or protected attributes with an underscore.
- Initialize in the `__init__` method.

Compliant:
```python # pseudocode
# Attributes #
parse: MethodMultiplexer
dispatcher: AnyCallable | None = None
_initialized: bool

def __init__(self, *args: Any, **kwargs: Any) -> None:
    # Attributes #
    self.parse: MethodMultiplexer = MethodMultiplexer(instance=self, select=self._parse_method)
    self._initialized: bool = False

    # Parent Initialization #
    super().__init__(*args, **kwargs)
```

##### 1.6.3.6 Properties

Use properties to control attribute access that requires trivial logic.

### Rationale
Properties are recommended for providing a clean, attribute-like interface while maintaining control over data validation or derivation.

Directives:
- Create properties with the `@property` decorator.
- Ensure implementations are cheap, straightforward, and unsurprising.
- Do not use properties for simple reads and writes; make the attribute public instead.
- Do not use properties to implement computations that a subclass might want to override or extend.

##### 1.6.3.7 Magic Methods

Magic methods (also known as dunder methods) are special methods invoked by Python's syntax rather than by explicit calls.

### Rationale
Magic methods are required for enabling objects to interact with Python's internal protocols and built-in functions.

Directives:
- Define after properties and before instance methods.
- Group under the `# Magic Methods #` header comment.
- Use double underscores (e.g., `__str__`).
- Organize by functionality (e.g., Construction, Container, Representation, etc.).

###### 1.6.3.7.1 Magic Method Subcategories

Organize magic methods into subcategories based on their functionality to improve code readability and organization. Precede each subcategory with a comment indicating the subcategory name.

Common magic method subcategories include:

- **Construction/Destruction**: Methods related to object creation and cleanup
  - `__new__`, `__init__`, `__del__`, `__copy__`, `__deepcopy__`

- **Container Methods**: Methods that implement container-like behavior
  - `__len__`, `__getitem__`, `__setitem__`, `__delitem__`, `__iter__`, `__contains__`

- **Representation**: Methods that provide string representations of the object
  - `__repr__`, `__str__`, `__format__`

- **Type Conversion**: Methods that handle type conversion
  - `__bool__`, `__int__`, `__float__`, `__complex__`, `__bytes__`

- **Comparison**: Methods that implement comparison operations
  - `__lt__`, `__le__`, `__eq__`, `__ne__`, `__gt__`, `__ge__`

- **Arithmetic**: Methods that implement arithmetic operations
  - `__add__`, `__sub__`, `__mul__`, `__matmul__`, `__truediv__`, `__floordiv__`, `__mod__`, `__pow__`
  - `__radd__`, `__rsub__`, `__rmul__`, `__rmatmul__`, `__rtruediv__`, `__rfloordiv__`, `__rmod__`, `__rpow__`
  - `__iadd__`, `__isub__`, `__imul__`, `__imatmul__`, `__itruediv__`, `__ifloordiv__`, `__imod__`, `__ipow__`

- **Attribute Access**: Methods that control attribute access
  - `__getattr__`, `__getattribute__`, `__setattr__`, `__delattr__`, `__dir__`

- **Descriptor Protocol**: Methods that implement the descriptor protocol
  - `__get__`, `__set__`, `__delete__`

- **Context Management**: Methods that implement the context manager protocol
  - `__enter__`, `__exit__`

Compliant:
```python # pseudocode
# Magic Methods #
# Construction/Destruction
def __init__(self, *args: Any, **kwargs: Any) -> None:
    """Initializes the object."""
    pass

def __copy__(self) -> "MyClass":
    """Creates a shallow copy of this object."""
    return MyClass(self.data)

# Container Methods
def __len__(self) -> int:
    """Returns the number of items in this container."""
    return len(self.data)

def __getitem__(self, key: Any) -> Any:
    """Gets an item by key."""
    return self.data[key]

# Representation
def __repr__(self) -> str:
    """Returns a string representation of this object."""
    return f"{self.__class__.__name__}({self.data!r})"

# Comparison
def __eq__(self, other: Any) -> bool:
    """Checks if this object is equal to another object."""
    if not isinstance(other, self.__class__):
        return NotImplemented
    return self.data == other.data
```

##### 1.6.3.8 Instance Methods

Instance methods are methods that operate on instance data and require an instance of the class to be called.

### Rationale
Instance methods are required for implementing the core behavior and logic of objects.

Directives:
- Define after magic methods and before getters and setters.
- Group under the `# Instance Methods #` header comment.
- Use `snake_case` for names.
- Provide descriptive docstrings and type hints.
- Organize by functionality using subcategory comments.

Compliant:
```python # pseudocode
# Instance Methods #
# Constructors
def construct(self, *args: Any, **kwargs: Any) -> None:
    """Constructs this object with the given arguments."""
    self.data = {}
    self.initialize(*args, **kwargs)

def initialize(self, data: dict | None = None) -> None:
    """Initializes this object with the given data."""
    if data:
        self.data.update(data)

# Parameter Parsers
def parse_input(self, input_data: Any) -> dict:
    """Parses the input data into a dictionary format."""
    if isinstance(input_data, dict):
        return input_data
    elif isinstance(input_data, str):
        return {"text": input_data}
    else:
        return {"value": input_data}

# Setters
def set_option(self, name: str, value: Any) -> None:
    """Sets an option with the given name and value."""
    self.data[name] = value

# Method Dispatching
def dispatch_call(self, method_name: str, *args: Any, **kwargs: Any) -> Any:
    """Dispatchs a call to the method with the given name."""
    method = getattr(self, method_name, None)
    if method is None:
        msg = f"No method named {method_name}"
        raise AttributeError(msg)
    return method(*args, **kwargs)
```

##### 1.6.3.9 Getters and Setters

Use getter and setter methods when they provide meaningful behavior or when the operation cost is significant.

### Rationale
Explicit accessors are recommended for complex operations to signal that the cost of access or mutation is not trivial.

Directives:
- Use public attributes for simple reads and writes.
- Use a setter function if setting a variable invalidates or rebuilds state.
- Follow the naming guidelines (e.g., `get_foo()`, `set_foo()`).
- Do not bind new getter/setter functions to an old property if the complexity has changed.

##### 1.6.3.10 Additional Definitions

Define other non-structural code at the end of the definitions section.

### Rationale
Placing miscellaneous definitions at the end ensures that they do not disrupt the predictable flow of the core module structure.

Directives:
- Group circular references under the `# Circular References #` header comment.
- Group external registrations under the `# Registration #` header comment.

### 1.7 Main

Use a `main()` function for executable scripts.

### Rationale
Standardizing the entry point is required for module importability and testing.

Directives:
- Always check `if __name__ == '__main__':` before executing.
- Use `app.run(main)` when using `absl`.
- Avoid calling functions or creating objects at the top level that should not be executed when the module is imported.


## 2 __init__.py File Layout

The `__init__.py` file marks a directory as a Python package. It should be used to initialize the package and expose its public API.

### Rationale
A well-structured `__init__.py` is required to provide a clear and concise entry point for package users.

Directives:
- Follow the same general structure as other Python files.
- Include a module docstring describing the package.
- Include the Header section with package metadata.
- Import and expose the public API of the package.
- Use wildcard imports (`from .submodule import *`) to expose public members from submodules.
- Keep implementation details out of this file.

Compliant:
```python # pseudocode
"""__init__.py
The templatepackage provides several base classes and tools.
"""

# Header #
__package_name__ = "templatepackage"

__author__ = "Anthony Fong"
__credits__ = ["Anthony Fong"]
__copyright__ = "Copyright 2021, Anthony Fong"
__license__ = "MIT"

__version__ = "1.12.0"


# Imports #
# Local Packages #
from .bases import *
from .functions import *
from .composition import *
```

