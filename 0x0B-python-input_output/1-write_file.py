#!/usr/bin/python3
"""Write to a file"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns
    the number of characters written"""
    with open(filename, "w", encoding="utf-8") as fo:
        return fo.write(text)
