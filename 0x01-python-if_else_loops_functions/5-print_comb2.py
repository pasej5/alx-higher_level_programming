#!/usr/bin/python3
"""program that prints numbers from 0 to 9"""

for number in range(0, 100):
    if number == 99:
        print("{}".format(number))
    else:
        print("{:02}".format(number), end=", ")
