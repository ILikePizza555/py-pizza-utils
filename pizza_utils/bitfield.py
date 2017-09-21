"""
A module for dealing with bitfields
"""
import math
from typing import Optional


class Bitfield():
    """
    Represents a bitfield of an arbirary size.

    Bitfields are little-endian.
    """
    def __init__(self, value: Optional[int] = 0):
        """
        Creates a bitfield with an optional given value. This value should be
        a integer representation of the bitfield.
        """
        self._value = value

    def __eq__(self, o):
        if isinstance(o, Bitfield):
            return self._value == o._value

        if type(o) == int:
            return self._value == o

        if type(o) == bytes:
            return self._value == sum(o)

        return NotImplemented

    def __lshift__(self, o):
        if type(o) != int:
            return NotImplemented

        self._value << o

    def __rshift__(self, o):
        if type(o) != int:
            return NotImplemented

        self._value >> o

    def __and__(self, o):
        if type(o) != int:
            return NotImplemented

        self._value & o

    def __xor__(self, o):
        if type(o) != int:
            return NotImplemented

        self._value ^ o

    def __or__(self, o):
        if type(o) != int:
            return NotImplemented

        self._value | o

    def __repr__(self):
        return "Bitfield " + bin(self._value)

    def __bytes__(self):
        return bytes([self._value])

    def __len__(self):
        """
        Returns the number of bits in this bitfield, which is the highest set 
        bit
        """
        return math.floor(math.log2(self._value)) + 1

    def __iter__(self):
        for i in range(0, len(self)):
            yield self[i]

    def __getitem__(self, key):
        """
        Returns the bit at the given index.

        If a slice is given instead, it will return a new bitfield of the
        sliced bits.
        """
        if type(key) == int:
            return max(0, min(1, self._value & 2**key))
        elif isinstance(key, slice):
            start = key.start if key.start is not None else 0
            stop = key.stop if key.stop is not None else len(self)
            step = key.step if key.step is not None else 1

            mask = sum([2**n for n in range(start, stop, step)])
            return Bitfield((self._value & mask) >> start)
        else:
            raise TypeError()

    def __setitem__(self, key, value):
        if type(key) != int:
            raise TypeError()

        mask = 2**key

        if value > 0:
            self._value = self._value | mask
        else:
            self._value = self._value & ~(mask)
