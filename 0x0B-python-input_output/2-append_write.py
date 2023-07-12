#!/usr/bin/python3
"""Function that appends a string at the end of a text file
(UTF-8) and returns the number of characters added."""


def append_write(filename="", text=""):
    """Appends a string to a text file (UTF-8) and
    returns the number of characters added.

    Args:
        filename: The name of the file to write.
        text: The text to append to the file.

    Returns:
        The number of characters added.
    """

    with open(filename, mode='a', encoding='utf-8') as file:
        file.write(text)
        return len(text)
