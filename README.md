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

### iterutils.map_nested(v, f) ###

Recursivly applies a function `f` over a nested data structure `v`

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

### listutils.chunk(l, n) ###

Generator that splits a list into n-sized chunks

Code taken from: https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks

## Bitfield ##

A module for dealing with bitfields

### class bitfield.Bitfield([value])

Represents a bitfield. This class functions as if the data is little-endian -- that is, the least significant bit is the first one.

An inital value for Bitfield may be passed to the constructor. If none is recieved, the value is 0.

Bitfield supports all binary arithmetic operations: `&`, `^`, `|`, `>>`, `<<`.

Getting bits in a Bitfield is done with the [] operator. When getting bits, if an index is passed, an integer of either 0 or 1 is returned. If a slice is passed, a new Bitfield object holding the selected bits is returned.

```python
>>> b = Bitfield(0b100101)
>>> b[2]
1
>>> b[2:]
Bitfield 0b1001
>>> b[:2]
Bitfield 0b1
```

Bitfield is iterable. Each bit is a seperator item. It's length is the number of all bits up until the highest set bit.

```python
>>> b = Bitfield(1)
>>> b << 10
Bitfield 0b10000000000
>>> len(b << 10)
11
>>> list(b << 10)
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
```