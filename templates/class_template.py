"""Paste‑ready class template.

Guidance:
- Keep attributes documented in the class docstring.
- Order: dunder/magic, constructors, classmethods, properties, public methods, private helpers, dunder hooks.
"""

from __future__ import annotations

from dataclasses import dataclass

__all__ = [
    # "User",
]


@dataclass(slots=True)
class User:
    """Represents a user in the system.

    Attributes:
        user_id: Stable identifier.
        name: Display name.
        active: Whether the user is active.
    """

    user_id: str
    name: str
    active: bool = True

    # ---- Constructors ----
    @classmethod
    def anonymous(cls) -> "User":
        """Create an anonymous user instance."""
        return cls(user_id="anonymous", name="Anonymous", active=False)

    # ---- Properties ----
    @property
    def is_anonymous(self) -> bool:
        """Whether this user is anonymous."""
        return self.user_id == "anonymous"

    # ---- Public Methods ----
    def deactivate(self) -> None:
        """Deactivate this user."""
        self.active = False

    # ---- Private Helpers ----
    def _ensure_active(self) -> None:
        if not self.active:
            raise RuntimeError("User is not active")

    # ---- Dunder Hooks ----
    def __str__(self) -> str:  # keep lightweight for logging/debugging
        return f"User(id={self.user_id!r}, name={self.name!r}, active={self.active})"
