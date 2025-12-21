
VALID_COLOURS = {"W", "Y", "R", "O", "G", "B"}
EXPECTED_FACES = {"U", "D", "F", "B", "L", "R"}

def validate_cube(cube):
    if not isinstance(cube, dict):
        return False, "Cube is not a dictionary"

    if set(cube.keys()) != EXPECTED_FACES:
        return False, "Cube does not contain exactly 6 faces"

    colour_count = {
        "W": 0, "Y": 0, "R": 0,
        "O": 0, "G": 0, "B": 0
    }

    for face in cube:
        if len(cube[face]) != 3:
            return False, f"Face {face} does not have 3 rows"

        for row in cube[face]:
            if len(row) != 3:
                return False, f"Face {face} does not have 3 columns"

            for tile in row:
                if tile == "x":
                    return False, "Cube is incomplete"

                if tile not in VALID_COLOURS:
                    return False, f"Invalid colour: {tile}"

                colour_count[tile] += 1

    for colour in colour_count:
        if colour_count[colour] != 9:
            return False, f"Incorrect number of {colour} tiles"

    return True, "Cube is valid"
