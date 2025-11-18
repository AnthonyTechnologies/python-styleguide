# Anthony's Python Style Guide

## Overview
This repository contains a practical, opinionated Python style guide that remixes the official Google Python Style Guide
and augments it with additional guidance for modern Python projects. It is intended to be copy‑pasted or referenced
directly in projects to keep code consistent, readable, and maintainable. The structure is a fork of the
[Google Style Guide](https://google.github.io/styleguide/pyguide.html) and [Hypermodern Python](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/) by [Claudio Jolowicz](https://github.com/cjolowicz).

## Machine‑readable Guide Index
For automation and easier adoption, this repo includes a machine‑readable guide index at `style_guide.toml`. Tools and
agents can ingest this file to configure linters/formatters consistently across projects. See also
[Linters Mapping](linters_mapping.md) for how this guide maps to popular tools.

## Design Goals
- Readability
- Consistency
- Modularity
- Project Tools Integration

## Contents
The guide is split into focused documents that can be read independently:

- Syntax: split into focused topics under `syntax/`:
  - [Formatting](syntax/formatting.md): `formatting.md` — code layout conventions such as indentation, line length, whitespace, and import organization to keep diffs small and style consistent.
  - [Naming](syntax/naming.md): `naming.md` — naming guide for modules, packages, classes, functions, variables, and constants to make intent and scope clear.
  - [Typing](syntax/typing.md): `typing.md` — practical guidance for type hints, optional vs. required annotations, and patterns for safer, clearer APIs.
  - [Docstrings](syntax/docstrings.md): `docstrings.md` — how to document modules, classes, and functions (style, sections, and examples) for great IDE and docs support.
  - [Comments](syntax/comments.md): `comments.md` — when and how to comment code effectively, including TODOs and clarifying non-obvious decisions.
  - [Strings](syntax/strings.md): `strings.md` — guidelines for quotes, f-strings, formatting, bytes vs. text, and encoding concerns.
  - [Exceptions & Error Messages](syntax/exceptions_error_messages.md): `exceptions_error_messages.md` — raising, catching, and designing helpful error messages without masking root causes.
  - [Logging](syntax/logging.md): `logging.md` — structured, level-appropriate logging; avoid print, include context, and keep logs machine-parseable.
  - [Resources](syntax/resources.md): `resources.md` — safe handling of files, network connections, subprocesses, and other resources with context managers.
- [Semantics](semantics.md): `semantics.md` — program structure and behavior guidelines such as mutable global state, function length, nested classes/functions, lexical scoping, and threading.
- [Project Structure](project_structure.md): `project_structure.md` — a reusable repository layout for source, tests, docs, examples, tutorials, and configurations.
- [Code & File Layout](code_file_layout.md): `code_file_layout.md` — how to organize modules and files internally (headers, imports, definitions order, etc.).
- [Documentation](documentation.md): `documentation.md` — Sphinx recommendations and configuration notes for building docs, including autodoc, autosummary, napoleon, intersphinx, and sphinx‑click.
- [Project Tooling](project_tools.md): `project_tools.md` — guidance for pre‑commit, nox, coverage, editorconfig, CI, and related developer tooling.
- Tests: split into focused topics under `tests/`:
  - [Unit Tests](tests/unit_tests.md): `unit_tests.md` — testing mindset and structure, including pytest conventions and fixtures.
  - [Performance Tests](tests/performance_tests.md): `performance_tests.md` — approaches for measuring and guarding performance characteristics.
- [Examples](examples.md): `examples.md` — runnable or illustrative examples showing how to apply the style.
- Tutorials: split into focused topics under `tutorials/`:
    - [Module Tutorials](tutorials/module_tutorials.md): `module_tutorials.md` — step‑by‑step learning paths for adopting the module conventions.
    - [Package Tutorials](tutorials/package_tutorials.md): `package_tutorials.md` — step‑by‑step learning paths for adopting the package conventions.

### Indexes and Templates
- [Guide Index (machine‑readable)](style_guide.toml): a compact TOML file mirroring the most important guide for automation.
- [Templates](templates/): paste‑ready templates for modules, classes, functions, and example files.
- [Linters Mapping](linters_mapping.md): how the Guide Index maps to Ruff, Mypy, isort, and docformatter settings.
- [Do/Don't Cheat Sheet](cheatsheet.md): a one‑page quick reference with code pairs.

## Quick Start
- Review high‑level expectations in Syntax topics (see the bullets under Contents → Syntax) and [Semantics](semantics.md).
- Structure repositories following [Project Structure](project_structure.md).
- Configure tooling following [Project Tools](project_tools.md) and [Documentation](documentation.md) guidance.
- Point your automation to [style_guide.toml](style_guide.toml) and align tool settings using [Linters Mapping](linters_mapping.md).
- Keep tests close to the code and mirror the package structure: [Unit Tests](tests/unit_tests.md).
- Consider the other documents’ guidelines in addition to the first ones listed here.
- You can vend this style guide into your project under `docs/python-styleguide/` as described in [Project Structure](project_structure.md).

## License
Distributed under the terms of the [MIT license](https://opensource.org/licenses/MIT), python-styleguide is free and open source software.

## Contributing
- Proposals for clarifications or updates should reference the section being changed and provide brief rationale.

## Related Resources
- Google Python Style Guide: https://google.github.io/styleguide/pyguide.html
- Hypermodern Python: https://cjolowicz.github.io/posts/hypermodern-python-01-setup/
- PEP 8: https://peps.python.org/pep-0008/
- Sphinx: https://www.sphinx-doc.org/
