#!/usr/bin/python3
"""Function that writes string to a text file(utf-8)"""


def write_file(filename="", text=""):
    """Writes a text file utf-8 and returns the number of char.

    Args:
        filename: The name of the file to write.
        text: The actual text to write to file
        """

        with open(filename, mode='w', encoding='utf-8') as file:
            file.write(text)
            return len(text)
