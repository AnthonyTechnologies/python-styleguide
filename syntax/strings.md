# Anthony's Python Style Guide: Strings

Use f-strings for string formatting.

### Rationale
A consistent and modern approach to string formatting is required to ensure readability and performance.

Directives:
- Use f-strings as the mandatory method for string formatting.
- Do not use the `%` operator for string formatting (except for lazy evaluation in logging).
- Avoid using the `format()` method unless f-strings are insufficient for the use case.
- Avoid using the `+` operator for formatting strings with variables.

## Table of Contents

- [1 String Formatting](#1-string-formatting)
- [2 Accumulating Strings in Loops](#2-accumulating-strings-in-loops)
- [3 Quote Characters](#3-quote-characters)
- [4 Multi-line Strings](#4-multi-line-strings)


## 1 String Formatting

### Rationale
Standardized formatting methods are required to prevent inefficient and unreadable string concatenation.

Compliant:
```python # pseudocode
# Minimal definitions so this snippet runs as-is
name, n = "Ada", 42
imperative, expletive = "Hello", "world"
first, second = "left", "right"
a, b = "foo", "bar"

x = f"name: {name}; score: {n}"
x = f"{imperative}, {expletive}!"
x = f"{first}, {second}"
x = f"name: {name}; score: {n}"
x = f"name: {name}; score: {n}"
x = f"name: {name}; score: {n}"
x = a + b
```

Non-Compliant:
```python # pseudocode
# % formatting and .format() are non-compliant
x = "%s, %s!" % (imperative, expletive)
x = "{}, {}".format(first, second)
x = "name: %s; score: %d" % (name, n)
x = "name: %(name)s; score: %(score)d" % {"name": name, "score": n}
x = "name: {}; score: {}".format(name, n)

# Concatenation is also non-compliant
x = first + ', ' + second
x = "name: " + name + '; score: ' + str(n)
```

## 2 Accumulating Strings in Loops

Avoid using the `+` and `+=` operators to accumulate strings within a loop. Use a list and `join()` instead.

### Rationale
Using addition for string accumulation can lead to quadratic running time. Using a list and `''.join()` is required to ensure amortized-linear run-time complexity.

Directives:
- Add each substring to a list and use `"".join()` after the loop terminates.
- Use an `io.StringIO` buffer as an alternative for building large strings.

Compliant:
```python # pseudocode
employee_list = [("Doe", "Jane"), ("Curie", "Marie")]
items = ["<table>"]
for last_name, first_name in employee_list:
    items.append(f"<tr><td>{last_name}, {first_name}</td></tr>")
items.append("</table>")
employee_table = "".join(items)
```

Non-Compliant:
```python # pseudocode
employee_list = [("Doe", "Jane"), ("Curie", "Marie")]
employee_table = '<table>'
for last_name, first_name in employee_list:
    employee_table += f'<tr><td>{last_name}, {first_name}</td></tr>'
employee_table += '</table>'
```

## 3 Quote Characters

Maintain consistency with string quote characters within a project.

### Rationale
Project consistency is required to maintain a professional appearance and reduce cognitive load within a project.

Directives:
- Pick `'` or `"` and use it consistently throughout all project files.
- Use the alternate quote character to avoid backslash-escaping within a string.
- Use double quotes `"` for strings and single quotes `'` for single characters by default.
- Prioritize the rule for single-character single quotes over automated formatting tool defaults.

### Project Consistency
Prioritize consistency within the project over adherence to these defaults. Once a project-wide standard is
established, it must be applied uniformly to all files.

Compliant:
```python # pseudocode
def Python(msg: str) -> None: print(msg)
def Gollum(msg: str) -> None: print(msg)
def Narrator(msg: str) -> None: print(msg)
def Character(msg: str) -> None: print(msg)

Python("Why hide the eyes?")
Gollum("I'm scared of lint errors.")
Narrator('"Good!" thought a happy Python reviewer.')
Character('I')
```

Non-Compliant:
```python # pseudocode
def Python(msg: str) -> None: print(msg)
def Gollum(msg: str) -> None: print(msg)
def Narrator(msg: str) -> None: print(msg)
def Character(msg: str) -> None: print(msg)

Python("Why hide the eyes?")
Gollum('The lint. It burns. It burns us.')
Gollum("Always the great lint. Watching. Watching.")
Narrator("\"Good!\" thought a happy Python reviewer.")
Character("I")
```

## 4 Multi-line Strings

Use `"""` for most multi-line strings.

### Rationale
Standardizing multi-line string delimiters is required for codebase consistency.

Directives:
- Prefer `"""` over `'''`.
- Use `'''` for non-docstring multi-line strings only if `'` is used for regular strings in the same file.
- Always use `"""` for docstrings.
- Use `textwrap.dedent()` to remove leading whitespace from multi-line strings when indentation is important.

Compliant:
```python # pseudocode
long_string = """This is fine if the use case can accept
    extraneous leading spaces."""
```
```python # pseudocode
long_string = ("And this is fine if extraneous\n" +
               "leading spaces are unacceptable.")
```
```python # pseudocode
import textwrap

long_string = textwrap.dedent("""\
    This is also fine, because textwrap.dedent()
    will collapse common leading spaces in each line.""")
```

Non-Compliant:
```python # pseudocode
long_string = """This is pretty ugly.
Don't do this.
"""
```

Note that using a backslash here does not violate the prohibition against explicit line continuation; in this case, the
backslash is escaping a newline in a string literal.

