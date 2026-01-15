import kociemba



def solve_cube(cube, method):
    # Takes a cube and a solving method, returns a list of moves to solve the cube
    if method == "KOCIEMBA":
        return solve_kociemba(cube)
    elif method == "CFOP":
        return solve_cfop(cube)

def solve_kociemba(cube):
    cube_string = cube_to_kociemba_string(cube)

    try:
        solution = kociemba.solve(cube_string)
    except Exception as e:
        raise ValueError("Cube is not solvable") from e

    return solution

def solve_cfop(cube):
    # placeholder
    return

def cube_to_string(cube):
    # Converts the cube dictionary to a string representation
    order = ["U", "R", "F", "D", "L", "B"]
    result = ""

    for face in order:
        for row in cube[face]:
            for tile in row:
                result += tile

    return result

def cube_to_kociemba_string(cube):
    # Converts a cube to Kociemba format
    order = ["U", "R", "F", "D", "L", "B"]
    cube_string = ""

    for face in order:
        for row in cube[face]:
            for tile in row:
                cube_string += tile

    convert = {
        'W': 'U',
        'R': 'R',
        'G': 'F',
        'Y': 'D',
        'O': 'L',
        'B': 'B'
    }
    kociemba_string = ""
    for char in cube_string:
        kociemba_string += convert[char]

    print(kociemba_string)    
    return kociemba_string

def is_solved(cube):
    # Checks if the cube is in a solved state
    for face in cube:
        colour = cube[face][1][1]
        for row in cube[face]:
            for sticker in row:
                if sticker != colour:
                    return False
    return True
