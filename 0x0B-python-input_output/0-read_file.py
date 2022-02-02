#!/usr/bin/python3
"""Write to a file"""


def read_file(filename=""):
    """Writes a string to a text file (UTF8) and returns
    the number of characters written"""
    with open(filename, "r", encoding="utf-8") as fo:
        txt = fo.read()
    print(txt, end="")
