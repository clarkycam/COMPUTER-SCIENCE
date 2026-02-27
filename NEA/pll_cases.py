#pll_cases.py

PLL_CASES = {
    # R' F R' B2 R F' R' B2 R2
    "Aa": ["R'", "F", "R'", "B2", "R", "F'", "R'", "B2", "R2"],

    # R2 B2 R F R' B2 R F' R
    "Ab": ["R2", "B2", "R", "F", "R'", "B2", "R", "F'", "R"],

    # R2 U F' R' U R U' R' U R U' R' U R U' F U' R2
    "E": ["R2", "U", "F'", "R'", "U", "R", "U'", "R'", "U", "R", "U'", "R'", "U", "R", "U'", "F", "U'", "R2"],

    # R' U R U' R2 F' U' F U R F R' F' R2
    "F": ["R'", "U", "R", "U'", "R2", "F'", "U'", "F", "U", "R", "F", "R'", "F'", "R2"],

    # R2 U R' U R' U' R U' R2 D U' R' U R D'
    "Ga": ["R2", "U", "R'", "U", "R'", "U'", "R", "U'", "R2", "D", "U'", "R'", "U", "R", "D'"],

    # D R' U' R U D' R2 U R' U R U' R U' R2
    "Gb": ["D", "R'", "U'", "R", "U", "D'", "R2", "U", "R'", "U", "R", "U'", "R", "U'", "R2"],

    # R2 U' R U' R U R' U R2 D' U R U' R' D
    "Gc": ["R2", "U'", "R", "U'", "R", "U", "R'", "U", "R2", "D'", "U", "R", "U'", "R'", "D"],

    # R U R' U' D R2 U' R U' R' U R' U R2 D'
    "Gd": ["R", "U", "R'", "U'", "D", "R2", "U'", "R", "U'", "R'", "U", "R'", "U", "R2", "D'"],

    # R2 U2 R U2 R2 U2 R2 U2 R U2 R2
    "H": ["R2", "U2", "R", "U2", "R2", "U2", "R2", "U2", "R", "U2", "R2"],

    # R U' L' U R' U2 L U' L' U2 L
    "Ja": ["R", "U'", "L'", "U", "R'", "U2", "L", "U'", "L'", "U2", "L"],

    # R U2 R' U' R U2 L' U R' U' L
    "Jb": ["R", "U2", "R'", "U'", "R", "U2", "L'", "U", "R'", "U'", "L"],

    # R F U' R' U R U F' R2 F' R U R U' R' F
    "Na": ["R", "F", "U'", "R'", "U", "R", "U", "F'", "R2", "F'", "R", "U", "R", "U'", "R'", "F"],

    # R' U L' U2 R U' L R' U L' U2 R U' L
    "Nb": ["R'", "U", "L'", "U2", "R", "U'", "L", "R'", "U", "L'", "U2", "R", "U'", "L"],

    # L U2 L' U2 L F' L' U' L U L F L2
    "Ra": ["L", "U2", "L'", "U2", "L", "F'", "L'", "U'", "L", "U", "L", "F", "L2"],

    # R' U2 R U2 R' F R U R' U' R' F' R2
    "Rb": ["R'", "U2", "R", "U2", "R'", "F", "R", "U", "R'", "U'", "R'", "F'", "R2"],

    # R U R' U' R' F R2 U' R' U' R U R' F'
    "T": ["R", "U", "R'", "U'", "R'", "F", "R2", "U'", "R'", "U'", "R", "U", "R'", "F'"],

    # R U R' U R' U' R2 U' R' U R' U R
    "Ua": ["R", "U", "R'", "U", "R'", "U'", "R2", "U'", "R'", "U", "R'", "U", "R"],

    # R' U R' U' R' U' R' U R U R2
    "Ub": ["R'", "U", "R'", "U'", "R'", "U'", "R'", "U", "R", "U", "R2"],

    # R' U R' U' R D' R' D R' U D' R2 U' R2 D R2
    "V": ["R'", "U", "R'", "U'", "R", "D'", "R'", "D", "R'", "U", "D'", "R2", "U'", "R2", "D", "R2"],

    # R2 U' R2 U' R2 U F U F' R2 F U' F'
    "Y": ["R2", "U'", "R2", "U'", "R2", "U", "F", "U", "F'", "R2", "F", "U'", "F'"],

    # R U R' U R' U' R' U R U' R' U' R2 U R
    "Z": ["R", "U", "R'", "U", "R'", "U'", "R'", "U", "R", "U'", "R'", "U'", "R2", "U", "R"],

    "PLL Solved": []
}

def is_pll_solved(cube):
    # Check if the cube is in a PLL solved state
    for face in ["U", "R", "F", "D", "L", "B"]:
        color = cube[face][1][1]  # center piece color
        for row in cube[face]:
            for sticker in row:
                if sticker != color:
                    return False
    return True

def get_side_edge_positions(cube):
    # get the positions of the edge pieces in the top layer
    faces = ["F", "R", "B", "L"]
    colours = []
    for face in faces:
        face_colours = [cube[face][0][col] for col in range(3)]
        colours.append(face_colours)

    # convetr to True/False grid
    pattern = []
    for face_colours in colours:
        face_pattern = []
        for color in face_colours:
            if color in ['R', 'O']:
                face_pattern.append(True)
            elif color in ['G', 'B']:
                    face_pattern.append(False)
        pattern.append(face_pattern)
    print(f"side edge pattern: {pattern}")
    return pattern

def get_green_edge_positions(cube):
    # get the positions of the green edge pieces in the top layer
    faces = ["F", "R", "B", "L"]
    colours = []
    for face in faces:
        face_colours = [cube[face][0][col] for col in range(3)]
        colours.append(face_colours)

    # convert to True/False grid (True for green edges)
    pattern = []
    for face_colours in colours:
        face_pattern = []
        for color in face_colours:
            if color == 'G':
                face_pattern.append(True)
            else:
                face_pattern.append(False)
        pattern.append(face_pattern)
    print(f"green edge pattern: {pattern}")
    return pattern

def get_red_edge_positions(cube):
    # get the positions of the red edge pieces in the top layer
    faces = ["F", "R", "B", "L"]
    colours = []
    for face in faces:
        face_colours = [cube[face][0][col] for col in range(3)]
        colours.append(face_colours)

    # convert to True/False grid (True for red edges)
    pattern = []
    for face_colours in colours:
        face_pattern = []
        for color in face_colours:
            if color == 'R':
                face_pattern.append(True)
            else:
                face_pattern.append(False)
        pattern.append(face_pattern)
    print(f"red edge pattern: {pattern}")
    return pattern

def match_pll_case(pattern, green_pattern, red_pattern):
    # match the side edge pattern to a PLL case

    if ((pattern == [[False, False, False], [True, True, False], [True, False, True], [False, True, True]]
        and (green_pattern == [
            [True, True, False], 
            [False, False, True], 
            [False, False, False], 
            [False, False, False]
        ] or green_pattern == [
            [False, False, True],
            [False, False, False],
            [False, True, False],
            [True, False, False]
        ])) or (pattern == [[True, True, True], [False, False, True], [False, True, False], [True, False, False]]
        and (red_pattern == [
            [True, True, False], 
            [False, False, True], 
            [False, False, False], 
            [False, False, False]
        ] or red_pattern == [
            [False, False, True],
            [False, False, False],
            [False, True, False],
            [True, False, False]
        ]))):
        return "Aa"
    
    if ((pattern == [[False, False, True], [False, True, False], [True, False, False], [True, True, True]]
        and (green_pattern == [
            [True, True, False], 
            [False, False, False], 
            [False, False, True], 
            [False, False, False]
        ] or green_pattern == [
            [False, False, False],
            [True, False, True],
            [False, True, False],
            [False, False, False]
        ])) or (pattern == [[True, True, False], [True, False, True], [False, True, True], [False, False, False]]
        and (red_pattern == [
            [True, True, False], 
            [False, False, False], 
            [False, False, True], 
            [False, False, False]
        ] or red_pattern == [
            [False, False, False],
            [True, False, True],
            [False, True, False],
            [False, False, False]
        ]))):
        return "Ab"
    
    if ((pattern == [[False, True, False], [True, False, True], [False, True, False], [True, False, True]]
        and (green_pattern == [
            [True, False, False], 
            [False, True, False], 
            [False, False, True], 
            [False, False, False]
        ] or green_pattern == [
            [False, False, True],
            [False, False, False],
            [True, False, False],
            [False, True, False]
        ])) or (pattern == [[True, False, True], [False, True, False], [True, True, True], [False, True, False]]
        and (red_pattern == [
            [True, False, False], 
            [False, True, False], 
            [False, False, True], 
            [False, False, False]
        ] or red_pattern == [
            [False, False, True],
            [False, False, False],
            [True, False, False],
            [False, True, False]
        ]))):
        return "E"
    
    if ((pattern == [[True, True, True], [False, False, True], [False, True, False], [True, False, False]]
        and (green_pattern == [
            [False, False, False], 
            [True, False, False], 
            [False, False, True], 
            [False, True, False]
        ] or green_pattern == [
            [False, False, False],
            [False, True, False],
            [True, False, False],
            [False, False, True]
        ])) or (pattern == [[False, False, False], [True, True, False], [True, False, True], [False, True, True]]
        and (red_pattern == [
            [False, False, False], 
            [True, False, False], 
            [False, False, True], 
            [False, True, False]
        ] or red_pattern == [
            [False, False, False],
            [False, True, False],
            [True, False, False],
            [False, False, True]
        ]))):
        return "F"
    
    if ((pattern == [[False, True, True], [False, True, False], [True, False, False], [True, False, True]]
        and (green_pattern == [
            [True, False, False], 
            [False, False, True], 
            [False, True, False], 
            [False, False, False]
        ] or green_pattern == [
            [False, False, False],
            [True, False, False],
            [False, False, True],
            [False, True, False]
        ])) or (pattern == [[True, False, False], [True, False, True], [False, True, True], [False, True, False]]
        and (red_pattern == [
            [True, False, False], 
            [False, False, True], 
            [False, True, False], 
            [False, False, False]
        ] or red_pattern == [
            [False, False, False],
            [True, False, False],
            [False, False, True],
            [False, True, False]
        ]))):
        return "Ga"
    
    if ((pattern == [[False, False, True], [False, False, False], [True, True, False], [True, True, True]]
        and (green_pattern == [
            [True, False, False], 
            [False, True, True], 
            [False, False, False], 
            [False, False, False]
        ] or green_pattern == [
            [False, True, False],
            [True, False, False],
            [False, False, True],
            [False, False, False]
        ])) or (pattern == [[True, True, False], [True, True, True], [False, False, True], [False, False, False]]
        and (red_pattern == [
            [True, False, False], 
            [False, True, True], 
            [False, False, False], 
            [False, False, False]
        ] or red_pattern == [
            [False, True, False],
            [True, False, False],
            [False, False, True],
            [False, False, False]
        ]))):
        return "Gb"
    
    if ((pattern == [[False, False, True], [False, True, False], [True, True, False], [True, False, True]]
        and (green_pattern == [
            [True, False, False], 
            [False, False, True], 
            [False, False, False], 
            [False, True, False]
        ] or green_pattern == [
            [False, True, False],
            [True, False, False],
            [False, False, True],
            [False, False, False]
        ])) or (pattern == [[True, True, False], [True, False, True], [False, False, True], [False, True, False]]
        and (red_pattern == [
            [True, False, False], 
            [False, False, True], 
            [False, False, False], 
            [False, True, False]
        ] or red_pattern == [
            [False, True, False],
            [True, False, False],
            [False, False, True],
            [False, False, False]
        ]))):
        return "Gc"
    
    if ((pattern == [[False, True, True], [False, False, False], [True, False, False], [True, True, True]]
        and (green_pattern == [
            [True, False, False], 
            [False, False, True], 
            [False, True, False], 
            [False, False, False]
        ] or green_pattern == [
            [False, False, False],
            [True, True, False],
            [False, False, True],
            [False, False, False]
        ])) or (pattern == [[True, False, False], [True, True, True], [False, True, True], [False, False, False]]
        and (red_pattern == [
            [True, False, False], 
            [False, False, True], 
            [False, True, False], 
            [False, False, False]
        ] or red_pattern == [
            [False, False, False],
            [True, True, False],
            [False, False, True],
            [False, False, False]
        ]))):
        return "Gd"
    
    if ((pattern == [[False, False, False], [True, True, True], [False, False, False], [True, True, True]]
        and (green_pattern == [
            [True, False, True], 
            [False, False, False], 
            [False, True, False], 
            [False, False, False]
        ] or green_pattern == [
            [False, True, False],
            [False, False, False],
            [True, False, True],
            [False, False, False]
        ])) or (pattern == [[True, True, True], [False, False, False], [True, True, True], [False, False, False]]
        and (red_pattern == [
            [True, False, True], 
            [False, False, False], 
            [False, True, False], 
            [False, False, False]
        ] or red_pattern == [
            [False, True, False],
            [False, False, False],
            [True, False, True],
            [False, False, False]
        ]))):
        return "H"
    
    if ((pattern == [[True, True, False], [True, True, True], [False, False, True], [False, False, False]]
        and (green_pattern == [
            [False, False, False], 
            [False, False, False], 
            [True, True, False], 
            [False, False, True]
        ] or green_pattern == [
            [False, False, True],
            [False, False, False],
            [False, False, False],
            [True, True, False]
        ])) or (pattern == [[False, False, True], [False, False, False], [True, True, False], [True, True, True]]
        and (red_pattern == [
            [False, False, False], 
            [False, False, False], 
            [True, True, False], 
            [False, False, True]
        ] or red_pattern == [
            [False, False, True],
            [False, False, False],
            [False, False, False],
            [True, True, False]
        ]))):
        return "Ja"
    
    if ((pattern == [[True, False, False], [True, True, True], [False, True, True], [False, False, False]]
        and (green_pattern == [
            [False, True, True], 
            [False, False, False], 
            [True, False, False], 
            [False, False, False]
        ] or green_pattern == [
            [False, False, False],
            [False, False, False],
            [False, False, False],
            [True, True, True]
        ])) or (pattern == [[False, True, True], [False, False, False], [True, False, False], [True, True, True]]
        and (red_pattern == [
            [False, True, True], 
            [False, False, False], 
            [True, False, False], 
            [False, False, False]
        ] or red_pattern == [
            [False, False, False],
            [False, False, False],
            [False, False, False],
            [True, True, True]
        ]))):
        return "Jb"
    
    if ((pattern == [[False, False, False], [True, True, True], [False, False, False], [True, True, True]]
        and (green_pattern == [
            [False, True, True], 
            [False, False, False], 
            [True, False, False], 
            [False, False, False]
        ] or green_pattern == [
            [True, False, False],
            [False, False, False],
            [False, True, True],
            [False, False, False]
        ])) or (pattern == [[True, True, True], [False, False, False], [True, True, True], [False, False, False]]
        and (red_pattern == [
            [False, True, True], 
            [False, False, False], 
            [True, False, False], 
            [False, False, False]
        ] or red_pattern == [
            [False, False, False],
            [False, False, False],
            [False, False, False],
            [True, True, True]
        ]))):
        return "Na"
    
    if ((pattern == [[False, False, False], [True, True, True], [False, False, False], [True, True, True]]
        and (green_pattern == [
            [True, True, False], 
            [False, False, False], 
            [False, False, True], 
            [False, False, False]
        ] or green_pattern == [
            [False, False, True],
            [False, False, False],
            [True, True, False],
            [False, False, False]
        ])) or (pattern == [[True, True, True], [False, False, False], [True, True, True], [False, False, False]]
        and (red_pattern == [
            [True, True, False], 
            [False, False, False], 
            [False, False, True], 
            [False, False, False]
        ] or red_pattern == [
            [False, False, True],
            [False, False, False],
            [True, True, False],
            [False, False, False]
        ]))):
        return "Nb"
    
    if ((pattern == [[False, True, False], [True, True, False], [True, False, True], [False, False, True]]
        and (green_pattern == [
            [False, False, False], 
            [False, False, True], 
            [False, True, False], 
            [True, False, False]
        ] or green_pattern == [
            [True, False, True],
            [False, False, False],
            [False, False, False],
            [False, True, False]
        ])) or (pattern == [[True, False, True], [False, False, True], [False, True, False], [True, True, False]]
        and (red_pattern == [
            [False, False, False], 
            [False, False, True], 
            [False, True, False], 
            [True, False, False]
        ] or red_pattern == [
            [True, False, True],
            [False, False, False],
            [False, False, False],
            [False, True, False]
        ]))):
        return "Ra"
    
    if ((pattern == [[True, False, True], [False, True, True], [False, True, False], [True, False, False]]
        and (green_pattern == [
            [False, True, False], 
            [True, False, False], 
            [False, False, True], 
            [False, False, False]
        ] or green_pattern == [
            [False, False, False],
            [False, False, False],
            [True, False, False],
            [False, True, True]
        ])) or (pattern == [[False, True, False], [True, False, False], [True, False, True], [False, True, True]]
        and (red_pattern == [
            [False, True, False], 
            [True, False, False], 
            [False, False, True], 
            [False, False, False]
        ] or red_pattern == [
            [False, False, False],
            [False, False, False],
            [True, False, False],
            [False, True, True]
        ]))):
        return "Rb"
    
    if ((pattern == [[False, False, True], [False, True, False], [True, False, False], [True, True, True]]
        and (green_pattern == [
            [True, True, False], 
            [False, False, True], 
            [False, False, False], 
            [False, False, False]
        ] or green_pattern == [
            [False, False, False],
            [True, False, False],
            [False, True, True],
            [False, False, False]
        ])) or (pattern == [[True, True, False], [True, False, True], [False, True, True], [False, False, False]]
        and (red_pattern == [
            [True, True, False], 
            [False, False, True], 
            [False, False, False], 
            [False, False, False]
        ] or red_pattern == [
            [False, False, False],
            [True, False, False],
            [False, True, True],
            [False, False, False]
        ]))):
        return "T"
    
    if ((pattern == [[False, False, False], [True, False, True], [False, True, False], [True, True, True]]
        and (green_pattern == [
            [True, True, True], 
            [False, False, False], 
            [False, False, False], 
            [False, False, False]
        ] or green_pattern == [
            [False, False, False],
            [False, True, False],
            [True, False, True],
            [False, False, False]
        ])) or (pattern == [[True, True, True], [False, True, False], [True, False, True], [False, False, False]]
        and (red_pattern == [
            [True, True, True], 
            [False, False, False], 
            [False, False, False], 
            [False, False, False]
        ] or red_pattern == [
            [False, False, False],
            [False, True, False],
            [True, False, True],
            [False, False, False]
        ]))):
        return "Ua"
    
    if ((pattern == [[False, False, False], [True, True, True], [False, True, False], [True, False, True]]
        and (green_pattern == [
            [True, True, True], 
            [False, False, False], 
            [False, False, False], 
            [False, False, False]
        ] or green_pattern == [
            [False, False, False],
            [False, False, False],
            [True, False, True],
            [False, True, False]
        ])) or (pattern == [[True, True, True], [False, False, False], [True, False, True], [False, True, False]]
        and (red_pattern == [
            [True, True, True], 
            [False, False, False], 
            [False, False, False], 
            [False, False, False]
        ] or red_pattern == [
            [False, False, False],
            [False, False, False],
            [True, False, True],
            [False, True, False]
        ]))):
        return "Ub"
    
    if ((pattern == [[False, False, False], [True, False, True], [False, True, False], [True, True, True]]
        and (green_pattern == [
            [True, True, False], 
            [False, False, False], 
            [False, False, True], 
            [False, False, False]
        ] or green_pattern == [
            [False, False, True],
            [False, True, False],
            [True, False, False],
            [False, False, False]
        ])) or (pattern == [[True, True, True], [False, True, False], [True, False, True], [False, False, False]]
        and (red_pattern == [
            [True, True, False], 
            [False, False, False], 
            [False, False, True], 
            [False, False, False]
        ] or red_pattern == [
            [False, False, True],
            [False, True, False],
            [True, False, False],
            [False, False, False]
        ]))):
        return "V"
    
    if ((pattern == [[False, False, False], [True, True, True], [False, True, False], [True, False, True]]
        and (green_pattern == [
            [True, True, False], 
            [False, False, False], 
            [False, False, True], 
            [False, False, False]
        ] or green_pattern == [
            [False, False, True],
            [False, False, False],
            [True, False, False],
            [False, True, False]
        ])) or (pattern == [[True, True, True], [False, False, False], [True, False, True], [False, True, False]]
        and (red_pattern == [
            [True, True, False], 
            [False, False, False], 
            [False, False, True], 
            [False, False, False]
        ] or red_pattern == [
            [False, False, True],
            [False, False, False],
            [True, False, False],
            [False, True, False]
        ]))):
        return "Y"
    
    if ((pattern == [[False, True, False], [True, False, True], [False, True, False], [True, False, True]]
        and (green_pattern == [
            [False, False, False], 
            [False, False, False], 
            [True, False, True], 
            [False, True, False]
        ] or green_pattern == [
            [True, False, True],
            [False, True, False],
            [False, False, False],
            [False, False, False]
        ])) or (pattern == [[True, False, True], [False, True, False], [True, False, True], [False, True, False]]
        and (red_pattern == [
            [False, False, False], 
            [False, False, False], 
            [True, False, True], 
            [False, True, False]
        ] or red_pattern == [
            [True, False, True],
            [False, True, False],
            [False, False, False],
            [False, False, False]
        ]))):
        return "Z"
    
    if (pattern == [[False, False, False], [True, True, True], [False, False, False], [True, True, True]]
        and green_pattern == [
            [True, True, True], 
            [False, False, False], 
            [False, False, False], 
            [False, False, False]
        ]):
        return "PLL Solved"
    
    return None