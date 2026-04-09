# Anthony's Python Style Guide: Common Bugs and Code Smells

Avoid patterns that lead to bugs, performance issues, or maintainability problems.

### Rationale
Identifying and eliminating code smells is required to ensure that the codebase remains robust, predictable, and easy to maintain.

## Table of Contents

- [1 Class Design](#1-class-design)
- [2 Name Shadowing](#2-name-shadowing)
- [3 Miscellaneous Smells](#3-miscellaneous-smells)


## 1 Class Design

### 1.1 Abstract Base Classes (ABC)

Ensure every Abstract Base Class contains at least one abstract method.

### Rationale
An ABC without abstract methods should be avoided because it contradicts the purpose of an abstract interface. Explicitly marking abstract methods is required to ensure that subclasses implement the necessary contract.

Directives:
- Inherit from `abc.ABC` to define an abstract class.
- Mark all methods that must be overridden with the `@abstractmethod` decorator.

### 1.2 Mutable Class Attributes

Avoid using mutable objects (e.g., lists, dicts) as class-level attributes.

### Rationale
Mutable class attributes are shared across all instances, which can lead to unexpected state sharing and difficult-to-track bugs.

Directives:
- Initialize mutable attributes in the `__init__` method for instance-specific state.
- Use `typing.ClassVar` to explicitly annotate intentional class-level shared state.

Compliant:
```python # pseudocode
from typing import ClassVar

class UserRegistry:
    # Explicitly shared
    _REGISTRY: ClassVar[dict[str, User]] = {}
    
    def __init__(self):
        # Specific to the instance
        self.tags: list[str] = []
```

Non-Compliant:
```python # pseudocode
class UserRegistry:
    # PROBLEM: This list is shared across ALL instances!
    tags: list[str] = []
```


## 2 Name Shadowing

Avoid using names for class attributes or module-level variables that shadow Python's built-in functions (e.g., `id`, `type`, `list`, `str`).

### Rationale
Shadowing built-ins is required to be avoided because it reduces readability and can lead to errors when attempting to access the original built-in functionality.

Compliant:
```python # pseudocode
class User:
    identifier: str
```

Non-Compliant:
```python # pseudocode
class User:
    # PROBLEM: Shadows the `id()` builtin
    id: str
```


## 3 Miscellaneous Smells

### 3.1 Unused Variables

Do not define variables that are never used.

### Rationale
Eliminating unused variables is required to reduce clutter and cognitive load.

Directives:
- Prefix unused variables required by a signature with an underscore (e.g., `_data`).

### 3.2 Simplified Conditionals

Use idiomatic Python for logical expressions.

### Rationale
Idiomatic conditionals are recommended to improve readability and consistency.

Directives:
- Use `x is None` instead of `x == None`.

### 3.3 Star Imports

Never use wildcard imports (`from module import *`) in project source code.

### Rationale
Wildcard imports must be avoided because they obscure the origin of names and can lead to unintended name collisions.
