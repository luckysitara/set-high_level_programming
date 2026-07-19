#!/usr/bin/python3
"""A class representing a magical circle with radius."""
class MagicClass:


    def __init__(self, radius):
        """Initialize a MagicClass instance with a given radius.:param radius: The radius of the circle."""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculate the area of the circle.Formula: A = π * r^2"""
        return self.__radius * self.__radius * 3.14

    def circumference(self):
        """Calculate the circumference of the circle Formula: C = 2 * π * """
        return 2 * 3.14 * self.__radius
