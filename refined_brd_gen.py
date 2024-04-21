
from random import randint, shuffle

#Initialize an empty (9x9) grid
grid = []
for turn in range(0,9):
    grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

soln_counter = 0
numbers_list = [1,2,3,4,5,6,7,8,9]

#A function to check if the grid is full
def checkGrid(grid):
    for row in range(0,9):
        for col in range(0,9):
            if grid[row][col]==0:
                return False
    #We have a complete grid
    return True 

# Backtracking/recursive function to check all possible combinations of numbers
# until a solution is found and to also fill up the grid.
def fillGrid(grid):
    #Find next empty cell
    for i in range(0,81):
        row=i//9
        col=i%9
        if grid[row][col]==0:
            shuffle(numbers_list)
            for value in numbers_list:
                #Check that this value has not already been used on this row
                if not(value in grid[row]):
                    #Check that this value has not already been used on this column
                    if not value in (grid[0][col],grid[1][col],grid[2][col],grid[3][col],grid[4][col],grid[5][col],grid[6][col],grid[7][col],grid[8][col]):
                        #Identify which of the 9 squares we are working on
                        square=[]
                        if row<3:
                            if col<3:
                                square=[grid[i][0:3] for i in range(0,3)]
                            elif col<6:
                                square=[grid[i][3:6] for i in range(0,3)]
                            else:  
                                square=[grid[i][6:9] for i in range(0,3)]
                        elif row<6:
                            if col<3:
                                square=[grid[i][0:3] for i in range(3,6)]
                            elif col<6:
                                square=[grid[i][3:6] for i in range(3,6)]
                            else:  
                                square=[grid[i][6:9] for i in range(3,6)]
                        else:
                            if col<3:
                                square=[grid[i][0:3] for i in range(6,9)]
                            elif col<6:
                                square=[grid[i][3:6] for i in range(6,9)]
                            else:  
                                square=[grid[i][6:9] for i in range(6,9)]
                        #Check that this value has not already be used on this 3x3 square
                        if not value in (square[0] + square[1] + square[2]):
                            grid[row][col]=value
                            if checkGrid(grid):
                                return True
                            else:
                                if fillGrid(grid):
                                    return True
            break
    grid[row][col]=0

# Backtracking or Recursive function to check
# all possible combinations of numbers
# until a solution is found
def solveGrid(grid):
    global soln_counter
    #Find next empty cell
    for i in range(0,81):
        row=i//9
        col=i%9
        if grid[row][col]==0:
            for value in range (1,10):
                #Check that this value has not already be used on this row
                if not(value in grid[row]):
                    #Check that this value has not already be used on this column
                    if not value in (grid[0][col],grid[1][col],grid[2][col],grid[3][col],grid[4][col],grid[5][col],grid[6][col],grid[7][col],grid[8][col]):
                        #Identify which of the 9 squares we are working on
                        square=[]
                        if row<3:
                            if col<3:
                                square=[grid[i][0:3] for i in range(0,3)]
                            elif col<6:
                                square=[grid[i][3:6] for i in range(0,3)]
                            else:  
                                square=[grid[i][6:9] for i in range(0,3)]
                        elif row<6:
                            if col<3:
                                square=[grid[i][0:3] for i in range(3,6)]
                            elif col<6:
                                square=[grid[i][3:6] for i in range(3,6)]
                            else:  
                                square=[grid[i][6:9] for i in range(3,6)]
                        else:
                            if col<3:
                                square=[grid[i][0:3] for i in range(6,9)]
                            elif col<6:
                                square=[grid[i][3:6] for i in range(6,9)]
                            else:  
                                square=[grid[i][6:9] for i in range(6,9)]
                        #Check that this value has not already be used on this 3x3 square
                        if not value in (square[0] + square[1] + square[2]):
                            grid[row][col]=value
                            if checkGrid(grid):
                                soln_counter+=1
                                break
                                # return True
                            else:
                                if solveGrid(grid):
                                    return True
            break
    grid[row][col]=0

def printGrid(grid):
    for i in range(9):
        for j in range(9):
            if j<6 and j%3 == 2:
                print(grid[i][j], end=" | ")
            else:
                print(grid[i][j], end=" ")
        print()
        if i<6 and i%3 == 2:
            print("=====================")


if __name__ == "__main__":
    
    # print(len(grid))
    
    fillGrid(grid)
    print("After fillGrid:")
    printGrid(grid)
    print(f"\nSolution Counter: {soln_counter}\n")
    
    # ==========================================
    # solveGrid(grid)
    # print("After solveGrid:")
    # printGrid(grid)
    # print(f"\nSolution Counter: {soln_counter}\n")
    
    # solveGrid(grid)
    # print("After solveGrid:")
    # printGrid(grid)
    # print(f"\nSolution Counter: {soln_counter}\n")
    
