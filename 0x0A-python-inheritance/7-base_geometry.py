#!/usr/bin/python3
"""Integer validator"""


class BaseGeometry:
    """Class BaseGeometry (based on 6-base_geometry.py)."""

    def area(self):
        """Public instance method: that raises an Exception
        with the message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method: that validates value"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
