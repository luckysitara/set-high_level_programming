#!/usr/bin/python3
"""Solves the N queens puzzle"""
import sys


def is_safe(board, row, col):
    """Check if a queen can be placed at board[row][col]"""
    for r in range(row):
        c = board[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve_nqueens(n, row, board, solutions):
    """Recursively solve the N queens puzzle using backtracking"""
    if row == n:
        solutions.append(list(board))
        return
    for col in range(n):
        if is_safe(board, row, col):
            board.append(col)
            solve_nqueens(n, row + 1, board, solutions)
            board.pop()


def main():
    """Entry point"""
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

    solutions = []
    solve_nqueens(n, 0, [], solutions)

    for solution in solutions:
        result = [[row, col] for row, col in enumerate(solution)]
        print(result)


if __name__ == "__main__":
    main()
