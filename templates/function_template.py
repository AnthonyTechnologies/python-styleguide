"""Paste‑ready function template using Google‑style docstring sections."""

from __future__ import annotations

from typing import Iterable, List

__all__ = [
    # "normalize_names",
]


def normalize_names(names: Iterable[str]) -> List[str]:
    """Normalize a sequence of names.

    Args:
        names: An iterable of raw names.

    Returns:
        A new list with names stripped and lower‑cased, preserving order.

    Raises:
        TypeError: If any item is not a string.
    """
    out: List[str] = []
    for n in names:
        if not isinstance(n, str):
            raise TypeError("all names must be str")
        out.append(n.strip().lower())
    return out
