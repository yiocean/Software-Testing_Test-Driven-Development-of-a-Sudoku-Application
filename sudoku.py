import copy
import random

class SudokuBoard:
    
    def __init__(self, grid):
        self.grid = copy.deepcopy(grid)
        self.size = 9
    
    def is_valid(self, row, col, num):
        for i in range(self.size):
            if self.grid[row][i] == num:
                return False
        
        for i in range(self.size):
            if self.grid[i][col] == num:
                return False
        
        start_row = 3 * (row // 3)
        start_col = 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.grid[i + start_row][j + start_col] == num:
                    return False
        
        return True
    
    def find_empty(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == 0:
                    return (i, j)
        return None
    
    def solve(self, randomize=False):
        find = self.find_empty()
        if not find:
            return True 
        else:
            row, col = find
        
        numbers = list(range(1, self.size + 1))
        if randomize:
            random.shuffle(numbers)
        
        for num in numbers:
            if self.is_valid(row, col, num):
                self.grid[row][col] = num
                
                if self.solve(randomize):
                    return True
                
                self.grid[row][col] = 0
        
        return False


def generate(difficulty):
    empty_grid = [[0] * 9 for _ in range(9)]
    solution_board = SudokuBoard(empty_grid)
    solution_board.solve(randomize=True) 
    
    puzzle_board = SudokuBoard(solution_board.grid)
    cells_to_remove = difficulty
    
    while cells_to_remove > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if puzzle_board.grid[row][col] != 0:
            puzzle_board.grid[row][col] = 0
            cells_to_remove -= 1
    
    return puzzle_board, solution_board