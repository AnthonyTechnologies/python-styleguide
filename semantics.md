# Anthony's Python Style Guide: Semantics

This document provides guidelines for the semantic aspects of Python code based on Google's Python Style Guide with
customizations [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html). It is mostly copy-pasted
from there but has some edits. This document addresses programming practices that affect code behavior and
maintainability, including the use of mutable global state, function length, nested classes and functions, lexical
scoping, and threading considerations. These guidelines help developers write code that is semantically sound, leading
to more robust, maintainable, and bug-free applications.

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

### 1.1 Definition
Module-level values or class attributes that can get mutated during program execution.

### 1.2 Pros
Occasionally useful.

### 1.3 Cons
Breaks encapsulation: Such design can make it hard to achieve valid objectives. For example, if global state is used to
manage a database connection, then connecting to two different databases at the same time (such as for computing
differences during a migration) becomes difficult. Similar problems easily arise with global registries.

Has the potential to change module behavior during the import, because assignments to global variables are done when the
module is first imported.

### 1.4 Decision
Avoid mutable global state.

In those rare cases where using global state is warranted, mutable global entities should be declared at the module
level or as a class attribute and made internal by prepending an `_` to the name. If necessary, external access to
mutable global state must be done through public functions or class methods. See Naming below. Please explain the design
reasons why mutable global state is being used in a comment or a doc linked to from a comment.

Module-level constants are permitted and encouraged. For example: `_MAX_HOLY_HANDGRENADE_COUNT = 3` for an internal use
constant or `SIR_LANCELOTS_FAVORITE_COLOR = "blue"` for a public API constant. Constants must be named using all caps
with underscores. See Naming below.


## 2 Function Length
Prefer small and focused functions.

We recognize that long functions are sometimes appropriate, so no hard limit is placed on function length. If a function
exceeds about 40 lines, think about whether it can be broken up without harming the structure of the program.

Even if a long function works perfectly now, someone modifying it in a few months may add new behavior. This could
result in bugs that are hard to find. Keeping functions short and simple makes it easier for other people to read
and modify the code.

Long and complicated functions may be encountered when working with existing code. Do not be intimidated by modifying such code: if working with a function proves to be difficult, if errors are hard to debug, or if a piece of it is needed in several different contexts, consider breaking up the function into smaller and more manageable pieces.


## 3 Nested/Local/Inner Classes and Functions
Nested local functions or classes are fine when used to close over a local variable. Inner classes are fine.

### 3.1 Definition
A class can be defined inside of a method, function, or class. A function can be defined inside a method or function.
Nested functions have read-only access to variables defined in enclosing scopes.

### 3.2 Pros
Allows definition of utility classes and functions that are only used inside of a very limited scope. Commonly used for
implementing decorators.

### 3.3 Cons
Nested functions and classes cannot be directly tested. Nesting can make the outer function longer and less readable.

### 3.4 Decision
They are fine with some caveats. Avoid nested functions or classes except when closing over a local value other than
`self` or `cls`. Do not nest a function just to hide it from users of a module. Instead, prefix its name with an `_` at
the module level so that it can still be accessed by tests.


## 4 Lexical Scoping
Okay to use, but try to avoid.

### 4.1 Definition
A nested Python function can refer to variables defined in enclosing functions, but cannot assign to them. Variable
bindings are resolved using lexical scoping, that is, based on the static program text. Any assignment to a name in a
block will cause Python to treat all references to that name as a local variable, even if the use precedes the
assignment. If a global declaration occurs, the name is treated as a global variable.

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
and …) programmers.

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
Okay to use, but try to avoid.


## 5 Lambda Functions
Okay for one-liners. Prefer generator expressions over map() or filter() with a lambda.

### 5.1 Definition
Lambdas define anonymous functions in an expression, as opposed to a statement.

### 5.3 Pros
Convenient.

### 5.4 Cons
Harder to read and debug than local functions. The lack of names means stack traces are difficult to understand.
Expressiveness is limited because the function may only contain an expression.

### 5.5 Decision
Lambdas are allowed. If the code inside the lambda function spans multiple lines or is longer than 120 chars, it might
be better to define it as a regular nested function.

For common operations like multiplication, use the functions from the operator module instead of lambda functions. For
example, prefer `operator.mul` to `lambda x, y: x * y`.

## 6 Threading

Do not rely on the atomicity of built-in types.

While Python's built-in data types such as dictionaries appear to have atomic operations, there are corner cases where
they aren't atomic (e.g. if `__hash__` or `__eq__` are implemented as Python methods) and their atomicity should not be
relied upon. Avoid relying on atomic variable assignment (since this in turn depends on dictionaries).

Use the queue module's Queue data type as the preferred way to communicate data between threads. Otherwise, use the
threading module and its locking primitives. Prefer condition variables and `threading.Condition` instead of using
lower-level locks.


## 7 Comprehensions & Generator Expressions
Okay to use for simple cases.

### 7.1 Definition
List, Dict, and Set comprehensions as well as generator expressions provide a concise and efficient way to create
container types and iterators without resorting to the use of traditional loops, `map()`, `filter()`, or `lambda`.

### 7.2 Pros
Simple comprehensions can be clearer and simpler than other dict, list, or set creation techniques. Generator
expressions can be very efficient, since they avoid the creation of a list entirely.

### 7.3 Cons
Complicated comprehensions or generator expressions can be hard to read.

### 7.4 Decision
Comprehensions are allowed, however multiple for clauses or filter expressions are not permitted. Optimize for
readability, not conciseness.

Examples:

Correct:
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

Incorrect:
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

Use default iterators and operators for types that support them, like lists, dictionaries, and files. The built-in types
define iterator methods, too. Prefer these methods to methods that return lists, except that a container should not be
mutated while iterating over it.

Examples:

Correct:
```python # pseudocode
for key in adict: ...
if obj in alist: ...
for line in afile: ...
for k, v in adict.items(): ...
```

Incorrect:
```python # pseudocode
for key in adict.keys(): ...
for line in afile.readlines(): ...
```

## 9 Generators

Use "Yields:" rather than "Returns:" in the docstring for generator functions.

If the generator manages an expensive resource, make sure to force the clean up.

A good way to do the clean up is by wrapping the generator with a context manager PEP-0533.


## 10 Conditional Expressions
Okay for simple cases.

### 10.1 Definition
Conditional expressions (sometimes called a "ternary operator") are mechanisms that provide a shorter syntax for if
statements. For example: `x = 1 if cond else 2`.

### 10.2 Pros
Shorter and more convenient than an if statement.

### 10.3 Cons
May be harder to read than an if statement. The condition may be difficult to locate if the expression is long.

### 10.4 Decision
Okay to use for simple cases. Each portion must fit on one line: true-expression, if-expression, else-expression. Use a
complete if statement when things get more complicated.

Examples:

Correct:
```python # pseudocode
one_line = 'yes' if predicate(value) else 'no'
```
```python # pseudocode
slightly_split = ('yes' if predicate(value)
                  else 'no, nein, nyet')
```
```python # pseudocode
the_longest_ternary_style_that_can_be_done = (
    'yes, true, affirmative, confirmed, correct'
    if predicate(value)
    else 'no, false, negative, nay'
)
```

Incorrect:
```python # pseudocode
# No:
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
Use the "implicit" false if at all possible (with a few caveats).

Use the "implicit" false if possible, e.g., `if foo:` rather than `if foo != []:`. There are a few caveats to keep in mind:

Always use `if foo is None:` (or `is not None`) to check for a None value. E.g., when testing whether a variable or
argument that defaults to None was set to some other value. The other value might be a value that's false in a boolean
context!

Never compare a boolean variable to False using `==`. Use `if not x:` instead. If distinguishing False from
None is necessary, then chain the expressions, such as `if not x and x is not None:`.

For sequences (strings, lists, tuples), use the fact that empty sequences are false, so `if seq:` and `if not seq:` are
preferable to `if len(seq):` and `if not len(seq):` respectively.

When handling integers, implicit false may involve more risk than benefit (i.e., accidentally handling None as 0). A
value that is known to be an integer (and is not the result of len()) may be compared against the integer 0.

Examples:

Correct:
```python # pseudocode
if not users:
    print('no users')
```
```python # pseudocode
if i % 10 == 0:
    self.handle_multiple_of_ten()
```
```python # pseudocode
def f(x=None):
    if x is None:
        x = []
```

Incorrect:
```python # pseudocode
if len(users) == 0:
    print('no users')
```
```python # pseudocode
if not i % 10:
    self.handle_multiple_of_ten()
```
```python # pseudocode
def f(x=None):
    x = x or []
```
Note that '0' (i.e., 0 as string) evaluates to true.

Note that Numpy arrays may raise an exception in an implicit boolean context. Prefer the .size attribute when testing
emptiness of a np.array (e.g. `if not users.size`).

