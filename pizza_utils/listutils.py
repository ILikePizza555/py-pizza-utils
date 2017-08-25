"""
A collection of utilities for working with lists
"""


def split(l, i):
    """Splits a list at the given index. Returns a tuple containing two lists."""

    return l[:i], l[i:]


def chunk(l, n):
    """
    Generator that splits a list into n-sized chunks

    Code taken from: https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks
    """
    for i in range(0, len(l), n):
        yield l[i: i+n]