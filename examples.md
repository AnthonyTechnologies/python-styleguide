# Anthony's Python Style Guide: Examples

Use examples to provide practical demonstrations of library functionality and serve as reference implementations for common use cases.

### Rationale
Well-crafted examples are required to reduce the learning curve for new users and provide quick reference for experienced developers.

Directives:
- Write examples in Python files (.py) rather than Jupyter notebooks to facilitate easier implementation into other projects.
- Follow general style guidelines (naming, layout, docstrings) in all example code.
- Prioritize clarity and educational value.

## Table of Contents

- [1 Directory Hierarchy](#1-directory-hierarchy)
- [2 Example Structure](#2-example-structure)
    - [2.1 Example File Header](#21-example-file-header)
    - [2.2 Main Section for Examples](#22-main-section-for-examples)
    - [2.3 Example Category Functions](#23-example-category-functions)
- [3 Example Semantics and Syntax](#3-example-semantics-and-syntax)
    - [3.1 Example Documentation](#31-example-documentation)
        - [3.1.1 Print Statements](#311-print-statements)
        - [3.1.2 Error Handling](#312-error-handling)
    - [3.2 Assertions](#32-assertions)
    - [3.3 Writing Style](#33-writing-style)
        - [3.3.1 Third-Person Descriptive Voice](#331-third-person-descriptive-voice)
        - [3.3.2 Third-Person Imperative Voice](#332-third-person-imperative-voice)
- [4 Example Content Guidelines](#4-example-content-guidelines)
    - [4.1 Self-Contained Examples](#41-self-contained-examples)
    - [4.2 Progressive Complexity](#42-progressive-complexity)
    - [4.3 Real-World Scenarios](#43-real-world-scenarios)
    - [4.4 Edge Cases](#44-edge-cases)
    - [4.5 Implement Base Classes](#45-implement-base-classes)
- [5 Example Styles](#5-example-styles)
    - [5.1 Cookbook Style](#51-cookbook-style)
    - [5.2 Compare and Contrast](#52-compare-and-contrast)
    - [5.3 Step-by-Step Transformation](#53-step-by-step-transformation)
    - [5.4 Annotated Examples](#54-annotated-examples)
    - [5.5 Interactive Examples](#55-interactive-examples)
    - [5.6 Error-Driven Learning](#56-error-driven-learning)
    - [5.7 Incremental Complexity](#57-incremental-complexity)
    - [5.8 Visual Learning](#58-visual-learning)
    - [5.9 Example Styles Conclusions](#59-example-styles-conclusions)
- [6 Example-Specific Best Practices](#6-example-specific-best-practices)
- [7 Testing Examples](#7-testing-examples)


## 1 Directory Hierarchy

Organize examples within a directory structure that mirrors the package structure.

### Rationale
A mirrored directory structure is required to make examples easily discoverable based on the component they demonstrate.

Directives:
- Create a directory for each major package under the `examples/` directory.
- Use subdirectories for subpackages when they contain multiple components.
- Group related examples together.
- Name files with an `_example.py` suffix (e.g., `name_example.py`).
- Use `snake_case` for all filenames.

Example:
```
examples/
├── bases/                          # Examples for the bases package
│   ├── collections/                # Examples for the bases.collections subpackage
│   │   └── baseobject_example.py
│   ├── basecallable_example.py
│   └── sentinelobject_example.py
└── cachingtools/                   # Examples for the cachingtools package
    ├── caches/                     # Examples for the cachingtools.caches subpackage
    └── cachingobject_example.py
```

## 2 Example Structure

Follow the [Code and File Layout](code_file_layout.md) guidelines for all example files, incorporating the additional considerations detailed below.

### Rationale
A consistent structure is required to ensure that examples are easy to read, understand, and adapt for other projects.

### 2.1 Example File Header

Include a descriptive module docstring in every example file.

### Rationale
Clear headers are required to provide an immediate summary of the example's purpose and the concepts it demonstrates.

Directives:
- Explain what the example demonstrates.
- Provide a numbered list of key concepts or features.
- Place imports from the library being demonstrated in the `Third-Party Packages` section to simulate external usage.

Example:
```python # pseudocode
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""sentinelobject_example.py
An example of how to create and use SentinelObject.

This example demonstrates:
1. Creating custom sentinel objects
2. Using sentinel objects as markers
3. Using sentinel objects in dictionaries
4. Comparing sentinel objects
"""

# Imports #
# Standard Libraries #

# Third-Party Packages #
from baseobjects.bases import SentinelObject

# Local Packages #


```

For general file header guidelines, imports organization, and definitions structure, refer to the [Code and File Layout](code_file_layout.md) document.

### 2.2 Main Section for Examples

Use the `if __name__ == "__main__":` block to orchestrate the demonstration.

### Rationale
A standardized entry point is required to make examples directly runnable and to provide a logical flow for the demonstration.

Directives:
- Organize demonstrations from basic to advanced.
- Use `print()` statements to provide context and display results.
- Include comments explaining the purpose and expected outcome of each step.
- Break down excessive logic into supporting functions categorized by functionality.

Examples:
```python # pseudocode
# Main #
if __name__ == "__main__":
    # Create a data processor with some sample data
    expected = "10 Hello [1, 2, 3]"
    print("Creating a data processor...")
    processor = DataProcessor({
        "item1": 10,
        "item2": "Hello",
        "item3": [1, 2, 3]
    })

    # Demonstrate basic caching
    print("\nDemonstrating basic caching with timed_cache...")
    print("First call (not cached):")
    result1 = processor.process_data("item1")
    print(f"Result: {result1} == {expected}")

    # More demonstrations...
```

```python # pseudocode
# Functions #
# Example Sections #
def method_execution_overview():
  """A long function which demonstrates usage of method execution."""
  print(f"Method Execution Overview: \n")
  ...


def arbitrate_state_overview():
  """A long function which demonstrates usage of arbitrate state."""
  print(f"Arbitrate State Overview: \n")
  ...


async def method_execution_async_overview():
  """A long function which demonstrates async usage of method execution."""
  ...


# Main #
if __name__ == "__main__":
  # Set Default Process Context
  method_execution_overview()
  asyncio.run(method_execution_async_overview())
  arbitrate_state_overview()
```

### 2.3 Example Category Functions

Use supporting functions to categorize complex demonstrations.

### Rationale
Function-based categorization is recommended to improve the modularity and readability of extensive examples.

Directives:
- Organize demonstrations in a logical sequence.
- Use `print()` statements to explain the context.
3. Include comments to explain the purpose of each demonstration.
4. Include comments to show the executed outcome and the expected outcome.

Examples:
```python # pseudocode
# Functions #
# Example Sections #
def arbitrate_state_overview():
    print(f"Arbitrate State Overview: \n")

    # Create Process Arbitrate
    arbitrate = ProcessArbitratorExample(2, secret=-1)

    # Check Values
    print(f"Default Values:")
    print(f"number: {arbitrate.number} == 2")
    print(f"item: {arbitrate.item} == 10")
    print(f"secret: {arbitrate.secret} == -1")
    print(f"")

    # Start Server
    arbitrate.start_server()  # All attributes are sent to the server (including untransmittable attributes)

    # Check Server Status
    assert arbitrate.is_proxy()
    assert arbitrate.is_alive()

    # Make a local change which will not be reflected in the server
    arbitrate.number = 1
    arbitrate.item = 50
    arbitrate.secret = -20

    print(f"Local Changes:")
    print(f"Local vs Server number: {arbitrate.number} != {arbitrate.get_attribute('number')}")
    print(f"Local vs Server item: {arbitrate.item} != {arbitrate.get_attribute('item')}")
    print(f"Local vs Server secret: {arbitrate.secret} != {arbitrate.get_attribute('secret')}")
    print(f"")

    # Update local values from the server (except for untransmittable attributes)
    arbitrate.update()

    print(f"Local Update:")
    print(f"Local vs Server number: {arbitrate.number} == {arbitrate.get_attribute('number')}")
    print(f"Local vs Server item: {arbitrate.item} == {arbitrate.get_attribute('item')}")
    print(f"Local vs Server secret: {arbitrate.secret} != {arbitrate.get_attribute('secret')}")
    print(f"")

    # Update server values from the local (except for untransmittable attributes)
    arbitrate.number = 1
    arbitrate.item = 50
    arbitrate.secret = -20
    arbitrate.update_server()

    print(f"Sever Update:")
    print(f"Local vs Server number: {arbitrate.number} == {arbitrate.get_attribute('number')}")
    print(f"Local vs Server item: {arbitrate.item} == {arbitrate.get_attribute('item')}")
    print(f"Local vs Server secret: {arbitrate.secret} != {arbitrate.get_attribute('secret')}")
    print(f"")

    # Stop Server
    arbitrate.stop_server()

    # Check Server Status
    assert not arbitrate.is_proxy()
    assert not arbitrate.is_alive()


# Main #
if __name__ == "__main__":
    # Examples #
    arbitrate_state_overview()
```


## 3 Example Semantics and Syntax

Ensure examples conform to the semantics and syntax described in [Semantics Guidelines](semantics.md) and the Syntax topics [Formatting](syntax/formatting.md), [Naming](syntax/naming.md), [Typing](syntax/typing.md), [Docstrings](syntax/docstrings.md), [Comments](syntax/comments.md), [Strings](syntax/strings.md), [Exceptions & Error Messages](syntax/exceptions_error_messages.md), [Logging](syntax/logging.md), and [Resources](syntax/resources.md). In some cases, deviate from the general guidelines. The following sections describe semantics and syntax which take precedence over the general style guide.

### 3.1 Example Documentation

Refer to the Syntax topics, particularly [Docstrings](syntax/docstrings.md) and [Comments](syntax/comments.md), for general code style, docstrings, and comments guidelines. The following sections cover documentation aspects specific to example files.

#### 3.1.1 Print Statements

Use `print()` statements in examples as a narrative to guide the user through the demonstration.

### Rationale
Frequent output is required to ensure that the execution flow and state changes are transparent to the user.

Directives:
- Use `print()` statements to indicate what is being demonstrated.
- Print input values, results, and expected results to show the effect of operations.
- Use descriptive messages that explain the context.
- Format output to improve readability.

Example:

```python # pseudocode
print("\nDemonstrating LRU cache with maxsize=2...")
print("Processing item1:")
advanced1 = processor.advanced_process("item1", 2)
print(f"Result: {advanced1} == 'item1item1'")
```

#### 3.1.2 Error Handling

Include explicit error handling in examples to demonstrate robust usage.

### Rationale
Showing how to handle exceptions is recommended to prepare users for real-world integration challenges.

Directives:
- Show how to handle common exceptions.
- Demonstrate best practices for error recovery.
- Include examples of input validation and error prevention.

Example:

```python # pseudocode
try:
    result = processor.process_data(user_input)
    print(f"Result: {result}")
except KeyError:
    print(f"Error: Key '{user_input}' not found in data")
except Exception as e:
    print(f"Unexpected error: {e}")
```

### 3.2 Assertions

Use `assert` statements to verify correctness within examples.

### Rationale
Assertions are recommended in examples because they serve as a form of executable documentation that clarifies the expected state. While discouraged in production source code, they are appropriate for demonstrations where the user manages error handling.

Directives:
- Include at least one assertion in each major section of an example.
- Use specific assertions that verify a single aspect of behavior.
- Include descriptive error messages in assertions to make failures informative.

Example:
```python # pseudocode
# Simple assertions
assert result == expected
assert instance is not None

# More complex assertions
assert id(new.immutable) == id(test_object.immutable)
assert id(new.mutable) != id(test_object.mutable)
assert unpickled.immutable == test_object.immutable
assert unpickled.mutable == test_object.mutable
assert unpickled is not test_object
```

### 3.3 Writing Style

Follow the [Writing Voice](guide_voice.md) guidelines for all example documentation and code comments.

### Rationale
A consistent writing voice is required to maintain the "Standard-Setter" persona and ensure that all examples are professional, objective, and easy to follow.

Directives:
- Use the direct imperative mood for setup and execution instructions.
- Use the third-person descriptive voice for explaining example logic.
- Avoid all pronouns in both documentation and code comments.
- Integrate RFC 2119 keywords naturally into sentences using lowercase.


## 4 Example Content Guidelines

### 4.1 Self-Contained Examples

Ensure examples are self-contained and runnable without external dependencies.

### Rationale
Self-contained examples are required to allow users to verify functionality immediately without additional configuration or resource provisioning.

Directives:
- Include all necessary imports.
- Generate sample data within the example.
- Avoid reliance on external files or services unless they are the subject of the demonstration.
- Mock external resources or provide clear setup instructions if they are necessary.

Example:

```python # pseudocode
# Generate sample data
data = {
    "item1": 10,
    "item2": "Hello",
    "item3": [1, 2, 3]
}

# Use the generated data in the example
processor = DataProcessor(data)
```

### 4.2 Progressive Complexity

Structure examples to progress from simple usage to complex scenarios.

### Rationale
Gradual introduction of features is recommended to prevent overwhelming new users and to build a solid foundation of understanding.

Directives:
- Start with basic usage of core functionality.
- Gradually introduce advanced features.
- Demonstrate how multiple components work together in complex scenarios.

Example:

```python # pseudocode
# Basic usage
print("Basic usage:")
result = processor.process_data("item1")

# Advanced usage
print("\nAdvanced usage:")
advanced_result = processor.advanced_process("item1", factor=2)

# Complex scenario
print("\nComplex scenario:")
# Demonstrate multiple components working together
```

### 4.3 Real-World Scenarios

Include examples that demonstrate library usage in real-world contexts.

### Rationale
Real-world scenarios are required to justify the library's features and show how they solve common development challenges.

Directives:
- Show how the library solves practical problems.
- Demonstrate integration with common systems or other libraries.
- Provide context for why a specific approach is recommended.

Example:

```python # pseudocode
# Real-world scenario: Caching expensive API calls
print("\nScenario: Caching expensive API calls")
api_client = APIClient()
cached_api = CachedAPIClient(api_client)

# First call (not cached)
print("First call (not cached):")
result1 = cached_api.get_data("endpoint1")

# Second call (cached)
print("\nSecond call (cached):")
result2 = cached_api.get_data("endpoint1")
```

### 4.4 Edge Cases

Include examples that demonstrate behavior under unusual conditions.

### Rationale
Edge case examples are required to document the library's robustness and guide users on correct error handling and boundary conditions.

Directives:
- Show behavior with unusual or invalid inputs.
- Demonstrate resource constraint management and performance considerations.

### 4.5 Implement Base Classes

Demonstrate the implementation of base classes to show extensibility.

### Rationale
Implementation examples are required to guide users on how to customize and extend the library for their specific needs.


## 5 Example Styles

Use diverse example styles to cater to different learning objectives.

### Rationale
A variety of styles is recommended to engage different types of learners and provide comprehensive coverage of the library's capabilities.

### 5.1 Cookbook Style

Provide practical, ready-to-use snippets for common tasks.

### Rationale
The cookbook style is recommended for its high utility and immediate value to developers looking for quick solutions.

Directives:
- Use problem-solution pairs.
- Include brief explanations of why the solution works.
- Focus on practical application.

```python # pseudocode
# Problem: How to efficiently filter a dictionary by value
# Solution:
data = {"a": 1, "b": 2, "c": 3, "d": 4}
filtered = {k: v for k, v in data.items() if v > 2}
expected = {'c': 3, 'd': 4}
print(f"Filtered dictionary: {filtered} == {expected}")  # Output: Filtered dictionary: {'c': 3, 'd': 4}
```

### 5.2 Compare and Contrast

Show multiple approaches to solving the same problem, highlighting trade-offs.

### Rationale
Comparing different implementations is required to help users understand the benefits and drawbacks of various techniques, such as readability versus performance.

Directives:
- Present at least two different implementations.
- Explain the advantages and disadvantages of each approach.
- Include performance considerations when relevant.

```python # pseudocode
# Approach 1: Using a for loop (more readable)
print("Approach 1: Using a for loop")
result1 = []
for item in data:
    if process_condition(item):
        result1.append(transform(item))
print(f"Result: {result1} == {expected_result1}")

# Approach 2: Using a list comprehension (more concise)
print("\nApproach 2: Using a list comprehension")
result2 = [transform(item) for item in data if process_condition(item)]
print(f"Result: {result2} == {expected_result2}")
```

### 5.3 Step-by-Step Transformation

Show the evolution of data through a series of operations.

### Rationale
Step-by-step demonstrations are recommended for complex processing pipelines to make each transformation clear and verifiable.

Directives:
- Start with initial data.
- Apply transformations one at a time.
- Show intermediate results after each step.

```python # pseudocode
# Initial data
data = [1, 2, 3, 4, 5]
print(f"Initial data: {data}")

# Step 1: Square each number
squared = [x**2 for x in data]
print(f"After squaring: {squared} == {expected_squared}")

# Step 2: Filter out values less than 10
filtered = [x for x in squared if x >= 10]
print(f"After filtering: {filtered} == {expected_filtered}")

# Step 3: Calculate the sum
total = sum(filtered)
print(f"Final result (sum): {total} == {expected_total}")
```

### 5.4 Annotated Examples

Provide code examples with detailed comments explaining each line or block.

### Rationale
Deeply annotated examples are required for complex patterns to explain the "why" behind the implementation choices.

Directives:
- Explain both the action and the rationale in comments.
- Highlight important concepts or patterns.
- Maintain a consistent comment style throughout.

```python # pseudocode
# Create a processor with caching capabilities
processor = DataProcessor(
    cache_enabled=True,  # Enable caching for better performance
    max_cache_size=100,  # Limit cache size to prevent memory issues
    ttl=3600  # Set time-to-live for cache entries (in seconds)
)

# Process data with automatic caching
# The first call will be slow as it computes the result
result1 = processor.process("example_key")
print(f"First call result: {result1} == {expected_result1}")

# The second call will be fast as it retrieves from cache
result2 = processor.process("example_key")
print(f"Second call result: {result2}  == {expected_result2}")
```

### 5.5 Interactive Examples

Create examples that encourage users to modify parameters and observe different outcomes.

### Rationale
Interactive elements are recommended to promote active learning and help users understand how different inputs affect system behavior.

Directives:
- Provide a working base example.
- Suggest specific modifications for the user to try.
- Explain the expected outcomes for those modifications.

```python # pseudocode
# Base example - try modifying the parameters!
def calculate_result(x, y, operation="add"):
    """Calculates the result based on operation.

    Try changing:
    - x and y to different numbers
    - operation to "subtract", "multiply", or "divide"
    """
    if operation == "add":
        return x + y
    elif operation == "subtract":
        return x - y
    elif operation == "multiply":
        return x * y
    elif operation == "divide":
        return x / y if y != 0 else "Error: Division by zero"

# Example usage
x, y = 10, 5
operation = "add"  # Try changing this!
result = calculate_result(x, y, operation)
print(f"{x} {operation} {y} = {result}")
```

### 5.6 Error-Driven Learning

Use examples to intentionally show common errors and their resolutions.

### Rationale
Showing incorrect code is recommended to help users recognize and avoid common pitfalls and to demonstrate effective debugging techniques.

Directives:
- Show the incorrect code first.
- Explain the error produced and why it occurs.
- Provide the corrected version.

```python # pseudocode
# NON-COMPLIANT: This will raise a KeyError
print("Non-compliant approach:")
try:
    data = {"a": 1, "b": 2}
    value = data["c"]  # KeyError: 'c'
    print(f"Value: {value}")
except KeyError as e:
    print(f"Error: {e}")

# COMPLIANT: Using get() method with a default value
print("\nCompliant approach:")
data = {"a": 1, "b": 2}
value = data.get("c", 0)  # Returns 0 if key doesn't exist
print(f"Value: {value}  == {expected_value1}")
```

### 5.7 Incremental Complexity

Start with a minimal example and gradually add features.

### Rationale
Building complexity incrementally is required to help users master individual concepts before combining them into a full solution.

Directives:
- Begin with the simplest possible implementation.
- Add features one at a time.
- Explain each addition and its specific purpose.

```python # pseudocode
# Stage 1: Basic implementation
print("Stage 1: Basic implementation")
cache = {}
result1 = cache.get("key", None)
if result1 is None:
    result1 = expensive_computation("key")
    cache["key"] = result1
print(f"Result: {result1} == {expected_result1}")

# Stage 2: Add timeout functionality
print("\nStage 2: Add timeout functionality")
cache_with_time = {}
current_time = time.time()
key = "example_key"
result2 = None

# Check if key exists and is not expired
if key in cache_with_time:
    timestamp, value = cache_with_time[key]
    if current_time - timestamp < 3600:  # 1 hour timeout
        result2 = value

# If not in cache or expired, compute and store
if result2 is None:
    result2 = expensive_computation(key)
    cache_with_time[key] = (current_time, result2)

print(f"Result: {result2} == {expected_result2}")
```

### 5.8 Visual Learning

Use ASCII art, tables, or other visual representations to illustrate concepts.

### Rationale
Visual aids are recommended for structural concepts, such as trees or network protocols, where spatial representation improves clarity.

Directives:
- Use visual elements to clarify complex relationships or structures.
- Ensure visuals are readable in monospace fonts.
- Include explanatory text alongside all visuals.

```python # pseudocode
# Example of a binary tree structure
"""
Binary Tree:
       A
     /   \
    B     C
   / \   / \
  D   E F   G

Traversal order:
- In-order: D, B, E, A, F, C, G
- Pre-order: A, B, D, E, C, F, G
- Post-order: D, E, B, F, G, C, A
"""

# Implementation of a simple binary tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Create the tree structure shown above
root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.left.left = Node("D")
root.left.right = Node("E")
root.right.left = Node("F")
root.right.right = Node("G")
```

### 5.9 Example Styles Conclusions

Choose the style or combination of styles that best suits the learning objective.

### Rationale
Matching the example style to the concept being taught is required to maximize educational effectiveness.

Directives:
- Use **Cookbook Style** for task-oriented learning.
- Use **Compare and Contrast** for critical thinking about implementation choices.
- Use **Step-by-Step Transformation** for data pipelines.
- Use **Annotated Examples** for deep dives into complex code.
- Use **Interactive Examples** for active experimentation.
- Use **Error-Driven Learning** for pitfall avoidance.
- Use **Incremental Complexity** for building full system understanding.
- Use **Visual Learning** for structural or spatial concepts.


## 6 Example-Specific Best Practices

Follow these best practices to ensure that examples are effective educational tools.

### Rationale
Adhering to best practices is required to maintain a high standard of quality and consistency across all library examples.

Directives:
- Prioritize educational clarity over absolute code optimization.
- Show both basic and advanced approaches when relevant.
- Use named constants instead of hardcoded values.
- Ensure examples are self-contained.
- Structure examples with progressive disclosure of complexity.
- Use existing tests as inspiration but do not copy them exactly.


## 7 Testing Examples

Test examples to ensure they remain accurate and functional.

### Rationale
Regular testing of examples is required to prevent documentation rot and ensure that demonstrations remain valid as the library evolves.

Directives:
- Run every example to verify it produces the expected output.
- Verify that examples work with all supported Python versions.
- Test examples against the latest version of the library.
- Include comments specifying expected output or behavior.

