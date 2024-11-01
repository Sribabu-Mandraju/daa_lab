# Function to check if a number can be placed at a given position
def is_valid(board, row, col, num):
    # Check if num is not in the current row, column, or 3x3 subgrid
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True

# Recursive function to solve the Sudoku puzzle
def solve_sudoku(board):
    # Find an empty cell
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # 0 indicates an empty cell
                # Try placing numbers 1 to 9
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num  # Place num in cell
                        if solve_sudoku(board):  # Recursive call
                            return True
                        board[row][col] = 0  # Undo placement if it leads to no solution
                return False  # No valid number found, backtrack
    return True  # Puzzle solved

# Function to print the board
def print_board(board):
    for row in board:
        print(" ".join(str(num) for num in row))

# Example usage
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(board):
    print("Sudoku solved:")
    print_board(board)
else:
    print("No solution exists.")
