#!/usr/bin/python3

def fizzbuzz():
    """For multiples of three print Fizz
    for multiples of five print Buzz.
    multiples of both three and five print FizzBuzz
    """
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(number), end="")
