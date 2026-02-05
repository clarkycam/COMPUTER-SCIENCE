# cfop.py
import copy
from main import apply_move



def solve_cfop(cube):
    # solves the cube using the CFOP method
    moves=[]

    cross_moves = solve_cross(cube)
    f2l_moves = solve_f2l(cube)
    oll_moves = []  # Placeholder for OLL moves
    pll_moves = []  # Placeholder for PLL moves
    
    moves.extend(cross_moves)
    moves.extend(f2l_moves)
    moves.extend(oll_moves)
    moves.extend(pll_moves)
    return moves




# --- Solve Cross ---

MOVES = ["U", "Uprime", "U2", "D", "Dprime", "D2", 
         "L", "Lprime", "L2", "R", "Rprime", "R2", 
         "F", "Fprime", "F2", "B", "Bprime", "B2"]

INVERSE = {
    "U": "Uprime", "Uprime": "U", "U2": "U2",
    "D": "Dprime", "Dprime": "D", "D2": "D2",
    "L": "Lprime", "Lprime": "L", "L2": "L2",
    "R": "Rprime", "Rprime": "R", "R2": "R2",
    "F": "Fprime", "Fprime": "F", "F2": "F2",
    "B": "Bprime", "Bprime": "B", "B2": "B2"
}

def is_cross_solved(cube):
    # checks if white cross is solved and aligned with centers
    if cube["D"][0][1] != 'Y' or cube["D"][1][0] != 'Y' or cube["D"][1][2] != 'Y' or cube["D"][2][1] != 'Y':
        return False
    if cube["F"][2][1] != cube["F"][1][1]: return False 
    if cube["R"][2][1] != cube["R"][1][1]: return False 
    if cube["B"][2][1] != cube["B"][1][1]: return False 
    if cube["L"][2][1] != cube["L"][1][1]: return False 
    return True

def get_cross_estimate(cube):
    # counts how many white edges arent on the top face
    misplaced = 0

    if cube["D"][0][1] != 'Y': misplaced += 1
    if cube["D"][1][0] != 'Y': misplaced += 1
    if cube["D"][1][2] != 'Y': misplaced += 1
    if cube["D"][2][1] != 'Y': misplaced += 1
    
    return misplaced

def solve_cross(cube):
    if is_cross_solved(cube):
        return []

    # IDA* Search
    for threshold in range(1, 9):
        print(f"Searching depth {threshold}...")
        found, path = search(cube, 0, threshold, [])
        if found:
            return path
    return []

def search(cube, g, threshold, path):
    # g: moves already made
    # threshold: max allowed moves for this iteration
    h = get_cross_estimate(cube)
    f = g + h # Total estimated cost
    
    if f > threshold:
        return False, []
    if is_cross_solved(cube):
        return True, path

    for move in MOVES:
        # dont repeat same face move
        if path:
            if path[-1][0] == move[0]: continue
            
        apply_move(move, cube)
        found, res = search(cube, g + 1, threshold, path + [move])
        if found: return True, res
        apply_move(INVERSE[move], cube) # backtrack

    return False, []



# --- Solve F2L ---

# Corners are sets of 3 coordinates (Face, Row, Col)
CORNER_LOCATIONS = [
    [("U", 0, 0), ("B", 0, 2), ("L", 0, 0)],
    [("U", 0, 2), ("B", 0, 0), ("R", 0, 2)],
    [("U", 2, 0), ("F", 0, 0), ("L", 0, 2)],
    [("U", 2, 2), ("F", 0, 2), ("R", 0, 0)],
    [("D", 0, 0), ("F", 2, 0), ("L", 2, 2)],
    [("D", 0, 2), ("F", 2, 2), ("R", 2, 0)],
    [("D", 2, 0), ("B", 2, 2), ("L", 2, 0)],
    [("D", 2, 2), ("B", 2, 0), ("R", 2, 2)],
]

# Edges are sets of 2 coordinates
EDGE_LOCATIONS = [
    [("U", 0, 1), ("B", 0, 1)], [("U", 1, 0), ("L", 0, 1)],
    [("U", 1, 2), ("R", 0, 1)], [("U", 2, 1), ("F", 0, 1)],
    [("D", 0, 1), ("F", 2, 1)], [("D", 1, 0), ("L", 2, 1)],
    [("D", 1, 2), ("R", 2, 1)], [("D", 2, 1), ("B", 2, 1)],
    [("F", 1, 0), ("L", 1, 2)], [("F", 1, 2), ("R", 1, 0)],
    [("B", 1, 0), ("R", 1, 2)], [("B", 1, 2), ("L", 1, 0)],
]

def solve_f2l(cube):
    # placeholder function for F2L solving
    identify_f2l_pairs(cube)
    return []

def is_f2l_solved(cube):
    # checks if the first two layers are solved
    side_faces = ["F", "R", "B", "L"]

    for face in side_faces:
        centre_colour = cube[face][1][1]

        # check middle and top rows
        for row in [0, 1]:
            for col in range(3):
                if cube[face][row][col] != centre_colour:
                    print("F2L is not solved")
                    return False
                
    print("F2L is solved")
    return True

def identify_f2l_pairs(cube):
    # Mapping slots to the colors they need
    slot_targets = [
        {"name": "orange-blue", "colors": {'Y', 'O', 'B'}},
        {"name": "red-blue",    "colors": {'Y', 'R', 'B'}},
        {"name": "red-green",   "colors": {'Y', 'R', 'G'}},
        {"name": "orange-green","colors": {'Y', 'O', 'G'}},
    ]

    for target in slot_targets:
        found_corner = None
        found_edge = None
        
        # Finding the Corner
        for coords in CORNER_LOCATIONS:
            current_colors = {cube[f][r][c] for f, r, c in coords}
            if current_colors == target['colors']:
                found_corner = coords
                break
        
        #Finding the Edge
        edge_colors_needed = target['colors'] - {'Y'}
        for coords in EDGE_LOCATIONS:
            current_colors = {cube[f][r][c] for f, r, c in coords}
            if current_colors == edge_colors_needed:
                found_edge = coords
                break
        
        print(f"slot {target['name']}: corner:{found_corner} edge:{found_edge}\n")

