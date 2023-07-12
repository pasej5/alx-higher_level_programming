#!/usr/bin/python3
"""Function that creates an object from a JSON file"""
import json


def load_from_json_file(filename):
    """Creates ab object from a JSON file.

    Args:
        filename: The name of the JSON file t load

    Return:
        The object loaded from the JSON file.
    """

    with open(filename) as file:
        return json.load(file)
