"""Useful function decorators"""
from typing import Callable, Optional


def enforce_state(property_name: str, expected_value):
    """
    A decorator meant for class member functions. On calling a member, it
    will first check if the given property matches the given value. If it
    does not, a value error will be thrown.
    """
    def dec(func: Callable):
        def wrapper(self, *args, **kwargs):
            actual_value = vars(self)[property_name]

            if actual_value != expected_value:
                err = "Cannot call {fname}(), {vname} is {val}! (Expected: {exp})".format(
                    fname=func.__name__, vname=property_name, val=actual_value, exp=expected_value
                )
                raise ValueError(err)
            else:
                return func(self, *args, **kwargs)

        return wrapper
    return dec
