# Anthony's Python Style Guide

This repository contains a practical, opinionated Python style guide that remixes the official Google Python Style Guide
and augments it with additional guidance for modern Python projects which use Python version greater than or equal to 
3.10. It is intended to be copy‑pasted or referenced directly in projects to keep code consistent, readable, and
maintainable. The structure is a fork of the [Google Style Guide](https://google.github.io/styleguide/pyguide.html) and 
[Hypermodern Python](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/) by 
[Claudio Jolowicz](https://github.com/cjolowicz).

## Features
- Readability
- Consistency
- Modularity
- Project Tools Integration
- Automation

## Machine‑Readable Style Guide Index
For automation and easier adoption, this repo includes a machine‑readable style guide index in 
[`style_guide.toml`](style_guide.toml). Tools and agents can ingest this file to configure linters/formatters
consistently across projects and should be their entry point to using this style guide. If tools and agents need further
clarification, they can review the corresponding files. 

Specific projects tool guidelines can be found in [`project_tools.md`](project_tools.md), for which their configurations 
are set in their respective configuration files, not in `style_guide.toml`.

## Contents
The guide is split into focused documents and templates that can be read independently:

- Top-level files:
  - [`README.md`](README.md): overview and navigation for this style guide repository.
  - [`LICENSE`](LICENSE): open‑source license (MIT).
  - [`style_guide.toml`](style_guide.toml): compact TOML index of key rules for tooling automation.


- Syntax: split into focused topics under `syntax/`:
    - [`formatting.md`](syntax/formatting.md) — code layout conventions such as indentation, line length, whitespace,
      and import organization to keep diffs small and style consistent.
    - [`naming.md`](syntax/naming.md) — naming guide for modules, packages, classes, functions, variables, and constants
      to make intent and scope clear.
    - [`typing.md`](syntax/typing.md) — practical guidance for type hints, optional vs. required annotations, and
      patterns for safer, clearer APIs.
    - [`docstrings.md`](syntax/docstrings.md) — how to document modules, classes, and functions (style, sections, and
      examples) for great IDE and docs support.
    - [`comments.md`](syntax/comments.md) — when and how to comment code effectively, including TODOs and clarifying
      non-obvious decisions.
    - [`strings.md`](syntax/strings.md) — guidelines for quotes, f-strings, formatting, bytes vs. text, and encoding
      concerns.
    - [`exceptions_error_messages.md`](syntax/exceptions_error_messages.md) — raising, catching, and designing helpful
      error messages without masking root causes.
    - [`logging.md`](syntax/logging.md) — structured, level-appropriate logging; avoid print, include context, and keep
      logs machine-parseable.
    - [`resources.md`](syntax/resources.md) — safe handling of files, network connections, subprocesses, and other
      resources with context managers.
- [`semantics.md`](semantics.md) — program structure and behavior guidelines such as mutable global state, function
  length, nested classes/functions, lexical scoping, and threading.
- [`project_structure.md`](project_structure.md) — a reusable repository layout for source, tests, docs, examples,
  tutorials, and configurations.
- [`code_file_layout.md`](code_file_layout.md) — how to organize modules and files internally (headers, imports,
  definitions order, etc.).
- [`documentation.md`](documentation.md) — Sphinx recommendations and configuration notes for building docs, including
  autodoc, autosummary, napoleon, intersphinx, and sphinx‑click.
- [`project_tools.md`](project_tools.md) — guidance for pre‑commit, nox, coverage, editorconfig, CI, and related
  developer tooling.


- Tests: split into focused topics under `tests/`:
    - [`unit_tests.md`](tests/unit_tests.md) — testing mindset and structure, including pytest conventions and fixtures.
    - [`performance_tests.md`](tests/performance_tests.md) — approaches for measuring and guarding performance
      characteristics.


- [`examples.md`](examples.md) — runnable or illustrative examples showing how to apply the style.


- Tutorials: split into focused topics under `tutorials/`:
    - [`module_tutorials.md`](tutorials/module_tutorials.md) — step‑by‑step learning paths for adopting the module
      conventions.
    - [`package_tutorials.md`](tutorials/package_tutorials.md) — step‑by‑step learning paths for adopting the package
      conventions.


- Templates: paste‑ready skeletons under `templates/`:
  - [`__init__template.py`](templates/__init__template.py): template for package initialization modules.
  - [`module_template.py`](templates/module_template.py): template for a new module with recommended layout.
  - [`class_template.py`](templates/class_template.py): template for class design and docstrings.
  - [`function_template.py`](templates/function_template.py): template for well‑documented functions.
  - [`unit_test_template.py`](templates/unit_test_template.py): template for pytest unit tests.
  - [`performance_test_template.py`](templates/performance_test_template.py): template for performance tests.
  - [`example_template.py`](templates/example_template.py): minimal example file showing the conventions.
  - [`tutorial_example.ipynb`](templates/tutorial_example.ipynb): notebook‑style tutorial example.

## Style Guide Implementation

This style guide is modular and can be adopted incrementally. The following outline is the recommended way to implement
this style guide. However, adaptation can be implemented in any way: in a different order, skip some topics entirely, 
etc.

1. Review key aspects of the style guide:
    - Review templates in [`templates/`](templates/) to get a feel for the conventions
    - Study the Syntax and Semantics topics in [`syntax/`](syntax/) and [`semantics.md`](semantics.md)
    - Structure repositories following [`project_structure.md`](project_structure.md)

2. For a new project, consider using the project template:
    - The [Project Template](#project-template) section describes the project template project and links to the 
      repositories

3. Set up tooling and automation:
    - Configure tools following [`project_tools.md`](project_tools.md) and [`documentation.md`](documentation.md)
      guidance
    - Point your automation to [`style_guide.toml`](style_guide.toml)
    - Align tool settings using instructions in [`project_tools.md`](project_tools.md)
    - Add pre-commit hooks and CI checks to catch style violations early

4. Copy or vend the guide:
    - Copy relevant files into your repo (commonly into docs/python-styleguide/), or
    - Reference this repo directly from your docs/CONTRIBUTING.md
    - You can vend this style guide into your project under `docs/python-styleguide/` as described
      in [`project_structure.md`](project_structure.md)

5. Review or use templates:
    - Review templates in [`templates/`](templates/) to get a feel for the conventions
    - Copy or use templates from `templates/` to get started quickly

6. Start with fundamentals:
    - Apply syntax/formatting.md and syntax/naming.md first for fast wins
    - Adopt code_file_layout.md to keep modules consistent

7. Implement testing strategy:
    - Keep tests close to the code
    - Mirror your package structure in tests; see [`unit_tests.md`](tests/unit_tests.md)

8. Expand coverage gradually:
    - Introduce typing, docstrings, logging, and error design guidelines as the codebase matures
    - Consider the other documents' guidelines in addition to the fundamentals

## Project Template

A python package template project is available at https://github.com/AnthonyTechnologies/python-templatepackage. It is a
cookiecutter template that can be used to generate a new python package with this style guide applied. It also includes
configurations for the tools in [`project_tools.md`](project_tools.md). 

## License
Distributed under the terms of the [MIT license](https://opensource.org/licenses/MIT), python-styleguide is free and open source software.

## Contributing
- Proposals for clarifications or updates should reference the section being changed and provide a brief rationale.

## Credits and Related Resources
- Google Python Style Guide: https://google.github.io/styleguide/pyguide.html
- Hypermodern Python: https://cjolowicz.github.io/posts/hypermodern-python-01-setup/
- PEP 8: https://peps.python.org/pep-0008/
- Sphinx: https://www.sphinx-doc.org/
