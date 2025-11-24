"""class_template.py
Template module demonstrating the structure and style of a class definition.

This module provides a template for defining classes, including attributes, methods, properties, and magic methods.
It demonstrates the organization of class members and the use of type hints in accordance with the project's style guide.
Normally, the name of this module should match the name of the class it contains, but it is named after class_template
to make it easier to find when browsing the templates directory.
"""

# Header #
__package_name__ = "package_template"

__author__ = "Author Name"
__credits__ = ["Author Name"]
__copyright__ = "Copyright 2021, Author Name"
__license__ = "License"

__version__ = "0.1.0"


# Imports #
# Standard Libraries #
from typing import ClassVar, Any


# Definitions #
# Classes #
class User:
    """Represents a user in the system.

    Attributes:
        user_id: Stable identifier.
        name: Display name.
        active: Whether the user is active.
    """

    # Static Methods #
    @staticmethod
    def create_from_data(data: dict[str, Any]) -> "User":
        """Creates a User from a simple data dictionary.

        Args:
            data: Dictionary containing keys like 'user_id', 'name', and optional 'active'.

        Returns:
            A new User instance.
        """
        return User(
            user_id=str(data.get("user_id", "anonymous")),
            name=str(data.get("name", "Anonymous")),
            active=bool(data.get("active", True)),
        )

    # Class Attributes #
    anonymous_id: ClassVar[str] = "anonymous"
    _default_active: ClassVar[bool] = True

    # Class Magic Methods #
    def __new__(cls, *args: Any, **kwargs: Any):
        """Allocates a new User instance (rarely overridden; shown for template completeness)."""
        return super().__new__(cls)

    # Class Methods #
    # Constructors
    @classmethod
    def anonymous(cls) -> "User":
        """Creates an anonymous user instance."""
        return cls(user_id=cls.anonymous_id, name="Anonymous", active=False)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "User":
        """Constructs a User from a dictionary.

        Args:
            data: Dictionary with keys 'user_id', 'name', and optional 'active'.

        Returns:
            A new User instance.
        """
        return cls(
            user_id=str(data["user_id"]),
            name=str(data["name"]),
            active=bool(data.get("active", cls._default_active)),
        )

    # Attributes #
    user_id: str
    name: str
    active: bool = True

    # Properties #
    @property
    def is_anonymous(self) -> bool:
        """Whether this user is anonymous."""
        return self.user_id == self.anonymous_id

    # Magic Methods #
    # Construction/Destruction
    def __init__(self, user_id: str, name: str, active: bool = True) -> None:
        """Initializes a User instance.

        Args:
            user_id: Stable identifier.
            name: Display name.
            active: Whether the user is active.
        """
        # Attributes are assigned directly to keep the example simple
        self.user_id = user_id
        self.name = name
        self.active = active

    def __copy__(self) -> "User":
        """Returns a shallow copy of this user."""
        return User(user_id=self.user_id, name=self.name, active=self.active)

    # Representation
    def __str__(self) -> str:  # keep lightweight for logging/debugging
        """Returns a concise, human-readable string representation."""
        return f"User(id={self.user_id!r}, name={self.name!r}, active={self.active})"

    def __repr__(self) -> str:
        """Returns an unambiguous representation for debugging."""
        return (
            f"{self.__class__.__name__}(user_id={self.user_id!r}, name={self.name!r}, active={self.active!r})"
        )

    # Comparison
    def __eq__(self, other: Any) -> bool:
        """Compares users by stable identifier."""
        if not isinstance(other, User):
            return NotImplemented
        return self.user_id == other.user_id

    # Type Conversion
    def __bool__(self) -> bool:
        """A user is truthy when active."""
        return self.active

    # Instance Methods #
    # Constructors/Destructors
    def construct(self, *, activate: bool | None = None) -> None:
        """Adjusts state optionally after construction.

        Args:
            activate: If provided, overrides the active state after construction.
        """
        if activate is not None:
            self.active = bool(activate)

    # Validation
    def _ensure_active(self) -> None:
        """Ensures the user is active before allowing state changes.

        Raises:
            RuntimeError: If the user is inactive.
        """
        if not self.active:
            raise RuntimeError("User is not active")

    # Parameter Parsers
    def _parse_activation(self, value: Any) -> bool:
        """Parses an arbitrary value into an activation boolean.

        This helper demonstrates the Parameter Parsers subcategory.
        
        Args:
            value: The value to parse.
        """
        if isinstance(value, str):
            return value.strip().lower() in {"1", "true", "yes", "on"}
        return bool(value)

    # Operations
    def deactivate(self) -> None:
        """Deactivates this user."""
        self.active = False

    # Conversion
    def to_dict(self) -> dict[str, Any]:
        """Converts this user to a simple dictionary."""
        return {"user_id": self.user_id, "name": self.name, "active": self.active}

    # Getters and Setters #
    def get_display_name(self) -> str:
        """Returns the current display name, applying any formatting rules if needed."""
        return self.name

    def set_display_name(self, name: str) -> None:
        """Sets the display name with minimal validation.

        Prefer using setters only when non-trivial logic is required; shown here for template completeness.
        
        Args:
            name: The new display name.
        """
        self._ensure_active()
        self.name = name.strip() if name else self.name
