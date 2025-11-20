"""function_template.py
A one-line summary of the module or program, terminated by a period.

Leave one blank line. The rest of this docstring should contain an overall description of the module or program. The
description can be broken up into multiple paragraphs to present the functionality into logical sections. Bullet-point
and numerical lists may be used as well, but only add them if they are needed.
"""

# Header #
__package_name__ = "package_name"

__author__ = "Author Name"
__credits__ = ["Author Name"]
__copyright__ = "Copyright 2021, Author Name"
__license__ = "License"

__version__ = "0.1.0"


# Imports #
# Standard Libraries #
from typing import Callable, Iterable

# Local Packages #
# from package_name.module import helper


# Definitions #
# Constants #
DEFAULT_NORMALIZE_STRIP: str = ""  # Characters to strip in normalization (empty means whitespace only)


# Functions #
# Decorators #
def require_iterable_of_str(func: Callable[[Iterable[str]], list[str]]) -> Callable[[Iterable[str]], list[str]]:
    """A decorator that validates the input is an iterable of strings.

    This decorator is intended to be placed before the functions it decorates, per the style guide.

    Args:
        func: The function to wrap. It must accept an Iterable[str] and return list[str].

    Returns:
        A wrapped function enforcing type checks at runtime.
    """

    def wrapper(names: Iterable[str]) -> list[str]:
        """Runtime type guard that enforces an iterable of str before calling func.

        Args:
            names: The incoming iterable to validate.

        Returns:
            The result of calling the wrapped function with a validated list[str].

        Raises:
            TypeError: If any element is not a str.
        """
        out: list[str] = []
        for n in names:
            if not isinstance(n, str):
                raise TypeError("all names must be str")
            out.append(n)
        # Pass a validated iterable (list[str]) to the function
        return func(out)

    return wrapper


# Normalization Functions #
@require_iterable_of_str
def normalize_names(names: Iterable[str]) -> list[str]:
    """Normalizes a sequence of names.

    Normalization currently consists of stripping leading/trailing whitespace (and optionally
    characters configured by DEFAULT_NORMALIZE_STRIP) and lower-casing each string. Order is preserved.

    Args:
        names: An iterable of raw names.

    Returns:
        A new list with names stripped and lower-cased, preserving order.
    """
    strip_chars = DEFAULT_NORMALIZE_STRIP or None  # None => whitespace-only strip
    return [n.strip(strip_chars).lower() for n in names]


def unique_normalized(names: Iterable[str]) -> list[str]:
    """Returns unique normalized names, preserving first‑occurrence order.

    This function demonstrates grouping of related functions by functionality.

    Args:
        names: An iterable of raw names.

    Returns:
        A list of unique normalized names in their first-seen order.
    """
    seen: set[str] = set()
    result: list[str] = []
    for name in normalize_names(names):
        if name not in seen:
            seen.add(name)
            result.append(name)
    return result
