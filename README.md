# py-pizza-utils #
My personal python utilities

# Testing #

All tests are located in the tests/ directory and use the unittest module

# Installation #

`pip install git+https://github.com/ILikePizza555/py-pizza-utils`

# Documentation #

Currently, the library is small enough to make the docs all one file

## Iterutils ##

A collection of utilities for iteration

### iterutils.sliding(iterable, size, fillvalue=None) ###

Creates a sliding iterator of size `size` for the given `iterable`. `fillvalue` specifies the value to return when the iterable runs out of items.

## Stringutils ##

### stringutils.find_from(string, subs, [start, [end]]) ###

Returns a tuple of the lowest index where a substring for `string` in the iterable `subs` was found, and the metioned substring.
If multiple substrings are found, it will return the first one.
If nothing is found, it will return (-1, None)

`start` and `end` follows the python slice notation

```
>>> find_from("abcd", ("d", "c", "b", "a"))
(0, "a")
```

## Listutils ##

### listutils.split(l, index) ###

Splits a list at the given index. Returns a tuple containing two lists.