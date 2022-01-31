#!/usr/bin/python3
"""Full rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle that inherits from BaseGeometry
    (7-base_geometry.py)."""

    def __init__(self, width, height):
        """Instantiation with width and height"""
        BaseGeometry.integer_validator(self, "width", width)
        self.__width = width
        BaseGeometry.integer_validator(self, "height", height)
        self.__height = height

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return informal string representation of the rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
