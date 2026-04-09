# Anthony's Python Style Guide: Semantics

This document establishes guidelines for the semantic aspects of Python code, including program structure, behavior, and maintainability.

### Rationale
Semantically sound code is required to ensure that applications are robust, maintainable, and predictable.

## Table of Contents

- [1 Mutable Global State](#1-mutable-global-state)
    - [1.1 Definition](#11-definition)
    - [1.2 Pros](#12-pros)
    - [1.3 Cons](#13-cons)
    - [1.4 Decision](#14-decision)
- [2 Function Length](#2-function-length)
- [3 Nested/Local/Inner Classes and Functions](#3-nestedlocalinner-classes-and-functions)
    - [3.1 Definition](#31-definition)
    - [3.2 Pros](#32-pros)
    - [3.3 Cons](#33-cons)
    - [3.4 Decision](#34-decision)
- [4 Lexical Scoping](#4-lexical-scoping)
    - [4.1 Definition](#41-definition)
    - [4.2 Pros](#42-pros)
    - [4.3 Cons](#43-cons)
    - [4.4 Decision](#44-decision)
- [5 Lambda Functions](#5-lambda-functions)
    - [5.1 Definition](#51-definition)
    - [5.2 Pros](#52-pros)
    - [5.3 Cons](#53-cons)
    - [5.4 Decision](#54-decision)
- [6 Threading](#6-threading)
- [7 Comprehensions & Generator Expressions](#7-comprehensions--generator-expressions)
    - [7.1 Definition](#71-definition)
    - [7.2 Pros](#72-pros)
    - [7.3 Cons](#73-cons)
    - [7.4 Decision](#74-decision)
- [8 Default Iterators and Operators](#8-default-iterators-and-operators)
- [9 Generators](#9-generators)
- [10 Conditional Expressions](#10-conditional-expressions)
    - [10.1 Definition](#101-definition)
    - [10.2 Pros](#102-pros)
    - [10.3 Cons](#103-cons)
    - [10.4 Decision](#104-decision)
- [11 True/False Evaluations](#11-truefalse-evaluations)


## 1 Mutable Global State

Avoid mutable global state.

### Rationale
Mutable global state breaks encapsulation and can lead to unpredictable behavior, especially during concurrent execution or module imports.

Directives:
- Do not use mutable module-level values or class attributes.
- Use module-level constants for fixed values.
- Declare mutable entities as internal (prefixed with `_`) and provide access through public functions or class methods if global state is strictly required.
- Explain the necessity of global state in a comment.


## 2 Function Length

Use small and focused functions.

### Rationale
Short functions are required to improve readability, simplify testing, and reduce the likelihood of introducing bugs during modification.

Directives:
- Aim for functions that are approximately 40 lines or fewer.
- Break up functions that exceed this length if the program structure allows.
- Prioritize clarity and simplicity over brevity.


## 3 Nested/Local/Inner Classes and Functions

Nested local functions or classes are permissible when used to close over a local variable.

### Rationale
Nesting allows for the definition of utility entities within a limited scope, which is required for patterns like decorators.

Directives:
- Avoid nesting functions or classes unless closing over a local value (other than `self` or `cls`).
- Do not nest entities solely to hide them from module users; use an internal name (prefixed with `_`) at the module level instead.


## 4 Lexical Scoping

Use lexical scoping with caution.

### Rationale
Lexical scoping provides a powerful mechanism for referring to variables in enclosing scopes, but it can lead to confusing bugs if variable bindings are misunderstood.

Directives:
- Ensure understanding of how Python resolves names in nested scopes before using lexical scoping.
- Avoid re-assigning names in inner scopes that are also used in outer scopes to prevent unintended shadowing.

Example:
```python # pseudocode
from collections.abc import Callable

def get_adder(summand1: float) -> Callable[[float], float]:
    """Returns a function that adds numbers to a given number."""
    def adder(summand2: float) -> float:
        return summand1 + summand2

    return adder
```
### 4.2 Pros
Often results in clearer, more elegant code. Especially comforting to experienced Lisp and Scheme (and Haskell and ML
and �) programmers.

### 4.3 Cons
Can lead to confusing bugs, such as this example based on PEP-0227:
```python # pseudocode
from collections.abc import Iterable
i = 4
def foo(x: Iterable[int]):
    def bar():
        print(i, end='')
    # ...
    # A bunch of code here
    # ...
    for i in x:  # Ah, i *is* local to foo, so this is what bar sees
        print(i, end='')
    bar()
```
So `foo([1, 2, 3])` will print `1 2 3 3`, not `1 2 3 4`.

### 4.4 Decision
Use them when necessary, but try to avoid them.


## 5 Lambda Functions

Use lambda functions for simple, one-line expressions.

### Rationale
Lambdas are recommended for concise, anonymous function definitions where a full function name is not necessary for clarity.

Directives:
- Prefer generator expressions over `map()` or `filter()` with a lambda.
- Avoid multi-line lambdas or those exceeding 120 characters; define a regular nested function instead.
- Use the `operator` module for common operations (e.g., `operator.mul`) instead of lambda functions.

## 6 Threading

Do not rely on the atomicity of built-in types.

### Rationale
Built-in operations may not be atomic in all corner cases, making reliance on them unsafe for thread-critical logic.

Directives:
- Use `queue.Queue` for inter-thread communication.
- Use the `threading` module and its locking primitives for shared state.
- Prefer `threading.Condition` over lower-level locks.


## 7 Comprehensions & Generator Expressions

Use comprehensions and generator expressions for simple cases.

### Rationale
Comprehensions provide a concise and efficient way to create containers, but they can become unreadable if they are overly complex.

Directives:
- Use list, dict, and set comprehensions for simple mapping and filtering.
- Use generator expressions for memory-efficient iteration.
- Do not use multiple `for` clauses or filter expressions in a single comprehension.
- Optimize for readability rather than absolute conciseness.

Compliant:
```python # pseudocode
result = [mapping_expr for value in iterable if filter_expr]
```
```python # pseudocode
result = [
    is_valid(metric={'key': value})
    for value in interesting_iterable
    if a_longer_filter_expression(value)
]
```
```python # pseudocode
descriptive_name = [
    transform({'key': key, 'value': value}, color='black')
    for key, value in generate_iterable(some_input)
    if complicated_condition_is_met(key, value)
]
```
```python # pseudocode
result = []
for x in range(10):
    for y in range(5):
        if x * y > 10:
            result.append((x, y))
```
```python # pseudocode
return {
    x: complicated_transform(x)
    for x in long_generator_function(parameter)
    if x is not None
}
```
```python # pseudocode
return (x**2 for x in range(10))
```
```python # pseudocode
unique_names = {user.name for user in users if user is not None}
```

Non-Compliant:
```python # pseudocode
result = [(x, y) for x in range(10) for y in range(5) if x * y > 10]
```
```python # pseudocode
return (
    (x, y, z)
    for x in range(5)
    for y in range(5)
    if x != y
    for z in range(5)
    if y != z
)
```


## 8 Default Iterators and Operators

Use default iterators and operators for types that support them (e.g., lists, dictionaries, files).

### Rationale
Default iterators are required to ensure code is Pythonic, efficient, and consistent with built-in behavior.

Directives:
- Prefer default iteration (e.g., `for key in adict`) over explicit method calls (e.g., `for key in adict.keys()`).
- Avoid mutating a container while iterating over it.

Compliant:
```python # pseudocode
for key in adict: ...
if obj in alist: ...
for line in afile: ...
for k, v in adict.items(): ...
```

Non-Compliant:
```python # pseudocode
for key in adict.keys(): ...
for line in afile.readlines(): ...
```

## 9 Generators

Use generators to implement efficient iterators.

### Rationale
Generators are recommended for handling large data sets or expensive operations because they yield values lazily.

Directives:
- Use `Yields:` instead of `Returns:` in the docstring.
- Ensure generators that manage expensive resources are properly cleaned up, ideally using a context manager.


## 10 Conditional Expressions

Use conditional expressions (ternary operators) for simple, one-line cases.

### Rationale
Conditional expressions are recommended for improving brevity in simple assignments without sacrificing clarity.

Directives:
- Use the `true_value if condition else false_value` syntax.
- Ensure each portion fits on one line.
- Use a complete `if` statement for complex logic.

Compliant:
```python # pseudocode
one_line = 'yes' if predicate(value) else 'no'
```

Non-Compliant:
```python # pseudocode
bad_line_breaking = ('yes' if predicate(value) else
                     'no')
```
```python # pseudocode
portion_too_long = ('yes'
                    if some_long_module.some_long_predicate_function(
                        really_long_variable_name)
                    else 'no, false, negative, nay')
```


## 11 True/False Evaluations

Use the implicit "falsiness" of Python objects where possible.

### Rationale
Implicit Boolean evaluations are required to write idiomatic Python code that is concise and readable.

Directives:
- Use `if not x:` to check for empty containers or `None`.
- Use `if x:` to check for non-empty containers or non-zero values.
- Prefer `if x is None:` or `if x is not None:` when explicitly checking for the `None` singleton.
- Avoid comparing Boolean variables to `True` or `False`.
- Use the `.size` attribute when testing emptiness of a NumPy array.

Compliant:
```python # pseudocode
if not users:
    print('no users')

if i % 10 == 0:
    self.handle_multiple_of_ten()

def f(x=None):
    if x is None:
        x = []
```

Non-Compliant:
```python # pseudocode
if len(users) == 0:
    print('no users')

if not i % 10:
    self.handle_multiple_of_ten()

def f(x=None):
    x = x or []
```
Directives:
- Use the `.size` attribute when testing emptiness of a NumPy array (e.g., `if not users.size`).
- Note that '0' (as a string) evaluates to true.

