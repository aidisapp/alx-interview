#!/usr/bin/python3
"""
N-Queens problem solver
"""

import sys


def is_safe(queens, row, col):
    """Check if placing a queen at (row, col) is safe from attacks."""
    for r, c in queens:
        if c == col or r - c == row - col or r + c == row + col:
            return False
    return True


def solve_nqueens(n, row=0, queens=[]):
    """Backtracking solution for the N-Queens problem."""
    if row == n:
        print(queens)
        return

    for col in range(n):
        if is_safe(queens, row, col):
            queens.append([row, col])
            solve_nqueens(n, row + 1, queens)
            queens.pop()


if __name__ == '__main__':
    # Handle command-line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n)
