from sudoku import SudokuBoard, generate, validate_puzzle, generate_unique, rate_difficulty


def test_is_valid():
    """Test whether the is_valid method correctly verifies the validity of a number placement"""
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
    """Test whether the solve method can correctly solve the Sudoku puzzle"""
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
    """Test whether the generate function produces a valid Sudoku puzzle"""
    difficulty = 45
    puzzle_board, solution_board = generate(difficulty)
    
    empty_cells = sum(row.count(0) for row in puzzle_board.grid)
    assert empty_cells == difficulty, f"Puzzle should have {difficulty} empty cells, but has {empty_cells}"
    
    assert all(cell != 0 for row in solution_board.grid for cell in row), "Solution should have no empty cells"
    
    puzzle_copy = SudokuBoard(puzzle_board.grid)
    assert puzzle_copy.solve() is True, "Generated puzzle must be solvable"

# Part 2: Advanced Features (Bonus)

def test_count_solutions():
    """Test whether the count_solutions method correctly counts the number of solutions"""
    unique_puzzle = [
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
    board = SudokuBoard(unique_puzzle)
    assert board.count_solutions() == 1, "This puzzle should have exactly 1 solution"
    
    no_solution_puzzle = [
        [1, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    board2 = SudokuBoard(no_solution_puzzle)
    assert board2.count_solutions() == 0, "Invalid puzzle should have 0 solutions"


def test_generate_unique_solution():
    """Test generate_unique produces puzzles with a unique solution - Bonus 2.1"""

    for difficulty in [30, 40, 50]:
        puzzle, solution = generate_unique(difficulty)
        
        empty_cells = sum(row.count(0) for row in puzzle.grid)
        assert empty_cells == difficulty, f"Puzzle should have {difficulty} empty cells"
        
        assert all(cell != 0 for row in solution.grid for cell in row), "Solution should be complete"
        
        count = puzzle.count_solutions()
        assert count == 1, f"Puzzle should have exactly 1 solution, but has {count}"
        
        test_board = SudokuBoard(puzzle.grid)
        assert test_board.solve() is True, "Puzzle should be solvable"


def test_difficulty_rating():
    """Test difficulty rating engine - Bonus 2.2"""
    
    # Easy puzzle: requires only basic techniques (many hints)
    easy_puzzle = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 0, 0, 0, 0, 0, 7, 9]
    ]
    board = SudokuBoard(easy_puzzle)
    difficulty = rate_difficulty(board)
    assert difficulty == "Easy", f"Should be Easy, but got {difficulty}"
    
    # Medium puzzle: has more blanks
    medium_puzzle = [
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
    board = SudokuBoard(medium_puzzle)
    difficulty = rate_difficulty(board)
    assert difficulty in ["Easy", "Medium"], f"Should be Easy or Medium, but got {difficulty}"
    
    # Hard puzzle: large number of blanks
    hard_puzzle = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 8, 5],
        [0, 0, 1, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 7, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 1, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 7, 3],
        [0, 0, 2, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 9]
    ]
    board = SudokuBoard(hard_puzzle)
    difficulty = rate_difficulty(board)
    assert difficulty in ["Easy", "Medium", "Hard"], f"Should be Easy, Medium or Hard, but got {difficulty}"


def test_validate_puzzle():
    """Test puzzle validation function - Bonus 2.3"""
    
    # Test 1: Valid puzzle
    valid_puzzle = [
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
    errors = validate_puzzle(valid_puzzle)
    assert len(errors) == 0, "Valid puzzle should have no errors"
    
    # Test 2: Duplicate numbers in a row
    row_duplicate = [
        [1, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    errors = validate_puzzle(row_duplicate)
    assert len(errors) > 0, "Should detect row duplicate"
    assert "row" in errors[0].lower(), "Error message should mention row"
    
    # Test 3: Duplicate numbers in a column
    col_duplicate = [
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    errors = validate_puzzle(col_duplicate)
    assert len(errors) > 0, "Should detect column duplicate"
    assert "col" in errors[0].lower() or "column" in errors[0].lower(), "Error message should mention column"
    
    # Test 4: Duplicate numbers in a 3x3 box
    box_duplicate = [
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    errors = validate_puzzle(box_duplicate)
    assert len(errors) > 0, "Should detect box duplicate"
    assert "box" in errors[0].lower(), "Error message should mention box"
    
    # Test 5: Invalid number range
    invalid_number = [
        [10, 0, 0, 0, 0, 0, 0, 0, 0],  # 10 is out of range
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    errors = validate_puzzle(invalid_number)
    assert len(errors) > 0, "Should detect invalid number"
    assert "range" in errors[0].lower() or "invalid" in errors[0].lower(), "Error message should mention invalid number"
    
    # Test 6: Incorrect grid size (not 9x9)
    wrong_size = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    errors = validate_puzzle(wrong_size)
    assert len(errors) > 0, "Should detect wrong grid size"
    assert "9x9" in errors[0] or "size" in errors[0].lower(), "Error message should mention size"
