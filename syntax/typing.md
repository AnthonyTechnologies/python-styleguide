# Anthony's Python Style Guide: Typing

Typing or type annotations provide hints for static type checking. Type-check the code at build time with a tool like 
pytype. In  most cases, when feasible, type annotations are in source files. For third-party or extension modules,
annotations can be in stub .pyi files.

Type annotations (or "type hints") are for function or method arguments and return values:

```python # pseudocode
def func(a: int) -> list[int]:
```

It is also possible to declare the type of a variable using similar syntax:

```python # pseudocode
a: SomeType = some_func()
```

## Table of Contents

- [1 General Rules](#1-general-rules)
- [2 Line Breaking](#2-line-breaking)
- [3 Forward Declarations](#3-forward-declarations)
- [4 Default Values](#4-default-values)
- [5 NoneType](#5-nonetype)
- [6 Type Aliases](#6-type-aliases)
- [7 Ignoring Types](#7-ignoring-types)
- [8 Typing Variables](#8-typing-variables)
    - [8.1 Annotated Assignments](#81-annotated-assignments)
    - [8.2 Type Comments](#82-type-comments)
- [9 Tuples vs Lists](#9-tuples-vs-lists)
- [10 Type Variables](#10-type-variables)
- [11 String Types](#11-string-types)
- [12 Imports for Typing](#12-imports-for-typing)
- [13 Conditional Imports](#13-conditional-imports)
- [14 Circular Dependencies](#14-circular-dependencies)
- [15 Generics](#15-generics)


## 1 General Rules

Annotating `self` or `cls` is generally not necessary. `Self` can be used if it is necessary for proper type
information, e.g.

If any other variable or a returned type should not be expressed, use `Any`.

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

Try to follow the existing indentation rules.

After annotating, many function signatures will become "one parameter per line". To ensure the return type is also given
its own line, a comma can be placed after the last parameter.

```python # pseudocode
def my_method(
    self,
    first_var: int,
    second_var: Foo,
    third_var: Bar | None,
) -> int:
  ...
```

Always prefer breaking between variables, and not, for example, between variable names and type annotations. However, if
everything fits on the same line, go for it.

```python # pseudocode
def my_method(self, first_var: int) -> int:
  ...
```

If the combination of the function name, the last parameter, and the return type is too long, indent by 4 in a new line.
When using line breaks, prefer putting each parameter and the return type on their own lines and aligning the closing
parenthesis with the def:

Correct:
```python # pseudocode
def my_method(
    self,
    other_arg: MyLongType | None,
) -> tuple[MyLongType1, MyLongType1]:
  ...
```

Optionally, the return type may be put on the same line as the last parameter:

```python # pseudocode
# Okay:
def my_method(
    self,
    first_var: int,
    second_var: int) -> dict[OtherLongType, MyLongType]:
  ...
```

pylint allows moving the closing parenthesis to a new line and aligning with the opening one, but this is less
readable.

Incorrect:
```python # pseudocode
def my_method(self,
              other_arg: MyLongType | None,
             ) -> dict[OtherLongType, MyLongType]:
  ...
```

As in the examples above, prefer not to break types. However, sometimes they are too long to be on a single line (try to
keep sub-types unbroken).

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

If a single name and type is too long, consider using an alias for the type. The last resort is to break after the colon
and indent by 4.

Correct:
```python # pseudocode
def my_function(
    long_variable_name:
        long_module_name.LongTypeName,
) -> None:
  ...
```

Incorrect:
```python # pseudocode
def my_function(
    long_variable_name: long_module_name.
        LongTypeName,
) -> None:
  ...
```


## 3 Forward Declarations

If it is necessary to use a class name (from the same module) that is not yet defined â€“ for example, if the class name is needed
inside the declaration of that class, or when using a class that is defined later in the code â€“ either use `from
__future__ import annotations` or use a string for the class name.

Correct:
```python # pseudocode
from __future__ import annotations

class MyClass:
  def __init__(self, stack: Sequence[MyClass], item: OtherClass) -> None:

class OtherClass:
  ...
```

Incorrect:
```python # pseudocode
class MyClass:
  def __init__(self, stack: Sequence["MyClass"], item: "OtherClass") -> None:

class OtherClass:
  ...
```


## 4 Default Values

As per PEP-008, use spaces around the `=` only for arguments that have both a type annotation and a default value.

Correct:
```python # pseudocode
def func(a: int = 0) -> int:
  ...
```

Incorrect:
```python # pseudocode
def func(a:int=0) -> int:
  ...
```


## 5 NoneType

In the Python type system, `NoneType` is a "first class" type, and for typing purposes, `None` is an alias for
`NoneType`. If an argument can be `None`, it has to be declared. Use `|` union type expressions (recommended in
new Python 3.11+ code), or the older `Optional` and `Union` syntaxes.

Use explicit `X | None` instead of implicit. Earlier versions of type checkers allowed `a: str = None` to be interpreted
as `a: str | None = None`, but that is no longer the preferred behavior.

Correct:
```python # pseudocode
def modern_or_union(a: str | int | None, b: str | None = None) -> str:
  ...
def union_optional(a: Union[str, int, None], b: Optional[str] = None) -> str:
  ...
```

Incorrect:
```python # pseudocode
def nullable_union(a: Union[None, str]) -> str:
  ...
def implicit_optional(a: str = None) -> str:
  ...
```


## 6 Type Aliases

It is possible to declare aliases of complex types. The name of an alias should be CapWorded. If the alias is used only in this
module, it should be _Private.

Note that the `: TypeAlias` annotation is only supported in versions 3.11+.

```python # pseudocode
from typing import TypeAlias

_LossAndGradient: TypeAlias = tuple[tf.Tensor, tf.Tensor]
ComplexTFMap: TypeAlias = Mapping[str, _LossAndGradient]
```


## 7 Ignoring Types

Type checking can be disabled on a line with the special comment `# type: ignore`.

pytype has a disable option for specific errors (similar to lint):

```python # pseudocode
# pytype: disable=attribute-error
```


## 8 Typing Variables

### 8.1 Annotated Assignments

If an internal variable has a type that is hard or impossible to infer, specify its type with an annotated assignment -
use a colon and type between the variable name and value (the same as is done with function arguments that have a
default value):

```python # pseudocode
a: Foo = SomeUndecoratedFunction()
```

### 8.2 Type Comments

Though they may remain in the codebase (they were necessary before Python 3.6), do not add any more uses of a
`# type: <type name>` comment on the end of the line:

```python # pseudocode
a = SomeUndecoratedFunction()  # type: Foo
```


## 9 Tuples vs Lists

Typed lists can only contain objects of a single type. Typed tuples can either have a single repeated type or a set
number of elements with different types. The latter is commonly used as the return type from a function.

```python # pseudocode
a: list[int] = [1, 2, 3]
b: tuple[int, ...] = (1, 2, 3)
c: tuple[int, str, float] = (1, "2", 3.5)
```


## 10 Type Variables

The Python type system has generics. A type variable, such as `TypeVar` and `ParamSpec`, is a common way to use them.

Example:

```python # pseudocode
from collections.abc import Callable
from typing import ParamSpec, TypeVar
_P = ParamSpec("_P")
_T = TypeVar("_T")
...
def next(l: list[_T]) -> _T:
  return l.pop()

def print_when_called(f: Callable[_P, _T]) -> Callable[_P, _T]:
  def inner(*args: _P.args, **kwargs: _P.kwargs) -> _T:
    print("Function was called")
    return f(*args, **kwargs)
  return inner
```

A `TypeVar` can be constrained:

```python # pseudocode
AddableType = TypeVar("AddableType", int, float, str)
def add(a: AddableType, b: AddableType) -> AddableType:
  return a + b
```

A common predefined type variable in the typing module is `AnyStr`. Use it for multiple annotations that can be `bytes`
or `str` and must all be the same type.

```python # pseudocode
from typing import AnyStr
def check_length(x: AnyStr) -> AnyStr:
  if len(x) <= 42:
    return x
  raise ValueError()
```

A type variable must have a descriptive name, unless it meets all of the following criteria:

- not externally visible
- not constrained

Correct:
```python # pseudocode
_T = TypeVar("_T")
_P = ParamSpec("_P")
AddableType = TypeVar("AddableType", int, float, str)
AnyFunction = TypeVar("AnyFunction", bound=Callable)
```

Incorrect:
```python # pseudocode
T = TypeVar("T")
P = ParamSpec("P")
_T = TypeVar("_T", int, float, str)
_F = TypeVar("_F", bound=Callable)
```


## 11 String Types

Do not use `typing.Text` in new code. It's only for Python 2/3 compatibility.

Use `str` for string/text data. For code that deals with binary data, use `bytes`.

```python # pseudocode
def deals_with_text_data(x: str) -> str:
  ...
def deals_with_binary_data(x: bytes) -> bytes:
  ...
```

If all the string types of a function are always the same, for example if the return type is the same as the argument
type in the code above, use `AnyStr`.


## 12 Imports for Typing

For symbols (including types, functions, and constants) from the typing or collections.abc modules used to support
static analysis and type checking, always import the symbol itself. This keeps common annotations more concise and
matches typing practices used around the world. It is acceptable to import multiple specific symbols on one
line from the typing and collections.abc modules. For example:

```python # pseudocode
from collections.abc import Mapping, Sequence
from typing import Any, Generic, cast, TYPE_CHECKING
```

Given that this way of importing adds items to the local namespace, names in typing or collections.abc should be treated
similarly to keywords, and not be defined in the Python code, typed or not. If there is a collision between a type and
an existing name in a module, import it using `import x as y`.

```python # pseudocode
from typing import Any as AnyType
```

When annotating function signatures, prefer abstract container types like `collections.abc.Sequence` over concrete types
like `list`. If a concrete type is needed (for example, a tuple of typed elements), prefer built-in types like
`tuple` over the parametric type aliases from the typing module (e.g., `typing.Tuple`).

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


## 13 Conditional Imports

Use conditional imports only in exceptional cases where the additional imports needed for type checking must be avoided
at runtime. This pattern is discouraged; alternatives such as refactoring the code to allow top-level imports should be
preferred.

Imports that are needed only for type annotations can be placed within an `if TYPE_CHECKING:` block.

Conditionally imported types need to be referenced as strings, to be forward compatible with Python 3.6 where the
annotation expressions are actually evaluated.

Only entities that are used solely for typing should be defined here; this includes aliases. Otherwise it will be a
runtime error, as the module will not be imported at runtime.

The block should be right after all the normal imports.

There should be no empty lines in the typing imports list.

Sort this list as if it were a regular imports list.

```python # pseudocode
import typing
if typing.TYPE_CHECKING:
  import sketch
def f(x: "sketch.Sketch"): ...
```


## 14 Circular Dependencies

Circular dependencies that are caused by typing are code smells. Such code is a good candidate for refactoring. Although
technically it is possible to keep circular dependencies, various build systems do not permit this because each
module must depend on the other.

Replace modules that create circular dependency imports with `Any`. Set an alias with a meaningful name, and use the
real type name from this module (any attribute of `Any` is `Any`). Alias definitions should be separated from the last
import by one line.

```python # pseudocode
from typing import Any

some_mod = Any  # some_mod.py imports this module.
...

def my_method(self, var: "some_mod.SomeType") -> None:
  ...
```


## 15 Generics

When annotating, prefer to specify type parameters for generic types in a parameter list; otherwise, the generics'
parameters will be assumed to be `Any`.

Correct:
```python # pseudocode
def get_names(employee_ids: Sequence[int]) -> Mapping[int, str]:
  ...
```

Incorrect:
```python # pseudocode
# This is interpreted as get_names(employee_ids: Sequence[Any]) -> Mapping[Any, Any]
def get_names(employee_ids: Sequence) -> Mapping:
  ...
```

If the best type parameter for a generic is `Any`, make it explicit, but remember that in many cases `TypeVar` might be
more appropriate:

Correct:
```python # pseudocode
def get_names(employee_ids: Sequence[Any]) -> Mapping[Any, str]:
  """Returns a mapping from employee ID to employee name for given IDs."""
```

Incorrect:
```python # pseudocode
_T = TypeVar('_T')
def get_names(employee_ids: Sequence[_T]) -> Mapping[_T, str]:
  """Returns a mapping from employee ID to employee name for given IDs."""
```

