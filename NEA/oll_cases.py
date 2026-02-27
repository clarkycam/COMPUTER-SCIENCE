#oll_cases.py

OLL_CASES = {
    "I-Shape": ["F", "R", "U", "R'", "U'", "F'"],

    "L-Shape": ["B", "U", "L", "U'", "L'", "B'"],

    "Antisune": ["R", "U2", "R'", "U'", "R", "U'", "R'"],

    "Sune": ["R", "U", "R'", "U", "R", "U2", "R'"],

    "L": ["R", "U2", "R", "D", "R'", "U2", "R", "D'", "R2"],

    "T": ["L", "F", "R'", "F'", "L'", "F", "R", "F'"],

    "Pi": ["R", "U2", "R2", "U'", "R2", "U'", "R2", "U2", "R"],

    "U": ["R2", "D", "R'", "U2", "R", "D'", "R'", "U2", "R'"],

    "H": ["R", "U", "R'", "U", "R", "U'", "R'", "U", "R", "U2", "R'"],

    "Dot-Shape": ["F", "R", "U", "R'", "U'", "F'", "B", "U", "L", "U'", "L'", "B'"],
}


def is_oll_solved(cube):
    # Check if the top face is a single color
    top_color = cube["U"][0][0]
    for row in cube["U"]:
        for sticker in row:
            if sticker != top_color:
                return False
    return True


def get_white_top_positions(cube):
    # Get the positions of the white stickers on the top face of the cube. This will help us determine which OLL case we are in.
    white_grid = []
    for row in range(3):
        white_row = []
        for col in range(3):
            white_row.append(cube["U"][row][col] == 'W')
        white_grid.append(white_row)
    print(f"white_grid: {white_grid}")
    return white_grid


def get_side_white_positions(cube):
    # Get the positions of the white stickers on the adjacent side faces (F, R, B, L) in the top layer.
    side_grid = {
        'F': [cube["F"][0][col] == 'W' for col in range(3)],
        'R': [cube["R"][0][col] == 'W' for col in range(3)],
        'B': [cube["B"][0][col] == 'W' for col in range(3)],
        'L': [cube["L"][0][col] == 'W' for col in range(3)]
    }
    print(f"side_grid: {side_grid}")
    return side_grid


def match_oll_case(white_grid, side_grid):
    # Given the positions of the white stickers on the top face and the adjacent side faces, determine which OLL case we are in by comparing against known patterns for each case.
    if all(white_grid[r][c] for r in range(3) for c in range(3)):
        return None

    
    center = white_grid[1][1]
    top_edge = white_grid[0][1]
    right_edge = white_grid[1][2]
    bottom_edge = white_grid[2][1]
    left_edge = white_grid[1][0]

    # I-Shape
    if center and left_edge and right_edge and not top_edge and not bottom_edge:
        return "I-Shape"
    
    # L-Shape
    if center and bottom_edge and right_edge and not top_edge and not left_edge:
        return "L-Shape"
    
    # Dot-Shape
    if center and not top_edge and not right_edge and not bottom_edge and not left_edge:
        return "Dot-Shape"
    
    # Antisune
    if white_grid == [
        [False, True, True],
        [True, True, True],
        [False, True, False]
    ] and side_grid == {
        'F': [True, False, False],
        'R': [True, False, False],
        'B': [False, False, False],
        'L': [True, False, False]
    }:
        return "Antisune"
    
    # Sune
    if white_grid == [
        [False, True, False],
        [True, True, True],
        [True, True, False]
    ] and side_grid == {
        'F': [False, False, True],
        'R': [False, False, True],
        'B': [False, False, True],
        'L': [False, False, False]
    }:
        return "Sune"
    
    # L
    if white_grid == [
        [True, True, False],
        [True, True, True],
        [False, True, True]
    ] and side_grid == {
        'F': [True, False, False],
        'R': [False, False, True],
        'B': [False, False, False],
        'L': [False, False, False]
    }:
        return "L"
    
    # T
    if white_grid == [
        [False, True, True],
        [True, True, True],
        [False, True, True]
    ] and side_grid == {
        'F': [True, False, False],
        'R': [False, False, False],
        'B': [False, False, True],
        'L': [False, False, False]
    }:
        return "T"
    
    # Pi
    if white_grid == [
        [False, True, False],
        [True, True, True],
        [False, True, False]
    ] and side_grid == {
        'F': [False, False, True],
        'R': [False, False, False],
        'B': [True, False, False],
        'L': [True, False, True]
    }:
        return "Pi"
    
    # U
    if white_grid == [
        [True, True, True],
        [True, True, True],
        [False, True, False]
    ] and side_grid == {
        'F': [True, False, True],
        'R': [False, False, False],
        'B': [False, False, False],
        'L': [False, False, False]
    }:
        return "U"
    
    # H
    if white_grid == [
        [False, True, False],
        [True, True, True],
        [False, True, False]
    ] and side_grid == {
        'F': [False, False, False],
        'R': [True, False, True],
        'B': [False, False, False],
        'L': [True, False, True]
    }:
        return "H"
    
    return None