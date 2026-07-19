#!/usr/bin/python3
"""Defines a class with restricted instance attributes"""


class LockedClass:
    """Prevents dynamic creation of instance attributes,
    except for 'first_name'
    """
    __slots__ = ["first_name"]
