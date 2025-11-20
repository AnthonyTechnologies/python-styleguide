# Anthony's Python Style Guide: Strings

Use an f-string, the % operator, or the format method for formatting strings, even when the parameters are all strings.
Use sound judgment to decide between string formatting options. A single join with + is okay but do not format with
+.

## Table of Contents

- [1 String Formatting](#1-string-formatting)
- [2 Accumulating Strings in Loops](#2-accumulating-strings-in-loops)
- [3 Quote Characters](#3-quote-characters)
- [4 Multi-line Strings](#4-multi-line-strings)


## 1 String Formatting

Correct:
```python # pseudocode
# Minimal definitions so this snippet runs as-is
name, n = "Ada", 42
imperative, expletive = "Hello", "world"
first, second = "left", "right"
a, b = "foo", "bar"

x = f"name: {name}; score: {n}"
x = "%s, %s!" % (imperative, expletive)
x = "{}, {}".format(first, second)
x = "name: %s; score: %d" % (name, n)
x = "name: %(name)s; score: %(score)d" % {"name": name, "score": n}
x = "name: {}; score: {}".format(name, n)
x = a + b
```

Incorrect:
```python # pseudocode
first, second = "left", "right"
name, n = "Ada", 42
x = first + ', ' + second
x = "name: " + name + '; score: ' + str(n)
```

## 2 Accumulating Strings in Loops

Avoid using the `+` and `+=` operators to accumulate a string within a loop. In some conditions, accumulating a string
with addition can lead to quadratic rather than linear running time. Although common accumulations of this sort may be
optimized on CPython, that is an implementation detail. The conditions under which an optimization applies are not easy
to predict and may change. Instead, add each substring to a list and `''.join` the list after the loop terminates, or
write each substring to an `io.StringIO` buffer. These techniques consistently have amortized-linear run-time
complexity.

Correct:
```python # pseudocode
employee_list = [("Doe", "Jane"), ("Curie", "Marie")]
items = ['<table>']
for last_name, first_name in employee_list:
    items.append('<tr><td>%s, %s</td></tr>' % (last_name, first_name))
items.append('</table>')
employee_table = ''.join(items)
```

Incorrect:
```python # pseudocode
employee_list = [("Doe", "Jane"), ("Curie", "Marie")]
employee_table = '<table>'
for last_name, first_name in employee_list:
    employee_table += '<tr><td>%s, %s</td></tr>' % (last_name, first_name)
employee_table += '</table>'
```

## 3 Quote Characters

Be consistent with the choice of string quote character within a file. Pick `'` or `"` and stick with it. It is okay to
use the other quote character on a string to avoid the need to backslash-escape quote characters within the string.
Typically, double quotes `"` should be used for strings and `'` should be used for single characters.

Correct:
```python # pseudocode
def Python(msg: str) -> None: print(msg)
def Gollum(msg: str) -> None: print(msg)
def Narrator(msg: str) -> None: print(msg)
def Character(msg: str) -> None: print(msg)

Python('Why hide the eyes?')
Gollum("I'm scared of lint errors.")
Narrator('\"Good!\" thought a happy Python reviewer.')
Character('I')
```

Incorrect:
```python # pseudocode
def Python(msg: str) -> None: print(msg)
def Gollum(msg: str) -> None: print(msg)
def Character(msg: str) -> None: print(msg)

Python("Why hide the eyes?")
Gollum('The lint. It burns. It burns us.')
Gollum("Always the great lint. Watching. Watching.")
Character("I")
```

## 4 Multi-line Strings

Prefer `"""` for multi-line strings rather than `'''`. Projects may choose to use `'''` for all non-docstring multi-line
strings if and only if they also use `'` for regular strings. Docstrings must use `"""` regardless.

Multi-line strings do not flow with the indentation of the rest of the program. If it is necessary to avoid embedding extra
space in the string, use either concatenated single-line strings or a multi-line string with `textwrap.dedent()` to
remove the initial space on each line:

Correct:
```python # pseudocode
long_string = """This is fine if the use case can accept
    extraneous leading spaces."""
```
```python # pseudocode
long_string = ("And this is fine if one cannot accept\n" +
               "extraneous leading spaces.")
```
```python # pseudocode
long_string = ("And this too is fine if one cannot accept\n"
               "extraneous leading spaces.")
```
```python # pseudocode
import textwrap

long_string = textwrap.dedent("""\
    This is also fine, because textwrap.dedent()
    will collapse common leading spaces in each line.""")
```

Incorrect:
```python # pseudocode
long_string = """This is pretty ugly.
Don't do this.
"""
```

Note that using a backslash here does not violate the prohibition against explicit line continuation; in this case, the
backslash is escaping a newline in a string literal.

