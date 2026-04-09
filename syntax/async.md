# Anthony's Python Style Guide: Asynchronous Programming

Use asynchronous programming, primarily with `asyncio`, to enable concurrent execution through an event loop.

### Rationale
Clear and robust async code is required to manage I/O-bound tasks efficiently and prevent common pitfalls like blocking the event loop.

## Table of Contents

- [1 General Guidelines](#1-general-guidelines)
- [2 Timeouts and Deadlines](#2-timeouts-and-deadlines)


## 1 General Guidelines

### Rationale
Maintaining a non-blocking event loop is required for the performance and responsiveness of asynchronous applications.

Directives:
- Use `asyncio` for I/O-bound tasks.
- Do not block the event loop. CPU-bound tasks and blocking I/O calls (e.g., `time.sleep()`) must not be performed within `async` functions. Use `asyncio.to_thread()` or separate processes instead.
- Prefer `async with` and `async for` to ensure resources are managed correctly and concurrently.


## 2 Timeouts and Deadlines

Avoid defining timeouts within function signatures.

### Rationale
Allowing the caller to manage timeouts is required to enable flexible composition of asynchronous operations and to support global deadline logic.

Directives:
- Do not define `timeout` parameters in async functions that perform I/O.
- Let the caller manage timeouts using `asyncio.timeout()` or `asyncio.wait_for()`.

Compliant:
```python # pseudocode
import asyncio

async def fetch_data(url: str) -> dict:
    # Function focus is on fetching, not timeout management
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def main():
    try:
        # Caller manages the timeout
        async with asyncio.timeout(5.0):
            data = await fetch_data("https://api.example.com/data")
    except TimeoutError:
        print("The request timed out.")
```

Non-Compliant:
```python # pseudocode
import asyncio

async def fetch_data(url: str, timeout: float = 10.0) -> dict:
    # PROBLEM: The timeout is hardcoded into the function's signature
    try:
        return await asyncio.wait_for(do_fetch(url), timeout=timeout)
    except asyncio.TimeoutError:
        raise
```
