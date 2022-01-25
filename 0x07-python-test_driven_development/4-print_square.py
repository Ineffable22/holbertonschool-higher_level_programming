#!/usr/bin/python3
"""Print square"""


def print_square(size):
    """
    Prints a square with the character #
    size length of the square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and type(size) < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)
