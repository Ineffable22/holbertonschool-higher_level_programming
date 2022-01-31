#!/usr/bin/python3
"""Square #2"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle (9-rectangle.py):"""
    def __init__(self, size):
        """Instantiation with size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Return the informal string representation of the square"""
        return "[Square] {0}/{0}".format(self.__size)
