# Anthony's Python Style Guide: Formatting

Code formatting establishes the visual and syntactic conventions that make Python source readable, consistent, and easy to maintain. While valid exceptions may exist, the goal is uniformity, predictability, and readability.

### Rationale
A consistent formatting style is required to reduce cognitive load and ensure that developers can focus on logic rather than layout.

## Table of Contents

- [1 Punctuation, Spelling, and Grammar](#1-punctuation-spelling-and-grammar)
- [2 Line Length](#2-line-length)
- [3 Semicolons](#3-semicolons)
- [4 Statements](#4-statements)
- [5 Parentheses](#5-parentheses)
- [6 Indentation](#6-indentation)
- [7 Trailing Commas in Sequences of Items](#7-trailing-commas-in-sequences-of-items)
- [8 Blank Lines](#8-blank-lines)
- [9 Whitespace](#9-whitespace)
- [10 Mathematical Notation](#10-mathematical-notation)
- [11 Comprehensions](#11-comprehensions)
- [12 Return Logic](#12-return-logic)
- [13 Exception Raising Syntax](#13-exception-raising-syntax)


## 1 Punctuation, Spelling, and Grammar

Maintain high standards for punctuation, spelling, and grammar. Well-written code is significantly easier to read and understand.

### Rationale
Clear communication in natural language is required for long-term maintainability and readability.

Directives:
- Ensure comments and docstrings are as readable as narrative text. Proper capitalization and punctuation must be used.
- Use complete sentences when they are more readable than sentence fragments.
- Maintain a consistent style for shorter comments, such as those at the end of a line of code.


## 2 Line Length

Limit the maximum line length to 120 characters. This rule is required to ensure that code remains readable on various screen sizes and in split-view editors.

### Rationale
Restricting line length prevents horizontal scrolling and improves the side-by-side comparison of files.

Explicit exceptions to the 120-character limit:
- Long import statements.
- URLs, pathnames, or long flags in comments.
- Long string module-level constants not containing whitespace that would be inconvenient to split across lines.
- Pylint disable comments.

Directives:
- Do not use a backslash for explicit line continuation. Backslashes must be avoided to prevent accidental errors and improve readability.
- Use Python's implicit line joining inside parentheses, brackets, and braces. If necessary, add an extra pair of parentheses around an expression.
- Use parentheses for implicit line joining when a literal string does not fit on a single line.
- Break lines at the highest possible syntactic level. If a line must be broken twice, it should be broken at the same syntactic level both times.
- Put long URLs on their own line within comments if necessary.

Compliant:
```python # pseudocode
foo_bar(
    self,
    width,
    height,
    color='black',
    design=None,
    x='foo',
    emphasis=None,
    highlight=0,
)
```
```python # pseudocode
if (width == 0 and height == 0 and
    color == 'red' and emphasis == 'strong'):
```
```python # pseudocode
(bridge_questions.clarification_on
    .average_airspeed_of.unladen_swallow) = 'African or European?'
```
```python # pseudocode
with (
    very_long_first_expression_function() as spam,
    very_long_second_expression_function() as beans,
    third_thing() as eggs,
):
    place_order(eggs, beans, spam, beans)
```

Non-Compliant:
```python # pseudocode
if width == 0 and height == 0 and \
    color == 'red' and emphasis == 'strong':
```
```python # pseudocode
bridge_questions.clarification_on \
     .average_airspeed_of.unladen_swallow = 'African or European?'
```
```python # pseudocode
with very_long_first_expression_function() as spam, \
     very_long_second_expression_function() as beans, \
     third_thing() as eggs:
    place_order(eggs, beans, spam, beans)
```

Compliant:
```python # pseudocode
x = ('This will build a very long long '
     'long long long long long long string')
```

Compliant:
```python # pseudocode
bridgekeeper.answer(
    name="Arthur",
    quest=questlib.find(owner="Arthur", perilous=True),
)
```
```python # pseudocode
answer = (a_long_line().of_chained_methods()
          .that_eventually_provides().an_answer())
```
```python # pseudocode
if (
    config is None
    or 'editor.language' not in config
    or config['editor.language'].use_spaces is False
):
    use_tabs()
```

Non-Compliant:
```python # pseudocode
bridgekeeper.answer(name="Arthur", quest=questlib.find(
    owner="Arthur", perilous=True))
```
```python # pseudocode
answer = a_long_line().of_chained_methods().that_eventually_provides(
    ).an_answer()
```
```python # pseudocode
if (config is None or 'editor.language' not in config or config[
    'editor.language'].use_spaces is False):
  use_tabs()
```

Compliant:
```python # pseudocode
# See details at
# http://www.example.com/us/developer/documentation/api/content/v2.0/csv_file_name_extension_full_specification.html
```

Compliant:
```python # pseudocode
# See details at
# http://www.example.com/us/developer/documentation/api/content/\
# v2.0/csv_file_name_extension_full_specification.html
```

Make note of the indentation of the elements in the line continuation examples above; see the indentation section for
explanation.

Ensure docstring summary lines remain within the 120-character limit.

In cases where a line exceeds 120 characters and the auto-formatter does not bring it below the limit, the line may exceed this maximum. Manually break the line up per the notes above when sensible.


## 3 Semicolons

Do not terminate lines with semicolons, and do not use semicolons to put two statements on the same line.

### Rationale
Semicolons are redundant in Python and must be avoided to maintain a clean, Pythonic style.


## 4 Statements

Generally, use only one statement per line.

### Rationale
Single-statement lines improve readability and simplify debugging and version control diffs.

Directives:
- Place the result of a test on the same line as the test only if the entire statement fits on one line.
- Do not use one-line statements with `try`/`except`. This is required to ensure that exceptions are not accidentally masked.
- Use a docstring and omit the `pass` statement when defining an empty class, method, or function.

Compliant:
```python # pseudocode
if foo: bar(foo)
```

Non-Compliant:
```python # pseudocode
if foo: bar(foo)
else:   baz(foo)

try:               bar(foo)
except ValueError: baz(foo)

try:
    bar(foo)
except ValueError: baz(foo)
```

## 5 Parentheses

Use parentheses sparingly.

### Rationale
Excessive parentheses increase visual noise without providing additional clarity and should be avoided.

Directives:
- Use parentheses around tuples if preferred, though this is not strictly required.
- Do not use parentheses in `return` statements or conditional statements unless using them for implied line continuation or to indicate a tuple.

Compliant:
```python # pseudocode
if foo:
    bar()
while x:
    x = bar()
if x and y:
    bar()
if not x:
    bar()
# For a 1 item tuple the ()s are more visually obvious than the comma.
onesie = (foo,)
return foo
return spam, beans
return (spam, beans)
for (x, y) in dict.items(): ...
```

Non-Compliant:
```python # pseudocode
if (x):
    bar()
if not(x):
    bar()
return (foo)
```

## 6 Indentation

Indent code blocks with 4 spaces.

### Rationale
Consistent indentation is required to maintain code structure and readability. This is especially important in Python where indentation is semantically significant.

Directives:
- Never use the tab character. Tab characters must be avoided to ensure code is rendered consistently across all environments.
- Ensure the editor is configured to use 4 spaces for indentation.
- Align wrapped elements vertically for implied line continuation or use a hanging 4-space indent.
- Place closing brackets at the end of the expression or on separate lines. If placed on a separate line, indent them the same as the line with the corresponding opening bracket.

Compliant:
```python # pseudocode
# Aligned with opening delimiter.
foo = long_function_name(var_one, var_two,
                         var_three, var_four)
meal = (spam,
        beans)
```
```python # pseudocode
# Aligned with opening delimiter in a dictionary.
foo = {
    'long_dictionary_key': value1 +
                           value2,
    ...
}
```
```python # pseudocode
# 4-space hanging indent; nothing on first line.
foo = long_function_name(
    var_one, var_two, var_three,
    var_four)
meal = (
    spam,
    beans)
```
```python # pseudocode
# 4-space hanging indent; nothing on first line,
# closing parenthesis on a new line.
foo = long_function_name(
    var_one, var_two, var_three,
    var_four
)
meal = (
    spam,
    beans,
)
```
```python # pseudocode
# 4-space hanging indent in a dictionary.
foo = {
    'long_dictionary_key':
        long_dictionary_value,
    ...
}
```

Non-Compliant:
```python # pseudocode
# Stuff on first line forbidden.
foo = long_function_name(var_one, var_two,
    var_three, var_four)
meal = (spam,
    beans)
```
```python # pseudocode
# 4-space hanging indent forbidden.
foo = long_function_name(
    var_one, var_two, var_three,
    var_four)
```
```python # pseudocode
# No hanging indent in a dictionary.
foo = {
    'long_dictionary_key':
    long_dictionary_value,
    ...
}
```


## 7 Trailing Commas in Sequences of Items

Use trailing commas in sequences of items if and only if the closing container token `]`, `)`, or `}` does not appear on the same line as the final element. A trailing comma is required for tuples with a single element.

### Rationale
Trailing commas should be used to simplify version control diffs and to provide a hint to auto-formatters to place items on separate lines.

Compliant:
```python # pseudocode
golomb3 = [0, 1, 3]
golomb4 = [
    0,
    1,
    4,
    6,
]
```

Non-Compliant:
```python # pseudocode
golomb4 = [
    0,
    1,
    4,
    6,]
```


## 8 Blank Lines

Use two blank lines between top-level definitions and one blank line between method definitions.

### Rationale
Vertical whitespace is required to visually separate logical blocks of code and improve readability.

Directives:
- Use two blank lines between top-level function or class definitions.
- Use one blank line between method definitions and between the docstring of a class and the first method.
- Do not use a blank line following a `def` line.
- Use single blank lines as appropriate within functions or methods to separate logical steps.
- Place related comments immediately preceding the definition.


## 9 Whitespace

Follow standard typographic rules for the use of spaces around punctuation.

### Rationale
Consistent whitespace is required to maintain a clean appearance and to ensure that code adheres to established Python conventions.

Directives:
- Do not use whitespace inside parentheses, brackets, or braces.
- Do not use whitespace before a comma, semicolon, or colon.
- Use whitespace after a comma, semicolon, or colon, except at the end of a line.
- Use no whitespace before the open paren/bracket that starts an argument list, indexing, or slicing.
- Do not use trailing whitespace.
- Use a single space on either side of binary operators for assignment, comparisons, and Booleans.
- Use best judgment for the insertion of spaces around arithmetic operators.
- Never use spaces around `=` when passing keyword arguments or defining a default parameter value, unless a type annotation is present.
- Avoid using spaces to vertically align tokens on consecutive lines.

Compliant:
```python # pseudocode
spam(ham[1], {'eggs': 2}, [])
```

Non-Compliant:
```python # pseudocode
spam( ham[ 1 ], { 'eggs': 2 }, [ ] )
```

Compliant:
```python # pseudocode
if x == 4:
     print(x, y)
 x, y = y, x
```

Non-Compliant
```python # pseudocode
if x == 4 :
     print(x , y)
 x , y = y , x
```

Compliant:
```python # pseudocode
spam(1)
```

Non-Compliant:
```python # pseudocode
spam (1)
```

Compliant:
```python # pseudocode
dict['key'] = list[index]
```

Non-Compliant:
```python # pseudocode
dict ['key'] = list [index]
```

Compliant:
```python # pseudocode
x == 1
```

Non-Compliant:
```python # pseudocode
x<1
```

Compliant:
```python # pseudocode
def complex(real, imag=0.0): return Magic(r=real, i=imag)
def complex(real, imag: float = 0.0): return Magic(r=real, i=imag)
```

Non-Compliant:
```python # pseudocode
def complex(real, imag = 0.0): return Magic(r = real, i = imag)
def complex(real, imag: float=0.0): return Magic(r = real, i = imag)
```

Compliant:
```python # pseudocode
foo = 1000  # comment
long_name = 2  # comment that should not be aligned

dictionary = {
    'foo': 1,
    'long_name': 2,
}
```

Non-Compliant:
```python # pseudocode
foo       = 1000  # comment
long_name = 2     # comment that should not be aligned

dictionary = {
    'foo'      : 1,
    'long_name': 2,
}
```


## 10 Mathematical Notation

Use short variable names that match established notation in a reference paper or algorithm for mathematically-heavy code.

### Rationale
In mathematical contexts, matching established notation is required to improve readability and verifiability for domain experts.

Directives:
- Cite the source of all naming conventions in a comment or docstring. Citing the source is required to provide context for the naming choices.
- Prefer PEP 8-compliant descriptive names for public APIs.
- Use tool-specific suppression directives to silence warnings when necessary.


## 11 Comprehensions

Use list, set, and dictionary comprehensions and generator expressions for concise and efficient container creation.

### Rationale
Comprehensions are recommended over functional programming constructs like `map()` and `filter()` for simple logic because they are more readable and performant in Python.

Compliant:
```python # pseudocode
# List comprehension
[x * 2 for x in numbers if x > 0]

# Generator expression
sum(x * 2 for x in numbers)

# Dictionary comprehension
{k: v for k, v in data.items() if v is not None}
```

Non-Compliant:
```python # pseudocode
# Avoid map and filter for simple logic
list(map(lambda x: x * 2, filter(lambda x: x > 0, numbers)))
```


## 12 Return Logic

Structure return statements to maximize clarity and minimize nesting.

### Rationale
Clear return logic is required to ensure that the execution flow of a function is intuitive and easy to follow.

### 12.1 Unnecessary Else after Return
Do not use an `else` or `elif` block immediately following a `return`, `raise`, `break`, or `continue` statement.

### Rationale
Eliminating unnecessary blocks reduces nesting and improves readability.

Compliant:
```python # pseudocode
def check_value(x):
    if x > 0:
        return "Positive"
    return "Non-positive"
```

Non-Compliant:
```python # pseudocode
def check_value(x):
    if x > 0:
        return "Positive"
    else:
        return "Non-positive"
```


## 13 Exception Raising Syntax

Do not use redundant parentheses around the exception object if it does not take any arguments.

### Rationale
Consistent exception syntax is recommended to maintain a clean and uniform codebase.

Compliant:
```python # pseudocode
msg = "Invalid input"
raise ValueError(msg)
raise ValueError
```

Non-Compliant:
```python # pseudocode
raise ValueError()
```


