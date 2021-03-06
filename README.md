# py-pizza-utils #
My personal python utilities

# Testing #

All tests are located in the tests/ directory and use the unittest module

# Installation #

`pip install git+https://github.com/ILikePizza555/py-pizza-utils`

# Documentation #

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

```python
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

An inital value for `Bitfield` may be passed to the constructor. If none is recieved, the value is 0.

`Bitfield` supports all binary arithmetic operations: `&`, `^`, `|`, `>>`, `<<`.

Getting bits in a `Bitfield` is done with the `[]` operator. When getting bits, if an index is passed, an integer of either 0 or 1 is returned. If a slice is passed, a new `Bitfield` object holding the selected bits is returned.

```python
>>> b = Bitfield(0b100101)
>>> b[2]
1
>>> b[2:]
Bitfield 0b1001
>>> b[:2]
Bitfield 0b1
```

Setting bits in a `Bitfield` is done in a similar manner to lists.

```python
>>> b = Bitfield(0b100101)
>>> b[3] = 1
>>> b
Bitfield 0b101101
```

`Bitfield` is iterable. Each bit is a seperator item. It's length is the number of all bits up until the highest set bit.

```python
>>> b = Bitfield(1)
>>> b << 10
Bitfield 0b10000000000
>>> len(b << 10)
11
>>> list(b << 10)
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
```

It is important to note that the length of a bitfield is an implementation detail. Accessing a bit greather than it's Bitfield's length will return 0. Setting a bit greather than it's Bitfield's length will increase the size of the bitfield. *Accessing or setting bits using a negative index is untested and unsupported.*

## Decs ##

A collection of function decorators.

### decs.enforce_state(property_name, expected_value) ###

A decorator for class member functions. 

If the given class property is not equivalent to the expected value when calling the class member, a ValueError will be thrown.

#### Example ###

Consider the class:

```python
class Test:
    def __init__(self):
        self.state = 0
        
    @decs.enforce_state("state", 5)
    def member(self):
        pass
```

Attempting to call member in this state will result in an error:

```
>>> a = Test()
>>> a.member()
[...]
ValueError: Cannot call member(), state is 0! (Expected: 5)
```