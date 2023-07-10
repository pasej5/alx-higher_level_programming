#!/usr/bin/python3
"""Defining an object attribute look up function"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.
    """
    return dir(obj)
