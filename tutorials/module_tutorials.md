# Anthony's Python Style Guide: Module Tutorials

A tutorial is a step-by-step guide to a specific topic. It provides a clear and concise explanation of the topic,
demonstrating the functionality and use cases. It is designed to be self-contained and easy to follow.
However, the purpose of a tutorial is to not only educate users on functionality but also provide inspiration for new
approaches to solving problems.

This document provides specific guidelines for creating Jupyter Notebook tutorials focused on individual modules.

Unlike package-level tutorials, these module tutorials offer a more targeted approach, helping users understand the
functionality, features, and use cases of specific modules. The guidelines cover how to define the audience and scope,
structure the tutorial content, demonstrate module-specific functionality, show interactions with other modules, and
present practical examples. By following these guidelines, developers can create focused, effective tutorials that help
users leverage the full potential of individual modules within the larger package ecosystem.

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

Jupyter Notebooks are a powerful tool for creating interactive tutorials. They allow users to combine text, code, and
visualizations into a single document. They are ideal for educational purposes, as they provide a clear and concise
explanation of a topic, demonstrating the functionality and use cases.

Consider and report the following when creating a tutorial:
- **Kernel Choice:** Specify if needed.
- **Magic Commands:** Explain any used.


## 2 Directory Hierarchy

Organize tutorials in a directory structure that mirrors the package structure. This makes it easy for users to find tutorials relevant to specific components.

- Create a directory for each major package under the `tutorials/` directory.
- Give subpackages their own subdirectories when they contain multiple components.
- Group related tutorials together in the same directory.
- Start filenames with a descriptive name followed by `_tutorial` (e.g., `name_tutorial.py`).
- Use the format `<component_name>_tutorial.py` for individual component tutorials.
- For tutorials that demonstrate multiple components working together, use a descriptive name that indicates the functionality being demonstrated, e.g., `caching_with_sentinel_tutorial.py`.
- Use lowercase with underscores for file names (snake_case).

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

Ensure tutorial files follow a consistent naming convention to make them easily identifiable:

- Use the format `<component_name>_tutorial.py` for individual module tutorials.
- Use lowercase with underscores for file names (snake_case).
- Avoid generic names like `tutorial.py` or `demo.py`.

A clear and logical flow is essential in a tutorial. Use these recommended sections:

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

Ensure the contents of a tutorial are accessible, practical, and valuable to users. Presentation is crucial to ensure that it is easy to follow and understand.

### 4.1 Define the Audience and Scope

**Target Audience:** The target audience will be the main user-base reading and using this tutorial.
- Typically, assume the target audience is familiar with the Python Standard Library, popular packages, and possibly some dependencies.
- For modules, assume the audience is familiar with the package's modules and their dependencies.
- Adjust the target audience depending on the goal of the tutorial.
- Tailor language, complexity of examples, and depth of explanation to the intended audience.

**Module Scope:** Clearly define what this module does and what it *does not* do.
- Consider how this tutorial fits into the understanding of the broader package.

**Prerequisites:** List knowledge and resource requirements needed to complete the tutorial.
- List concepts of the broader package used in the module.
- List any advanced or obscure Python Standard Library concepts used.
- List dependency concepts used in the module.
- List any resources the user must import.

### 4.2 Language

Ensure the language used in module tutorials is clear, accessible, and professional. Effective communication is crucial for ensuring users can understand and implement the module's functionality. Follow these guidelines to maintain consistent and user-friendly language throughout the tutorial:

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
- Ensure top-to-bottom cell execution.
- Build each section upon the previous ones.

### 4.4 Markdown Cells

Use Markdown cells to provide context, explanations, and documentation. Use them to break up code sections, explain concepts, and guide users through the learning process. Ensure these cells are well-formatted and informative to make the tutorial easy to follow.

- Introduce each code cell or group of related code cells with a Markdown cell.
- Explain the purpose of the code, rather than providing a line-by-line translation.
- Use Markdown formatting (headings, lists, bold, italics, code highlighting) to improve readability.

### 4.5 Code Cells

Use code cells to demonstrate the functionality of the module. Provide a clear and concise way to demonstrate the module's functionality and provide examples of how to use it.

- Ensure every code cell is runnable independently or in sequence.
- Place imports and variable initializations correctly.
- Test all code cells thoroughly.
- Display Outputs: ensure cell outputs are visible and illustrative.
- Ensure plots render correctly in the notebook.

### 4.6 Self-Contained Examples

Use self-contained examples to ensure that users can run and understand the tutorial without external dependencies or setup requirements. Provide complete, runnable units of code that demonstrate specific functionality while being independent of external resources. This approach makes the tutorial more accessible and reduces potential points of failure.

- Avoid reliance on external files or services if possible. If necessary, provide clear instructions on how to obtain/set them up, or include mock data/objects directly in the notebook.
- For data, consider including a small CSV or generating data programmatically.
- If there are unit tests, use them as a reference but do not copy them exactly. Use the tutorial and examples to educate the user on how to use key aspects of the module and how to create new programs, not just test it.

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

## 6 Tips for Module Tutorial Effectiveness

This section provides practical recommendations for creating impactful and successful module tutorials. These tips help
ensure the tutorial achieves its educational goals while maintaining user engagement.

- **Focus:** Keep the tutorial tightly focused on the functionalities of the specific module. Avoid extensive detours into other modules unless demonstrating direct interaction.
- **Context within Package:** Briefly remind users how this module fits into the overall architecture or purpose of the parent package.
- **Independence:** While part of a package, aim for the module tutorial to be as understandable as possible, even if a user jumps directly to it (though prerequisites should be stated).
- **Test Thoroughly:** Run in a clean kernel. Have someone unfamiliar with the module test it.
- **Keep Updated:** Module APIs can change. Ensure the tutorial reflects the current version of the module.


Adhere to this style guide to create clear, focused, and highly effective Jupyter Notebook tutorials for individual modules within Python packages, enabling users to leverage their full potential.

