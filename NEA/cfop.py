import copy
from main import apply_move



# --- Solve Cross with IDA* Search ---
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
    if cube["U"][0][1] != 'W' or cube["U"][1][0] != 'W' or cube["U"][1][2] != 'W' or cube["U"][2][1] != 'W':
        return False
    if cube["F"][0][1] != cube["F"][1][1]: return False 
    if cube["R"][0][1] != cube["R"][1][1]: return False 
    if cube["B"][0][1] != cube["B"][1][1]: return False 
    if cube["L"][0][1] != cube["L"][1][1]: return False 
    return True

def get_cross_estimate(cube):
    # counts how many white edges arent on the top face
    misplaced = 0
    # List of the 4 target edge positions for white cross
    if cube["U"][0][1] != 'W': misplaced += 1
    if cube["U"][1][0] != 'W': misplaced += 1
    if cube["U"][1][2] != 'W': misplaced += 1
    if cube["U"][2][1] != 'W': misplaced += 1
    
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
        # Avoid redundant moves (e.g. R followed by R')
        if path:
            if path[-1][0] == move[0]: continue
            
        apply_move(move, cube)
        found, res = search(cube, g + 1, threshold, path + [move])
        if found: return True, res
        apply_move(INVERSE[move], cube) # Backtrack

    return False, []