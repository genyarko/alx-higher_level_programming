#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for x in row:
            print("{:d}".format(x), end=" ")
        print()
