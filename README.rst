Anthony's Python Style Guide
============================

Overview
--------
This repository contains a practical, opinionated Python style guide that remixes the official Google Python Style Guide
and augments it with additional guidance for modern Python projects. It is intended to be copy‑pasted or referenced
directly in projects to keep code consistent, readable, and maintainable. The structure is a fork of the
`Google Style Guide`_ and `Hypermodern Python`_ by `Claudio Jolowicz`_.

What this style guide covers
----------------------------
The guide is split into focused documents that can be read independently:

- Syntax — formatting, naming, imports, typing, docstrings, comments, strings, exceptions, comprehensions, decorators, default arguments, and more.
  See: `syntax.md <syntax.md>`_
- Semantics — program structure and behavior guidelines such as mutable global state, function length, nested classes/functions, lexical scoping, and threading.
  See: `semantics.md <semantics.md>`_
- Project Structure — a reusable repository layout for source, tests, docs, examples, tutorials, and configurations.
  See: `project_structure.md <project_structure.md>`_
- Code & File Layout — how to organize modules and files internally (headers, imports, definitions order, etc.).
  See: `code_file_layout.md <code_file_layout.md>`_
- Documentation — Sphinx recommendations and configuration notes for building docs, including autodoc, autosummary, napoleon, intersphinx, and sphinx‑click.
  See: `documentation.md <documentation.md>`_
- Project Tools — guidance for pre‑commit, nox, coverage, editorconfig, CI, and related developer tooling.
  See: `project_tools.md <project_tools.md>`_
- Unit Tests — testing mindset and structure, including pytest conventions and fixtures.
  See: `unit_tests.md <unit_tests.md>`_
- Performance Tests — approaches for measuring and guarding performance characteristics.
  See: `performance_tests.md <performance_tests.md>`_
- Examples — runnable or illustrative examples showing how to apply the style.
  See: `examples.md <examples.md>`_
- Tutorials — step‑by‑step learning paths for adopting the conventions.
  See: `module_tutorials.md <module_tutorials.md>`_ and `package_tutorials.md <package_tutorials.md>`_

Quick start
-----------
- Projects should first review the high‑level expectations in Syntax and Semantics: `syntax.md <syntax.md>`_ and `semantics.md <semantics.md>`_.
- Repositories should be structured following Project Structure: `project_structure.md <project_structure.md>`_.
- Tooling should be configured following Project Tools and Documentation guidance: `project_tools.md <project_tools.md>`_ and `documentation.md <documentation.md>`_.
- Tests should be kept close to the code and mirror the package structure: `unit_tests.md <unit_tests.md>`_.

Design goals
------------
- Consistency over personal preference where it improves readability.
- Pragmatic defaults that work well with modern tooling (type checkers, formatters, linters, Sphinx, nox, pre‑commit).
- Clear separation of concerns: code, tests, docs, and examples.
- Incremental adoption: each document is self‑contained so teams can onboard gradually.

How to use this guide in a project
----------------------------------
- The repository or individual files can be copied into a project's documentation (for example, under ``docs/style/``) and linked from the project README.
- The repository layout from Project Structure can be adopted to enable tooling to auto‑discover configurations.
- Formatting and linting can be enforced via pre‑commit hooks as described in Project Tools.
- The guide should be versioned alongside the source so changes are reviewed like code.

Contributing and deviations
---------------------------
- If deviation is necessary, document the exception in code comments or in a project‑local style note that links back to the relevant section here.
- Proposals for clarifications or updates should reference the section being changed and provide brief rationale.

Related resources
-----------------
- Google Python Style Guide: https://google.github.io/styleguide/pyguide.html
- Hypermodern Python: https://cjolowicz.github.io/posts/hypermodern-python-01-setup/
- PEP 8: https://peps.python.org/pep-0008/
- Sphinx: https://www.sphinx-doc.org/

Repository map
--------------
The top‑level files in this repository:

- ``syntax.md`` — syntactic guidance.
- ``semantics.md`` — semantic guidance.
- ``project_structure.md`` — repository layout.
- ``code_file_layout.md`` — file and module organization details.
- ``documentation.md`` — Sphinx and docs practices.
- ``project_tools.md`` — tooling configuration and usage.
- ``unit_tests.md`` — unit testing guidance.
- ``performance_tests.md`` — performance testing notes.
- ``examples.md`` — examples overview.
- ``module_tutorials.md`` / ``package_tutorials.md`` — tutorial material.

License
-------
Unless otherwise noted in individual files, content in this repository is provided under the same license as the parent
project. If these documents are copied into a project, license them according to the project’s policies.

Credits
-------

The project is based on `@cjolowicz`_'s `Hypermodern Python Cookiecutter`_.

.. _Google Style Guide: https://google.github.io/styleguide/pyguide.html
.. _Hypermodern Python: https://cjolowicz.github.io/posts/hypermodern-python-01-setup/
.. _Claudio Jolowicz: https://github.com/cjolowicz
.. _@cjolowicz: https://github.com/cjolowicz
.. _Hypermodern Python Cookiecutter: https://github.com/cjolowicz/cookiecutter-hypermodern-python
