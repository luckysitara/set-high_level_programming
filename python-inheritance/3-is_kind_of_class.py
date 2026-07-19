#!/usr/bin/python3
"""Defines is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """Check if obj is an instance of a_class or a subclass of it"""
    return isinstance(obj, a_class)
