#!/usr/bin/python3
"""Class Square"""


class Square:
    """Defines a square
    Private instance attribute: size:
    property def size(self): to retrieve it
    property setter def size(self, value): to set it:
    size must be an integer, otherwise raise a TypeError exception
    with the message size must be an integer
    if size is less than 0, raise a ValueError exception with the
    message size must be >= 0
    Instantiation with optional size: def __init__(self, size=0):
    Public instance method: def area(self): that returns the current
    square area
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initilizes the data"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Retrieves the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size to a value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position to a value."""
        if len(value) < 2 or not isinstance(value, int):
            raise TypeError("size must be an integer")
        self.__position = value

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character #:
        at the position given by the position attribute.
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.position[1]):
                print()
            for j in range(0, self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
