#!/usr/bin/python3
"""Function that writes an object to a text file using JSON represantation"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file using JSON representation.

    Args:
        my_obj: The object to be saved to the file
        filename: The name of the file to write

    Return:
        None
    """

    with open(filename, mode='w') as file:
        json.dump(my_obj, file)
