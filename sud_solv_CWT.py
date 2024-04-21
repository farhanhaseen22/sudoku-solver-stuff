
# This is the sudoku solver made by Coding with Tim(CWT).
# However, it has a fixed board and it solves it only 1 time.

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


def solve(given_board):
    find = find_empty(given_board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(given_board, i, (row, col)):
            given_board[row][col] = i

            if solve(given_board):
                return True

            given_board[row][col] = 0

    return False


def valid(given_board, num, pos):
    # Check row
    for i in range(len(given_board[0])):
        if given_board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(given_board)):
        if given_board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if given_board[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(given_board):
    for i in range(len(given_board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
            print("- - - - - - - - - - - - - ")

        for j in range(len(given_board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(given_board[i][j])
            else:
                print(str(given_board[i][j]) + " ", end="")


def find_empty(given_board):
    for i in range(len(given_board)):
        for j in range(len(given_board[0])):
            if given_board[i][j] == 0:
                return (i, j)  # row, col
    return None


print_board(board)
solve(board)
print("====================================")
print_board(board)
