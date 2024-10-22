def is_safe(board, row, col, n):
    # Check this column on the upper side
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper diagonal on the left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper diagonal on the right side
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_nqueens_util(board, row, n):
    # If all queens are placed, return True
    if row >= n:
        return True

    # Try placing this queen in all columns one by one
    for col in range(n):
        if is_safe(board, row, col, n):
            # Place the queen
            board[row][col] = 1

            # Recur to place the rest of the queens
            if solve_nqueens_util(board, row + 1, n):
                return True

            # If placing queen at board[row][col] doesn't lead to a solution,
            # backtrack and remove the queen
            board[row][col] = 0

    return False

def solve_nqueens(n):
    # Initialize the chessboard with 0s
    board = [[0 for _ in range(n)] for _ in range(n)]

    if not solve_nqueens_util(board, 0, n):
        print("No solution exists")
        return False

    # Print the solution board
    print_board(board, n)
    return True

def print_board(board, n):
    for i in range(n):
        for j in range(n):
            print("Q" if board[i][j] == 1 else ".", end=" ")
        print()

# Example usage
n = 8  # Change n to the size of the board you want
solve_nqueens(n)
