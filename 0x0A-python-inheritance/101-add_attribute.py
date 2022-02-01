#!/usr/bin/python3
"""Adds a new attribute to an object if it’s possible"""


def add_attribute(obj, att, value):
    """
    Adds a new attribute
    obj: The class
    att: Name of the attribute
    value: Value of the attribute
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, att, value)
        return
    raise TypeError("can't add new attribute")
