def isSafe(board,row,col,n):
    for i in range(row):
        if board[i][col] ==1:
            return False
    
    i,j = row,col
    while i>=0 and j>=0:
        if board[i][j] == 1:
            return False
        j -=1
        i -=1
    i,j = row,col
    
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1


    return True

def solve_check(board,row,n):
    if row>=n:
        return True
    for col in range(n):
        if isSafe(board,row,col,n):
            board[row][col] = 1
            if solve_check(board,row+1,n):
                return True
            board[row][col] = 0
    return False


def printBoard(board,n):
    for i in range(n):
        for j in range(n):
            print("Q" if board[i][j] == 1 else ".", end = " ")
        print()
          
def solveQueens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    if not solve_check(board,0,n):
        print("no solutions")
        return False
    printBoard(board,n)
    return True

  
n = 4  # Change n to the size of the board you want
solveQueens(n)