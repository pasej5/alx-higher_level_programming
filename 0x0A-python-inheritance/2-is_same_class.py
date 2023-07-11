#!/usr/bin/python3
"""True if the object is exactly an instance"""


def is_same_class(obj, a_class):
    """
    Checks if the object is exactly an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True or False.
    """
    return type(obj) == a_class
