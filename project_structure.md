# Anthony's Python Style Guide: Project Structure

This document describes an opinionated, practical structure for Python projects used in this repository and intended to
be reusable for most Python packages. The structure is a fork of ["Hypermodern Python"](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/) by [Claudio Jolowicz](https://github.com/cjolowicz).

A consistent structure improves:
- Discoverability: developers can quickly find code, tests, docs, and examples.
- Maintainability: changes affect a single, well‑defined place.
- Tooling integration: common tools (pytest, nox, pre-commit, type checkers, doc builders) work with little or no extra configuration.

## Table of Contents

- [1 Project Overview](#1-project-overview)
- [2 Project Root Structure](#2-project-root-structure)
    - [2.1 Configurations](#21-configurations)
        - [2.1.1 Python Project Config](#211-python-project-config)
        - [2.1.2 Development Tools](#212-development-tools)
    - [2.2 Source Code](#22-source-code)
    - [2.3 Tests](#23-tests)
    - [2.4 Documentation](#24-documentation)
    - [2.5 Examples](#25-examples)
    - [2.6 Tutorials](#26-tutorials)
- [3 Implementation Guidelines](#3-implementation-guidelines)
    - [3.1 Applying Generically](#31-applying-generically)
    - [3.2 Best Practices](#32-best-practices)


## 1 Project Overview

Split a Python project into:
- Configurations that define the behavior of the project and its tools.
- Source code (installable package under `src/`).
- Tests that mirror source code.
- Documentation (narrative guides, API references, and style guides).
- Examples that demonstrate typical usage.
- Tutorials for step-by-step learning paths.

Maintain this separation to keep responsibilities clear and enable parallel development across these areas.


## 2 Project Root Structure

A typical repository root resembles the following:

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

### 2.1 Configurations

Configuration files define how the project is built, tested, documented, formatted, and released. Keep these files at the repository root so tools can auto-discover them.

Guidelines:
- Refer to [project_tools.md](project_tools.md) for how pre-commit, nox, and other tools are configured and used.
- Centralize tool configurations (ruff/flake8, black, isort, pytest, coverage, mypy, sphinx) inside `pyproject.toml` when supported.
- Treat `pyproject.toml` as the source of truth for package metadata.
- Keep versioning unified (prefer single-source versioning via package `__init__` or Poetry’s version field).
- When using Poetry, it is acceptable to expose metadata via the PEP 621 `[project]` table and set dynamic fields (e.g., version, readme) that are sourced from `[tool.poetry]`. Document this clearly in the `README`/`CONTRIBUTING` to avoid confusion.
- Ensure CI runs nox sessions to keep local and CI workflows aligned.
- Make pre-commit mandatory in contributor docs.

### 2.2 Source Code

Use the `src/` layout to prevent accidental imports from the project root and to mirror how the package is installed from a wheel/SDist.

Guidelines:
- Refer to [code_file_layout.md](code_file_layout.md) for file structure, headers, imports, and definitions layout.
- Refer to the Syntax topics — [Formatting](syntax/formatting.md), [Naming](syntax/naming.md), [Typing](syntax/typing.md), [Docstrings](syntax/docstrings.md), [Comments](syntax/comments.md), [Strings](syntax/strings.md), [Exceptions & Error Messages](syntax/exceptions_error_messages.md), [Logging](syntax/logging.md), and [Resources](syntax/resources.md) — for naming, docstrings, comments, and formatting rules.
- Refer to [semantics.md](semantics.md) for code organization principles and design guidance.

Structure:
```
src/
└── packagename/
    ├── module1/
    ├── module2/
    ├── module3/
    ├── testsuite/       # Base test suites for the package
    ├── __init__.py
    └── py.typed         # Present if typing information is shipped
```

Guidelines:
- Organize by domain: each top-level subpackage focuses on a clear subject (e.g., bases, collections, functions, operations for baseobjects).
- Keep public API explicit via __all__ or documented imports in __init__.py.
- Consider private implementation modules prefixed with _ when appropriate.

### 2.3 Tests

Tests should mirror the source structure to make navigation intuitive.

Related guidelines:
- Unit Tests — see [unit_tests.md](tests/unit_tests.md) for conventions on structure, naming, fixtures, and assertions.
- Performance Tests — see [performance_tests.md](tests/performance_tests.md) for organizing and executing performance-focused tests.

Structure:
```
tests/
├── module1/
├── module2/
├── module3/
├── .ruff_tests.toml
└── __init__.py
```

Recommendations:
- Separate performance tests when applicable:
```
tests/
└── module1/
    ├── performance/
    └── functional_test.py
```
- Include unit, integration, and property-based tests where they add value.
- Prefer descriptive test names and arrange-act-assert structure.

Linting:
- This directory uses a local Ruff configuration at tests/.ruff_tests.toml to tailor linting rules for tests. It
extends/overrides root pyproject [tool.ruff] settings for files under tests/.

### 2.4 Documentation

Use documentation to consolidate user and developer knowledge.

Guidelines:
- Refer to [documentation.md](documentation.md) for guidelines on writing, organizing, and maintaining documentation, including docstrings, user guides, and API references.
- Refer to [project_tools.md](project_tools.md) for how documentation is built and served via nox (docs and docs-build sessions) and where Sphinx is configured.
- Author in a format supported by the documentation toolchain (e.g., Sphinx/reStructuredText, MkDocs/Markdown).
- Keep API docs generated from code docstrings where possible.
- Cross-link examples and tutorials to relevant guides.

### 2.5 Examples

Ensure examples demonstrate common usage scenarios and mirror the `src/` structure.

Guidelines:
- Refer to [examples.md](examples.md) for structure, formatting, narrative style, and expectations for runnable snippets.
- Ensure each example is a runnable, minimal script focused on one concept.
- Include comments and expected outputs when helpful.

Structure:
```
examples/
├── module1/
├── module2/
├── module3/
├── .ruff_examples.toml
└── __init__.py
```

Linting:
- This directory uses a local Ruff configuration at examples/.ruff_examples.toml to tailor linting rules for example code. It extends/overrides root pyproject [tool.ruff] settings for files under examples/.

### 2.6 Tutorials

Use tutorials to provide step-by-step learning paths and deeper explorations. Tutorials should also mirror the `src/` structure.

Guidelines:
- Refer to [module_tutorials.md](tutorials/module_tutorials.md) for how to design, structure, and validate tutorials focused on a single module.
- Refer to [package_tutorials.md](tutorials/package_tutorials.md) for end-to-end package tutorials, including structure, scope, and documentation tips.
- Build progressively: start from basics and layer complexity.
- Include prerequisites, goals, time estimates, and validation steps.

Structure:
```
tutorials/
├── module1/
├── module2/
├── module3/
├── .ruff_tutorials.toml
└── __init__.py
```

Linting:
- This directory uses a local Ruff configuration at tutorials/.ruff_tutorials.toml to tailor linting rules for tutorial content. It extends/overrides root pyproject [tool.ruff] settings for files under tutorials/.


## 3 Implementation Guidelines

### 3.1 Applying Generically

Apply this structure to a new or existing project:

Guidelines:
- Refer to the Syntax topics — [Formatting](syntax/formatting.md), [Naming](syntax/naming.md), [Typing](syntax/typing.md), [Docstrings](syntax/docstrings.md), [Comments](syntax/comments.md), [Strings](syntax/strings.md), [Exceptions & Error Messages](syntax/exceptions_error_messages.md), [Logging](syntax/logging.md), and [Resources](syntax/resources.md) — for code-level conventions to apply when creating modules and packages.
- Refer to [semantics.md](semantics.md) for organizing code by responsibility and maintaining cohesion.
- Refer to [project_tools.md](project_tools.md) for automating checks and workflows via pre-commit and nox.

1. Create foundational directories:
   - `src/`, `tests/`, `docs/`, `examples/`, `tutorials/` (as needed).
   - Add root configuration files.
2. Identify logical domains:
   - Split source into coherent subpackages per domain.
   - Avoid “misc” or overly broad modules.
3. Mirror structure across artifacts:
   - Align tests and examples with `src/` modules.
4. Automate common flows:
   - Use nox to standardize test, lint, type-check, build, and docs sessions.
   - Wire pre-commit to run formatters/linters locally.
5. Document:
   - Provide a `README`, contribution guide, and usage docs.
   - Maintain a changelog and API docs for public packages.

### 3.2 Best Practices

1. Keep modules focused and cohesive.
2. Maintain parallel structure for code, tests, and examples.
3. Use descriptive, consistent naming.
4. Separate implementation details with private modules (prefix with _).
5. Provide typing information (py.typed) and type hints.
6. Document public APIs with docstrings; generate API docs.
7. Include unit, integration, and, where helpful, performance tests.
8. Prefer automation (nox, pre-commit) to enforce consistency.

By following these guidelines, the result is a Python project that is easy to navigate, test, and maintain.
