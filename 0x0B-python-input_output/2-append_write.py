#!/usr/bin/python3
"""function that appends a string at the end of a text,
file utf-8and the returns the number of characters"""


def append_write(filename="", text=""):
    """Appends a text file to UTF-8

    Args:
        filename: the name of the file to write.
        text: the text to write to the file

    Return:
        The number of characters added.
    """

    with open(filename, mode='a', encoding='utf-8') as file
    file.write(text)
    return len(text)
