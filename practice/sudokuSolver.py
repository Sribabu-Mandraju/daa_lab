def canBePlace(board,row,col,num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row,start_col = 3*(row//3),3*(col//3)
    for i in range(start_row,3):
        for j in range(start_col,3):
            if board[i][j] == num:
                return False
    return True

def solveSudoko(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1,10):
                    if canBePlace(board,row,col,num):
                        board[row][col] = num
                        if solveSudoko(board):
                            return True
                        board[row][col] = 0
                return False
    return True

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

if solveSudoko(board):
    print("Sudoku solved:")
    print_board(board)
else:
    print("No solution exists.")

            
    
        