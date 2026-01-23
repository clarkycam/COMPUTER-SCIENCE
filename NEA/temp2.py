import copy
from main import apply_move

# Full 18-move set (Half-Turn Metric)
MOVES = ["U", "Uprime", "U2", "D", "Dprime", "D2", 
         "L", "Lprime", "L2", "R", "Rprime", "R2", 
         "F", "Fprime", "F2", "B", "Bprime", "B2"]

# Inverses to "undo" moves during backtracking
INVERSE = {
    "U": "Uprime", "Uprime": "U", "U2": "U2",
    "D": "Dprime", "Dprime": "D", "D2": "D2",
    "L": "Lprime", "Lprime": "L", "L2": "L2",
    "R": "Rprime", "Rprime": "R", "R2": "R2",
    "F": "Fprime", "Fprime": "F", "F2": "F2",
    "B": "Bprime", "Bprime": "B", "B2": "B2"
}

def solve_cfop(cube):
    # Only returning Cross for now as requested
    return solve_cross(cube)

def is_cross_solved(cube):
    """Checks if White Cross is solved and aligned with centers."""
    # Assuming 'U' is the White face
    # 1. Check top stickers are White
    if cube["U"][0][1] != 'W' or cube["U"][1][0] != 'W' or \
       cube["U"][1][2] != 'W' or cube["U"][2][1] != 'W':
        return False
    
    # 2. Check side alignment (Edge sticker matches side center)
    if cube["F"][0][1] != cube["F"][1][1]: return False # Green
    if cube["R"][0][1] != cube["R"][1][1]: return False # Red
    if cube["B"][0][1] != cube["B"][1][1]: return False # Blue
    if cube["L"][0][1] != cube["L"][1][1]: return False # Orange
    
    return True

def solve_cross(cube):
    """IDDFS Solver for the white cross."""
    if is_cross_solved(cube):
        return []

    # Iteratively increase depth from 1 to 8
    for depth in range(1, 9):
        print(f"Searching depth {depth}...")
        found, path = depth_limited_search(cube, depth, [])
        if found:
            return path
    return []

def depth_limited_search(cube, depth, path):
    if is_cross_solved(cube):
        return True, path
    
    if depth <= 0:
        return False, []

    for move in MOVES:
        # Optimization: Don't turn the same face twice (e.g., skip R2 if last move was R)
        if path and path[-1][0] == move[0]:
            continue
            
        # Apply the move to the cube object
        apply_move(move, cube)
        
        # Search deeper
        found, result_path = depth_limited_search(cube, depth - 1, path + [move])
        
        if found:
            return True, result_path
            
        # BACKTRACK: Undo the move to restore the cube for the next attempt
        apply_move(INVERSE[move], cube)
        
    return False, []