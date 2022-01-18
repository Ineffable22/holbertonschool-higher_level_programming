#!/usr/bin/python3
"""Class Square"""


class Square:
    """Defines a square
    Private instance attribute: size
    Instantiation with size (no type/value verification)
    """
    def __init__(self, size):
        """Initialize the data"""
        self.__size = size
