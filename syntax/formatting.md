# Anthony's Python Style Guide: Formatting

The code formatting should establish the visual and syntactic conventions that make Python source readable, consistent, 
and easy to maintain across a codebase. While there can be sensible exceptions, the aim is uniformity, predictability,
and readability.

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


## 1 Punctuation, Spelling, and Grammar

Pay attention to punctuation, spelling, and grammar; it is easier to read well-written code.

Comments and docstrings should be as readable as narrative text, with proper capitalization and punctuation. In many 
cases, complete sentences are more readable than sentence fragments. Shorter comments, such as comments at the end of 
a line of code, can sometimes be less formal, but the style should remain consistent.


## 2 Line Length

Maximum line length is 120 characters.

Explicit exceptions to the 120 character limit:
- Long import statements.
- URLs, pathnames, or long flags in comments.
- Long string module-level constants not containing whitespace that would be inconvenient to split across lines such as URLs or pathnames.
- Pylint disable comments. (e.g.: `# pylint: disable=invalid-name`)

Do not use a backslash for explicit line continuation.

Instead, make use of Python's implicit line joining inside parentheses, brackets, and braces. If necessary, an extra pair of parentheses can be added around an expression.

Note that this rule doesn't prohibit backslash-escaped newlines within strings (see below).

Examples:

Correct:
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

Incorrect:
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

When a literal string won't fit on a single line, use parentheses for implicit line joining.

```python # pseudocode
x = ('This will build a very long long '
     'long long long long long long string')
```

Prefer breaking lines at the highest possible syntactic level. If a line must be broken twice, break it at the same
syntactic level both times.

Correct:
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

Incorrect:
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

Within comments, put long URLs on their own line if necessary.

Correct:
```python # pseudocode
# See details at
# http://www.example.com/us/developer/documentation/api/content/v2.0/csv_file_name_extension_full_specification.html
```

Correct:
```python # pseudocode
# See details at
# http://www.example.com/us/developer/documentation/api/content/\
# v2.0/csv_file_name_extension_full_specification.html
```

Make note of the indentation of the elements in the line continuation examples above; see the indentation section for
explanation.

Docstring summary lines must remain within the 120 character limit.

In all other cases where a line exceeds 120 characters, and the Black or Pyink auto-formatter does not help bring the
line below the limit, the line is allowed to exceed this maximum. Authors are encouraged to manually break the line up
per the notes above when it is sensible.


## 3 Semicolons

Do not terminate lines with semicolons, and do not use semicolons to put two statements on the same line.


## 4 Statements

Generally only one statement per line.

However, placing the result of a test on the same line as the test is acceptable only if the entire statement fits on one line. In
particular, this must never be done with try/except since the try and except cannot both fit on the same line, and it is
acceptable with an if only when there is no else.

Examples:

Correct:
```python # pseudocode
if foo: bar(foo)
```

Incorrect:
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

It is fine, though not required, to use parentheses around tuples. Do not use them in return statements or conditional
statements unless using parentheses for implied line continuation or to indicate a tuple.

Examples:

Correct:
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

Incorrect:
```python # pseudocode
if (x):
    bar()
if not(x):
    bar()
return (foo)
```

## 6 Indentation

Indent code blocks with 4 spaces.

Never use the tab character.

Some editors automatically insert spaces when the Tab key is pressed. Ensure the editor is configured to use 4 spaces for indentation.

Implied line continuation should align wrapped elements vertically (see line length examples), or use a hanging 4-space
indent. Closing (round, square, or curly) brackets can be placed at the end of the expression, or on separate lines, but
then should be indented the same as the line with the corresponding opening bracket.

Examples:

Correct:
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
# 2-space hanging indent; nothing on first line.
foo = long_function_name(
    var_one, var_two, var_three,
    var_four)
meal = (
    spam,
    beans)
```
```python # pseudocode
# 2-space hanging indent; nothing on first line,
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
# 2-space hanging indent in a dictionary.
foo = {
    'long_dictionary_key':
        long_dictionary_value,
    ...
}
```

Incorrect:
```python # pseudocode
# Stuff on first line forbidden.
foo = long_function_name(var_one, var_two,
    var_three, var_four)
meal = (spam,
    beans)
```
```python # pseudocode
# 2-space hanging indent forbidden.
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

Trailing commas in sequences of items are required if and only if the closing container token `]`, `)`, or `}` does not
appear on the same line as the final element, as well as for tuples with a single element. The presence of a trailing
comma is also used as a hint to the Python code auto-formatter Black or Pyink to direct it to auto-format the container
of items to one item per line when the `,` after the final element is present.

Correct:
```python # pseudocode
golomb3 = [0, 1, 3]
golomb4 = [
    0,
    1,
    4,
    6,
]
```

Incorrect:
```python # pseudocode
golomb4 = [
    0,
    1,
    4,
    6,]
```


## 8 Blank Lines

Two blank lines between top-level definitions, be they function or class definitions. One blank line between method
definitions and between the docstring of a class and the first method. No blank line following a def line. Use single
blank lines as judged appropriate within functions or methods.

Blank lines need not be anchored to the definition. For example, related comments immediately preceding function, class,
and method definitions can make sense. Consider whether the comment might be more useful as part of the docstring.


## 9 Whitespace

Follow standard typographic rules for the use of spaces around punctuation.

No whitespace inside parentheses, brackets, or braces.

Correct:
```python # pseudocode
spam(ham[1], {'eggs': 2}, [])
```

Incorrect:
```python # pseudocode
spam( ham[ 1 ], { 'eggs': 2 }, [ ] )
```

No whitespace before a comma, semicolon, or colon. Do use whitespace after a comma, semicolon, or colon, except at the
end of the line.

Correct:
```python # pseudocode
if x == 4:
     print(x, y)
 x, y = y, x
```

Incorrect
```python # pseudocode
if x == 4 :
     print(x , y)
 x , y = y , x
```

No whitespace before the open paren/bracket that starts an argument list, indexing, or slicing.

Correct:
```python # pseudocode
spam(1)
```

Incorrect:
```python # pseudocode
spam (1)
```

Correct:
```python # pseudocode
dict['key'] = list[index]
```

Incorrect:
```python # pseudocode
dict ['key'] = list [index]
```

No trailing whitespace.

Surround binary operators with a single space on either side for assignment (`=`), comparisons (`==`, `<`, `>`, `!=`,
`<>`, `<=`, `>=`, `in`, `not in`, `is`, `is not`), and Booleans (`and`, `or`, `not`). Use best judgment for the
insertion of spaces around arithmetic operators (`+`, `-`, `*`, `/`, `//`, `%`, `**`, `@`).

Correct:
```python # pseudocode
x == 1
```

Incorrect:
```python # pseudocode
x<1
```

Never use spaces around `=` when passing keyword arguments or defining a default parameter value, with one exception:
when a type annotation is present, do use spaces around the `=` for the default parameter value.

Correct:
```python # pseudocode
def complex(real, imag=0.0): return Magic(r=real, i=imag)
def complex(real, imag: float = 0.0): return Magic(r=real, i=imag)
```

Incorrect:
```python # pseudocode
def complex(real, imag = 0.0): return Magic(r = real, i = imag)
def complex(real, imag: float=0.0): return Magic(r = real, i = imag)
```

Don't use spaces to vertically align tokens on consecutive lines, since it becomes a maintenance burden (applies to `:`,
`#`, `=`, etc.):

Correct:
```python # pseudocode
foo = 1000  # comment
long_name = 2  # comment that should not be aligned

dictionary = {
    'foo': 1,
    'long_name': 2,
}
```

Incorrect:
```python # pseudocode
foo       = 1000  # comment
long_name = 2     # comment that should not be aligned

dictionary = {
    'foo'      : 1,
    'long_name': 2,
}
```


## 10 Mathematical Notation

For mathematically-heavy code, short variable names that would otherwise violate the style guide are preferred when they
match established notation in a reference paper or algorithm.

When using names based on established notation:

- Cite the source of all naming conventions, preferably with a hyperlink to academic resource itself, in a comment or docstring. If the source is not accessible, clearly document the naming conventions.
- Prefer PEP8-compliant descriptive_names for public APIs, which are much more likely to be encountered out of context.
- Use a narrowly-scoped `python # pseudocodelint: disable=invalid-name` directive to silence warnings. For just a few variables, use the directive as an endline comment for each one; for more, apply the directive at the beginning of a block.


