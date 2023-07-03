#!/usr/bin/python3
def matrix_devided(matrix, div):
    """
    Devides all elements of a matrix by a devisor.

    Args: 
        matrix (list): A matrix represented aa a list of listsof integers or floats.
        div (number): The divisor.

    Returns:
        list: a new matrix with all elements divided by the divisor, rounded by 2 decimal places

    Raises:
        TypeError: if the matrix is not a matrix (lists of lists) of integers/floats,
                    or if each row of the matrix does not have the same size,
                    or if the divisor is not a number.

        ZerrorDivisionError: If the divisor is zero.
    """
    
    if not all(isintance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row)) == len(matrix[0] for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(elem / div, 2)for element in row] for row in matrix]

    return new_matrix
