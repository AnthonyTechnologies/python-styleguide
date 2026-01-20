# Anthony's Python Style Guide: Project Tooling

This document describes the core development tools that may be used across projects and how they fit into day‑to‑day
workflows. Of these tools, two tools are central for managing the other tools:

- nox — automates repeatable development tasks in isolated virtual environments (tests, type checks, docs, etc.).
- pre-commit — automates formatting and quick static checks on each commit/push.

Configurations for all these tools are not explicitly listed here to allow for flexibility in specification designation.
Configurations should be contained in their respective projects. However, examples of the configuration files can be
found in the Python Package Project Template repository https://github.com/AnthonyTechnologies/python-packagetemplate.

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

Nox provides reproducible automation by running tasks inside session‑scoped virtual environments defined in noxfile.py.

Configuration: noxfile.py (repository root)

### 1.1 Purpose

Nox orchestrates common dev tasks, including:

- pre-commit — runs the full pre-commit suite in a controlled virtualenv and patches installed git hooks to use it.
- mypy — static type checking with strict settings.
- tests — runs test suite with coverage collection enabled by default.
- coverage — reports or combines coverage data.
- typeguard — runtime type checking during tests for additional guarantees.
- xdoctest — validates examples embedded in docstrings and modules.
- docs-build — builds Sphinx documentation.
- docs — live‑reloading Sphinx docs during development.

The default sessions list is set in noxfile.py (nox.options.sessions).

### 1.2 Installation

- Install Nox and its Poetry integration:
  - pip install nox nox-poetry

### 1.3 Common Sessions

From noxfile.py, notable sessions include:

- nox -s pre-commit — run pre-commit hooks in a managed env.
- nox -s mypy — run static type checks.
- nox -s tests — run unit tests.
- nox -s coverage -- report — show coverage report; combine if multiple files exist.
- nox -s typeguard — run tests with runtime type checking enabled.
- nox -s xdoctest — run doctests/examples.
- nox -s docs-build — build docs into docs/_build.
- nox -s docs — serve docs with live rebuilds.

### 1.4 Running Sessions

- List available sessions:
  - nox -l
- Run one session (example: tests):
  - nox -s tests
- Pass through extra arguments to tools (example: pytest options):
  - nox -s tests -- -k "pattern" -q


## 2 Pre-commit

pre-commit manages and runs lightweight checks before code is committed or pushed. It helps keep the repository clean
and consistent by catching issues early.

Configuration: .pre-commit-config.yaml (repository root)

### 2.1 Purpose

Current hooks configured in .pre-commit-config.yaml include:

- check-added-large-files — blocks accidentally committing very large files.
- check-toml — validates TOML files (e.g., pyproject.toml).
- check-yaml — validates YAML files (e.g., CI workflows).
- ruff-check — fast linter for Python with an extensive rule set.
- ruff-format — opinionated Python code formatter via Ruff.
- isort — sorts and groups imports consistently.
- end-of-file-fixer — ensures a single trailing newline.
- trailing-whitespace-fixer — removes stray trailing whitespace.
- pip-audit — scans Python environments for known vulnerabilities.

Note: Some hooks are provided through the "local" repo and run using system installs. Their behavior is governed by
per‑tool settings in pyproject.toml where applicable (e.g., [tool.ruff], [tool.isort]).

### 2.2 Installation

- Ensure Python and pip are available in the environment.
- Install pre-commit into the active environment:
  - pip install pre-commit
- Install the git hooks into the repository:
  - pre-commit install --install-hooks

### 2.3 Running Hooks

- Automatically runs on git commit and, for some hooks, on push.
- Run against all files manually:
  - pre-commit run --all-files
- Run a specific hook:
  - pre-commit run ruff-check --all-files

### 2.4 Updating Hooks

- Update hook revisions to the latest recommended versions:
  - pre-commit autoupdate


## 3 Ruff

Ruff is a fast Python linter and code formatter written in Rust.

Configuration: [tool.ruff], [tool.ruff.lint], [tool.ruff.format] in pyproject.toml

### 3.1 Purpose

- Enforces rulesets, line length, docstyle, and formatting
- Supports directory-specific configurations:
    - examples/.ruff_examples.toml — relaxed rules for narrative/demo code
    - tests/.ruff_tests.toml — adapted rules for testing patterns
    - tutorials/.ruff_tutorials.toml — optimized for learner readability
- Local configs extend/override root settings for their directory tree

### 3.2 Installation

- Install Ruff:
    - pip install ruff

### 3.3 Running Ruff

- Format files:
    - ruff format .
- Check files:
    - ruff check .

### 3.4 Updating

- Update to latest version:
    - pip install --upgrade ruff


## 4 isort

isort is a Python utility to sort imports alphabetically and automatically separate them into sections.

Configuration: [tool.isort] in pyproject.toml

### 4.1 Purpose

- Controls import grouping
- Sets line length limits
- Configures import section headings
- Maintains consistent import ordering

### 4.2 Installation

- Install isort:
    - pip install isort

### 4.3 Running isort

- Sort imports in a file:
    - isort file.py
- Check if files are sorted:
    - isort --check-only file.py
- Show diff without changes:
    - isort --diff file.py

### 4.4 Updating

- Update to latest version:
    - pip install --upgrade isort


## 5 pip-audit

pip-audit is a tool for scanning Python environments for packages with known vulnerabilities.

Configuration: .pre-commit-config.yaml

### 5.1 Purpose

- Scans dependencies for vulnerabilities
- Checks against PyPI JSON API and OSV
- Integration with pre-commit
- Provides detailed security reports

### 5.2 Installation

- Install pip-audit:
    - pip install pip-audit

### 5.3 Running pip-audit

- Check current environment:
    - pip-audit
- Run via pre-commit:
    - pre-commit run pip-audit --all-files

### 5.4 Updating

- Update to latest version:
    - pip install --upgrade pip-audit


## 6 mypy

mypy is a static type checker for Python code.

Configuration: [tool.mypy] in pyproject.toml

### 6.1 Purpose

- Performs static type checking
- Enforces strict validation settings
- Provides verbose error reporting
- Conducts comprehensive type analysis

### 6.2 Installation

- Install mypy:
    - pip install mypy

### 6.3 Running mypy

- Check types in a file:
    - mypy file.py
- Check with specific config:
    - mypy --config-file mypy.ini file.py
- Show error codes:
    - mypy --show-error-codes file.py

### 6.4 Updating

- Update to latest version:
    - pip install --upgrade mypy


## 7 pytest

pytest is a feature-rich testing framework for Python.

Configuration: Via nox sessions and CLI flags

### 7.1 Purpose

- Discovers and runs test cases
- Provides rich assertion introspection
- Supports test fixtures and parameterization
- Integrates with coverage reporting
- Primary configuration through nox
- Customizable via standard CLI flags in sessions

### 7.2 Installation

- Install pytest:
    - pip install pytest

### 7.3 Running pytest

- Run all tests:
    - pytest
- Run specific test file:
    - pytest tests/test_file.py
- Run with verbose output:
    - pytest -v
- Run with specific marker:
    - pytest -m marker_name

### 7.4 Updating

- Update to latest version:
    - pip install --upgrade pytest


## 8 coverage

coverage provides code coverage measurement and reporting for Python projects.

Configuration: [tool.coverage.*] in pyproject.toml

### 8.1 Purpose

- Measures code execution during tests
- Generates detailed coverage reports
- Enforces minimum coverage thresholds
- Supports branch coverage analysis
- Configurable paths and patterns
- Report thresholds (fail_under=100)

### 8.2 Installation

- Install coverage:
    - pip install coverage

### 8.3 Running coverage

- Run coverage collection:
    - coverage run -m pytest
- Generate report:
    - coverage report
- Generate HTML report:
    - coverage html
- Show missing lines:
    - coverage report --show-missing

### 8.4 Updating

- Update to latest version:
    - pip install --upgrade coverage


## 9 typeguard

typeguard provides runtime type checking for Python.

Configuration: Via nox session

### 9.1 Purpose

- Performs runtime type checking
- Validates type hints during execution
- Complements static type checking
- Enabled through dedicated nox session
- Reports type violations during tests

### 9.2 Installation

- Install typeguard:
    - pip install typeguard

### 9.3 Running typeguard

- Run with pytest:
    - pytest --typeguard-packages=package_name
- Enable for specific module:
    - python -m typeguard module_name
- Use as a decorator:
    - @typeguard.typechecked

### 9.4 Updating

- Update to latest version:
    - pip install --upgrade typeguard


## 10 xdoctest

xdoctest is an improved doctest implementation.

Configuration: Via nox sessions

### 10.1 Purpose

- Validates code examples in docstrings
- Provides better error messages than standard doctest
- Supports native Python syntax
- Invoked through dedicated nox sessions
- Uses default settings unless overridden
- Accepts custom flags when needed

### 10.2 Installation

- Install xdoctest:
    - pip install xdoctest

### 10.3 Running xdoctest

- Run all doctests:
    - python -m xdoctest module_name
- Run specific test:
    - python -m xdoctest module_name function_name
- Run with verbose output:
    - python -m xdoctest module_name -v

### 10.4 Updating

- Update to latest version:
    - pip install --upgrade xdoctest


## 11 Sphinx

Sphinx is a documentation generator for Python projects.

Configuration: docs/conf.py and nox session arguments

### 11.1 Purpose

- Generates project documentation
- Builds multiple output formats
- Supports extensive extensions
- Includes features like:
    - sphinx-click
    - sphinx-rtd-theme
    - furo
    - myst-parser
    - Core sphinx features

### 11.2 Installation

- Install Sphinx and extensions:
    - pip install sphinx sphinx-rtd-theme sphinx-click furo myst-parser

### 11.3 Running Sphinx

- Build HTML documentation:
    - sphinx-build -b html docs/source docs/build
- Run live server:
    - sphinx-autobuild docs/source docs/build
- Check documentation:
    - sphinx-build -b linkcheck docs/source docs/build

### 11.4 Updating

- Update to latest version:
    - pip install --upgrade sphinx
