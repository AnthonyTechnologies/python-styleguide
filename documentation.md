# Anthony's Python Style Guide: Documentation

Use Sphinx to build documentation from reStructuredText source files and Python docstrings.

### Rationale
Sphinx is required to provide a robust and extensible documentation system that integrates with Python code and supports multiple output formats.

Directives:
- Generate API reference pages from code using `autodoc` and `autosummary`.
- Parse Google and NumPy-style docstrings with `Napoleon`.
- Provide deep links back to source code using `viewcode`.
- Link to external projects, such as the Python standard library, with `intersphinx`.
- Include and track TODOs during development using the `todo` extension.
- Use `sphinx-click` for Click-based command-line interface documentation.

## Table of Contents

- [1 Project Layout and Entry Points](#1-project-layout-and-entry-points)
- [2 Sphinx Configuration](#2-sphinx-configuration)
    - [2.1 Enabled Extensions and Rationale](#21-enabled-extensions-and-rationale)
    - [2.2 HTML Theme](#22-html-theme)
    - [2.3 Intersphinx](#23-intersphinx)
    - [2.4 Type Hints and Docstring Styles](#24-type-hints-and-docstring-styles)
    - [2.5 Todos](#25-todos)
    - [2.6 Read the Docs Build Configuration](#26-read-the-docs-build-configuration)
- [3 Building the Docs](#3-building-the-docs)
    - [3.1 One-Off Build](#31-one-off-build)
    - [3.2 Live Rebuilds During Authoring](#32-live-rebuilds-during-authoring)
    - [3.3 Cleaning Builds](#33-cleaning-builds)
- [4 Authoring Guidelines](#4-authoring-guidelines)
    - [4.1 reStructuredText vs. Markdown](#41-restructuredtext-vs-markdown)
    - [4.2 API Docs via Autodoc + Autosummary](#42-api-docs-via-autodoc--autosummary)
    - [4.3 Click CLIs](#43-click-clis)
    - [4.4 Cross-Referencing and Intersphinx](#44-cross-referencing-and-intersphinx)
    - [4.5 Source Links and Readability](#45-source-links-and-readability)
    - [4.6 Writing Style](#46-writing-style)
        - [4.6.1 Third-Person Descriptive Voice](#461-third-person-descriptive-voice)
        - [4.6.2 Third-Person Imperative Voice](#462-third-person-imperative-voice)
- [5 Where Things Are Configured](#5-where-things-are-configured)
- [6 Style Guide](#6-style-guide)
    - [6.1 Git Submodule](#61-git-submodule)
    - [6.2 Keep It Up to Date](#62-keep-it-up-to-date)
    - [6.3 Render or Link It in Sphinx](#63-render-or-link-it-in-sphinx)
- [7 Troubleshooting](#7-troubleshooting)


## 1 Project Layout and Entry Points

- Documentation root: docs/
  - Sphinx configuration: docs/conf.py
  - Primary index: docs/index.rst
  - Build output: docs/_build/
- Top-level README used on the repository home page: README.rst

Build and serve docs through Nox sessions defined in noxfile.py.


## 2 Sphinx Configuration

See docs/conf.py for the authoritative configuration. Important highlights:

```python # pseudocode
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx_click",
]

html_theme = "sphinx_rtd_theme"
```

### 2.1 Enabled Extensions

Directives:
- Use `sphinx.ext.autodoc` to import modules and pull in docstrings for API pages.
- Use `sphinx.ext.autosummary` to auto-generate summary tables and stub pages.
- Use `sphinx.ext.napoleon` to support Google and NumPy docstring styles.
- Use `sphinx.ext.viewcode` to add "View Source" links for documented objects.
- Use `sphinx.ext.intersphinx` to cross-link to external documentation.
- Use `sphinx.ext.todo` to allow the inclusion of todo directives.
- Use `sphinx_click` to render documentation for Click-based CLIs.

### 2.2 HTML Theme

Use `sphinx_rtd_theme` as the default theme.

### Rationale
The Read the Docs theme is required to provide a consistent and accessible interface for documentation.

### 2.3 Intersphinx

- Configured mapping:
  - python ? https://docs.python.org/3
- Add additional mappings in conf.py if cross-referencing external libraries becomes useful.

### 2.4 Type Hints and Docstring Styles

Directives:
- Set `autodoc_typehints = "description"` to show type hints in the parameter and returns sections.
- Prefer the Google docstring style for all new content.

### 2.5 Todos

- .. todo:: directives are included in builds (todo_include_todos = True). Use sparingly and convert todos into issues as work is planned.

### 2.6 Read the Docs Build Configuration

Configure RTD builds via a YAML file located at docs/.readthedocs.yaml. Typical key settings:

- version: 2 ï¿½ RTDï¿½s v2 configuration schema.
- build:
  - os: ubuntu-20.04 ï¿½ Linux image used for builds.
  - tools.python: "3.12" ï¿½ Python version used on RTD.
- sphinx:
  - configuration: docs/conf.py ï¿½ RTD invokes Sphinx with this config file.
- formats: all ï¿½ Build all supported formats (HTML, PDF via LaTeX, and EPUB).
- python.install:
  - requirements: docs/requirements.txt ï¿½ Additional doc-specific dependencies are installed from this pinned file.
  - path: . ï¿½ Installs the project itself into the RTD environment so autodoc can import modules.

Notes and recommendations:
- Keep docs/requirements.txt aligned with extensions and themes configured in docs/conf.py (e.g., sphinx, sphinx-rtd-theme, sphinx-click; optional furo, myst-parser). Pin versions to ensure reproducible RTD builds.
- Local builds via nox -s docs-build / nox -s docs do not use .readthedocs.yaml; they rely on noxfile.pyï¿½s session dependencies. When changing Sphinx extensions or themes, update both the nox sessions and docs/requirements.txt to keep parity with RTD.
- If the location of conf.py or the Python version changes, reflect those changes in docs/.readthedocs.yaml to avoid RTD build failures.


## 3 Building the Docs

Execute all commands via Nox to ensure reproducibility.

### Rationale
Using Nox is required to provide a consistent and isolated environment for documentation builds.

### 3.1 One-Off Build

Directives:
- Build static HTML into `docs/_build` using `nox -s docs-build`.
- Pass extra options after the session name if necessary (e.g., `nox -s docs-build -- -W`).

### 3.2 Live Rebuilds During Authoring

Directives:
- Serve documentation with live reload using `nox -s docs`.
- Disable the default browser opening behavior by removing `--open-browser` in `noxfile.py` if preferred.

### 3.3 Cleaning Builds

- The `docs-build` and `docs` sessions remove `docs/_build` before each run. Delete any cached auto-generated API stubs locally if a fully clean environment is needed.


## 4 Authoring Guidelines

### 4.1 reStructuredText vs. Markdown

Use reStructuredText (.rst) as the canonical format for documentation.

### Rationale
ReST is the native format for Sphinx and provides the most comprehensive support for advanced directives and cross-referencing.

### 4.2 API Docs via Autodoc + Autosummary

- Keep public APIs well-documented with complete docstrings. autosummary_generate is enabled, which can generate index pages and per-object stubs when autosummary tables are included in .rst files.
- Provide clear type hints; they will be rendered in the description sections.
- For module organization and public/private boundaries, follow the guidance in semantics.md and project_structure.md. Only public objects should be included in user-facing API pages.

### 4.3 Click CLIs

- For Click-based CLIs, document commands using sphinx-click directives.
- Example usage in a .rst file:

  .. code-block:: rst

     Command-line Interface
     ----------------------

     .. click:: package.module:cli
        :prog: tool-name
        :show-nested:

- Replace the token `package.module:cli` with the import path and callable for the project's Click entry point.

### 4.4 Cross-Referencing and Intersphinx

- Use Sphinx cross-reference roles to link to symbols:
  - :py:mod:`package.module`, :py:class:`package.Class`, :py:meth:`package.Class.method`.
- For Python stdlib references, intersphinx provides automatic links, e.g., :class:`dict`, :mod:`asyncio`.

### 4.5 Source Links and Readability

- viewcode adds "View Source" links to documented objects. Ensure source files remain readable and follow the code style guide so rendered source is approachable.

### 4.6 Writing Style

Follow the [Writing Voice](guide_voice.md) guidelines for all documentation.

### Rationale
A consistent writing voice is required to maintain the "Standard-Setter" persona and ensure that all documentation is professional, objective, and actionable.

Directives:
- Use the direct imperative mood for rules and requirements.
- Use the third-person descriptive voice for explaining systems and features.
- Avoid all pronouns to maintain neutrality.
- Integrate RFC 2119 keywords naturally into sentences using lowercase.


## 5 Where Things Are Configured

- docs/conf.py - Sphinx configuration (extensions, theme, intersphinx, napoleon, todo, autodoc/autosummary options).
- docs/.readthedocs.yaml - Read the Docs build configuration (Python version, OS image, Sphinx entry point, output formats, and install steps).
- noxfile.py - Sessions for building and serving the docs; installs Sphinx and selected extensions.
- pyproject.toml - Project metadata and tooling configs that indirectly affect example code in docs.


## 6 Style Guide

Include this style guide as a Git submodule in `docs/python-styleguide`.

### Rationale
Using a Git submodule is recommended to keep the style guide close to the project documentation, allowing for version pinning and easier updates.

### 6.1 Git Submodule

Run these commands from the repository root (replace the remote URL if the fork or hosting differs):

```bash
# Add the style guide as a submodule under docs/python-styleguide
git submodule add -b main https://github.com/example-org/python-styleguide.git docs/python-styleguide

# Commit the .gitmodules entry and submodule pointer
git commit -m "docs: add python-styleguide as submodule"

# If cloning a repo that already has the submodule, initialize it with:
git submodule update --init --recursive
```

Notes:
- Pin submodules to a specific commit; they do not auto-track the remote branch. This is desirable for reproducible docs builds.
- If submodules are not preferred, git subtree is an alternative; however, submodules are simpler to keep read-only and clearly versioned.

### 6.2 Keep It Up to Date

To pull the latest from the style guide:

```bash
# Option A: update from the superproject, keeping the pointer fast-forwarded
git submodule update --remote --merge docs/python-styleguide

# Option B: cd into the submodule and pull explicitly
cd docs/python-styleguide
git fetch origin
git checkout main
git pull --ff-only
cd -

# Commit the updated submodule pointer in the superproject
git commit -am "docs: bump python-styleguide submodule"
```

CI/hosting considerations:
- Read the Docs: ensure submodules are fetched. In docs/.readthedocs.yaml add:

  ```yaml
  submodules:
    include:
      - docs/python-styleguide
  ```

- Other CI: ensure the checkout step initializes submodules, e.g., git submodule update --init --recursive.

### 6.3 Render or Link It in Sphinx

This repository largely uses Markdown (.md) files. To render them inside the project's Sphinx documentation:

1) Enable MyST-Parser in docs/conf.py:

```python # pseudocode
extensions = [
    # existing extensions...
    "myst_parser",
]
```

Ensure myst-parser is installed in the documentation environment (nox session and/or docs/requirements.txt).

2) Include the files in a toctree, for example in docs/index.rst:

.. code-block:: rst

   .. toctree::
      :maxdepth: 2
      :caption: Python Style Guide

      python-styleguide/README.md
      python-styleguide/documentation.md
      python-styleguide/syntax/formatting.md
      python-styleguide/syntax/naming.md
      python-styleguide/syntax/typing.md
      python-styleguide/syntax/docstrings.md
      python-styleguide/syntax/comments.md
      python-styleguide/syntax/strings.md
      python-styleguide/syntax/exceptions_error_messages.md
      python-styleguide/syntax/logging.md
      python-styleguide/syntax/resources.md
      python-styleguide/semantics.md
      python-styleguide/project_structure.md
      python-styleguide/code_file_layout.md
      python-styleguide/tutorials/module_tutorials.md
      python-styleguide/tutorials/package_tutorials.md
      python-styleguide/tests/unit_tests.md
      python-styleguide/tests/performance_tests.md
      python-styleguide/project_tools.md
      python-styleguide/examples.md

If enabling Markdown rendering is not desired, it is still possible to:
- Link to the files as plain hyperlinks (they will render on Git hosting platforms but not as Sphinx pages), or
- Include only README.rst (since it is already in ReST) and link out to the rest of the repository.


## 7 Troubleshooting

- Import errors during autodoc
  - Sphinx imports modules to extract docstrings. The configuration ensures src/ is on sys.path. If import errors occur, confirm the module is installable or visible under src/ and that any optional dependencies are available.
- Missing API pages
  - autosummary only generates pages for entries included in autosummary tables. Ensure .rst files include the relevant modules/objects, or generate stubs ahead of time if needed.
- Theme issues or missing styles
  - Confirm sphinx_rtd_theme is installed in the session environment. The nox sessions install it automatically.
- Markdown not rendering
  - MyST is not enabled by default. Use .rst or enable myst-parser in conf.py if Markdown support is required.

