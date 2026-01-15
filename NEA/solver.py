def solve_cube(cube, method):
    # Takes a cube and a solving method, returns a list of moves to solve the cube.
    if method == "KOCIEMBA":
        return solve_kociemba(cube)
    elif method == "CFOP":
        return solve_cfop(cube)

def solve_kociemba(cube):
    # placeholder
    return

def solve_cfop(cube):
    # placeholder
    return

def cube_to_string(cube):
    # Converts the cube dictionary to a string representation for solvers.
    order = ["U", "R", "F", "D", "L", "B"]
    result = ""

    for face in order:
        for row in cube[face]:
            for tile in row:
                result += tile

    return result

def is_solved(cube):
    # Checks if the cube is in a solved state.
    for face in cube:
        colour = cube[face][1][1]
        for row in cube[face]:
            for sticker in row:
                if sticker != colour:
                    return False
    return True
