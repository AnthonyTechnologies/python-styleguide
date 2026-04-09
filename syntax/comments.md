# Anthony's Python Style Guide: Comments

Use comments to outline sections of code and explain complex logic. All comments must be written in the third-person to maintain a professional and objective tone.

### Rationale
Clear and objective comments are required to help maintainers understand the "why" and "how" of complex operations without cluttering the code with redundant descriptions of simple logic.

Directives:
- Use the third-person declarative voice for explaining features (e.g., "Calculates the sum").
- Use the third-person imperative voice for instructions or requirements (e.g., "The user must call this function first").
- Avoid first-person ("we") and second-person ("you") perspectives.

## Table of Contents

- [1 Block and Inline](#1-block-and-inline)
- [2 TODO Comments](#2-todo-comments)


## 1 Block and Inline

Group operations into sections and use comments to define the purpose of each section.

### Rationale
Sectioning code with comments is required to improve discoverability and reduce cognitive load when navigating large modules.

Directives:
- Start comments with `# ` (a hash followed by a space).
- Include a title comment at the start of each major code section.
- Provide explanatory comments before complicated logic blocks.
- Describe goals and high-level implementation rather than line-by-line actions.
- Use inline comments for non-obvious operations, starting at least 2 spaces away from the code.

Compliant:
```python # pseudocode
# Find Location in the Array
# A weighted dictionary search is used to determine where i is in the array. The position is extrapolated based on the
# largest number in the array and the array size, and then a binary search is performed to obtain the index.
if i & (i-1) == 0:  # True if i is 0 or a power of 2.
```

Non-Compliant:
```python # pseudocode
# Now go through the b array and make sure whenever x occurs the next element is x+1
for i, v in enum(b):
    if v == x:
        b[i + 1] = x + 1
```


## 2 TODO Comments

Use `TODO` comments for temporary, short-term, or non-optimal solutions.

### Rationale
Standardized `TODO` comments are required to ensure that pending work is easily searchable and contains enough context for future resolution.

Directives:
- Start the comment with `TODO` in all caps, followed by a colon.
- Include a link to a resource (ideally a bug or issue reference) for context.
- Follow the context with an explanatory string introduced by a hyphen `-`.
- Avoid referring to specific individuals or teams.
- Ensure that `TODO` comments referring to future events include specific dates or triggers.

Compliant:
```python # pseudocode
# TODO: crbug.com/192795 - Investigate cpufreq optimizations.
```

Non-Compliant:
```python # pseudocode
# TODO: @username - File an issue.
```

