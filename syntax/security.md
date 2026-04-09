# Anthony's Python Style Guide: Security

Use secure programming practices to protect systems and data from common vulnerabilities.

### Rationale
Maintaining high security standards is required to prevent data breaches, system compromises, and other malicious activities.

## Table of Contents

- [1 General Security Practices](#1-general-security-practices)
- [2 Restricted Operations](#2-restricted-operations)


## 1 General Security Practices

### Rationale
These practices are required to mitigate the most common security risks in software development.

Directives:
- Validate all input. Data from external sources (e.g., users, APIs, files) must be validated against expected types, ranges, and formats.
- Avoid shell execution. Do not use `os.system()` or `subprocess.run(shell=True)` with untrusted input to prevent shell injection attacks.
- Keep secrets out of the source code. API keys, passwords, and tokens must not be hardcoded. Use environment variables or a dedicated secret management system instead.


## 2 Restricted Operations

### 2.1 Assert Statements

Do not use `assert` statements for security validation or logic control in production code.

### Rationale
The `assert` statement is required to be limited to internal self-checks and debugging because it is disabled when Python is run with optimizations (e.g., `python -O`). Using it for production logic can result in security checks being skipped entirely.

Directives:
- Use explicit `if` checks and raise exceptions for production logic.
- Limit `assert` to tests and non-critical development checks.

Compliant:
```python # pseudocode
def process_data(data: dict):
    # Explicit validation for production logic
    if "id" not in data:
        msg = "Missing 'id' in data"
        raise ValueError(msg)
    # ...
```

Non-Compliant:
```python # pseudocode
def process_data(data: dict):
    # PROBLEM: This check will be skipped if Python is run with optimizations
    assert "id" in data, "Missing 'id' in data"
    # ...
```

### 2.2 Insecure Serialization

Avoid the `pickle` module for untrusted data.

### Rationale
The `pickle` module is recommended only for internal, trusted data because it is inherently insecure and can lead to arbitrary code execution when deserializing malicious payloads.

Directives:
- Use safer alternatives like `json`, `msgpack`, or `tomllib` for data interchange.
- Ensure the source is fully trusted if `pickle` must be used.
