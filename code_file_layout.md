# Anthony's Python Style Guide: Code and File Layout

This document provides comprehensive guidelines for organizing Python code in a file. It details the standard structure
and layout that all Python files must follow, including the ordering of sections like shebang lines, module docstrings,
imports, and definitions. The guidelines cover how to organize constants, functions, and classes, with special attention
to class structure and the organization of methods within classes. Following these guidelines ensures consistency across
the codebase, making it easier to navigate, understand, and maintain the project's source code.

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

Follow this structure for each Python file, except for internal files:

1. Shebang Line (If applicable)
2. Module Docstring
3. Future Imports
4. Header Section
5. Imports Section
6. Definitions section with constants, functions, classes, etc.
7. Main Section

Finally, ensure there is always a blank line at the end of the file.

### 1.1 Shebang Line

Omit the `#!` line for most `.py` files. Start the main file of a program with `#!/usr/bin/env python3` (to
support virtualenvs) or `#!/usr/bin/python3` per PEP-394.

Use this line for the kernel to find the Python interpreter; Python ignores it when importing modules. Include it only on a file intended for direct execution.

### 1.2 Future Imports

New language version semantic changes may be gated behind a special future import to enable them on a per-file basis
within earlier runtimes.

Use `from __future__ import` statements to start using more modern Python syntax features today. Remove those lines once it is no longer necessary to run on a version where the features are hidden behind a `__future__` import.

In code that may execute on versions as old as 3.5 rather than >= 3.7, import:

```python # pseudocode
# Futures #
from __future__ import generator_stop
from __future__ import annotations
```

For more information, read the Python future statement definitions documentation.

Do not remove these imports until it is certain the code is only ever used in a sufficiently modern environment. Even if the specific feature enabled by a particular future import is not currently used in the code, keep it in place to prevent later modifications from inadvertently depending on the older behavior.

Guidelines:
- Put the Future Imports section before the Header section to comply with Python's syntax requirements.
- Omit the Future Imports section if there are no future imports.

### 1.3 Module Docstring

Describe the contents of the file in the module docstring. Find the guidelines for docstrings in [Docstrings](syntax/docstrings.md). These guidelines reiterate what is also in the Syntax topics.

Guidelines:
- Start files with a docstring describing the contents and usage of the module.
- Use the file name exactly as it is in the file system (typically lowercase) as the first line of the module.
- Provide a one-line summary of the module or program, terminated by a period, on the second line.
- Leave the third line blank.
- Include a detailed description of the module or program starting from the fourth line.

```python # pseudocode
"""file_name.py
A one-line summary of the module or program, terminated by a period.

Leave one blank line. Include an overall description of the module or program in the rest of the docstring. The
description can be broken up into multiple paragraphs to present the functionality into logical sections. Bullet-point
and numerical lists may be used as well, but only add them if they are needed.
"""
```

### 1.4 Header Section

The header section contains metadata about the file and the package. Include this section in all Python files.

Guidelines:
- Include the header comment `# Header #` in the Header section.
- Include the package name as `__package_name__` in the Header section.
- Include author information as `__author__` in the Header section.
- Include credits as `__credits__` in the Header section.
  - Ensure credits are a list of strings or the contributors' names.
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

Python import statements link code across multiple files. Ensure imported items are easily trackable. Also, use trackback tools to find which definition is used.

Guidelines:
- Put imports at the top of the file, just after any module comments and docstrings and before module globals and constants.
- Include the header comment `# Imports #` in the Imports section.
- Group imports, in order, by standard library, third party, and project modules.
  - Include the header comment `# Standard Libraries #` for the standard library import group.
  - Include the header comment `# Third-Party Packages #` for the third party import group.
  - Include the header comment `# Local Packages #` for the project import group.
- Ensure there is one blank line between each import group.
- Sort imports lexicographically within each grouping, ignoring case, according to each module's full package path.
- Group imports from most generic to least generic.
- Put package and module imports on separate lines.
- Use `from x import y` for individual types, classes, or functions.
- Avoid wildcard imports (`from module import *`), except when a module's `__init__.py` imports all items from a sub-module.
- For conflicts, import the parent module/package then call the item from that module/package.
- For some conflicts, if a normally lower case class name conflicts, import it as a camel case variant (e.g., `from datetime import tzinfo as TZInfo`).
- Use `from x import y as z` in any of the following circumstances:
  - Two modules named y are to be imported.
  - y conflicts with a top-level name defined in the current module.
  - y conflicts with a common parameter name that is part of the public API (e.g., features).
  - y is an inconveniently long name.
  - y is too generic in the context of the code (e.g., from storage.file_system import options as fs_options).
- Use `import y as z` only when z is a standard abbreviation (e.g., `import numpy as np`).

Exemptions:
- Symbols from the following modules are used to support static analysis and type checking:
  - typing module
  - collections.abc module
  - typing_extensions module
- Redirects from the six.moves module

Examples:

Correct:
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

# Local Packages #
from ..bases import BaseObject
from .utils import helper_function
```

Incorrect:
```python # pseudocode
import os, sys
```

### 1.6 Definitions Section

The definitions section contains code that defines constants, functions, classes, etc. If there are no definitions, omit the section.

Include the header comment `# Definitions #` in the definitions section.

Organize definitions into the following subsections in the recommended order:
1. Constants
2. Functions
3. Classes
4. Additional Definitions

However, optionally, organize the definition subsections in any order that makes sense for the code and omit them if there are no definitions in that section.

#### 1.6.1 Constants

Constants are values that must not be changed during program execution. Typically, define them at the module level.

Guidelines:
- Include the header comment `# Constants #` in the Constants section.
- Name constants using ALL_CAPS_WITH_UNDERSCORES.
- Place constants before function and class definitions.
- Ensure constants have a clear, descriptive name that indicates their purpose.
- Provide a comment for complex constants explaining their purpose or derivation.

Example:
```python # pseudocode
# Constants #
EXCEL_INIT_DATE = datetime(1899, 12, 30)  # The initial date of Excel's date system
```

#### 1.6.2 Functions

Functions are reusable blocks of code that perform specific tasks. Define them at the module level.

Guidelines:
- Place functions after constants and before class definitions.
- Include the header comment `# Functions #` in the Functions section.
- Ensure each function has a descriptive docstring that explains its purpose, parameters, and return values (See Syntactic Guidelines).
- Use snake_case (lowercase with underscores) for function names, except for decorators use lowercase with or without underscores (no underscores is preferred).
- Include type hints for function parameters.
- Include type hints for function return values.
- Organize functions by functionality.
- Group related functions together.
- Place decorator functions before the functions they decorate.

Example:
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
    raise TypeError(f"{timestamp.__class__} cannot be converted to a datetime")
```

#### 1.6.3 Classes

Classes are blueprints for creating objects that encapsulate data and behavior. Define them at the module level.

Guidelines:
- Place classes after constants and functions.
- Include the header comment `# Classes #` in the Classes section.
- Use CamelCase (capitalize the first letter of each word) for class names, except for decorator classes use lowercase with or without underscores (no underscores is preferred).
- Ensure each class has a descriptive docstring that explains its purpose (See Syntactic Guidelines).
- Follow a consistent internal organization for classes (see subsections below).
- Group related classes together.
- Define base classes before derived classes.

Example:
```python # pseudocode
# Classes #
class BaseObject(ABC):
    """An abstract class that implements some basic functions that all objects must have."""

    # Class structure follows...
```

Follow a consistent internal organization for classes with the following sections:
1. Docstring
2. Static Methods
3. Class Attributes
4. Class Magic Methods
5. Class Methods
6. Attributes
7. Properties
8. Magic Methods
9. Instance Methods

However, the only required section is the docstring. Omit all other sections if they are not needed.

The docstring standards and best practices are described in the Syntactic Guidelines document.

##### 1.6.3.1 Static Methods

Static methods are methods that don't operate on instance data and don't require an instance of the class to be called.

Guidelines:
- Define at the beginning of the class, before class attributes.
- Group under a comment: `# Static Methods #`.
- Decorate with `@staticmethod`.
- Use snake_case (lowercase with underscores) for names.
- Provide a descriptive docstring that explains their purpose, parameters, and return values.
- Include type hints for parameters and return values.

Example:
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

Class attributes are variables that are shared by all instances of a class. They are defined at the class level.

Guidelines:
- Define after static methods and before class magic methods.
- Group under a comment: `# Class Attributes #`.
- Use snake_case (lowercase with underscores).
- Include type hints.
- Use `ClassVar` for type hints (this distinguishes class attributes from instance attributes). An exception is
  `UnitTestClass`, which should NOT use `ClassVar`.
- Prefix private class attributes with an underscore.
- Organize by related functionality.

Example:
```python # pseudocode
# Class Attributes #
method_type: ClassVar[type[DynamicMethod]] = singlekwargdispatchmethod
_bind_method: ClassVar[str] = "bind_method_dispatcher"

_kwarg: ClassVar[str | None] = None
_parse_method: ClassVar[str] = "parse_first"
```

##### 1.6.3.3 Class Magic Methods

Class magic methods are special methods that are invoked by Python's syntax rather than by explicit method calls. They
are defined at the class level and operate on the class itself rather than instances.

Guidelines:
- Define after class attributes and before class methods.
- Group under a comment: `# Class Magic Methods #`.
- Prefix and suffix with double underscores (e.g., `__new__`).
- Provide descriptive docstrings that explain their purpose, parameters, and return values.
- Include type hints for parameters and return values.
- Organize by functionality (e.g., Construction/Destruction).

Example:
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

Class methods are methods that operate on the class itself rather than instances. They receive the class as their first argument (conventionally named `cls`).

Guidelines:
- Define after class magic methods and before instance attributes.
- Group under a comment: `# Class Methods #`.
- Decorate with `@classmethod`.
- Use snake_case (lowercase with underscores) for names.
- Provide descriptive docstrings that explain their purpose, parameters, and return values.
- Include type hints for parameters and return values.
- Organize by functionality.

Example:
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

Instance attributes are variables that are specific to each instance of a class. They are typically defined in class
scope and can be initialized in the `__init__` or `construct` methods.

Guidelines:
- Define after class methods and before properties.
- Group under a comment: `# Attributes #` in the class definition scope (they are defined outside of `__init__`).
- Define all instance attributes in this section at the class definition scope.
- Use snake_case (lowercase with underscores).
- Prefix private/protected instance attributes with an underscore.
- Include type hints.
- Do NOT use `ClassVar` for type hints (this distinguishes instance attributes from class attributes).
- Document in the class docstring (check Docstrings in Syntactic Guidelines for more information).
- Organize by related functionality.
- Initialize in the `__init__` method, but it is not required.

Example:
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

Properties may be used to control getting or setting attributes that require trivial computations or logic. Ensure property implementations match the general expectations of regular attribute access: that they are cheap, straightforward, and unsurprising.

Use properties only when necessary and match the expectations of typical attribute access; follow the getters and setters rules otherwise.

For example, using a property to simply both get and set an internal attribute is not allowed: there is no computation occurring, so the property is unnecessary (make the attribute public instead). In comparison, use a property to control attribute access or to calculate a trivially derived value: the logic is simple and unsurprising.

Create properties with the `@property` decorator. Manually implementing a property descriptor is considered a power feature.

Inheritance with properties can be non-obvious. Do not use properties to implement computations a subclass may ever want to override and extend.

##### 1.6.3.7 Magic Methods

Magic methods (also known as dunder methods) are special methods that are invoked by Python's syntax rather than by explicit method calls. They are defined at the instance level.

Guidelines:
- Define after properties and before instance methods.
- Group under a comment: `# Magic Methods #`.
- Prefix and suffix with double underscores (e.g., `__str__`).
- Provide descriptive docstrings that explain their purpose, parameters, and return values (see Syntactic Guidelines).
- Include type hints for parameters and return values.
- Organize by functionality (e.g., Construction/Destruction, Comparison, etc.).

Example:
```python # pseudocode
# Magic Methods #
# Construction/Destruction
def __init__(self, *args: Any, **kwargs: Any) -> None:
    """Initializes the object.

    Args:
        *args: Arguments for initialization.
        **kwargs: Keyword arguments for initialization.
    """
    super().__init__(*args, **kwargs)

def __copy__(self) -> Any:
    """The copy magic method (shallow).

    Returns:
        A shallow copy of this object.
    """
    return self.copy()
```

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

Example:
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

Instance methods are methods that operate on instance data and require an instance of the class to be called. They
receive the instance as their first argument (conventionally named `self`).

Guidelines:
- Define after magic methods and before getters and setters.
- Group under a comment: `# Instance Methods #`.
- Use snake_case (lowercase with underscores) for names.
- Provide descriptive docstrings that explain their purpose, parameters, and return values (see Syntactic Guidelines).
- Include type hints for parameters and return values.
- Organize by functionality (e.g., Constructors/Destructors, Setters, Parsers, etc.).
- Group related methods together with subcategory comments.

Example:
```python # pseudocode
# Instance Methods #
# Constructors
def construct(self, *args: Any, **kwargs: Any) -> None:
    """Constructs this object.

    Args:
        *args: Arguments for inheritance.
        **kwargs: Keyword arguments for inheritance.
    """
    pass

# Setters
def set_kwarg(self, kwarg: str | None) -> None:
    """Sets the name of the kwarg for dispatching.

    Args:
        kwarg: The name of the kwarg or None for checking the first kwarg.
    """
    self._kwarg = kwarg
```

###### 1.6.3.8.1 Instance Method Subcategories

Organize instance methods into subcategories based on their functionality to improve code readability and organization. Precede each subcategory with a comment indicating the subcategory name.

Common instance method subcategories include:

- **Constructors/Destructors**: Methods related to object construction and cleanup
  - `construct`, `initialize`, `setup`, `cleanup`, `dispose`

- **Setters**: Methods that set object attributes or state
  - `set_*`, `update_*`, `configure_*`

- **Getters**: Methods that retrieve object attributes or state
  - `get_*`, `retrieve_*`, `find_*`

- **Parameter Parsers**: Methods that parse or validate input parameters
  - `parse_*`, `validate_*`, `check_*`

- **Binding**: Methods related to binding functions or methods
  - `bind_*`, `unbind_*`, `rebind_*`

- **Method Dispatching**: Methods that handle method dispatching or routing
  - `dispatch_*`, `route_*`, `handle_*`

- **Conversion**: Methods that convert between different formats or types
  - `to_*`, `from_*`, `as_*`, `convert_*`

- **Validation**: Methods that validate object state or data
  - `validate_*`, `is_valid_*`, `check_*`

- **Utility**: Helper methods that provide common functionality
  - `utility_*`, `helper_*`, `format_*`

- **Operations**: Methods that perform specific operations on the object
  - `calculate_*`, `compute_*`, `process_*`

Example:
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
        raise AttributeError(f"No method named {method_name}")
    return method(*args, **kwargs)
```

##### 1.6.3.9 Getters and Setters

Use getter and setter methods (also called accessors and mutators) when they provide a meaningful role or behavior for getting or setting a variable's value.

In particular, use them when getting or setting the variable is complex or the cost is significant, either currently or in a reasonable future.

For example, if a pair of getters/setters simply read and write an internal attribute, make the internal attribute public instead. By comparison, if setting a variable means some state is invalidated or rebuilt, use a setter function. The function invocation hints that a potentially non-trivial operation is occurring. Alternatively, use properties when simple logic is needed, or refactor to no longer need getters and setters.

Follow the Naming guidelines for getters and setters, such as `get_foo()` and `set_foo()`.

If the past behavior allowed access through a property, do not bind the new getter/setter functions to the property. Ensure any code still attempting to access the variable by the old method breaks visibly so that users are aware of the change in complexity.

##### 1.6.3.10 Additional Definitions

In some cases, there is other code that is not part of the class, function, or module structure. Those can be defined
at the end of the definitions section.

For example, a class may have a circular reference. In that case, the reference may be defined in a definition section
called: `# Circular References #`.

Alternatively, a class or function may need to be registered to an object which is not defined in the same file. In
that case, the registration may be defined in a definitions section called: `# Registration #`.

### 1.7 Main

In Python, pydoc as well as unit tests require modules to be importable. If a file is intended for use as an executable, its main functionality must be in a `main()` function. Always check if `__name__ == '__main__'` before executing the main program so that it is not executed when the module is imported.

When using absl, use app.run:

```python # pseudocode
from absl import app
...

def main(argv: Sequence[str]):
    # process non-flag arguments
    ...

if __name__ == '__main__':
    app.run(main)
```

Otherwise, use:

```python # pseudocode
def main():
    ...

if __name__ == '__main__':
    main()
```

All code at the top level will be executed when the module is imported. Be careful not to call functions, create
objects, or perform other operations that must not be executed when the file is being pydoced.


## 2 \_\_init__.py File Layout

The `__init__.py` file is a special file in Python that marks a directory as a Python package. It can be empty or contain code to initialize the package.

Guidelines:
- Follow the same general structure as other Python files.
- Include a module docstring that describes the package.
- Include the Header section with package metadata.
- Import and expose the public API of the package.
- Use wildcard imports (`from .submodule import *`) to expose all public members from submodules.
- Keep it simple and focused on package initialization.
- Do not include implementation details.
- Include logic to handle package imports (i.e., try-catch import block).

Example:
```python # pseudocode
"""__init__.py
templatepackage provides several base classes and tools.
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

