# cfop.py
import copy
from main import apply_move



def solve_cfop(cube):
    # solves the cube using the CFOP method
    moves=[]

    cross_moves = solve_cross(cube)
    print("Cross moves:", cross_moves)
    f2l_moves = solve_f2l(cube)
    print("F2L moves:", f2l_moves)
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
    [("U", 2, 2), ("R", 0, 0), ("F", 0, 2)], # UFR
    [("U", 2, 0), ("F", 0, 0), ("L", 0, 2)], # UFL
    [("U", 0, 0), ("L", 0, 0), ("B", 0, 2)], # UBL
    [("U", 0, 2), ("B", 0, 0), ("R", 0, 2)], # UBR
    [("D", 0, 2), ("F", 2, 2), ("R", 2, 0)], # DFR (Slot: red-green)
    [("D", 0, 0), ("L", 2, 2), ("F", 2, 0)], # DFL (Slot: orange-green)
    [("D", 2, 0), ("B", 2, 2), ("L", 2, 0)], # DBL (Slot: orange-blue)
    [("D", 2, 2), ("R", 2, 2), ("B", 2, 0)], # DBR (Slot: red-blue)
]

# Edges are sets of 2 coordinates
EDGE_LOCATIONS = [
    [("U", 2, 1), ("F", 0, 1)], [("U", 1, 2), ("R", 0, 1)], # UF, UR
    [("U", 0, 1), ("B", 0, 1)], [("U", 1, 0), ("L", 0, 1)], # UB, UL
    [("D", 0, 1), ("F", 2, 1)], [("D", 1, 2), ("R", 2, 1)], # DF, DR
    [("D", 2, 1), ("B", 2, 1)], [("D", 1, 0), ("L", 2, 1)], # DB, DL
    [("F", 1, 2), ("R", 1, 0)], [("R", 1, 2), ("B", 1, 0)], # FR, RB
    [("B", 1, 2), ("L", 1, 0)], [("L", 1, 2), ("F", 1, 0)], # BL, LF
]

def get_specific_pair(cube, slot_name):
    """Finds the current coordinates of a specific corner and edge pair."""
    mapping = {
        "red-green":   {'Y', 'R', 'G'},
        "orange-green":{'Y', 'O', 'G'},
        "red-blue":    {'Y', 'R', 'B'},
        "orange-blue": {'Y', 'O', 'B'},
    }
    target_c = mapping[slot_name]
    target_e = target_c - {'Y'}

    found_c = next(coords for coords in CORNER_LOCATIONS if {cube[f][r][c] for f, r, c in coords} == target_c)
    found_e = next(coords for coords in EDGE_LOCATIONS if {cube[f][r][c] for f, r, c in coords} == target_e)
    return found_c, found_e

def move_pair_to_top(cube, slot_name):
    """Brings the corner and edge of a slot to the U layer if they are trapped below."""
    moves = []

    def execute(m_list):
        for m in m_list:
            apply_move(m, cube)
            moves.append(m)

    # 1. Handle Corner
    c_pos, _ = get_specific_pair(cube, slot_name)
    if all(face != "U" for face, r, c in c_pos):
        # Find which D-face coordinate it has to know which slot it's in
        d_coord = next(coord for coord in c_pos if coord[0] == "D")
        if d_coord == ("D", 0, 2): execute(["R", "U", "Rprime"])       # From FR
        elif d_coord == ("D", 0, 0): execute(["Fprime", "Uprime", "F"]) # From FL
        elif d_coord == ("D", 2, 2): execute(["Bprime", "Uprime", "B"]) # From BR
        elif d_coord == ("D", 2, 0): execute(["L", "U", "Lprime"])       # From BL

    # 2. Handle Edge (re-scan in case it moved)
    _, e_pos = get_specific_pair(cube, slot_name)
    if all(face != "U" for face, r, c in e_pos):
        # Clear the top space so we don't kick the corner back down
        execute(["U"])
        
        # Check middle layer positions
        if ("F", 1, 2) in e_pos or ("R", 1, 0) in e_pos: execute(["R", "U", "Rprime"])
        elif ("L", 1, 2) in e_pos or ("F", 1, 0) in e_pos: execute(["F", "U", "Fprime"])
        elif ("R", 1, 2) in e_pos or ("B", 1, 0) in e_pos: execute(["B", "U", "Bprime"])
        elif ("B", 1, 2) in e_pos or ("L", 1, 0) in e_pos: execute(["L", "U", "Lprime"])

    return moves

def solve_f2l(cube):
    """Main F2L sequence."""
    all_f2l_moves = []
    
    # We will solve one pair as the 'Next Step'
    target_slot = "red-green"
    
    print(f"Setting up F2L pair for: {target_slot}")
    setup_moves = move_pair_to_top(cube, target_slot)
    all_f2l_moves.extend(setup_moves)
    
    return all_f2l_moves

def is_f2l_solved(cube):
    """Checks if the first two layers (D and middle) are solved."""
    side_faces = ["F", "R", "B", "L"]
    # Check D face is all Yellow
    for r in range(3):
        for c in range(3):
            if cube["D"][r][c] != 'Y': return False

    # Check bottom and middle rows of side faces
    for face in side_faces:
        center = cube[face][1][1]
        for row in [1, 2]: # Row 1 (middle), Row 2 (bottom)
            for col in range(3):
                if cube[face][row][col] != center: return False
    return True