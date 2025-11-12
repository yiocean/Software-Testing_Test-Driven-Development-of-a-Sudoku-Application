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
    
    def count_solutions(self, limit=2):
        count = [0]
        def solve_and_count(grid):
            if count[0] >= limit:
                return
            empty = None
            for i in range(self.size):
                for j in range(self.size):
                    if grid[i][j] == 0:
                        empty = (i, j)
                        break
                if empty:
                    break
            if not empty:
                count[0] += 1
                return
            row, col = empty
            for num in range(1, self.size + 1):
                valid = True
                if num in grid[row]:
                    valid = False
                if valid:
                    for i in range(self.size):
                        if grid[i][col] == num:
                            valid = False
                            break
                if valid:
                    start_row = 3 * (row // 3)
                    start_col = 3 * (col // 3)
                    for i in range(3):
                        for j in range(3):
                            if grid[i + start_row][j + start_col] == num:
                                valid = False
                                break
                        if not valid:
                            break
                if valid:
                    grid[row][col] = num
                    solve_and_count(grid)
                    grid[row][col] = 0
        grid_copy = copy.deepcopy(self.grid)
        solve_and_count(grid_copy)
        return count[0]


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


def validate_puzzle(grid):
    errors = []
    if not isinstance(grid, list):
        errors.append("Grid must be a list")
        return errors
    if len(grid) != 9:
        errors.append(f"Grid must be 9x9, but has {len(grid)} rows")
        return errors
    for i, row in enumerate(grid):
        if not isinstance(row, list):
            errors.append(f"Row {i} must be a list")
            return errors
        if len(row) != 9:
            errors.append(f"Row {i} must have 9 columns, but has {len(row)}")
            return errors
    for i in range(9):
        for j in range(9):
            val = grid[i][j]
            if not isinstance(val, int) or val < 0 or val > 9:
                errors.append(f"Invalid number {val} at position ({i}, {j}). Must be 0-9")
                return errors
    for i in range(9):
        seen = set()
        for j in range(9):
            val = grid[i][j]
            if val != 0:
                if val in seen:
                    errors.append(f"Duplicate {val} in row {i}")
                seen.add(val)
    for j in range(9):
        seen = set()
        for i in range(9):
            val = grid[i][j]
            if val != 0:
                if val in seen:
                    errors.append(f"Duplicate {val} in column {j}")
                seen.add(val)
    for box_row in range(3):
        for box_col in range(3):
            seen = set()
            for i in range(3):
                for j in range(3):
                    val = grid[box_row * 3 + i][box_col * 3 + j]
                    if val != 0:
                        if val in seen:
                            errors.append(f"Duplicate {val} in box ({box_row}, {box_col})")
                        seen.add(val)
    return errors


def generate_unique(difficulty, max_attempts=100):
    empty_grid = [[0] * 9 for _ in range(9)]
    solution_board = SudokuBoard(empty_grid)
    solution_board.solve(randomize=True)
    puzzle_board = SudokuBoard(solution_board.grid)
    positions = [(i, j) for i in range(9) for j in range(9)]
    random.shuffle(positions)
    removed = 0
    attempts = 0
    for row, col in positions:
        if removed >= difficulty:
            break
        attempts += 1
        if attempts > max_attempts:
            return generate_unique(difficulty, max_attempts)
        original_value = puzzle_board.grid[row][col]
        puzzle_board.grid[row][col] = 0
        if puzzle_board.count_solutions(limit=2) == 1:
            removed += 1
        else:
            puzzle_board.grid[row][col] = original_value
    return puzzle_board, solution_board


def rate_difficulty(board):
    empty_count = sum(row.count(0) for row in board.grid)
    if empty_count <= 35:
        return "Easy"
    elif empty_count <= 55:
        return "Medium"
    else:
        return "Hard"
