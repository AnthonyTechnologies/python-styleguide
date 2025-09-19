# Anthony's Python Style Guide: Project Structure

## Table of Contents

- [1 Background](#1-background)
- [2 Project Directory Structure](#2-project-directory-structure)
  - [2.1 Overview](#21-overview)
  - [2.2 Source Code Directory](#22-source-code-directory)
  - [2.3 Tests Directory](#23-tests-directory)
  - [2.4 Examples Directory](#24-examples-directory)
  - [2.5 Documentation Directory](#25-documentation-directory)
  - [2.6 Tutorials Directory](#26-tutorials-directory)
- [3 Configuration Files](#3-configuration-files)
  - [3.1 Project Configuration](#31-project-configuration)
  - [3.2 Development Tools](#32-development-tools)
- [4 Implementation Guidelines](#4-implementation-guidelines)
  - [4.1 Applying This Structure Generically](#41-applying-this-structure-generically)
  - [4.2 Best Practices](#42-best-practices)


## 1 Background

This document outlines the recommended project structure for Python projects. A well-organized project structure
enhances code readability, maintainability, and collaboration. Following these guidelines ensures consistency across 
projects and makes it easier for developers to navigate and understand the codebase.

## 2 Project Directory Structure

### 2.1 Overview

A well-structured Python project typically includes the following top-level directories:

```
project_root/
├── src/                  # Source code
├── tests/                # Test files
├── examples/             # Example usage
├── docs/                 # Documentation
├── tutorials/            # Detailed tutorials
├── LICENSE.rst           # License information
├── README.rst            # Project overview
├── CONTRIBUTING.rst      # Contribution guidelines
├── pyproject.toml        # Project configuration
└── poetry.lock           # Dependency lock file
```

### 2.2 Source Code Directory (`src/`)

The `src/` directory contains the actual implementation of your package. Using a `src/` layout (as opposed to placing modules directly in the project root) provides several benefits:

- Ensures your package is installed in development mode exactly as it would be when installed from PyPI
- Prevents accidental imports from the project root
- Makes namespace packages easier to work with

Within the `src/` directory, organize your code into logical modules:

```
src/
└── your_package/
    ├── module1/
    ├── module2/
    ├── module3/
    └── __init__.py
```

Each module should focus on a specific functionality domain. For example, in the `baseobjects` package:

- `bases/`: Low-level base classes
- `collections/`: Objects for storing other objects
- `functions/`: Objects for creating function and method objects
- `operations/`: Functions for specific operations

### 2.3 Tests Directory (`tests/`)

The `tests/` directory should mirror the structure of your `src/` directory, making it easy to locate tests for specific modules:

```
tests/
├── module1/
├── module2/
├── module3/
└── __init__.py
```

For performance-critical code, consider adding a `performance/` subdirectory within each module's test directory to separate performance tests from functional tests:

```
tests/
└── module1/
    ├── performance/
    └── functional_test.py
```

### 2.4 Examples Directory (`examples/`)

The `examples/` directory should also mirror your package structure, providing usage examples for each module:

```
examples/
├── module1/
├── module2/
├── module3/
└── __init__.py
```

Each example should be a standalone script that demonstrates how to use a specific feature or component of your package.

### 2.5 Documentation Directory (`docs/`)

The `docs/` directory contains all project documentation:

```
docs/
├── api/                  # API documentation
├── guides/               # User guides
├── notes/                # Development notes
└── python-styleguide/    # Style guidelines
```

Documentation should be written in a format that can be processed by documentation generators like Sphinx.

### 2.6 Tutorials Directory (`tutorials/`)

For more complex packages, a separate `tutorials/` directory can provide in-depth, step-by-step guides:

```
tutorials/
├── getting_started/
├── advanced_usage/
└── specific_features/
```

## 3 Configuration Files

### 3.1 Project Configuration

- `pyproject.toml`: Modern Python project configuration using PEP 518 standard
- `poetry.lock`: Dependency lock file when using Poetry for dependency management
- `setup.py` or `setup.cfg`: Traditional project configuration (if not using pyproject.toml)

### 3.2 Development Tools

- `.pre-commit-config.yaml`: Configuration for pre-commit hooks
- `noxfile.py`: Configuration for automated testing with nox
- `conftest.py`: Shared pytest fixtures
- `codecov.yml`: Configuration for code coverage reporting

## 4 Implementation Guidelines

### 4.1 Applying This Structure Generically

This structure can be applied to any Python project by following these steps:

1. **Start with the basic directory structure**:
   - Create `src/`, `tests/`, `docs/`, and `examples/` directories
   - Add appropriate configuration files

2. **Identify logical modules**:
   - Break your code into logical, focused modules
   - Create a directory for each module under `src/your_package/`

3. **Mirror the structure**:
   - Create matching directories in `tests/` and `examples/` for each module
   - Ensure tests and examples are organized to match your source code

4. **Document everything**:
   - Create comprehensive documentation in the `docs/` directory
   - Include a detailed README with installation and basic usage instructions

### 4.2 Best Practices

1. **Keep modules focused**: Each module should have a clear, specific purpose.

2. **Maintain parallel structure**: Tests and examples should mirror your source code structure.

3. **Use descriptive names**: Directory and file names should clearly indicate their purpose.

4. **Separate implementation from interface**: Consider using private modules (prefixed with `_`) for implementation details.

5. **Include type hints**: Use `py.typed` file to indicate your package supports type checking.

6. **Document public APIs**: Every public class, function, and method should have docstrings.

7. **Provide examples**: Include example usage for all major features.

8. **Test thoroughly**: Include unit tests, integration tests, and where appropriate, performance tests.

By following these guidelines, you'll create a Python project that is easy to navigate, maintain, and contribute to.