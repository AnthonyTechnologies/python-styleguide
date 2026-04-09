# Anthony's Python Style Guide: Package Tutorials

Use tutorials to provide step-by-step guidance on package usage, demonstrating core concepts and practical use cases.

### Rationale
High-quality package tutorials are required to educate users on library features and facilitate rapid adoption of project components.

Directives:
- Focus package tutorials on entire packages or subpackages.
- Use Jupyter Notebooks (.ipynb) for an interactive learning experience.
- Follow general style guidelines (naming, layout, docstrings) within all code cells.

## Table of Contents

- [1 Jupyter Notebook](#1-jupyter-notebook)
- [2 Directory Hierarchy](#2-directory-hierarchy)
- [3 Package Tutorial Notebook Structure](#3-package-tutorial-notebook-structure)
    - [3.1 Title and Introduction](#31-title-and-introduction)
    - [3.2 Installation](#32-installation)
    - [3.3 Importing the Package](#33-importing-the-package)
    - [3.4 Core Concepts & Basic Usage](#34-core-concepts--basic-usage)
    - [3.5 Advanced Features](#35-advanced-features)
    - [3.6 Examples](#36-examples)
    - [3.7 API Highlights](#37-api-highlights)
    - [3.8 Troubleshooting / FAQs](#38-troubleshooting--faqs)
    - [3.9 Conclusion and Next Steps](#39-conclusion-and-next-steps)
- [4 Content Guidelines](#4-content-guidelines)
    - [4.1 Define the Audience and Scope](#41-define-the-audience-and-scope)
    - [4.2 Language](#42-language)
    - [4.3 Logical Flow](#43-logical-flow)
    - [4.4 Markdown Cells](#44-markdown-cells)
    - [4.5 Code Cells](#45-code-cells)
    - [4.6 Self-Contained Examples](#46-self-contained-examples)
    - [4.7 Error Handling Examples](#47-error-handling-examples)
- [5 Formatting and Style](#5-formatting-and-style)
    - [5.1 Headings](#51-headings)
    - [5.2 Code Blocks](#52-code-blocks)
    - [5.3 Emphasis](#53-emphasis)
    - [5.4 Lists](#54-lists)
    - [5.5 Links](#55-links)
- [6 Tips for Effectiveness](#6-tips-for-effectiveness)


## 1 Jupyter Notebook

Use Jupyter Notebooks to create interactive and educational tutorials that combine text, code, and visualizations.

### Rationale
Jupyter Notebooks are recommended for tutorials because they allow users to execute code in real-time, promoting active learning and experimentation.

Directives:
- Specify the required kernel.
- Explain any magic commands used in the notebook.


## 2 Directory Hierarchy

Organize tutorials within a directory structure that mirrors the package structure.

### Rationale
A mirrored directory structure is required to make tutorials easily discoverable based on the package they cover.

Directives:
- Create a directory for each major package under the `tutorials/` directory.
- Use subdirectories for subpackages.
- Name files with a `_package_tutorial.ipynb` suffix.
- Use `snake_case` for all filenames.

Example:
```
tutorials/
+-- bases/                          # Tutorials for the bases package
�   +-- collections/                # Tutorials for the bases.collections subpackage
�   �   +-- collections_package_tutorial.py
�   +-- bases_package_tutorial.py
+-- cachingtools/                   # Tutorials for the cachingtools package
�   +-- cachingtools_package_tutorial.py
+-- baseobjects_package_tutorial.py
```


## 3 Package Tutorial Notebook Structure

Establish a clear and logical flow for all package tutorial notebooks.

### Rationale
A standardized structure is required to ensure that tutorials are easy to navigate and consistent across the project.

Directives:
- Include these sections in order:
    1. Title and Introduction
    2. Installation
    3. Importing the Package
    4. Core Concepts & Basic Usage
    5. Advanced Features
    6. Examples
    7. API Highlights
    8. Troubleshooting / FAQs
    9. Conclusion and Next Steps

### 3.1 Title and Introduction

Use the Title and Introduction section to set the stage for the package's tutorial. Provide users with a clear understanding of what they will learn and how this package fits into the larger package ecosystem. Ensure this section serves as an engaging entry point while remaining informative and concise.

- Formatting: Markdown Cell
- Clear Title: "Using [PackageName]", "[PackageName] for [Specific Task]", etc.
- Brief Overview:
    - Explain the package's primary responsibilities and features.
    - Explain how this package relates to the parent package.
    - Explain what will be covered in this tutorial.
    - Briefly summarize the prerequisites.
- Table of Contents (Optional but Recommended): Markdown links to major sections within this package tutorial.

### 3.2 Installation

Use the Installation section to provide clear instructions for setting up the package. Ensure this section is straightforward and covers both standard and alternative installation methods, allowing users to successfully install the package regardless of their setup.

- Formatting: Markdown and Code Cells
- Instructions: Clear, step-by-step installation instructions using pip or conda.
    ```python # pseudocode
    # !pip install example-package-name
    # or
    # !conda install -c example-channel example-package-name
    ```
- Dependencies: Mention any critical dependencies if they are not automatically handled.
- Verification (Optional):** A small code snippet to verify successful installation.

If the package tutorial is a subpackage, an Installation section is not required.

### 3.3 Importing the Package

Use the Importing the Package section to demonstrate how to import and access package functionality. Clearly show standard import patterns and useful alternatives. Explain any naming conventions or common aliases.

- Formatting: Markdown and Code Cells
- Show the standard way to import the package or its key subpackages.

Example:
```python # pseudocode
import package_name
# or
from package_name import specific_package
# or
import package_name as alias
```

### 3.4 Core Concepts & Basic Usage

Use the Core Concepts & Basic Usage section to introduce the fundamental building blocks and primary functionality of the package. Ensure this section forms the foundation of the tutorial, helping users understand essential concepts before moving to advanced features. Demonstrate basic operations and typical usage patterns.

- Formatting: Markdown and Code Cells
- Introduce the fundamental concepts and objects of the package.
- Provide simple, executable examples for the most common use cases.
- Explain the basic operations and typical usage patterns.
- Give a brief overview of the key modules in the package and direct users to view the module tutorials rather than
  going into detail.
- Explain each code cell:
    - What the code does.
    - Why it's done that way.
    - The expected output (and show it, by running the cell).

### 3.5 Advanced Features

Use the Advanced Features section to introduce more advanced features of the package. Provide users with a deeper understanding of capabilities and functionality so they can make informed decisions when using the package.

- Formatting: Markdown and Code Cells
- Introduce more complex functionalities, options, or configurations.
- Break down complex examples into smaller, understandable steps.
- Clearly explain the parameters and their impact.

### 3.6 Examples

Use the Examples section to demonstrate how to solve real-world problems with the package. Provide concrete examples to help users understand applicability and value. Use small, relatable datasets or scenarios when possible.

- Formatting: Markdown and Code Cells
- Showcase how the package can be used to solve real-world problems.
- This section helps users understand the package's value and applicability.
- If possible, use a small, relatable dataset or scenario.

### 3.7 API Highlights

Use the API Highlights section to provide a quick overview of the package's API. Provide a quick reference for users to access package functionality and make informed decisions.

- Formatting: Markdown Cell
- Briefly mention key functions/classes and their purpose.
- Provide a link to the full API documentation. Avoid replicating the entire API reference here.

### 3.8 Troubleshooting / FAQs

Use this section to provide solutions to common issues users might encounter. Offer workarounds and best practices to help users make informed decisions.

- Formatting: Markdown Cell
- Address common issues users might encounter.
- Provide solutions or workarounds.
- Link to issue trackers or support forums.

### 3.9 Conclusion and Next Steps

Use the Conclusion and Next Steps section to wrap up the tutorial and provide guidance for further learning. Help users solidify their understanding and show paths for continued exploration.

- Formatting: Markdown Cell
- Summarize what was covered.
- Encourage further exploration.
- Suggest next steps:
    - Trying other features.
    - Reading more advanced tutorials.
    - Consulting the full documentation.
    - Contributing to the package.

## 4 Content Guidelines

Ensure the contents of a tutorial are accessible, practical, and valuable.

### Rationale
Clear content presentation is required to ensure that tutorials are easy to follow and that users can successfully implement the demonstrated functionality.

### 4.1 Define the Audience and Scope

Identify the target audience and the specific goals of the tutorial.

### Rationale
Defining the audience and scope is recommended to manage user expectations and maintain content focus.

Directives:
- Assume the audience is familiar with the Python Standard Library and common packages.
- Clearly define what the package does and what it does not do.
- List all prerequisites, including knowledge and resource requirements.

### 4.2 Writing Voice

Follow the [Writing Voice](../guide_voice.md) guidelines for all tutorial content.

### Rationale
A consistent writing voice is required to maintain the "Standard-Setter" persona and ensure that all tutorials are professional, objective, and educational.

Directives:
- Use the direct imperative mood for setup and execution instructions.
- Use the third-person descriptive voice for explaining package features and behavior.
- Avoid all pronouns in both narrative text and code comments.
- Integrate RFC 2119 keywords naturally into sentences using lowercase.

### 4.3 Logical Flow

Organize content from simple to complex.

### Rationale
A progressive logical flow is required to build user mastery before introducing advanced concepts.

Directives:
- Ensure top-to-bottom cell execution is possible.
- Maintain smooth transitions between sections.

### 4.4 Markdown Cells

Use Markdown cells for narrative explanations and documentation.

### Rationale
Clear narrative text is required to explain the "why" behind the code examples.

Directives:
- Introduce each code cell or group of related cells with a Markdown cell.
- Explain the purpose of the code rather than providing a line-by-line translation.

### 4.5 Code Cells

Use code cells for runnable demonstrations.

### Rationale
Executable code is required to provide a verifiable and interactive learning experience.

Directives:
- Ensure all code cells are runnable independently or in sequence.
- Test all code cells thoroughly.
- Ensure outputs are illustrative and visible.

### 4.6 Self-Contained Examples

Ensure each major section has self-contained code.

### Rationale
Self-contained code cells are recommended to allow users to verify functionality without complex setup.

Directives:
- Avoid reliance on external files or services where possible.
- Provide mock data or clear setup instructions if external resources are necessary.

### 4.7 Error Handling Examples

Demonstrate how to handle common errors.

### Rationale
Showing error handling is recommended to prepare users for real-world integration challenges.


## 5 Formatting and Style

Follow standardized formatting conventions to ensure consistency.

### Rationale
Consistent formatting is required to create a professional and easily navigable document.

Directives:
- Use `#` for the main title and `##` for major sections.
- Use backticks for inline code and triple backticks for code blocks.
- Specify the language for syntax highlighting in all code blocks.
- Use bold for strong emphasis and italics for mild emphasis.
- Use descriptive text for all hyperlinks.


## 6 Tips for Effectiveness

### Rationale
Adhering to these tips is recommended to maximize the educational impact of the tutorial.

Directives:
- Assume the user is a beginner and build complexity gradually.
- Encourage interaction by inviting users to modify parameters.
- Provide context for *why* something is done, not just *how*.
- Test the tutorial in a clean kernel to verify correctness.
- Update the tutorial whenever the package API changes.

