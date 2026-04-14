# Anthony's Python Style Guide: Summary for AI Agents

This document is the primary entry point for AI coding agents to understand the project's style and architectural standards. It provides compact instructions for common tasks and points to detailed documentation for further reading.

## How to use this guide
1. Follow imperative directives.
2. Review detailed documentation via Markdown links when working on specific topics.
3. Mirror [`templates`](./templates) coding style.
4. Consult tooling configurations in `pyproject.toml`, `noxfile.py`, and `.pre-commit-config.yaml`.

---

## 1 Core Tenets
- **Project Consistency**: Prioritize consistency within the project over strict adherence to this global guide.
- **Readability**: Prioritize code that is easy for humans and agents to read and understand.
- **Consistency**: Maintain a uniform style across the entire codebase.
- **Modularity**: Design for isolated, reusable components.
- **Automation**: Leverage tooling to enforce style and catch errors early.

---

## 2 Project Structure
*Refer to [`project_structure.md`](./project_structure.md) for full details.*

### Directives:
- Use the `src/` layout. Place all installable packages under the `src/` directory.
- Mirror tests. Ensure the `tests/` directory structure mirrors the `src/` package structure exactly.
- Centralize configurations. Keep tool configurations (e.g., `pyproject.toml`, `noxfile.py`) at the repository root.
- Separate resources. Use `docs/` for documentation, `examples/` for runnable usage examples, and `tutorials/` for step-by-step guides.

### Typical Directory:
```
project_root/
├── .github                 # GitHub workflow configurations
├── docs/                   # Project documentation (incl. python-styleguide)
├── examples/               # Runnable usage examples mirroring src/ API areas
├── src/                    # Source code (installable packages live here)
├── tests/                  # Test suite mirroring src/ (unit, integration, perf)
├── tutorials/              # In‑depth, step‑by‑step guides
├── .codecov.yml            # Code coverage configuration
├── .editorconfig           # General config for code editors
├── .gitignore              # Specifies which files Git should ignore
├── .pre-commit-config.yaml # Pre-commit hook configurations
├── CODE_OF_CONDUCT.rst     # Community standards
├── CONTRIBUTING.rst        # How to contribute
├── LICENSE                 # License
├── noxfile.py              # Automation for tests, linting, docs, etc.
├── pyproject.toml          # Config for the project and build/tooling
└── README.rst              # Project overview (reStructuredText)
```

Files and classes must use `# Section Name #` markers to organize code.
- **Class Structure**: Mirror the layout in [`templates/src/templatepackage/user.py`](./templates/src/templatepackage/user.py).
- **Sections**: Use markers like `# Header #`, `# Imports #`, `# Classes #`, `# Static Methods #`, `# Instance Methods #`.

```python
# Classes #

class User:
    """User representation."""

    # Static Methods #

    @staticmethod
    def create() -> "User":
        ...
```

---

## 3 Formatting
*Refer to [`formatting.md`](./syntax/formatting.md) for full details.*

### Directives:
- Limit line length. All lines must be 120 characters or fewer.
  - Exceptions: URLs, imports, pathnames, long string constants, and Pylint disable comments.
- Avoid backslashes for line continuation. Never use `\` for explicit line continuation. Use implicit joining within parentheses, brackets, or braces.
- Use 4 spaces for indentation. Indentation must be 4 spaces per level.
- Do not use semicolons. Semicolons should not be used to terminate or join statements.
- Use trailing commas. Use trailing commas in multi-line sequences (lists, dicts, function arguments).
- Prefer comprehensions. Use list/dict/set comprehensions instead of `map()` or `filter()` for simple logic.
- Simplify return logic. Avoid `else` or `elif` immediately after a `return` or `raise`.
- Follow PEP 8 whitespace rules. Space after commas and around operators is required.

---

## 4 Naming Conventions
*Refer to [`naming.md`](./syntax/naming.md) for full details.*

### Directives:
- Use descriptive names for all entities.
- Compact Naming Guide:
  | Entity Type | Public | Internal/Protected |
  | :--- | :--- | :--- |
  | Packages | `lowercasenounderscores` | - |
  | Modules | `lower_with_under` | `_lower_with_under` |
  | Classes/Exceptions | `CapWords` | `_CapWords` |
  | Functions/Methods/Variables | `lower_with_under` | `_lower_with_under` |
  | Constants | `ALL_CAPS_WITH_UNDER` | `_ALL_CAPS_WITH_UNDER` |
- Never use dashes in filenames. Use `.py` filename extension.
- Prepend a single underscore `_` for internal or protected members. Avoid double underscores (`__`).
- Avoid abbreviations. Use only if universally understood.
- Use single letter names sparingly. Limited to counters (`i`, `j`), exceptions (`e`), or file handles (`f`) in very short scopes.

---

## 5 Typing
*Refer to [`typing.md`](./syntax/typing.md) for full details.*

### Directives:
- Python 3.14+ required.
- Use modern syntax. Built-in generics (e.g., `list[str]`, `dict[str, int]`) must be used instead of `typing.List` or `typing.Dict`.
- Use the `|` operator for Union types. For example, `int | None` should be used instead of `typing.Union`.
- Annotate all function arguments and return types.
- Do not annotate `self` or `cls`. Use `Self` only if explicitly required.

---

## 6 Docstrings and Comments
*Refer to [`docstrings.md`](./syntax/docstrings.md) and [`comments.md`](./syntax/comments.md) for full details.*

### Directives:
- Follow Google style. Use Google style as the baseline for all docstrings.
- Use third-person declarative mood for summary lines and feature descriptions (e.g., "Returns the value").
- Use third-person imperative mood for instructions or requirements (e.g., "The user must call...").
- Include module docstrings. Every file must start with a docstring containing filename, one-line summary, blank line, and detailed description.
- Use triple double quotes `"""` for docstrings.
- Start comments with `# `.
- Format inline comments. Place inline comments at least 2 spaces away from the code.
- Use standardized TODOs: `# TODO: <link_to_issue> - <description>`.

---

## 7 Strings
*Refer to [`strings.md`](./syntax/strings.md) for full details.*

### Directives:
- Use f-strings for all string formatting. Avoid `%` and `.format()`.
- Do not use the `+` operator for formatting.
- Maintain quote consistency. Use double quotes `"` for strings and single quotes `'` for single characters.
- Use triple double quotes for multi-line strings. Use `textwrap.dedent()` to manage indentation.

---

## 8 Exceptions and Logging
*Refer to [`exceptions_error_messages.md`](./syntax/exceptions_error_messages.md) and [`logging.md`](./syntax/logging.md) for full details.*

### Directives:
- Reserve `assert` for tests and examples. Production code must not use `assert` for logic; use `if` checks and explicit exceptions.
- Suffix custom exceptions with `Error`.
- Store messages in a `msg` variable. Store logging, error, and warning messages in a local variable named `msg` before use.
- Use f-strings for exception and warning messages. Messages should state expected versus actual values.
- Use `%` style formatting for logging patterns. Patterns must be stored in the `msg` variable and arguments passed separately.
- Minimize the size of `try` blocks.
- Use appropriate logging levels. Do not use `print()`.
- All exception, logging, and warning messages **must** be stored in a local variable named `msg` before use.

```python
# Compliant
msg = f"Expected {expected}, got {actual}"
raise ValueError(msg)

# Non-Compliant
raise ValueError(f"Expected {expected}, got {actual}")
```

---

## 9 Semantics and File Layout
*Refer to [`semantics.md`](./semantics.md) and [`code_file_layout.md`](./code_file_layout.md) for full details.*

### Directives:
- Keep functions short and focused. Aim for fewer than 40 lines.
- Avoid mutable globals. Use constants or class-level attributes instead.
- Follow the standardized file layout order.
- Organize class layout. Group methods by type (Static -> Class -> Instance) and use `# Section Name #` markers.

---

## 10 Testing
*Refer to [`unit_tests.md`](./tests/unit_tests.md) and [`performance_tests.md`](./tests/performance_tests.md) for full details.*

### Directives:
- Use `pytest` for the testing framework.
- Follow naming conventions for test files. Files must be named `test_*.py` or `*_test.py`.
- Use plain `assert` statements.
- Organize fixtures by scope. Place shared fixtures in `conftest.py`.
- Mirror the `src/` structure for performance tests: `tests/<module>/performance/`.

---

## 12 Security and Bug Prevention
*Refer to [`security.md`](./syntax/security.md) and [`bugs.md`](./syntax/bugs.md) for full details.*

### Directives:
- Never use `assert` for production logic.
- Avoid the `pickle` module for untrusted data. Use `json` or `msgpack`.
- Do not shadow built-ins.
- Avoid mutable class attributes. Initialize lists or dicts in `__init__`; use `ClassVar` for shared state.
- Include abstract methods in ABCs. Abstract base classes must have at least one `@abstractmethod`.

---

## 13 Asynchronous Programming
*Refer to [`async.md`](./syntax/async.md) for full details.*

### Directives:
- Avoid internal timeouts in async functions. Callers should manage timeouts.
- Do not block the event loop. Avoid `time.sleep` in `async` functions.

---

## 14 Tooling
*Refer to [`project_tools.md`](./project_tools.md) for full details.*

### Directives:
- Use `ruff` for linting and formatting.
- Use `mypy` for type checking.
- Use `nox` for automation.
- Use `pre-commit` hooks.
