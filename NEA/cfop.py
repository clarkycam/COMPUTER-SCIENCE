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
    # checks if yellow cross is solved and aligned with centers
    if cube["D"][0][1] != 'Y' or cube["D"][1][0] != 'Y' or cube["D"][1][2] != 'Y' or cube["D"][2][1] != 'Y':
        return False
    if cube["F"][2][1] != cube["F"][1][1]: return False 
    if cube["R"][2][1] != cube["R"][1][1]: return False 
    if cube["B"][2][1] != cube["B"][1][1]: return False 
    if cube["L"][2][1] != cube["L"][1][1]: return False 
    return True

def get_cross_estimate(cube):
    # counts how many yellow edges aren't in the correct position on bottom face
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
        found, path = search(cube, 0, threshold, [])
        if found:
            print(f"Cross moves: {path}")
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
    pairs = identify_f2l_pairs(cube)
    moves = []
    
    # For now, just handle red-green slot
    rg_corner, rg_edge = pairs["red-green"]
    extraction_moves = move_pair_to_top(cube, rg_corner, rg_edge, "red-green")
    
    # Apply the moves to the cube
    for move in extraction_moves:
        apply_move(move, cube)
    
    # Verify both pieces are in top layer
    pairs_after = identify_f2l_pairs(cube)
    rg_corner_after, rg_edge_after = pairs_after["red-green"]
    
    corner_ok = is_in_top_layer(rg_corner_after)
    edge_ok = is_in_top_layer(rg_edge_after)
    
    if not corner_ok or not edge_ok:
        print(f"VERIFICATION FAILED - Corner in top: {corner_ok}, Edge in top: {edge_ok}")
        print(f"Corner coords: {rg_corner_after}")
        print(f"Edge coords: {rg_edge_after}")
        
        # Undo all the moves
        for move in reversed(extraction_moves):
            apply_move(INVERSE[move], cube)
        
        # Split extraction into corner and edge parts
        corner_moves = []
        edge_moves = []
        corner_in_bottom = not is_in_top_layer(rg_corner)
        edge_in_middle = is_in_middle_layer(rg_edge)
        
        if corner_in_bottom:
            corner_moves = extract_corner_to_top(rg_corner, "red-green")
        if edge_in_middle:
            edge_moves = extract_edge_to_top(rg_edge, "red-green")
        
        # Try adding U moves between corner and edge extraction
        u_variants = ["U", "U2", "Uprime"]
        success = False
        
        for u_move in u_variants:
            print(f"Trying with {u_move} between extractions...")
            
            # Build new extraction sequence
            new_extraction = corner_moves + [u_move] + edge_moves
            
            # Apply it
            for move in new_extraction:
                apply_move(move, cube)
            
            # Verify
            pairs_check = identify_f2l_pairs(cube)
            rg_corner_check, rg_edge_check = pairs_check["red-green"]
            corner_ok_check = is_in_top_layer(rg_corner_check)
            edge_ok_check = is_in_top_layer(rg_edge_check)
            
            if corner_ok_check and edge_ok_check:
                print(f"SUCCESS with {u_move} between extractions")
                extraction_moves = new_extraction
                success = True
                break
            else:
                print(f"Failed with {u_move} - Corner in top: {corner_ok_check}, Edge in top: {edge_ok_check}")
                # Undo for next attempt
                for move in reversed(new_extraction):
                    apply_move(INVERSE[move], cube)
        
        if not success:
            print("STILL FAILED after trying U moves between extractions")
            # Restore the original failed state for now
            for move in extraction_moves:
                apply_move(move, cube)
    else:
        print("VERIFICATION PASSED - Both pieces in top layer")
    
    moves.extend(extraction_moves)
    print(f"F2L moves: {extraction_moves}")
    
    return moves

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

    pairs = {}
    
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
        
        pairs[target['name']] = (found_corner, found_edge)
    
    return pairs


def is_in_top_layer(coords):
    """Check if piece coordinates are in the top (U) layer"""
    # If any coordinate is on D face, it's in the bottom layer
    for face, row, col in coords:
        if face == "D":
            return False
    
    # For side faces, check if any coordinate is on row 0 (top)
    for face, row, col in coords:
        if face == "U":
            return True
        if face in ["F", "R", "B", "L"] and row == 0:
            return True
    
    return False


def is_in_middle_layer(coords):
    """Check if edge piece is in the middle layer (not top or bottom)"""
    for face, row, col in coords:
        if face == "U" or face == "D":
            return False
        if row == 1:  # Middle row of side faces
            return True
    return False


def are_in_same_slot(corner_coords, edge_coords):
    """
    Check if corner (in bottom) and edge (in middle) are in the same F2L slot.
    Same slot means they share the same two side faces.
    """
    # Get the side faces for corner (exclude D face)
    corner_faces = set()
    for face, row, col in corner_coords:
        if face != "D":
            corner_faces.add(face)
    
    # Get the side faces for edge
    edge_faces = set()
    for face, row, col in edge_coords:
        edge_faces.add(face)
    
    # If they share the same two side faces, they're in the same slot
    return corner_faces == edge_faces




def move_pair_to_top(cube, corner_coords, edge_coords, slot_name):
    """
    Move both corner and edge pieces to the top layer.
    Returns list of moves to execute.
    """
    moves = []
    
    corner_in_bottom = not is_in_top_layer(corner_coords)
    edge_in_middle = is_in_middle_layer(edge_coords)
    edge_in_top = is_in_top_layer(edge_coords)
    
    # Check corner status
    if is_in_top_layer(corner_coords):
        print("Corner is already in top layer")
    else:
        print("Corner is NOT in top layer - needs extraction")
    
    # Check edge status
    if edge_in_top:
        print("Edge is already in top layer")
    elif edge_in_middle:
        print("Edge is in middle layer - needs extraction")
    else:
        print("Edge is NOT in top layer")
    
    # Extract corner first if it's in the bottom
    if corner_in_bottom:
        corner_moves = extract_corner_to_top(corner_coords, slot_name)
        moves.extend(corner_moves)
        print(f"Corner extraction moves: {corner_moves}")
    
    # Extract edge if needed
    if edge_in_middle:
        edge_moves = extract_edge_to_top(edge_coords, slot_name)
        moves.extend(edge_moves)
        print(f"Edge extraction moves: {edge_moves}")
    
    return moves


def extract_corner_to_top(corner_coords, slot_name):
    """
    Extract a corner from the bottom layer to top layer.
    Determines which slot it's in and applies appropriate extraction algorithm.
    """
    # Determine which bottom corner position this is
    # Red-Green slot corresponds to D-F-R corner: [("D", 0, 2), ("F", 2, 2), ("R", 2, 0)]
    
    print(f"DEBUG: Checking corner_coords: {corner_coords}")
    
    # Check which corner slot this is in
    if ("D", 0, 2) in corner_coords:  # Front-Right (Red-Green slot)
        # Extract from FR slot: R U Rprime
        print("Matched Front-Right slot")
        return ["R", "U", "Rprime"]
    elif ("D", 0, 0) in corner_coords:  # Front-Left (Orange-Green slot)
        # Extract from FL slot: Lprime Uprime L
        print("Matched Front-Left slot")
        return ["Lprime", "Uprime", "L"]
    elif ("D", 2, 2) in corner_coords:  # Back-Right (Red-Blue slot)
        # Extract from BR slot: Rprime Uprime R
        print("Matched Back-Right slot")
        return ["Rprime", "Uprime", "R"]
    elif ("D", 2, 0) in corner_coords:  # Back-Left (Orange-Blue slot)
        # Extract from BL slot: L U Lprime
        print("Matched Back-Left slot")
        return ["L", "U", "Lprime"]
    
    print("ERROR: No slot matched!")
    return []


def extract_edge_to_top(edge_coords, slot_name):
    """
    Extract an edge from the middle layer to top layer.
    Determines which middle edge position it's in and applies appropriate extraction.
    """
    # Middle layer edges are between side faces
    # Red-Green edge in middle: [("F", 1, 2), ("R", 1, 0)]
    
    # Check which middle edge slot this is in
    if ("F", 1, 2) in edge_coords and ("R", 1, 0) in edge_coords:  # Front-Right
        # Extract from FR middle: R U R'
        return ["R", "U", "Rprime"]
    elif ("F", 1, 0) in edge_coords and ("L", 1, 2) in edge_coords:  # Front-Left
        # Extract from FL middle: L' U' L
        return ["Lprime", "Uprime", "L"]
    elif ("B", 1, 0) in edge_coords and ("R", 1, 2) in edge_coords:  # Back-Right
        # Extract from BR middle: R' U' R
        return ["Rprime", "Uprime", "R"]
    elif ("B", 1, 2) in edge_coords and ("L", 1, 0) in edge_coords:  # Back-Left
        # Extract from BL middle: L U L'
        return ["L", "U", "Lprime"]
    
    return []