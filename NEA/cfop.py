import copy
from main import apply_move
from f2l_cases import F2L_CASES, translate_algorithm, detect_f2l_case, align_corner_to_ufr



def solve_cfop(cube):
    # solves the cube using the CFOP method
    moves=[]

    cross_moves = solve_cross(cube)
    f2l_moves = solve_f2l(cube)
    oll_moves = solve_oll(cube)
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
    
    # ===== SOLVE RED-GREEN SLOT =====
    print("\n=== SOLVING RED-GREEN SLOT ===")
    rg_corner, rg_edge = pairs["red-green"]
    
    # Check if already solved before doing anything
    if is_pair_solved(cube, rg_corner, rg_edge, "red-green"):
        print("Red-green F2L pair is already solved - skipping")
    else:
        extraction_moves = move_pair_to_top(cube, rg_corner, rg_edge, "red-green")
        
        # Apply the moves to the cube
        for move in extraction_moves:
            apply_move(move, cube)
        
        # Verify both pieces are in top layer
        pairs_after = identify_f2l_pairs(cube)
        rg_corner_after, rg_edge_after = pairs_after["red-green"]
        
        # Check if solved after extraction
        if is_pair_solved(cube, rg_corner_after, rg_edge_after, "red-green"):
            print("F2L pair solved after extraction - verification skipped")
            moves.extend(extraction_moves)
            print(f"Red-green F2L moves: {extraction_moves}")
        else:
            corner_ok = is_in_top_layer(rg_corner_after)
            edge_ok = is_in_top_layer(rg_edge_after)

            if not corner_ok or not edge_ok:
                extraction_moves = verify_pair_in_top(cube, rg_corner_after, rg_edge_after, extraction_moves, "red-green")
            else:
                print("VERIFICATION PASSED - Both pieces in top layer")
            print(f"Red-green extraction moves: {extraction_moves}")

            
            # === STEP 2: INSERT THE PAIR INTO THE SLOT ===
            # Now both pieces are in top layer, detect which case and insert
            insertion_moves = insert_pair_into_slot(cube, rg_corner_after, rg_edge_after, "red-green")
            
            # Build final move list in correct order: extraction, alignment, insertion
            final_moves = extraction_moves + insertion_moves
            moves.extend(final_moves)
            print(f"Red-green F2L moves: {final_moves}")
    
    # Verify red-green slot is solved
    pairs_rg_verify = identify_f2l_pairs(cube)
    rg_corner_verify, rg_edge_verify = pairs_rg_verify["red-green"]
    if is_pair_solved(cube, rg_corner_verify, rg_edge_verify, "red-green"):
        print("✓ Red-green slot VERIFIED as solved")
    else:
        print("✗ WARNING: Red-green slot is NOT solved!")


    
    # ===== SOLVE ORANGE-GREEN SLOT =====
    print("\n=== SOLVING ORANGE-GREEN SLOT ===")
    pairs_og = identify_f2l_pairs(cube)
    og_corner, og_edge = pairs_og["orange-green"]
    
    # Check if already solved
    if is_pair_solved(cube, og_corner, og_edge, "orange-green"):
        print("Orange-green F2L pair is already solved - skipping extraction")
    else:
        og_extraction_moves = move_pair_to_top(cube, og_corner, og_edge, "orange-green")
        
        # Apply the moves to the cube
        for move in og_extraction_moves:
            apply_move(move, cube)
        
        # Verify both pieces are in top layer
        pairs_og_after = identify_f2l_pairs(cube)
        og_corner_after, og_edge_after = pairs_og_after["orange-green"]
        
        corner_ok_og = is_in_top_layer(og_corner_after)
        edge_ok_og = is_in_top_layer(og_edge_after)
        
        if corner_ok_og and edge_ok_og:
            print("✓ Orange-green pieces successfully extracted to top layer")
        else:
            og_extraction_moves = verify_pair_in_top(cube, og_corner_after, og_edge_after, og_extraction_moves, "orange-green")
        print(f"Orange-green extraction moves: {og_extraction_moves}")
    

        # ===== INSERT OG PAIR INTO SLOT =====
        og_insertion_moves = insert_pair_into_slot(cube, og_corner_after, og_edge_after, "orange-green")
        final_og_moves = og_extraction_moves + og_insertion_moves
        moves.extend(final_og_moves)
        print(f"Orange-green F2L moves: {final_og_moves}")
    
    # Verify orange-green slot is solved
    pairs_og_verify = identify_f2l_pairs(cube)
    og_corner_verify, og_edge_verify = pairs_og_verify["orange-green"]
    if is_pair_solved(cube, og_corner_verify, og_edge_verify, "orange-green"):
        print("✓ Orange-green slot VERIFIED as solved")
    else:
        print("✗ WARNING: Orange-green slot is NOT solved!")



    # ===== SOLVE RED-BLUE SLOT =====
    print("\n=== SOLVING RED-BLUE SLOT ===")
    pairs_rb = identify_f2l_pairs(cube)
    rb_corner, rb_edge = pairs_rb["red-blue"]
    
    # Check if already solved
    if is_pair_solved(cube, rb_corner, rb_edge, "red-blue"):
        print("Red-blue F2L pair is already solved - skipping extraction")
    else:
        rb_extraction_moves = move_pair_to_top(cube, rb_corner, rb_edge, "red-blue")
        
        # Apply the moves to the cube
        for move in rb_extraction_moves:
            apply_move(move, cube)
        
        # Verify both pieces are in top layer
        pairs_rb_after = identify_f2l_pairs(cube)
        rb_corner_after, rb_edge_after = pairs_rb_after["red-blue"]
        
        corner_ok_rb = is_in_top_layer(rb_corner_after)
        edge_ok_rb = is_in_top_layer(rb_edge_after)
        
        if corner_ok_rb and edge_ok_rb:
            print("✓ Red-blue pieces successfully extracted to top layer")
        else:
            rb_extraction_moves = verify_pair_in_top(cube, rb_corner_after, rb_edge_after, rb_extraction_moves, "red-blue")
        print(f"Red-blue extraction moves: {rb_extraction_moves}")
    

        # ===== INSERT RB PAIR INTO SLOT =====
        rb_insertion_moves = insert_pair_into_slot(cube, rb_corner_after, rb_edge_after, "red-blue")
        final_rb_moves = rb_extraction_moves + rb_insertion_moves
        moves.extend(final_rb_moves)
        print(f"Red-blue F2L moves: {final_rb_moves}")
    
    # Verify red-blue slot is solved
    pairs_rb_verify = identify_f2l_pairs(cube)
    rb_corner_verify, rb_edge_verify = pairs_rb_verify["red-blue"]
    if is_pair_solved(cube, rb_corner_verify, rb_edge_verify, "red-blue"):
        print("✓ Red-blue slot VERIFIED as solved")
    else:
        print("✗ WARNING: Red-blue slot is NOT solved!")



    # ==== SOLVE ORANGE-BLUE SLOT =====
    print("\n=== SOLVING ORANGE-BLUE SLOT ===")
    pairs_ob = identify_f2l_pairs(cube)
    ob_corner, ob_edge = pairs_ob["orange-blue"]

    # Check if already solved
    if is_pair_solved(cube, ob_corner, ob_edge, "orange-blue"):
        print("Orange-blue F2L pair is already solved - skipping extraction")
    else:
        ob_extraction_moves = move_pair_to_top(cube, ob_corner, ob_edge, "orange-blue")
        
        # Apply the moves to the cube
        for move in ob_extraction_moves:
            apply_move(move, cube)
        
        # Verify both pieces are in top layer
        pairs_ob_after = identify_f2l_pairs(cube)
        ob_corner_after, ob_edge_after = pairs_ob_after["orange-blue"]
        
        corner_ok_ob = is_in_top_layer(ob_corner_after)
        edge_ok_ob = is_in_top_layer(ob_edge_after)
        
        if corner_ok_ob and edge_ok_ob:
            print("✓ Orange-blue pieces successfully extracted to top layer")
        else:
            ob_extraction_moves = verify_pair_in_top(cube, ob_corner_after, ob_edge_after, ob_extraction_moves, "orange-blue")
        print(f"Orange-blue extraction moves: {ob_extraction_moves}")
    

        # ===== INSERT OB PAIR INTO SLOT =====
        ob_insertion_moves = insert_pair_into_slot(cube, ob_corner_after, ob_edge_after, "orange-blue")
        final_ob_moves = ob_extraction_moves + ob_insertion_moves
        moves.extend(final_ob_moves)
        print(f"Orange-blue F2L moves: {final_ob_moves}")
    
    # Verify orange-blue slot is solved
    pairs_ob_verify = identify_f2l_pairs(cube)
    ob_corner_verify, ob_edge_verify = pairs_ob_verify["orange-blue"]
    if is_pair_solved(cube, ob_corner_verify, ob_edge_verify, "orange-blue"):
        print("✓ Orange-blue slot VERIFIED as solved")
    else:
        print("✗ WARNING: Orange-blue slot is NOT solved!")



    print(f"\nTotal F2L moves: {moves}")
    return moves

def verify_pair_in_top(cube, corner_coords, edge_coords, extraction_moves, slot_name):
    corner_in_top = is_in_top_layer(corner_coords)
    edge_in_top = is_in_top_layer(edge_coords)
    
    if not corner_in_top or not edge_in_top:
        print(f"Verification failed for {slot_name} - Corner in top: {corner_in_top}, Edge in top: {edge_in_top}")
        print(f"Corner coords: {corner_coords}")
        print(f"Edge coords: {edge_coords}")
    
    #undo moves if verification failed
    for move in reversed(extraction_moves):
        apply_move(INVERSE[move], cube)

    #get new corner and edge coords after undoing
    pairs_after_undo = identify_f2l_pairs(cube)
    corner_after_undo, edge_after_undo = pairs_after_undo[slot_name]

    #determine what extractions we need based on the new positions
    corner_in_bottom = not is_in_top_layer(corner_after_undo)
    edge_in_middle = is_in_middle_layer(edge_after_undo)

    corner_moves = []
    if corner_in_bottom:
        corner_moves = extract_corner_to_top(corner_after_undo, slot_name)
    
    u_variants = ["U", "U2", "Uprime"]
    success = False

    for u_move in u_variants:
        print(f"Trying with {u_move} between corner and edge extraction...")
        for move in corner_moves:
            apply_move(move, cube)
        apply_move(u_move, cube)

        if corner_moves:
            pairs_check = identify_f2l_pairs(cube)
            _, edge_check = pairs_check[slot_name]
            edge_in_middle = is_in_middle_layer(edge_check)
            edge_coords_to_use = edge_check
        else:
            edge_coords_to_use = edge_after_undo
        
        edge_moves = []
        if edge_in_middle:
            edge_moves = extract_edge_to_top(edge_coords_to_use, slot_name)
        for move in edge_moves:
            apply_move(move, cube)
        
        #verify again
        pairs_verify = identify_f2l_pairs(cube)
        corner_verify, edge_verify = pairs_verify[slot_name]
        corner_ok_check = is_in_top_layer(corner_verify)
        edge_ok_check = is_in_top_layer(edge_verify)

        if corner_ok_check and edge_ok_check:
            print(f"SUCCESS with {u_move} between extractions")
            extraction_moves = corner_moves + [u_move] + edge_moves
            success = True
            break
        else:
            print(f"Failed with {u_move} - Corner in top: {corner_ok_check}, Edge in top: {edge_ok_check}")
            for move in reversed(edge_moves):
                apply_move(INVERSE[move], cube)
            apply_move(INVERSE[u_move], cube)
            for move in reversed(corner_moves):
                apply_move(INVERSE[move], cube)
    
    if not success:
        print("STILL FAILED after trying all U variants")
        for move in extraction_moves:
            apply_move(move, cube)
    
    return extraction_moves

def insert_pair_into_slot(cube, corner_coords, edge_coords, slot_name):
    pairs_for_insertion = identify_f2l_pairs(cube)
    corner_insert, edge_insert = pairs_for_insertion[slot_name]

    # Get corner position
    from f2l_cases import get_corner_u_position
    corner_pos = get_corner_u_position(corner_insert)
    print(f"DEBUG: Corner position before alignment: {corner_pos}, coords: {corner_insert}")

    # Align corner to UFR position if needed
    alignment_moves = align_corner_to_ufr(corner_pos, slot_name)
    if alignment_moves:
        print(f"Aligning corner to UFR with: {alignment_moves}")
        for move in alignment_moves:
            apply_move(move, cube)
    # ALWAYS re-identify pieces after potential alignment
    # This gives us the correct position AND orientation after alignment
    pairs_after_align = identify_f2l_pairs(cube)
    corner_final, edge_final = pairs_after_align[slot_name]

    # Detect which F2L case we're in (using FINAL positions after alignment)
    case_key = detect_f2l_case(cube, corner_final, edge_final, slot_name)
    if case_key:
        print(f"Detected F2L case: {case_key}")
        case_data = F2L_CASES[case_key]
        insertion_algorithm = case_data["algorithm"]
        translated_alg = translate_algorithm(insertion_algorithm, slot_name)
        print(f"Insertion algorithm: {translated_alg}")
        for move in translated_alg:
            apply_move(move, cube)
    else:
        print("ERROR: Could not detect F2L case during insertion!")
        translated_algorithm = []
    final_moves = (alignment_moves if alignment_moves else []) + (translated_alg if case_key else [])
    return final_moves


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


def is_pair_solved(cube, corner_coords, edge_coords, slot_name):
    """
    Check if an F2L pair is already solved (correctly placed AND oriented in its slot).
    """
    # Determine which slot we're checking
    slot_info = {
        "red-green": {
            "corner_pos": [("D", 0, 2), ("F", 2, 2), ("R", 2, 0)],
            "edge_pos": [("F", 1, 2), ("R", 1, 0)],
            "faces": ["F", "R"],
            "center_colors": None  # Will be filled from cube
        },
        "orange-green": {
            "corner_pos": [("D", 0, 0), ("F", 2, 0), ("L", 2, 2)],
            "edge_pos": [("F", 1, 0), ("L", 1, 2)],
            "faces": ["F", "L"],
            "center_colors": None
        },
        "red-blue": {
            "corner_pos": [("D", 2, 2), ("B", 2, 0), ("R", 2, 2)],
            "edge_pos": [("B", 1, 0), ("R", 1, 2)],
            "faces": ["B", "R"],
            "center_colors": None
        },
        "orange-blue": {
            "corner_pos": [("D", 2, 0), ("B", 2, 2), ("L", 2, 0)],
            "edge_pos": [("B", 1, 2), ("L", 1, 0)],
            "faces": ["B", "L"],
            "center_colors": None
        }
    }
    
    if slot_name not in slot_info:
        return False
    
    slot = slot_info[slot_name]
    
    # Check if corner is in correct position
    corner_coords_set = set(corner_coords)
    correct_corner_pos = set(slot["corner_pos"])
    if corner_coords_set != correct_corner_pos:
        return False
    
    # Check if edge is in correct position
    edge_coords_set = set(edge_coords)
    correct_edge_pos = set(slot["edge_pos"])
    if edge_coords_set != correct_edge_pos:
        return False
    
    # Check orientation: Yellow should be on bottom (D face) for corner
    yellow_on_bottom = False
    for face, row, col in corner_coords:
        if face == "D" and cube[face][row][col] == 'Y':
            yellow_on_bottom = True
            break
    
    if not yellow_on_bottom:
        return False
    
    # Check that edge colors match the center colors
    face1, face2 = slot["faces"]
    center1 = cube[face1][1][1]
    center2 = cube[face2][1][1]
    
    # Check if edge pieces match their respective center colors
    edge_colors_correct = True
    for face, row, col in edge_coords:
        piece_color = cube[face][row][col]
        if face == face1 and piece_color != center1:
            edge_colors_correct = False
        elif face == face2 and piece_color != center2:
            edge_colors_correct = False
    
    if not edge_colors_correct:
        return False
    
    # Check corner side colors match centers
    for face, row, col in corner_coords:
        if face in [face1, face2]:
            piece_color = cube[face][row][col]
            center_color = cube[face][1][1]
            if piece_color != center_color:
                return False
    
    return True




def move_pair_to_top(cube, corner_coords, edge_coords, slot_name):
    """
    Move both corner and edge pieces to the top layer.
    Returns list of moves to execute.
    NOTE: Does NOT apply moves to the cube - just returns them.
    """
    moves = []
    
    # First check if the pair is already solved in the slot
    if is_pair_solved(cube, corner_coords, edge_coords, slot_name):
        print("F2L pair is already solved - no extraction needed")
        return moves
    
    corner_in_bottom = not is_in_top_layer(corner_coords)
    edge_in_middle = is_in_middle_layer(edge_coords)
    
    # Check corner status
    if is_in_top_layer(corner_coords):
        print("Corner is already in top layer")
    else:
        print("Corner is NOT in top layer - needs extraction")
    
    # Check edge status
    if is_in_top_layer(edge_coords):
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
        
        # Simulate applying corner moves to check updated edge position
        cube_copy = copy.deepcopy(cube)
        for move in corner_moves:
            apply_move(move, cube_copy)
        
        # Re-check edge position after corner extraction
        pairs_updated = identify_f2l_pairs(cube_copy)
        _, edge_coords_updated = pairs_updated[slot_name]
        edge_in_middle = is_in_middle_layer(edge_coords_updated)
        edge_in_top = is_in_top_layer(edge_coords_updated)
        
        print(f"After corner extraction - Edge coords: {edge_coords_updated}")
        
        if edge_in_top:
            print("Edge is now in top layer after corner extraction - no edge extraction needed")
        elif edge_in_middle:
            print("Edge still in middle layer after corner extraction - needs extraction")
            edge_coords = edge_coords_updated  # Use updated coords for edge extraction
        else:
            print("WARNING: Edge was inserted into bottom layer during corner extraction!")
    
    # Extract edge if it's in middle layer
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


# --- Solve OLL ---

def solve_oll(cube):
    # Solves the OLL step by orienting all pieces in the top layer correctly.
    from oll_cases import is_oll_solved, get_white_top_positions, get_side_white_positions, match_oll_case, OLL_CASES
    
    moves = []
    max_iterations = 10
    iteration = 0
    
    print("\n=== SOLVING OLL ===")
    
    while not is_oll_solved(cube) and iteration < max_iterations:
        iteration += 1
        print(f"\nOLL Iteration {iteration}:")
        
        # Try to match a case with up to 3 U rotations
        case_name = None
        u_rotations = 0
        
        for attempt in range(4):
            # Get white positions
            white_grid = get_white_top_positions(cube)
            side_grid = get_side_white_positions(cube)
            
            # Try to match case
            case_name = match_oll_case(white_grid, side_grid)
            
            if case_name:
                print(f"Case '{case_name}' found after {u_rotations} U rotations")
                break
            
            # No match, try rotating U
            if attempt < 3:  # Don't rotate after the 4th attempt
                print(f"No case matched, trying U rotation {attempt + 1}")
                apply_move("U", cube)
                moves.append("U")
                u_rotations += 1
        
        if case_name is None:
            print("ERROR: No OLL case matched after all U rotations")
            break
        
        # Get algorithm
        algorithm = OLL_CASES.get(case_name)
        if not algorithm:
            print(f"ERROR: No algorithm found for case {case_name}")
            break
        
        # Convert notation (R' -> Rprime)
        converted_algorithm = []
        for move in algorithm:
            if "'" in move:
                converted_algorithm.append(move.replace("'", "prime"))
            else:
                converted_algorithm.append(move)
        
        print(f"Applying algorithm: {converted_algorithm}")
        
        # Apply algorithm
        for move in converted_algorithm:
            apply_move(move, cube)
        
        moves.extend(converted_algorithm)
    
    # Final check
    if is_oll_solved(cube):
        print("✓ OLL solved")
    else:
        print(f"✗ OLL not solved after {iteration} iterations")
    
    print(f"OLL moves: {moves}")
    return moves