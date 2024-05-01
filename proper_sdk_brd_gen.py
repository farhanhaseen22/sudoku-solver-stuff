
from random import randint, shuffle

# Initialize an empty (9x9) grid
grid = []
for turn in range(0,9):
    grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

soln_counter = 0
numbers_list = [1,2,3,4,5,6,7,8,9]

# A function to check the number of 0's in the grid
def checkNumberOfZeros(grid):
  countZero = 0
  for row in range(0,9):
      for col in range(0,9):
        if grid[row][col]==0:
          countZero+=1
  
  return countZero

# A function to check if the grid is full
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

# Backtracking or Recursive function to check all possible combinations of numbers
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
                            else:
                                if solveGrid(grid):
                                    return True
            break
    grid[row][col]=0


def board_generate(limit):
    
    fillGrid(grid)
    
    # this variable is regarded as the difficulty meter
    limit = limit
    # ==========================================
    attempts = 0
    soln_counter = 1
    cnoz = 0
    
    # while cnoz<limit:
    #     #Select a random cell that is not already empty
    #     row = randint(0,8)
    #     col = randint(0,8)
    #     while grid[row][col]==0:
    #         row = randint(0,8)
    #         col = randint(0,8)
    #     #Remember its cell value in case we need to put it back
    #     backup = grid[row][col]
    #     grid[row][col] = 0
        
    #     copyGrid = []
    #     for r in range(0,9):
    #         copyGrid.append([])
    #         for c in range(0,9):
    #             copyGrid[r].append(grid[r][c])

    #     soln_counter = 0
    #     solveGrid(copyGrid)
        
    #     if soln_counter != 1:
    #         grid[row][col]=backup
        
    #     attempts+=1
    #     cnoz = checkNumberOfZeros(grid)
    #     print(f"The Number of attempts so far: {attempts}")
    
    # # ==========================================
    # print("After all the Removing:")
    # return grid
    # # ==========================================
    
    return type(cnoz)
