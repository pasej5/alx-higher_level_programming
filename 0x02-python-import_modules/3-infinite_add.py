#!/usr/bin/python3

import sys
"""result of the addition of all arguments"""

if __name__ == "__main__":


    total = 0
    for i in range(len(sys.argv) - 1):
        total += int(sys.argv[i + 1])
    print("{}".format(total))
