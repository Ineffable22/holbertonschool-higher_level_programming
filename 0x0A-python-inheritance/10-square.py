#!/usr/bin/python3
"""Square #1"""
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
