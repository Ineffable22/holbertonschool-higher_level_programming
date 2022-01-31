#!/usr/bin/python3
"""My integer"""


class MyInt(int):
    """Class MyInt that inherits from int"""

    def __eq__(self, other):
        """Swap logic with __ne__"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Swap logic __eq__"""
        return super().__eq__(other)
