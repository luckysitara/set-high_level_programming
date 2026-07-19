#!/usr/bin/python3
"""Defines MyInt class"""


class MyInt(int):
    """Defines an int with inverted == and != operators"""

    def __eq__(self, other):
        """Return the inverted equality comparison"""
        return int(self) != int(other)

    def __ne__(self, other):
        """Return the inverted inequality comparison"""
        return int(self) == int(other)
