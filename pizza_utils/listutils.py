"""
A collection of utilities for working with lists
"""


def split(l, i):
    """Splits a list at the given index. Returns a tuple containing two lists."""

    return l[:i], l[i:]
