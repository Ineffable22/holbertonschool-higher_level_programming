#!/usr/bin/python3
"""Rectangle"""
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
