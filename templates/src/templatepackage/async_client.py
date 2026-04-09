"""async_client.py
Template module demonstrating asynchronous programming patterns.

This module provides a template for an asynchronous client, demonstrating the use of `asyncio`, `async with` for context
management, and caller-managed timeouts.
"""

# Header #
__package_name__ = "templatepackage"

__author__ = "Author Name"
__credits__ = ["Author Name"]
__copyright__ = "Copyright 2026, Author Name"
__license__ = "License"

__version__ = "0.1.0"


# Imports #
# Standard Libraries #
import asyncio
from collections.abc import AsyncIterator
from typing import Any


# Definitions #
# Classes #
class MockAsyncClient:
    """A mock asynchronous client.

    This class demonstrates how to implement an async context manager and perform non-blocking operations.

    Attributes:
        base_url: The base URL for the mock API.
        is_connected: Whether the client is currently connected.
    """

    # Magic Methods #
    # Construction/Destruction
    def __init__(self, base_url: str) -> None:
        """Initializes the MockAsyncClient.

        Args:
            base_url: The base URL.
        """
        self.base_url: str = base_url
        self.is_connected: bool = False

    # Context Management
    async def __aenter__(self) -> "MockAsyncClient":
        """Connects the client when entering the `async with` block.

        Returns:
            MockAsyncClient: The connected client instance.
        """
        await self.connect()
        return self

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        """Disconnects the client when exiting the `async with` block.

        Args:
            exc_type: Exception type.
            exc_val: Exception value.
            exc_tb: Exception traceback.
        """
        await self.disconnect()

    # Instance Methods #
    # Connection Operations
    async def connect(self) -> None:
        """Simulates connecting to a remote service."""
        await asyncio.sleep(0.1)  # Simulate I/O latency
        self.is_connected = True

    async def disconnect(self) -> None:
        """Simulates disconnecting from a remote service."""
        await asyncio.sleep(0.05)  # Simulate I/O latency
        self.is_connected = False

    # Data Operations
    async def fetch_resource(self, resource_id: str) -> dict[str, Any]:
        """Fetches a mock resource.

        This method does NOT manage its own timeouts, per the style guide. Callers should use `asyncio.timeout()`.

        Args:
            resource_id: The identifier of the resource to fetch.

        Returns:
            dict[str, Any]: The mock resource data.

        Raises:
            RuntimeError: If the client is not connected.
        """
        if not self.is_connected:
            msg = "Client must be connected before fetching resources"
            raise RuntimeError(msg)

        await asyncio.sleep(0.2)  # Simulate I/O latency
        return {"id": resource_id, "data": "mock_value", "status": "success"}

    async def stream_resources(self) -> AsyncIterator[str]:
        """Simulates streaming resources using an async generator.

        Yields:
            str: Resource identifiers.
        """
        for i in range(3):
            await asyncio.sleep(0.1)
            yield f"resource_{i}"


# Main #
async def main() -> None:
    """Demonstrates how to use the MockAsyncClient with caller-managed timeouts."""
    client = MockAsyncClient("https://api.example.com")

    try:
        # Caller-managed timeout using asyncio.timeout (Python 3.11+)
        async with asyncio.timeout(1.0):
            async with client as connected_client:
                data = await connected_client.fetch_resource("item_123")
                print(f"Fetched: {data}")

                async for item in connected_client.stream_resources():
                    print(f"Streamed: {item}")
    except TimeoutError:
        print("The operation timed out.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    asyncio.run(main())
