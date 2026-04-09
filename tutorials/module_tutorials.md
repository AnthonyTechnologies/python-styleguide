# Anthony's Python Style Guide: Module Tutorials

Use tutorials to provide step-by-step guidance on specific topics, demonstrating functionality and practical use cases.

### Rationale
High-quality tutorials are required to educate users on library features and inspire new approaches to problem-solving.

Directives:
- Focus module tutorials on individual components rather than the entire package.
- Use Jupyter Notebooks (.ipynb) to provide an interactive learning experience.
- Follow general style guidelines (naming, layout, docstrings) within code cells.

## Table of Contents

- [1 Jupyter Notebook](#1-jupyter-notebook)
- [2 Directory Hierarchy](#2-directory-hierarchy)
- [3 Module Tutorial Notebook Structure](#3-module-tutorial-notebook-structure)
  - [3.1 Title and Introduction](#31-title-and-introduction)
  - [3.2 Core Functionality](#32-core-functionality)
  - [3.3 Module Interaction](#33-module-interaction)
  - [3.4 Advanced Features](#34-advanced-features)
  - [3.5 Examples](#35-examples)
  - [3.6 API Highlights](#36-api-highlights)
  - [3.7 Troubleshooting / FAQs](#37-troubleshooting--faqs)
  - [3.8 Conclusion and Next Steps](#38-conclusion-and-next-steps)
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
- [6 Tips for Module Tutorial Effectiveness](#6-tips-for-module-tutorial-effectiveness)


## 1 Jupyter Notebook

Use Jupyter Notebooks to create interactive and educational tutorials that combine text, code, and visualizations.

### Rationale
Jupyter Notebooks are recommended for tutorials because they allow users to execute code in real-time, facilitating active learning and experimentation.

Directives:
- Specify the required kernel.
- Explain any magic commands used in the notebook.


## 2 Directory Hierarchy

Organize tutorials within a directory structure that mirrors the package structure.

### Rationale
A mirrored directory structure is required to make tutorials easily discoverable based on the module they cover.

Directives:
- Create a directory for each major package under the `tutorials/` directory.
- Use subdirectories for subpackages.
- Name files with a `_tutorial.ipynb` suffix (e.g., `name_tutorial.ipynb`).
- Use `snake_case` for all filenames.

Example:
```
tutorials/
├── bases/                          # Tutorials for the bases package
│   ├── collections/                # Tutorials for the bases.collections subpackage
│   │   └── basedict_tutorial.ipynb
│   ├── basecallable_tutorial.ipynb
│   └── sentinelobject_tutorial.ipynb
└── cachingtools/                   # Tutorials for the cachingtools package
    ├── caches/                     # Tutorials for the cachingtools.caches subpackage
    └── cachingobject_tutorial.ipynb
```


## 3 Module Tutorial Notebook Structure

Establish a clear and logical flow for all tutorial notebooks.

### Rationale
A standardized structure is required to ensure that tutorials are easy to navigate and that users know what to expect.

Directives:
- Use the `_tutorial.ipynb` suffix for filenames.
- Include these sections in order:
    1. Title and Introduction
    2. Core Functionality
    3. Module Interactions
    4. Advanced Features
    5. Examples
    6. API Highlights
    7. Troubleshooting / FAQs
    8. Conclusion and Next Steps

### 3.1 Title and Introduction

Use the Title and Introduction section to set the stage for the module's tutorial. Provide users with a clear understanding of what they will learn and how this module fits into the larger package ecosystem. Ensure this section serves as an engaging entry point while remaining informative and concise.

- Formatting: Markdown Cell
- Clear Title: "Using the [ModuleName] Module in [PackageName]", "[ModuleName] for [Specific Task]", etc.
- Brief Overview:
    - Explain the module's primary responsibilities and features.
    - Explain how this module relates to the parent package.
    - Explain what will be covered in this tutorial.
    - Briefly summarize the prerequisites.
- Table of Contents (Optional but Recommended): Markdown links to major sections within this module tutorial.

### 3.2 Core Functionality

Use the Core Functionality section to introduce users to the fundamental features and capabilities of the module. Ensure this section serves as the foundation for understanding how to use the module effectively by demonstrating its primary functions and basic usage patterns.

- Formatting: Markdown and Code Cells
- Introduce the key functions, classes, and concepts specific to this module.
- Explain the key concepts of the module and how to use them.
- Explain the concepts behind complex functions, methods, and data structure interactions.
- Provide simple, executable examples for each primary feature of the module.
- Explain each code cell:
    - What the code (from this module) does.
    - Explain the utility of the module and the code.
    - The expected output (and show it by running the cell).
- If the module has a central class, demonstrate its instantiation and methods.

### 3.3 Module Interaction

Use this section to explore how the module interfaces with other components of the package ecosystem. Demonstrate the module's role in larger workflows and how it can be integrated with other modules to achieve more complex functionality.

- Formatting: Markdown and Code Cells
- If this module is designed to work closely with other modules in the same package, demonstrate these interactions.
- Show how data or objects from this module can be used by, or accept input from, other parts of the package.

### 3.4 Advanced Features

Use the Advanced Features section to delve into more sophisticated aspects of the module, presenting complex functionalities and specialized use cases. Design this section for users who have mastered the basics and are ready to explore the module's full capabilities.

- Formatting: Markdown and Code Cells
- Cover more complex functionalities, configurations, or less common use cases specific to this module.
- Explain each feature in detail.
- Break down examples into understandable steps.

### 3.5 Examples

Use this section to bridge the gap between theory and practice by presenting real-world applications of the module. Through concrete examples and scenarios, help users better understand how to apply the module's features to solve actual problems.

- Formatting: Markdown and Code Cells
- Showcase how this specific module solves particular problems or aids in specific tasks.
- Use relatable scenarios or small datasets relevant to the module's purpose.
- This helps users see the module's practical value.


### 3.6 API Highlights

Use the API Highlights section to provide a curated overview of the module's most important API components. Ensure this section serves as a quick reference guide to the essential functions, classes, and methods that form the core of the module's interface.

- Formatting: Markdown Cell
- Briefly list key functions/classes within this module and their purpose.
- Link to the relevant section of the full API documentation for this module.


### 3.7 Troubleshooting / FAQs

Use this section to address common challenges and questions users might encounter while working with the module. Provide solutions, workarounds, and best practices to help users overcome typical obstacles and optimize their use of the module.

- Formatting: Markdown Cell
- Address common issues or questions specifically related to this module.
- Provide solutions or links to further help.

### 3.8 Conclusion and Next Steps

Use the Conclusion and Next Steps section to wrap up the tutorial and provide guidance for further learning. Help users solidify their understanding and show them paths for continued exploration of the module and package.

- Formatting: Markdown Cell
- Summarize what was covered about the module.
- Encourage further exploration of the module's capabilities.
- Mention if there are more examples in the examples section of the project.
- Suggest next steps:
  - Trying other features of this module.
  - Exploring related modules in the package.
  - Consulting the full API documentation for the module.


## 4 Content Guidelines

Ensure the contents of a tutorial are accessible, practical, and valuable.

### Rationale
Clear content presentation is required to ensure that tutorials are easy to follow and that users can successfully implement the demonstrated functionality.

### 4.1 Define the Audience and Scope

Identify the target audience and the specific goals of the tutorial.

### Rationale
Defining the audience and scope is recommended to manage user expectations and ensure that the content remains focused.

Directives:
- Assume the audience is familiar with the Python Standard Library and the package's core modules.
- Clearly define what the module does and what it does not do.
- List all prerequisites, including knowledge and resource requirements.

### 4.2 Writing Voice

Follow the [Writing Voice](../guide_voice.md) guidelines for all tutorial content.

### Rationale
A consistent writing voice is required to maintain the "Standard-Setter" persona and ensure that all tutorials are professional, objective, and educational.

Directives:
- Use the direct imperative mood for setup and execution instructions.
- Use the third-person descriptive voice for explaining module features and behavior.
- Avoid all pronouns in both narrative text and code comments.
- Integrate RFC 2119 keywords naturally into sentences using lowercase.

### 4.3 Logical Flow

Organize content from simple to complex.

### Rationale
A progressive logical flow is required to build user understanding before introducing advanced features.

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
Executable code is required to provide an interactive and verifiable learning experience.

Directives:
- Ensure all code cells are runnable independently or in sequence.
- Test all code cells thoroughly.
- Ensure outputs are illustrative and visible.

### 4.6 Self-Contained Examples

Ensure each major section has self-contained code.

### Rationale
Self-contained code is recommended to allow users to verify functionality without complex setup requirements.

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

## 6 Tips for Module Tutorial Effectiveness

### Rationale
Adhering to these tips is recommended to maximize the educational impact of the tutorial.

Directives:
- Keep the tutorial tightly focused on the functionalities of the specific module.
- Briefly remind the user how the module fits into the overall architecture.
- Aim for independence so the tutorial is understandable even if the user jumps directly to it.
- Run the tutorial in a clean kernel to verify its correctness.
- Update the tutorial whenever the module API changes.

