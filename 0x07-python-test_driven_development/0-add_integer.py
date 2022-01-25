#!/usr/bin/python3
"""
Integers addition
Adds 2 integers
otherwise raise a TypeError
"""


def add_integer(a, b=98):
    """Adds 2 integers
    a and b must be integers or floats
    Returns an integer: the addition of a and b"""
    if type(a) is not int and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
