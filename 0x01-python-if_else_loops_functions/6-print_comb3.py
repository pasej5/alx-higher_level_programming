#!/usr/bin/python3

"""Write a program that prints all possible different
    combinations of two digits. """
for digit1 in range(0, 10):
    for second_digit in range(digit1 + 1, 10):
        if digit1 == 8 and second_digit == 9:
            print("{}{}".format(digit1, second_digit))
        else:
            print("{}{}".format(digit1, second_digit), end=", ")
