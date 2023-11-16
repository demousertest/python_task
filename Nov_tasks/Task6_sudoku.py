def solveSudoku(board):
    def is_valid(num, row, col):
        # Check if 'num' is valid in the current row, column, and 3x3 subgrid
        for i in range(9):
            if board[row][i] == num or board[i][col] == num or board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
                return False
        return True

    def backtrack():
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    for num in map(str, range(1, 10)):
                        if is_valid(num, row, col):
                            board[row][col] = num
                            if backtrack():
                                return True
                            board[row][col] = "."
                    return False
        return True

    backtrack()

# Helper function to print the Sudoku board
def print_sudoku(board):
    for row in board:
        print(" ".join(row))

# Example input Sudoku board
input_board = [["5","3",".",".","7",".",".",".","."],
               ["6",".",".","1","9","5",".",".","."],
               [".","9","8",".",".",".",".","6","."],
               ["8",".",".",".","6",".",".",".","3"],
               ["4",".",".","8",".","3",".",".","1"],
               ["7",".",".",".","2",".",".",".","6"],
               [".","6",".",".",".",".","2","8","."],
               [".",".",".","4","1","9",".",".","5"],
               [".",".",".",".","8",".",".","7","9"]]

# Solve the Sudoku puzzle
solveSudoku(input_board)

# Print the solved Sudoku board
print_sudoku(input_board)
