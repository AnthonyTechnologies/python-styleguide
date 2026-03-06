# Anthony's Python Style Guide: Package Tutorials

A tutorial is a step-by-step guide to a specific topic. It provides a clear and concise explanation of the topic,
demonstrating the functionality and use cases. It is designed to be self-contained and easy to follow.
However, the purpose of a tutorial is to not only educate users on functionality but also provide inspiration for new
approaches to solving problems.

This document provides comprehensive guidelines for creating effective Jupyter Notebook tutorials for Python packages.

It outlines best practices for structuring tutorials, defining the target audience, presenting code examples, formatting
content, and leveraging Jupyter Notebook features. These guidelines help developers create clear, accessible, and
educational tutorials that enable users to quickly understand and effectively use the packages, enhancing the overall
user experience and adoption of the project's components.

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

Jupyter Notebooks are a powerful tool for creating interactive tutorials. They allow users to combine text, code, and
visualizations into a single document. They are ideal for educational purposes, as they provide a clear and concise
explanation of a topic, demonstrating the functionality and use cases.

Consider and report the following when creating a tutorial:
- **Kernel Choice:** Specify if needed.
- **Magic Commands:** Explain any used.


## 2 Directory Hierarchy

Organize tutorials in a directory structure that mirrors the package structure. This makes it easy for users to find tutorials relevant to specific components.

- Create a directory for each major package under the `tutorials/` directory.
- Use subdirectories for subpackages when they contain multiple components.
- Typically, provide a single tutorial for each major package and subpackage, though exceptions may occur.
- Start filenames with a descriptive name followed by `_package_tutorial` (e.g., `name_package_tutorial.py`).
- Use the format `<component_name>_package_tutorial.py` for individual component tutorials.
- For tutorials that demonstrate multiple components working together, use a descriptive name that indicates the functionality being demonstrated, e.g., `caching_with_sentinel_tutorial.py`.
- Use lowercase with underscores for file names (snake_case).

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

Ensure a clear and logical flow is essential. Use these recommended sections:

1. Title and Introduction
2. Installation
3. Importing the Package
4. Core Concepts & Basic Usage
5. Advanced Features
6. Examples
7. API Highlights
8. Troubleshooting / FAQs

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

Ensure the contents of a tutorial are accessible, practical, and valuable to users. Presentation is crucial to ensure that it is easy to follow and understand.

### 4.1 Define the Audience and Scope

**Target Audience:** The target audience will be the main user-base reading and using this tutorial.
- Typically, assume the target audience is familiar with the Python Standard Library, popular packages, and possibly some dependencies.
- For packages, assume the audience is familiar with the package's modules and their dependencies.
- Adjust the target audience depending on the goal of the tutorial.
- Tailor language, complexity of examples, and depth of explanation to the intended audience.

**package Scope:** Clearly define what this package does and what it *does not* do.
- Consider how this tutorial fits into the understanding of the broader package.

**Prerequisites:** List knowledge and resource requirements needed to complete the tutorial.
- List concepts of the broader package used in the package.
- List any advanced or obscure Python Standard Library concepts used.
- List dependency concepts used in the package.
- List any resources the user must import.

### 4.2 Language

Ensure the language used in package tutorials is clear, accessible, and professional. Effective communication is crucial for ensuring users can understand and implement the package's functionality. Follow these guidelines to maintain consistent and user-friendly language throughout the tutorial:

- Be polite, friendly, and approachable while remaining clear, concise, and certain.
- Use simple, direct language. Avoid jargon where possible, or explain it if necessary.
- Keep sentences and paragraphs short.
- When explaining features and how things work, use the third-person descriptive voice (e.g., "The module provides...").
- When instructing users on how to use things, use the third-person imperative voice. The voice should be active
  and be issued as commands (e.g., "The user should..."). Start with the Verb; avoid "The user should now try to
  click..." and use "Click..." instead.

### 4.3 Logical Flow

Logical flow of content is crucial for effective learning. Ensure the tutorial progresses naturally, building upon previous concepts and maintaining a clear connection between topics.

- Organize topics from simple to complex.
- Maintain smooth transitions between sections.
- Build each section upon the previous ones.

### 4.4 Markdown Cells

Use Markdown cells to provide context, explanations, and documentation. Use them to break up code sections, explain concepts, and guide users through the learning process. Ensure these cells are well-formatted and informative to make the tutorial easy to follow.

- Introduce each code cell or group of related code cells with a Markdown cell.
- Explain the purpose of the code, rather than providing a line-by-line translation.
- Use Markdown formatting (headings, lists, bold, italics, code highlighting) to improve readability.

### 4.5 Code Cells

Use code cells to demonstrate the functionality of the package. Provide a clear and concise way to demonstrate the package's functionality and provide examples of how to use it.

- Ensure every code cell is runnable independently or in sequence.
- Place imports and variable initializations correctly.
- Test all code cells thoroughly.
- Display Outputs: ensure cell outputs are visible and illustrative.
- Ensure plots render correctly in the notebook.

### 4.6 Self-Contained Examples

Use self-contained examples to ensure that users can run and understand the tutorial without external dependencies or setup requirements. Provide complete, runnable units of code that demonstrate specific functionality while being independent of external resources. This approach makes the tutorial more accessible and reduces potential points of failure.

- Avoid reliance on external files or services if possible. If necessary, provide clear instructions on how to obtain/set them up, or include mock data/objects directly in the notebook.
- For data, consider including a small CSV or generating data programmatically.
- If there are unit tests, use them as a reference but do not copy them exactly. Use the tutorial and examples to educate the user on how to use key aspects of the package and how to create new programs, not just test it.

### 4.7 Error Handling Examples

Use the Error Handling Examples section to demonstrate how to handle common errors and exceptions that users might encounter. Help users understand potential pitfalls and how to gracefully handle error conditions to make their code more robust and maintainable. This section is optional, but recommended.

- Show how to handle common exceptions or invalid inputs if relevant to the package's usage.


## 5 Formatting and Style

This section provides specific formatting and style guidelines to ensure consistency and readability. These conventions
help create a professional and easily navigable document.

### 5.1 Headings

- Use `#` for the main title (H1).
- Use `##` for major sections (H2).
- Use `###` for sub-sections (H3), and so on.
- Be consistent with heading levels.

### 5.2 Code Blocks

- In Markdown cells, use backticks for inline code: `my_function()`.
- Use triple backticks for code blocks:
    ```python # pseudocode
    # Python code goes here
    ```
- Specify the language for syntax highlighting in Markdown code blocks (e.g., ` ```python # pseudocode`).

### 5.3 Emphasis

- Use `**bold**` for strong emphasis (e.g., key terms, warnings).
- Use `*italics*` for mild emphasis or for terms being defined.

### 5.4 Lists

- Use numbered lists for sequential steps.
- Use bulleted lists for non-sequential items or features.

### 5.5 Links

- Use descriptive text for hyperlinks:
    - Good: `[Read the full API documentation](link-to-docs)`
    - Avoid: `Click [here](link-to-docs)`


## 6 Tips for Effectiveness

This section provides practical recommendations for creating impactful and successful package tutorials. These tips help
ensure the tutorial achieves its educational goals while maintaining user engagement.

- **Start Simple:** Assume the user is a beginner with the package.
- **Build Complexity Gradually:** Don't overwhelm users with too much information at once.
- **Encourage Interaction:** Phrase explanations to invite users to try modifying the code.
- **Provide Context:** Explain *why* something is done, not just *how*.
- **Test Thoroughly:**
    - Run the entire notebook from start to finish in a clean kernel.
    - Have someone else go through the tutorial.
- **Keep it Updated:** As the package evolves, update the tutorial to reflect changes.
- **Clear Outputs Before Distribution (Usually):** Unless the outputs are essential for understanding without running (e.g., a complex plot that takes time to generate), it's often best to "Clear All Outputs" before distributing the `.ipynb` file. This reduces file size and allows users to generate outputs themselves. Alternatively, ensure all outputs are clean and directly relevant.

Adhere to this style guide to create high-quality Jupyter Notebook tutorials that significantly enhance the user experience for Python packages.

