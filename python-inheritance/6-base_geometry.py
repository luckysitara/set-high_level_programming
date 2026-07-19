#!/usr/bin/python3
"""Defines BaseGeometry class"""


class BaseGeometry:
    """Base geometry class"""

    def area(self):
        """Raise an exception since area is not implemented"""
        raise Exception("area() is not implemented")
