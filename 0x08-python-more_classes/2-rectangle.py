#!/usr/bin/python3
"""String representation"""


class Rectangle:
    """Defines a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize the data"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Retrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width to a value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the position"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height to a value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the current rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the current rectangle perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2