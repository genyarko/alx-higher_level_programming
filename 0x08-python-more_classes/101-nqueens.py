#!/usr/bin/python3
"""
nqueens backtracking program to print the coordinates of n queens
on an nxn grid such that they are all in non-attacking positions
"""

import sys

def is_safe(board, row, col, N):
    # Check if no queen can attack the current cell
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve(board, row, N):
    if row == N:
        # All queens have been placed, print the solution
        print(board)
    else:
        # Try to place a queen in each column of the current row
        for col in range(N):
            if is_safe(board, row, col, N):
                board[row] = col
                solve(board, row + 1, N)
                board[row] = -1

def nqueens(N):
    # Check if N is valid
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the board with -1 in each cell
    board = [-1] * N
    solve(board, 0, N)

if __name__ == '__main__':
    # Parse command line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Solve the problem
    nqueens(N)
