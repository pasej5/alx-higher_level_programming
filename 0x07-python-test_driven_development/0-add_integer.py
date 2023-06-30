#!/usr/bin/python3
"""function that adds 2 integers"""


def add_integers(a, b=98):
    """ param a: integer a
        param b: integer b with default value of b
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    return a + b
