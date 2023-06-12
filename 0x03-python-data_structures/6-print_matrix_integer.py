#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    """function that prints a matrix of integers"""
    for row in matrix:
        formated_row = ' '.join([str(num) for num in row ])
        print(formated_row)
