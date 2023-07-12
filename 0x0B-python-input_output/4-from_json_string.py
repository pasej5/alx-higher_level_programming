#!/usr/bin/python3
"""Function that returns a Python data structure by JSON string"""
import json


def from_json_string(my_str):
    """Returns the Python data structure by JSON string

    Args:
        my_str: The object to be converted to JSON.

    Returns:
        The JSON python data structure.
    """

    return json.loads(my_str)

