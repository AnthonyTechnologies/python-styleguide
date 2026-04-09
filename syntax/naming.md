# Anthony's Python Style Guide: Naming

Use descriptive names for all entities, including functions, classes, variables, attributes, and files.

### Rationale
Clear and descriptive naming is required to ensure that code intent is obvious and to reduce the need for excessive comments.

Directives:
- Avoid abbreviations. Ambiguous or unfamiliar abbreviations must not be used. Do not abbreviate by deleting letters within a word.
- Use a `.py` filename extension for all Python files.
- Never use dashes in filenames.

Compliant:
`module_name`, `packagename`, `ClassName`, `method_name`, `ExceptionName`, `function_name`, `mydecorator`, `my_decorator`, `GLOBAL_CONSTANT_NAME`,
`global_var_name`, `instance_var_name`, `function_parameter_name`, `local_var_name`, `query_proper_noun_for_thing`,
`send_acronym_via_https`.

## Table of Contents

- [1 Names to Avoid](#1-names-to-avoid)
- [2 Naming Conventions](#2-naming-conventions)
- [3 File Naming](#3-file-naming)


## 1 Names to Avoid

Directives:
- Do not use dashes (-) in any package or module name.
- Avoid names that needlessly include the type of the variable (e.g., `id_to_name_dict`).
- Use single-character names sparingly. These should only be used for:
  - Counters or iterators (e.g., `i`, `j`, `k`, `v`).
  - Exception identifiers in `try`/`except` statements (e.g., `e`).
  - File handles in `with` statements (e.g., `f`).
  - Private type variables with no constraints (e.g., `_T`).
  - Names that match established mathematical notation.

### Rationale
Descriptiveness must be proportional to the scope of a name's visibility. Short names are required to be limited to very small scopes to prevent ambiguity.

## 2 Naming Conventions

"Internal" refers to entities internal to a module, or protected/private members within a class.

### Rationale
Clear naming conventions are required to signal the intended scope and usage of an entity to other developers and tools.

Directives:
- Prepend a single underscore (`_`) to protect module variables and functions.
- Avoid double underscores (`__`) unless strictly necessary. Name mangling impacts readability and testability, so a single underscore should be used instead.
- Place related classes and top-level functions together in a module.
- Follow specific casing rules for each entity type:
  - Packages: lowercase, no underscores.
  - Modules: lowercase, with underscores.
  - Classes and Exceptions: CapWords (PascalCase).
  - Functions, Methods, and Variables: lowercase, with underscores.
  - Constants: ALL_CAPS_WITH_UNDER.
- Import with an alias if a conflict occurs. For example, `from datetime import tzinfo as TZInfo` is permissible.

Compliant:

| Type | Public | Internal/Protected    |
| ---- | ------ |-----------------------|
| Packages | `lowercasenounderscores` |                       |
| Modules | `lower_with_under` | `_lower_with_under`   |
| Classes | `CapWords` | `_CapWords`           |
| Exceptions | `CapWords` |                       |
| Functions | `lower_with_under()` | `_lower_with_under()` |
| Decorators | `lowercasenounderscores` (preferred) or `lower_with_under` | `_lowercasenounderscores` or `_lower_with_under` |
| Global/Class Constants | `CAPS_WITH_UNDER` | `_CAPS_WITH_UNDER`    |
| Global/Class Variables | `lower_with_under` | `_lower_with_under`   |
| Instance Variables | `lower_with_under` | `_lower_with_under`   |
| Method Names | `lower_with_under()` | `_lower_with_under()` |
| Function/Method Parameters | `lower_with_under` | `_lower_with_under`   |
| Local Variables | `lower_with_under` |                       |

## 3 File Naming

Python filenames must have a `.py` extension and must not contain dashes (-).

### Rationale
Standardized file naming is required for consistency and to ensure that modules can be imported without issues in Python.

Directives:
- Ensure unit test files follow the `lower_with_under` naming convention (e.g., `<name>_test.py`).
