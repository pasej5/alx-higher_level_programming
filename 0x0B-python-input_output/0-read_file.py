#!/usr/bin/python3
"""Function that read and prints it out to stdout:"""


def read_file(filename=""):
    """reads and write a file to uft-8"""

    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
