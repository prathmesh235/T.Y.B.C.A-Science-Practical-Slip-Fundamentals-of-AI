
# N-Queens Problem using Backtracking

def print_board(board, n):
    for row in range(n):
        for col in range(n):
            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


def is_safe(board, row, col):
    for prev_row in range(row):
        # Check same column
        if board[prev_row] == col:
            return False

        # Check diagonal
        if abs(board[prev_row] - col) == abs(prev_row - row):
            return False

    return True


def solve_n_queens(board, row, n):
    # All queens have been placed
    if row == n:
        return True

    # Try each column in the current row
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col

            if solve_n_queens(board, row + 1, n):
                return True

            # Backtrack
            board[row] = -1

    return False


n = int(input("Enter the value of N: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    board = [-1] * n

    if solve_n_queens(board, 0, n):
        print("\nOne valid arrangement of", n, "queens:")
        print_board(board, n)
    else:
        print("No solution exists for N =", n)
