# Python Style Guide: Writing Voice

This guide defines the "Standard-Setter" writing voice used for all project documentation, including syntax rules, tutorials, and examples.

## 1 Standard-Setter Persona

The documentation must adopt the "Standard-Setter" persona. This persona acts as a neutral arbiter of quality rather than a rigid enforcer. It prioritizes clarity and the "why" behind rules, allowing developers to understand the goal even if they deviate from the specific implementation.

### Rationale
A neutral arbiter persona is required to foster a collaborative and educational environment where rules are seen as helpful standards rather than arbitrary restrictions.

## 2 Tone and Perspective

Maintain an objective, technical tone throughout all documentation.

### Rationale
An objective tone is required to provide clear, unbiased information and avoid the distraction of personal perspectives.

Directives:
- Avoid all pronouns (e.g., "you," "your," "we," "us," "I," "my") to maintain neutrality.
- Focus on the code, the system, or the user in the third person.

Compliant:
"The system requires an active user session to proceed."

Non-Compliant:
"You must have an active session to proceed."

## 3 Mood and Voice

Select the appropriate mood based on the context of the writing.

### Rationale
Using consistent moods for specific contexts is required to provide clear signals to the reader about whether a statement is a rule, a description, or an instruction.

### 3.1 Direct Imperative for Core Rules

Use the direct imperative mood for all core rules and directives.

Directives:
- State the rule as a direct command.
- Avoid passive or explanatory phrasing for requirements.

Compliant:
"Use 4 spaces for indentation. Do not use tabs."

Non-Compliant:
"Indentation should be 4 spaces, and tabs are not allowed."

### 3.2 Third-Person Declarative for Docstrings

Use the third-person declarative (present indicative) mood for function and class docstrings.

Directives:
- Describe what the function or class does as a fact.
- Contrast this with the project-wide direct imperative rule for documentation.

### Rationale
Maintaining the third-person declarative for docstrings is required to provide a clear, factual description of the code's behavior, distinguishing it from procedural instructions.

Compliant:
"Returns the sum of two integers."

Non-Compliant:
"Return the sum of two integers."

### 3.3 Third-Person Descriptive for General Explanations

Use the third-person descriptive voice for explaining features, systems, or logic.

Compliant:
"The `UserRegistry` class manages a collection of users."

## 4 Terminology (RFC 2119)

Explicitly define levels of flexibility using RFC 2119 keywords.

Directives:
- Incorporate keywords naturally into sentences.
- Use lowercase for keywords (e.g., must, should, may, required, recommended).
- Do not use all-caps or itemize keywords as standalone rules.

### Rationale
Standardized terminology is required to eliminate ambiguity regarding the strictness of a guideline.

Definitions:
- **must / required**: The rule is a hard requirement for the codebase to be accepted.
- **should / recommended**: The rule is a strong recommendation, but valid exceptions may exist.
- **may / optional**: The rule is truly optional; personal preference is permitted.

## 5 Rationale and Examples

Provide context and clarity for all major rules and guidelines.

### Rationale
Explanations and examples are required to ensure that the "why" behind a rule is understood and to eliminate ambiguity in its implementation.

Directives:
- Include a "Rationale" section for major headings and controversial rules.
- Provide "Compliant" and "Non-Compliant" code examples where ambiguity might exist.

## 6 Project Consistency

Prioritize consistency within the project over strict adherence to this global guide. Once a project-wide standard
is established, it must be applied uniformly across all files and modules within that project.

### Rationale
Project consistency is required to maintain readability and reduce cognitive load within a project. While style
differences between encapsulated projects are acceptable, internal uniformity ensures clarity for all contributors.

### Directives:
- Adhere to the established project-wide style in all files and modules.
- Ensure all new code and refactors align with the project's chosen naming and formatting conventions.
