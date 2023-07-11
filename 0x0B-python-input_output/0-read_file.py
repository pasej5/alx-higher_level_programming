#!/usr/bin/python3
"""Function that reads the text (UTF8) and prints it out to stdout:"""


def read_file(filename=""):
    """Function that reads a file"""

    with open(filename, encording='utf-8') as file:
        for line in file:
            print(line, end='')
