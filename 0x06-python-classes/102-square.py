#!/usr/bin/python3
"""Class Square"""


class Square:
    """Defines a square
    Private instance attribute: size:
    property def size(self): to retrieve it
    property setter def size(self, value): to set it:
    size must be a number (float or integer), otherwise raise
    a TypeError exception with the message size must be a number
    if size is less than 0, raise a ValueError exception with the
    message size must be >= 0
    Instantiation with size: def __init__(self, size=0):
    Public instance method: def area(self): that returns the current
    square area
    Square instance can answer to comparators: ==, !=, >, >=, < and
    <= based on the square area
    """
    def __init__(self, size=0):
        """Initilizes the data"""
        self.__size = size

    def __lt__(self, other):
        """Describes less than operator(<)"""
        return self.area() < other.area()

    def __le__(self, other):
        """Descries less than or equal to (<=)"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Describes greater than (>)"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Describes greater than or equal to (>=)"""
        return self.area() >= other.area()

    def __eq__(self, other):
        """Describes equality operator(==)"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Describes not equal to operator(!=)"""
        return self.area() != other.area()

    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int) or not isinstance(value, float):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.size ** 2
