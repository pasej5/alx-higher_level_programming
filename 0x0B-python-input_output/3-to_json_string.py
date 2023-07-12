#!/usr/bin/python3
"""Function that returns the JSON represantation of an object(string)"""
import json


def to_json_string(my_obj):
    """Function that returns the represantation of an bject string.

    Args:
        my_obj: My object

    Returns:
        returns the JSON representation of an object (string)
    """

    return json.dumps(my_obj)
