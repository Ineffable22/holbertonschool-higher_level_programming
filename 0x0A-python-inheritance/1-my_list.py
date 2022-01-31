#!/usr/bin/python3
"""My list"""


class MyList(list):
    """inherits from list"""
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """Prints the list, but sorted"""
        print(sorted(self))
