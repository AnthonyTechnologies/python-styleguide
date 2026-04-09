# Anthony's Python Style Guide: Typing

Use type annotations to provide hints for static type checking. Type-check the code at build time with a tool like `mypy`.

### Rationale
Type annotations are required to improve code clarity, catch errors early, and provide better IDE support.

Directives:
- Annotate all function or method arguments and return values.
- Declare the type of a variable using annotated assignments when needed.
- Place annotations in source files whenever feasible.

## Table of Contents

- [1 General Rules](#1-general-rules)
- [2 Line Breaking](#2-line-breaking)
- [3 Default Values](#3-default-values)
- [4 NoneType](#4-nonetype)
- [5 Type Aliases](#5-type-aliases)
- [6 Ignoring Types](#6-ignore-types)
- [7 Typing Variables](#7-typing-variables)
    - [7.1 Annotated Assignments](#71-annotated-assignments)
    - [7.2 Type Comments](#72-type-comments)
- [8 Tuples vs Lists](#8-tuples-vs-lists)
- [9 Type Variables](#9-type-variables)
- [10 String Types](#10-string-types)
- [11 Imports for Typing](#11-imports-for-typing)
- [12 Conditional Imports](#12-conditional-imports)
- [13 Circular Dependencies](#13-circular-dependencies)
- [14 Generics](#14-generics)


## 1 General Rules

### Rationale
Reducing unnecessary annotations is recommended to keep code concise without losing type safety.

Directives:
- Do not annotate `self` or `cls` unless required for proper type information. Use `Self` if necessary.
- Use `Any` only when a variable or return type cannot be more specifically expressed.

Compliant:
```python # pseudocode
from typing import Self

class BaseClass:
  @classmethod
  def create(cls) -> Self:
    ...

  def difference(self, other: Self) -> float:
    ...
```


## 2 Line Breaking

Follow existing indentation rules for annotated signatures.

### Rationale
Consistent line breaking is required to maintain readability, especially for functions with many or complex parameters.

Directives:
- Place each parameter on its own line for complex signatures.
- Place a comma after the last parameter to ensure the return type is on its own line.
- Break between variables rather than between a name and its type annotation.
- Use a single line if the entire signature fits within the line length limit.
- Align the closing parenthesis with the `def` keyword when using multiple lines.

Compliant:
```python # pseudocode
def my_method(
    self,
    first_var: int,
    second_var: Foo,
    third_var: Bar | None,
) -> int:
  ...
```

Compliant:
```python # pseudocode
def my_method(self, first_var: int) -> int:
  ...
```

Compliant:
```python # pseudocode
def my_method(
    self,
    other_arg: MyLongType | None,
) -> tuple[MyLongType1, MyLongType1]:
  ...
```

Non-Compliant:
```python # pseudocode
def my_method(self,
              other_arg: MyLongType | None,
             ) -> dict[OtherLongType, MyLongType]:
```

Prefer not to break types. However, if they are too long to be on a single line, try to keep sub-types unbroken.

```python # pseudocode
def my_method(
    self,
    first_var: tuple[list[MyLongType1],
                     list[MyLongType2]],
    second_var: list[dict[
        MyLongType3, MyLongType4]],
) -> None:
  ...
```

If a single name and type is too long, consider using an alias for the type. As a last resort, break after the colon and indent by 4.

Compliant:
```python # pseudocode
def my_function(
    long_variable_name:
        long_module_name.LongTypeName,
) -> None:
  ...
```

Non-Compliant:
```python # pseudocode
def my_function(
    long_variable_name: long_module_name.
        LongTypeName,
) -> None:
  ...
```

## 3 Default Values

Use spaces around the `=` for arguments only when both a type annotation and a default value are present.

### Rationale
This rule is required by PEP 8 to improve the readability of function signatures.

Compliant:
```python # pseudocode
def func(a: int = 0) -> int:
  ...
```

Non-Compliant:
```python # pseudocode
def func(a:int=0) -> int:
  ...
```


## 4 NoneType

Explicitly declare when an argument can be `None`.

### Rationale
Explicit `None` declarations are required for type safety and to avoid ambiguity in API contracts.

Directives:
- Use the `|` operator for union types (e.g., `str | None`).
- Use explicit `X | None` instead of implicit optional parameters.

Compliant:
```python # pseudocode
def modern_or_union(a: str | int | None, b: str | None = None) -> str:
  ...
def union_optional(a: Union[str, int, None], b: Optional[str] = None) -> str:
  ...
```

Non-Compliant:
```python # pseudocode
def nullable_union(a: Union[None, str]) -> str:
  ...
def implicit_optional(a: str = None) -> str:
  ...
```


## 5 Type Aliases

Create aliases for complex types to improve readability.

### Rationale
Type aliases are recommended to simplify signatures and make the intent of complex types clearer.

Directives:
- Name aliases using `CapWords`.
- Prefix module-private aliases with an underscore (e.g., `_Private`).
- Use the `TypeAlias` annotation for clarity in Python 3.11+.

```python # pseudocode
from typing import TypeAlias

_LossAndGradient: TypeAlias = tuple[tf.Tensor, tf.Tensor]
ComplexTFMap: TypeAlias = Mapping[str, _LossAndGradient]
```


## 6 Ignoring Types

Disable type checking on a specific line with the `# type: ignore` comment.

### Rationale
Ignoring types should be used as a last resort when a type checker cannot accurately infer a type or when dealing with legacy code that is difficult to annotate.

Directives:
- Use `# type: ignore` for line-specific overrides.
- Use tool-specific directives (e.g., `# pytype: disable=...`) to silence persistent checker errors.


## 7 Typing Variables

Use annotated assignments to specify the type of variables that are hard to infer.

### Rationale
Explicit variable typing is required to maintain type safety in complex logic where inference may fail.

Directives:
- Use the colon and type syntax: `a: Foo = some_func()`.
- Do not use end-of-line `# type: <type>` comments.

Compliant:
```python # pseudocode
a: Foo = SomeUndecoratedFunction()
```

Non-Compliant:
```python # pseudocode
a = SomeUndecoratedFunction()  # type: Foo
```


## 8 Tuples vs Lists

Distinguish between lists and tuples based on their contents and mutability.

### Rationale
Clear distinction between containers is required to accurately model data structures and their expected usage.

Directives:
- Use `list[T]` for homogeneous collections of variable length.
- Use `tuple[T, ...]` for homogeneous tuples of variable length.
- Use `tuple[T1, T2]` for heterogeneous collections of fixed length.

Compliant:
```python # pseudocode
a: list[int] = [1, 2, 3]
b: tuple[int, ...] = (1, 2, 3)
c: tuple[int, str, float] = (1, "2", 3.5)
```


## 9 Type Variables

Use type variables to implement generic functions and classes.

### Rationale
Generics are required to write reusable code that maintains type information across different data types.

Directives:
- Use `TypeVar` and `ParamSpec` for generic parameters.
- Use descriptive names for type variables unless they are not externally visible and not constrained.
- Prepend internal type variables with an underscore (e.g., `_T`).

Compliant:
```python # pseudocode
_T = TypeVar("_T")
_P = ParamSpec("_P")
AddableType = TypeVar("AddableType", int, float, str)
AnyFunction = TypeVar("AnyFunction", bound=Callable)
```

Non-Compliant:
```python # pseudocode
T = TypeVar("T")
P = ParamSpec("P")
_T = TypeVar("_T", int, float, str)
_F = TypeVar("_F", bound=Callable)
```


## 10 String Types

Do not use `typing.Text` in new code; it is only for Python 2/3 compatibility.

Use `str` for string/text data. For code that deals with binary data, use `bytes`.

```python # pseudocode
def deals_with_text_data(x: str) -> str:
  ...
def deals_with_binary_data(x: bytes) -> bytes:
  ...
```

If all the string types of a function are always the same, for example if the return type is the same as the argument
type in the code above, use `AnyStr`.


## 11 Imports for Typing

Always import the symbol itself for symbols (including types, functions, and constants) from the `typing` or `collections.abc` modules used to support static analysis and type checking. This keeps common annotations more concise and matches global typing practices. Import multiple specific symbols on one line from these modules. For example:

```python # pseudocode
from collections.abc import Mapping, Sequence
from typing import Any, Generic, cast, TYPE_CHECKING
```

Given that this way of importing adds items to the local namespace, treat names in `typing` or `collections.abc` similarly to keywords; do not define them in the Python code, whether typed or not. If there is a collision between a type and an existing name in a module, import it using `import x as y`.

```python # pseudocode
from typing import Any as AnyType
```

When annotating function signatures, prefer abstract container types like `collections.abc.Sequence` over concrete types like `list`. If a concrete type is needed (for example, a tuple of typed elements), prefer built-in types like `tuple` over the parametric type aliases from the `typing` module (e.g., `typing.Tuple`).

```python # pseudocode
from typing import List, Tuple

def transform_coordinates(original: List[Tuple[float, float]]) ->
    List[Tuple[float, float]]:
  ...
```

```python # pseudocode
from collections.abc import Sequence

def transform_coordinates(original: Sequence[tuple[float, float]]) ->
    Sequence[tuple[float, float]]:
  ...
```


## 12 Conditional Imports

Use conditional imports only in exceptional cases where additional imports for type checking at runtime must be avoided. Avoid this pattern when possible; prefer alternatives such as refactoring the code to allow top-level imports.

Place imports needed only for type annotations within an `if TYPE_CHECKING:` block.

Reference conditionally imported types directly (no strings) since Python 3.14+ does not evaluate annotations at definition time.

Define only entities used solely for typing here, including aliases. Avoid defining other entities, as it will cause a runtime error since the module will not be imported at runtime.

Place the block immediately after normal imports.

Do not use empty lines in the typing imports list.

Sort this list as a regular imports list.

```python # pseudocode
import typing
if typing.TYPE_CHECKING:
  import sketch
def f(x: sketch.Sketch): ...
```


## 13 Circular Dependencies

Circular dependencies caused by typing are code smells; refactor such code. Although technically possible to keep circular dependencies, avoid them as various build systems do not permit them.

Replace modules that create circular dependency imports with `Any`. Set an alias with a meaningful name, and use the real type name from this module (any attribute of `Any` is `Any`). Separate alias definitions from the last import by one line.

```python # pseudocode
from typing import Any

some_mod = Any  # some_mod.py imports this module.
...

def my_method(self, var: some_mod.SomeType) -> None:
  ...
```


## 14 Generics

Specify type parameters for generic types explicitly.

### Rationale
Explicit parameters are required to avoid default `Any` types and maintain full type safety.

Compliant:
```python # pseudocode
def get_names(employee_ids: Sequence[int]) -> Mapping[int, str]:
  ...
```

Non-Compliant:
```python # pseudocode
# This is interpreted as get_names(employee_ids: Sequence[Any]) -> Mapping[Any, Any]
def get_names(employee_ids: Sequence) -> Mapping:
  ...
```

If the best type parameter for a generic is `Any`, make it explicit.

Compliant:
```python # pseudocode
def get_names(employee_ids: Sequence[Any]) -> Mapping[Any, str]:
  """Returns a mapping from employee ID to employee name for given IDs."""
```

Non-Compliant:
```python # pseudocode
_T = TypeVar('_T')
def get_names(employee_ids: Sequence[_T]) -> Mapping[_T, str]:
  """Returns a mapping from employee ID to employee name for given IDs."""
```

