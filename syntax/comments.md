# Anthony's Python Style Guide: Comments

Comments should be used to outline sections of code and explain tricky parts of the code. All comments should be written
in the third-person. When explaining features and how things work, use the third-person descriptive voice (e.g.,
"Calculates the sum."). When instructing users on how to use things or providing requirements, use the third-person
imperative voice. The voice should be active and be issued as commands (e.g., "The user must call this function
first."). This ensures a professional and objective tone throughout the code. Avoid using first-person ("we") or
second-person ("you") perspectives.

## Table of Contents

- [1 Block and Inline](#1-block-and-inline)
- [2 TODO Comments](#2-todo-comments)


## 1 Block and Inline
In general, group operations into sections based on their purpose. Use comments to outline these sections and explain the purpose of the code.

Comments guidelines:
- Start comments with the `#` character, followed by a space before the text.
- Include a title comment at the start of code sections defining the purpose of that section.
- Provide a few lines of comments before complicated sections.
- Describe what the section is trying to accomplish and how it achieves that.
- Avoid describing what each line of code is doing.
- Add comments at the end of the line for non-obvious operations.
- Start inline comments at least 2 spaces away from the code they are commenting on.

Correct:
```python # pseudocode
# Find Location in the Array
# A weighted dictionary search is used to determine where i is in the array. The position is extrapolated based on the
# largest number in the array and the array size, and then a binary search is performed to obtain the exact index.
if i & (i-1) == 0:  # True if i is 0 or a power of 2.
```
Incorrect:
```python # pseudocode
# Now go through the b array and make sure whenever x occurs the next element is x+1
for i, v in enum(b):
    if v == x:
        b[i + 1] = x + 1
```


## 2 TODO Comments
Use TODO comments for code that is temporary, a short-term solution, or good-enough but not perfect.

A TODO comment begins with the word `TODO` in all caps, followed by a colon and a link to a resource that contains the context, ideally a bug reference. Use a bug reference when possible because bugs are tracked and have follow-up comments. Follow this piece of context with an explanatory string introduced with a hyphen `-`. The purpose is to maintain a consistent `TODO` format that can be searched to find more details.

```python # pseudocode
# TODO: crbug.com/192795 - Investigate cpufreq optimizations.
```

Avoid adding TODOs that refer to an individual or team as the context:

```python # pseudocode
# TODO: @username - File an issue and use a '*' for repetition.
```

If a TODO is of the form "At a future date do something" ensure that it either includes a very specific date
("Fix by November 2009") or a very specific event ("Remove this code when all clients can handle XML responses.") that
future code maintainers will comprehend. Issues are ideal for tracking this.

