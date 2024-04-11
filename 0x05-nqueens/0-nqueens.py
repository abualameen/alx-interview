#!/usr/bin/python3

import sys


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen in a given position.
    """
    # Check if there is a queen in the same row
    for i in range(col):
        if board[row][i] == 1:
            return False
    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    # Check lower left diagonal
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solve_nqueens(board, col, n):
    """
    Recursive function to find all possible solutions to N queens problem.
    """
    if col >= n:
        print(board)
        return
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve_nqueens(board, col + 1, n)
            board[i][col] = 0


def nqueens(n):
    """
    Main function to solve N queens problem.
    """
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [[0 for _ in range(n)] for _ in range(n)]
    solve_nqueens(board, 0, n)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    nqueens(n)
