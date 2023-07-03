#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    Args:
        matrix (list): A matrix represented as a list of lists of integers or floats.
        div (number): The divisor.

    Returns:
        list: A new matrix with all elements divided by the divisor, rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix is not a matrix (list of lists) of integers/floats,
                   or if each row of the matrix does not have the same size,
                   or if the divisor is not a number.
        ZeroDivisionError: If the divisor is zero.
    """
    # Check if matrix is a list of lists
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row has the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform division and round the result to 2 decimal places
    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]

    return new_matrix

