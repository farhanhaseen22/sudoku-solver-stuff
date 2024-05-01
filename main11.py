import proper_sdk_brd_gen as pbrd

# grid = []

grid = pbrd.board_generate(45)
print(grid)

# for i in range(9):
#         for j in range(9):
#             if j<6 and j%3 == 2:
#                 print(grid[i][j], end=" | ")
#             else:
#                 print(grid[i][j], end=" ")
#         print()
#         if i<6 and i%3 == 2:
#             print("=====================")
