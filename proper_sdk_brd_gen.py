from random import randint, shuffle

class SudokuGenerator:
    def __init__(self):
        pass

    def generate_board(self, limit):
        grid = self.__initialize_grid()
        self.__fill_grid(grid)
        self.__remove_cells(grid, limit)
        return grid

    def __initialize_grid(self):
        grid = []
        for _ in range(0, 9):
            grid.append([0] * 9)
        return grid

    def __check_number_of_zeros(self, grid):
        count_zero = 0
        for row in range(0, 9):
            for col in range(0, 9):
                if grid[row][col] == 0:
                    count_zero += 1
        return count_zero

    def __check_grid(self, grid):
        for row in range(0, 9):
            for col in range(0, 9):
                if grid[row][col] == 0:
                    return False
        return True

    def __fill_grid(self, grid):
        for _ in range(0, 81):
            row = _ // 9
            col = _ % 9
            if grid[row][col] == 0:
                shuffle(self.numbers_list)
                for value in self.numbers_list:
                    if value not in grid[row] and value not in (grid[0][col], grid[1][col], grid[2][col], grid[3][col],
                                                                 grid[4][col], grid[5][col], grid[6][col], grid[7][col], grid[8][col]):
                        square = self.__get_square(grid, row, col)
                        if value not in (square[0] + square[1] + square[2]):
                            grid[row][col] = value
                            if self.__check_grid(grid):
                                return True
                            else:
                                if self.__fill_grid(grid):
                                    return True
                break
        grid[row][col] = 0

    def __get_square(self, grid, row, col):
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
        return square

    def __solve_grid(self, grid):
        for _ in range(0, 81):
            row = _ // 9
            col = _ % 9
            if grid[row][col] == 0:
                for value in range(1, 10):
                    if value not in grid[row] and value not in (grid[0][col], grid[1][col], grid[2][col], grid[3][col],
                                                                 grid[4][col], grid[5][col], grid[6][col], grid[7][col], grid[8][col]):
                        square = self.__get_square(grid, row, col)
                        if value not in (square[0] + square[1] + square[2]):
                            grid[row][col] = value
                            if self.__check_grid(grid):
                                self.soln_counter += 1
                                break
                            else:
                                if self.__solve_grid(grid):
                                    return True
                break
        grid[row][col] = 0

    def __remove_cells(self, grid, limit):
        attempts = 0
        cnoz = 0
        while cnoz < limit:
            row = randint(0, 8)
            col = randint(0, 8)
            while grid[row][col] == 0:
                row = randint(0, 8)
                col = randint(0, 8)
            backup = grid[row][col]
            grid[row][col] = 0
            copy_grid = [row[:] for row in grid]
            self.soln_counter = 0
            self.__solve_grid(copy_grid)
            if self.soln_counter != 1:
                grid[row][col] = backup
            attempts += 1
            cnoz = self.__check_number_of_zeros(grid)
            print(f"The Number of attempts so far: {attempts}")
        print("After all the Removing:")


# Example usage:
if __name__ == "__main__":
    sudoku_gen = SudokuGenerator()
    board = sudoku_gen.generate_board(60)
    for row in board:
        print(row)

