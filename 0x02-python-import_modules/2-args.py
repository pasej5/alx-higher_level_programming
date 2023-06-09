#!/usr/bin/python3

import sys
""" program that prints the number of and the list of its arguments."""

if __name__ == "__main__":

    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    for number in range(count):
        print("{}: {}".format(number + 1, sys.argv[number + 1]))
