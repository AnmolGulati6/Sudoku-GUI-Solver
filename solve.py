# Written by Anmol Gulati

import copy
from random import randint, shuffle

# Initialise empty 9x9 board

grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]


# A backtracking function to check all possible combinations of numbers until a solution is found
def solveGrid(board):
    global counter
    counter = 0
    # Find next empty cell
    for i in range(0, 81):
        row = i // 9
        col = i % 9
        if board[row][col] == 0:
            for value in range(1, 10):
                # Check that this value has not already be used on this row
                if not (value in board[row]):
                    # Check that this value has not already be used on this column
                    if not value in (
                            board[0][col], board[1][col], board[2][col], board[3][col], board[4][col], board[5][col],
                            board[6][col],
                            board[7][col], board[8][col]):
                        # Identify which of the 9 squares we are working on
                        square = []
                        if row < 3:
                            if col < 3:
                                square = [board[i][0:3] for i in range(0, 3)]
                            elif col < 6:
                                square = [board[i][3:6] for i in range(0, 3)]
                            else:
                                square = [board[i][6:9] for i in range(0, 3)]
                        elif row < 6:
                            if col < 3:
                                square = [board[i][0:3] for i in range(3, 6)]
                            elif col < 6:
                                square = [board[i][3:6] for i in range(3, 6)]
                            else:
                                square = [board[i][6:9] for i in range(3, 6)]
                        else:
                            if col < 3:
                                square = [board[i][0:3] for i in range(6, 9)]
                            elif col < 6:
                                square = [board[i][3:6] for i in range(6, 9)]
                            else:
                                square = [board[i][6:9] for i in range(6, 9)]
                        # Check that this value has not already be used on this 3x3 square
                        if not value in (square[0] + square[1] + square[2]):
                            board[row][col] = value
                            if checkGrid(board):
                                counter += 1
                                break
                            else:
                                if solveGrid(board):
                                    return True
            break
    grid[row][col] = 0


# Formats the sudoku board for console
def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


# This function returns true if the grid is full
def checkGrid(board):
    for row in range(0, 9):
        for col in range(0, 9):
            if board[row][col] == 0:
                return False
    return True


numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# backtracking alg to check all possible combinations of numbers until a solution is found
def fillGrid(grid):
    global counter
    # Find next empty cell
    for i in range(0, 81):
        row = i // 9
        col = i % 9
        if grid[row][col] == 0:
            shuffle(numberList)
            for value in numberList:
                # Check that this value has not already be used on this row
                if not (value in grid[row]):
                    # Check that this value has not already be used on this column
                    if not value in (
                            grid[0][col], grid[1][col], grid[2][col], grid[3][col], grid[4][col], grid[5][col],
                            grid[6][col],
                            grid[7][col], grid[8][col]):
                        # Identify which of the 9 squares we are working on
                        square = []
                        if row < 3:
                            if col < 3:
                                square = [grid[i][0:3] for i in range(0, 3)]
                            elif col < 6:
                                square = [grid[i][3:6] for i in range(0, 3)]
                            else:
                                square = [grid[i][6:9] for i in range(0, 3)]
                        elif row < 6:
                            if col < 3:
                                square = [grid[i][0:3] for i in range(3, 6)]
                            elif col < 6:
                                square = [grid[i][3:6] for i in range(3, 6)]
                            else:
                                square = [grid[i][6:9] for i in range(3, 6)]
                        else:
                            if col < 3:
                                square = [grid[i][0:3] for i in range(6, 9)]
                            elif col < 6:
                                square = [grid[i][3:6] for i in range(6, 9)]
                            else:
                                square = [grid[i][6:9] for i in range(6, 9)]
                        # Check that this value has not already be used on this 3x3 square
                        if not value in (square[0] + square[1] + square[2]):
                            grid[row][col] = value
                            if checkGrid(grid):
                                return True
                            else:
                                if fillGrid(grid):
                                    return True
            break
    grid[row][col] = 0


fillGrid(grid)
# store a copy of the solution
solution = copy.deepcopy(grid)

# increase attempts to increase difficulty
attempts = 5
counter = 1
while attempts > 0:
    # Select random cell that is not already empty
    row = randint(0, 8)
    col = randint(0, 8)
    while grid[row][col] == 0:
        row = randint(0, 8)
        col = randint(0, 8)
    # store its cell value in case we need to put it back
    backup = grid[row][col]
    grid[row][col] = 0

    # Take a full copy of the grid
    copyGrid = []
    for r in range(0, 9):
        copyGrid.append([])
        for c in range(0, 9):
            copyGrid[r].append(grid[r][c])
    counter = 0
    solveGrid(copyGrid)
    if counter != 1:
        grid[row][col] = backup
        attempts -= 1
print("Problem: ")
print_board(grid)
print("_____________________")
print("Solution")
print_board(solution)
