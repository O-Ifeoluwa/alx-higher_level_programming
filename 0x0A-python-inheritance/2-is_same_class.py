#!/usr/bin/python3
"""returns True if the object is exactly an instance of the specified class, otherwise false"""


def is_same_class(obj, a_class):
    """exact same object"""
    return type(obj) == a_class
