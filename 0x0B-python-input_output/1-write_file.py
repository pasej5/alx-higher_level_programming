#!/usr/bin/python3
"""Function that writes a string to a text file (UTF-8) and returns the number of characters written."""


def write_file(filename="", text=""):
    """Writes a text file in UTF-8 and returns the number of characters written.

    Args:
        filename: The name of the file to write.
        text: The actual text to write to the file.

    Returns:
        The number of characters written to the file.
    """

    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(text)
        return len(text)
