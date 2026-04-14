# Anthony's Python Style Guide: Project Tooling

Use a standardized set of development tools to ensure consistency and automation across all projects. Two tools are central to managing the workflow:

- **nox**: Automates repeatable development tasks in isolated virtual environments.
- **pre-commit**: Automates formatting and quick static checks on each commit.

### Rationale
A unified tooling strategy is required to provide a predictable development environment and reduce manual effort for repetitive tasks like testing and linting.

Directives:
- Store tool configurations in their respective projects (e.g., `pyproject.toml`, `noxfile.py`).
- Refer to the [Python Package Project Template](https://github.com/AnthonyTechnologies/python-packagetemplate) for canonical configuration examples.

## Table of Contents

- [1 Nox](#1-nox)
    - [1.1 Purpose](#11-purpose)
    - [1.2 Installation](#12-installation)
    - [1.3 Common Sessions](#13-common-sessions)
    - [1.4 Running Sessions](#14-running-sessions)
- [2 Pre-commit](#2-pre-commit)
    - [2.1 Purpose](#21-purpose)
    - [2.2 Installation](#22-installation)
    - [2.3 Running Hooks](#23-running-hooks)
    - [2.4 Updating Hooks](#24-updating-hooks)
- [3 Ruff](#3-ruff)
    - [3.1 Purpose](#31-purpose)
    - [3.2 Installation](#32-installation)
    - [3.3 Running Ruff](#33-running-ruff)
    - [3.4 Updating](#34-updating)
- [4 isort](#4-isort)
    - [4.1 Purpose](#41-purpose)
    - [4.2 Installation](#42-installation)
    - [4.3 Running isort](#43-running-isort)
    - [4.4 Updating](#44-updating)
- [5 pip-audit](#5-pip-audit)
    - [5.1 Purpose](#51-purpose)
    - [5.2 Installation](#52-installation)
    - [5.3 Running pip-audit](#53-running-pip-audit)
    - [5.4 Updating](#54-updating)
- [6 mypy](#6-mypy)
    - [6.1 Purpose](#61-purpose)
    - [6.2 Installation](#62-installation)
    - [6.3 Running mypy](#63-running-mypy)
    - [6.4 Updating](#64-updating)
- [7 pytest](#7-pytest)
    - [7.1 Purpose](#71-purpose)
    - [7.2 Installation](#72-installation)
    - [7.3 Running pytest](#73-running-pytest)
    - [7.4 Updating](#74-updating)
- [8 coverage](#8-coverage)
    - [8.1 Purpose](#81-purpose)
    - [8.2 Installation](#82-installation)
    - [8.3 Running coverage](#83-running-coverage)
    - [8.4 Updating](#84-updating)
- [9 typeguard](#9-typeguard)
    - [9.1 Purpose](#91-purpose)
    - [9.2 Installation](#92-installation)
    - [9.3 Running typeguard](#93-running-typeguard)
    - [9.4 Updating](#94-updating)
- [10 xdoctest](#10-xdoctest)
    - [10.1 Purpose](#101-purpose)
    - [10.2 Installation](#102-installation)
    - [10.3 Running xdoctest](#103-running-xdoctest)
    - [10.4 Updating](#104-updating)
- [11 Sphinx](#11-sphinx)
    - [11.1 Purpose](#111-purpose)
    - [11.2 Installation](#112-installation)
    - [11.3 Running Sphinx](#113-running-sphinx)
    - [11.4 Updating](#114-updating)


## 1 Nox

Use Nox to provide reproducible automation by running tasks inside session‑scoped virtual environments.

### Rationale
Nox is required to ensure that all developers and CI systems run tasks in identical, isolated environments, preventing local environment inconsistency issues.

Directives:
- Define sessions in `noxfile.py` at the repository root.
- Use Nox to orchestrate common tasks:
    - `pre-commit`: Run the full pre-commit suite.
    - `mypy`: Perform static type checking.
    - `tests`: Run the test suite with coverage.
    - `coverage`: Report or combine coverage data.
    - `docs-build`: Build Sphinx documentation.
- Install Nox and the Poetry integration using `pip install nox nox-poetry`.
- Execute sessions using `nox -s <session_name>`.


## 2 Pre-commit

Use pre-commit to manage and run lightweight checks before code is committed or pushed.

### Rationale
Pre-commit is required to catch formatting issues, linting errors, and other common mistakes before they reach the repository, maintaining a high standard of code quality.

Directives:
- Configure hooks in `.pre-commit-config.yaml` at the repository root.
- Include essential hooks:
    - `check-added-large-files`
    - `ruff-check` and `ruff-format`
    - `isort`
    - `pip-audit`
- Install pre-commit into the active environment using `pip install pre-commit`.
- Install the git hooks using `pre-commit install`.
- Run against all files manually using `pre-commit run --all-files`.
- Keep hooks updated using `pre-commit autoupdate`.


## 3 Ruff

Use Ruff as a fast Python linter and code formatter.

### Rationale
Ruff is required to enforce rulesets, line length, and formatting consistently while maintaining high performance.

Directives:
- Configure Ruff in `pyproject.toml`.
- Use Ruff to:
    - Enforce line length and docstyle.
    - Support directory-specific configurations (e.g., `tests/.ruff_tests.toml`).
- Install with `pip install ruff`.
- Format files with `ruff format .` and check with `ruff check .`.


## 4 isort

Use isort to sort imports alphabetically and automatically separate them into sections.

### Rationale
Consistent import organization is required to improve readability and avoid merge conflicts.

Directives:
- Configure isort in `pyproject.toml`.
- Install with `pip install isort`.
- Sort imports with `isort .`.
- Check if files are sorted with `isort --check-only .`.


## 5 pip-audit

Use pip-audit to scan Python environments for packages with known vulnerabilities.

### Rationale
Vulnerability scanning is required to ensure that the project and its dependencies remain secure.

Directives:
- Install with `pip install pip-audit`.
- Check the current environment with `pip-audit`.
- Run through pre-commit using `pre-commit run pip-audit --all-files`.


## 6 mypy

Use mypy as a static type checker for Python code.

### Rationale
Static type checking is required to catch type-related errors early and provide comprehensive type analysis.

Directives:
- Configure mypy in `pyproject.toml`.
- Install with `pip install mypy`.
- Run checks with `mypy .`.


## 7 pytest

Use pytest as a feature-rich testing framework.

### Rationale
A robust testing framework is required to ensure that tests are easy to write, discover, and run.

Directives:
- Install with `pip install pytest`.
- Run tests with `pytest`.
- Use CLI flags (e.g., `-v`, `-m`) to customize output and markers.


## 8 coverage

Use coverage to measure and report code coverage.

### Rationale
Coverage measurement is required to identify untested parts of the codebase and maintain a high standard of testing.

Directives:
- Configure coverage in `pyproject.toml`.
- Install with `pip install coverage`.
- Run collection with `coverage run -m pytest`.
- Generate reports with `coverage report` or `coverage html`.


## 9 typeguard

Use typeguard for runtime type checking.

### Rationale
Runtime type checking is recommended to complement static analysis and provide additional guarantees during execution.

Directives:
- Install with `pip install typeguard`.
- Enable runtime checks during tests using `pytest --typeguard-packages=<package_name>`.
- Use the `@typeguard.typechecked` decorator for specific functions or classes.


## 10 xdoctest

Use xdoctest to validate code examples in docstrings.

### Rationale
Doctest validation is required to ensure that documentation examples remain accurate and runnable as the code evolves.

Directives:
- Install with `pip install xdoctest`.
- Run all doctests with `python -m xdoctest <module_name>`.
- Use the `-v` flag for verbose output.


## 11 Sphinx

Use Sphinx as the documentation generator.

### Rationale
Sphinx is required to produce professional, searchable, and well-structured documentation for the project.

Directives:
- Configure in `docs/conf.py`.
- Install Sphinx and extensions using `pip install sphinx sphinx-rtd-theme sphinx-click furo myst-parser`.
- Build HTML documentation using `sphinx-build -b html docs/source docs/build`.
- Use `sphinx-autobuild` for a live-reloading preview.
