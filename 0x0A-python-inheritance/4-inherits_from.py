#!/usr/bin/python3
"""Rturns True or false if the object ids an instance"""


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class that
    inherited (directly or indirectly) from
    the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of a class
        that inherited (directly or indirectly) from
        the specified class; False otherwise.
    """
    if issubclass(type(obj),a_class) and type(obj) != a_class):
        return True
    return False
