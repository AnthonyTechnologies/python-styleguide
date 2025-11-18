# Anthony's Python Style Guide: Comments

Comments should be used to outline sections of code and explain tricky parts of the code.

## Table of Contents

- [1 Block and Inline](#1-block-and-inline)
- [2 TODO Comments](#2-todo-comments)


## 1 Block and Inline
In general, operations can be grouped together into sections based on their purpose. Comments can be used to outline
these sections and explain the purpose of the code.

Comments guidelines:
- Comments start with the `#` character and are followed by a space before the text of the comment.
- The start of code sections should have a title comment defining the purpose of that section.
- Complicated sections should get a few lines of comments before the operations.
- Describe what the section is trying to accomplish and how it achieves that.
- Try not to describe what each line of code is doing.
- Non-obvious ones get comments at the end of the line.
- In-line comments should start at least 2 spaces away from the code they are commenting on.

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

A TODO comment begins with the word TODO in all caps, a following colon, and a link to a resource that contains the
context, ideally a bug reference. A bug reference is preferable because bugs are tracked and have follow-up comments.
Follow this piece of context with an explanatory string introduced with a hyphen `-`. The purpose is to have a
consistent TODO format that can be searched to find out how to get more details.

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

