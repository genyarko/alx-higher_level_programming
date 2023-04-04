#!/usr/bin/python3
"""
nqueens backtracking program to print the coordinates of n queens
on an nxn grid such that they are all in non-attacking positions
"""

import sys

def nqueens(N):
    # Check that N is an integer greater than or equal to 4
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the board
    board = [[0 for x in range(N)] for y in range(N)]

    # Helper function to check if a move is safe
    def is_safe(board, row, col):
        # Check this row on left side
        for i in range(col):
            if board[row][i]:
                return False

        # Check upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j]:
                return False

        # Check lower diagonal on left side
        for i, j in zip(range(row, N), range(col, -1, -1)):
            if board[i][j]:
                return False

        # The move is safe
        return True

    # Recursive function to solve the problem
    def solve(board, col, solutions):
        # If all queens are placed
        if col == N:
            solutions.append(board)
            return

        # Try placing this queen in all rows of current column
        for row in range(N):
            if is_safe(board, row, col):
                board[row][col] = 1
                solve(board, col+1, solutions)
                board[row][col] = 0

    # Find all solutions
    solutions = []
    solve(board, 0, solutions)

    # Print solutions
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    # Check command line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    nqueens(N)
