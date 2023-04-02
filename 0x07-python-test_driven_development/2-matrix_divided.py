def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given divisor.
    :param matrix: list of lists of integers or floats
    :param div: number (integer or float)
    :return: new matrix with elements divided by div, rounded to 2 decimal places
    """
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    new_matrix = []
    for row in matrix:
        new_row = []
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_row.append(round(item / div, 2))
        new_matrix.append(new_row)
    return new_matrix
