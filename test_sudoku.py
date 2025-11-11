# test_sudoku.py
from sudoku import SudokuBoard, generate

def test_is_valid():
    initial_grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    board = SudokuBoard(initial_grid)
    
    assert board.is_valid(0, 2, 4) is True, "is_valid(0, 2, 4) should be True"
    
    assert board.is_valid(0, 2, 5) is False, "is_valid(0, 2, 5) should be False due to row conflict"
    
    assert board.is_valid(0, 2, 8) is False, "is_valid(0, 2, 8) should be False due to column conflict"
    
    assert board.is_valid(1, 1, 9) is False, "is_valid(1, 1, 9) should be False due to box conflict"


def test_solve():
    puzzle_grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    solution_grid = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]
    
    puzzle = SudokuBoard(puzzle_grid)
    assert puzzle.solve() is True, "Solver should return True for a solvable puzzle"
    assert puzzle.grid == solution_grid, "The solved puzzle does not match the expected solution"


def test_generate():
    difficulty = 45
    puzzle_board, solution_board = generate(difficulty)
    
    empty_cells = sum(row.count(0) for row in puzzle_board.grid)
    assert empty_cells == difficulty, f"Puzzle should have {difficulty} empty cells, but has {empty_cells}"
    
    assert all(cell != 0 for row in solution_board.grid for cell in row), "Solution should have no empty cells"
    
    puzzle_copy = SudokuBoard(puzzle_board.grid)
    assert puzzle_copy.solve() is True, "Generated puzzle must be solvable"