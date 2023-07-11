#!/usr/bin/python3
"""Function that writes string to a text file(utf-8)"""


def write_file(filename="", text=""):
    """Writes a text and returns the number of char"""

    def write_file(filename="", text=""):
        with open(filename, mode='w', encoding='utf-8') as file:
            file.write(text)
            return len(text)
