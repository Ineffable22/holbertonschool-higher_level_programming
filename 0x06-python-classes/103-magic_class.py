#!/usr/bin/python3
import math


class MagicClass:
    """Class MagicClass
    """
    def __init__(self, radius):
        """Initializes Data"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self, radius):
        """Get area"""
        return (self.__radius ** 2) * math.pi

    def circumference(self, radius):
        """Get Circumference"""
        return 2 * math.pi * self.__radius
