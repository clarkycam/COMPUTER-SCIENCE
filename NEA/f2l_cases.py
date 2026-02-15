# F2L Cases - All for Front-Right (F-R) slot
# These will be translated for other slots as needed

F2L_CASES = {
    # ===== SECTION 1: BASIC CASES (4 cases) =====
    "basic_1": {
        "algorithm": ["R", "U", "Rprime"]
    },
    
    "basic_2": {
        "algorithm": ["Fprime", "Uprime", "F"]
    },
    
    "basic_3": {
        "algorithm": ["U", "R", "Uprime", "Rprime"]
    },
    
    "basic_4": {
        "algorithm": ["Uprime", "Fprime", "U", "F"]
    },
    
    # ===== SECTION 2: CORNER AND EDGE IN TOP (12 cases) =====
    "top_1": {
        "algorithm": ["Uprime", "R", "Uprime", "Rprime", "U", "R", "U", "Rprime"]
    },
    
    "top_2": {
        "algorithm": ["U", "Fprime", "U", "F", "Uprime", "Fprime", "Uprime", "F"]
    },
    
    "top_3": {
        "algorithm": ["Uprime", "R", "U", "Rprime", "U", "R", "U", "Rprime"]
    },
    
    "top_4": {
        "algorithm": ["U", "Fprime", "Uprime", "F", "Uprime", "Fprime", "Uprime", "F"]
    },
    
    "top_5": {
        "algorithm": ["Rprime", "U2", "R2", "U", "R2", "U", "R"]
    },
    
    "top_6": {
        "algorithm": ["Uprime", "R", "U2", "Rprime", "U", "Fprime", "Uprime", "F"]
    },
    
    "top_7": {
        "algorithm": ["R", "Uprime", "Rprime", "U2", "Fprime", "Uprime", "F"]
    },
    
    "top_8": {
        "algorithm": ["U", "Rprime", "F", "R", "Fprime", "U", "R", "U", "Rprime"]
    },
    
    "top_9": {
        "algorithm": ["U", "Fprime", "U2", "F", "U", "Fprime", "U2", "F"]
    },
    
    "top_10": {
        "algorithm": ["Uprime", "R", "U2", "Rprime", "Uprime", "R", "U2", "Rprime"]
    },
    
    "top_11": {
        "algorithm": ["U", "Fprime", "Uprime", "F", "U", "Fprime", "U2", "F"]
    },
    
    "top_12": {
        "algorithm": ["Uprime", "R", "U", "Rprime", "Uprime", "R", "U2", "Rprime"]
    },
    
    # ===== SECTION 3: CORNER POINTING UP, EDGE IN TOP (8 cases) =====
    "corner_up_1": {
        "algorithm": ["R", "U2", "Rprime", "Uprime", "R", "U", "Rprime"]
    },
    
    "corner_up_2": {
        "algorithm": ["Fprime", "U2", "F", "U", "Fprime", "Uprime", "F"]
    },
    
    "corner_up_3": {
        "algorithm": ["U", "R", "U2", "Rprime", "U", "R", "Uprime", "Rprime"]
    },
    
    "corner_up_4": {
        "algorithm": ["Uprime", "Fprime", "U2", "F", "Uprime", "Fprime", "U", "F"]
    },
    
    "corner_up_5": {
        "algorithm": ["U2", "R", "U", "Rprime", "U", "R", "Uprime", "Rprime"]
    },
    
    "corner_up_6": {
        "algorithm": ["U2", "Fprime", "Uprime", "F", "Uprime", "Fprime", "U", "F"]
    },
    
    "corner_up_7": {
        "algorithm": ["R", "U", "Rprime", "Uprime", "Uprime", "R", "U", "Rprime", "Uprime", "R", "U", "Rprime"]
    },
    
    "corner_up_8": {
        "algorithm": ["F", "U", "R", "Uprime", "Rprime", "Fprime", "R", "Uprime", "Rprime"]
    }
}

# Move translation tables for each slot
# Each slot rotates the cube so that slot becomes the "front-right" position
MOVE_TRANSLATION = {
    "red-green": {  # F-R slot (no rotation needed - this IS front-right)
        "R": "R", "Rprime": "Rprime", "R2": "R2",
        "L": "L", "Lprime": "Lprime", "L2": "L2",
        "F": "F", "Fprime": "Fprime", "F2": "F2",
        "B": "B", "Bprime": "Bprime", "B2": "B2",
        "U": "U", "Uprime": "Uprime", "U2": "U2",
        "D": "D", "Dprime": "Dprime", "D2": "D2"
    },
    "orange-green": {  # F-L slot (rotate 90° CCW: F stays, R→F, B→R, L→B)
        "R": "F", "Rprime": "Fprime", "R2": "F2",
        "L": "B", "Lprime": "Bprime", "L2": "B2",
        "F": "L", "Fprime": "Lprime", "F2": "L2",
        "B": "R", "Bprime": "Rprime", "B2": "R2",
        "U": "U", "Uprime": "Uprime", "U2": "U2",
        "D": "D", "Dprime": "Dprime", "D2": "D2"
    },
    "red-blue": {  # B-R slot (rotate 180°: F→B, R stays, B→F, L→L)
        "R": "B", "Rprime": "Bprime", "R2": "B2",
        "L": "F", "Lprime": "Fprime", "L2": "F2",
        "F": "R", "Fprime": "Rprime", "F2": "R2",
        "B": "L", "Bprime": "Lprime", "B2": "L2",
        "U": "U", "Uprime": "Uprime", "U2": "U2",
        "D": "D", "Dprime": "Dprime", "D2": "D2"
    },
    "orange-blue": {  # B-L slot (rotate 90° CW: F→R, R→B, B→L, L→F)
        "R": "L", "Rprime": "Lprime", "R2": "L2",
        "L": "R", "Lprime": "Rprime", "L2": "R2",
        "F": "B", "Fprime": "Bprime", "F2": "B2",
        "B": "F", "Bprime": "Fprime", "B2": "F2",
        "U": "U", "Uprime": "Uprime", "U2": "U2",
        "D": "D", "Dprime": "Dprime", "D2": "D2"
    }
}


def translate_algorithm(algorithm, slot_name):
    """
    Translate an F2L algorithm from the standard F-R slot to the target slot.
    
    Args:
        algorithm: List of moves in standard F-R notation
        slot_name: Target slot ("red-green", "orange-green", "red-blue", "orange-blue")
    
    Returns:
        List of translated moves for the target slot
    """
    if slot_name not in MOVE_TRANSLATION:
        return algorithm
    
    translation_map = MOVE_TRANSLATION[slot_name]
    translated = []
    
    for move in algorithm:
        translated.append(translation_map.get(move, move))
    
    return translated


def translate_corner_position_to_relative(actual_pos, slot_name):
    """
    Translate actual corner position to slot-relative position.
    For algorithms, we always treat the slot as if it's at F-R, so:
    - The corner that's "top-right" relative to the slot becomes "UFR"
    
    Args:
        actual_pos: Actual position on cube ("UFR", "UFL", "UBR", "UBL")
        slot_name: Which slot we're solving
    
    Returns:
        Relative position as if solving F-R slot
    """
    # Map actual positions to relative positions for each slot
    position_maps = {
        "red-green": {  # F-R slot - no translation
            "UFR": "UFR", "UBR": "UBR", "UBL": "UBL", "UFL": "UFL"
        },
        "orange-green": {  # F-L slot - rotate 90° CCW
            "UFL": "UFR", "UFR": "UBR", "UBR": "UBL", "UBL": "UFL"
        },
        "red-blue": {  # B-R slot - rotate 180°
            "UBR": "UFR", "UBL": "UBR", "UFL": "UBL", "UFR": "UFL"
        },
        "orange-blue": {  # B-L slot - rotate 90° CW
            "UBL": "UFR", "UFL": "UBR", "UFR": "UBL", "UBR": "UFL"
        }
    }
    
    return position_maps.get(slot_name, {}).get(actual_pos, actual_pos)


def translate_edge_position_to_relative(actual_pos, slot_name):
    """
    Translate actual edge position to slot-relative position.
    
    Args:
        actual_pos: Actual position on cube ("UF", "UR", "UB", "UL")
        slot_name: Which slot we're solving
    
    Returns:
        Relative position as if solving F-R slot
    """
    position_maps = {
        "red-green": {  # F-R slot - no translation
            "UF": "UF", "UR": "UR", "UB": "UB", "UL": "UL"
        },
        "orange-green": {  # F-L slot - rotate 90° CCW
            "UL": "UF", "UF": "UR", "UR": "UB", "UB": "UL"
        },
        "red-blue": {  # B-R slot - rotate 180°
            "UR": "UF", "UB": "UR", "UL": "UB", "UF": "UL"
        },
        "orange-blue": {  # B-L slot - rotate 90° CW
            "UB": "UF", "UL": "UR", "UF": "UB", "UR": "UL"
        }
    }
    
    return position_maps.get(slot_name, {}).get(actual_pos, actual_pos)


def detect_f2l_case(cube, corner_coords, edge_coords, slot_name):
    """
    Detect which F2L case we're in based on corner and edge positions/orientations.
    Supports all four F2L slots by translating to slot-relative positions.
    """
    # Get actual positions
    corner_u_pos = get_corner_u_position(corner_coords)
    edge_u_pos = get_edge_u_position(edge_coords)
    
    # Translate to slot-relative positions (as if we're always solving F-R)
    corner_relative_pos = translate_corner_position_to_relative(corner_u_pos, slot_name)
    edge_relative_pos = translate_edge_position_to_relative(edge_u_pos, slot_name)
    
    # Get orientations
    corner_orientation = get_corner_orientation(cube, corner_coords, slot_name)
    edge_orientation = get_edge_orientation(cube, edge_coords, slot_name)
    
    # Match using relative positions
    case = match_f2l_case(corner_relative_pos, corner_orientation, edge_relative_pos, edge_orientation)
    
    if not case:
        print(f"No case: C:{corner_relative_pos}/{corner_orientation}, E:{edge_relative_pos}/{edge_orientation}")
    
    return case


def get_corner_u_position(corner_coords):
    """
    Determine which U layer corner position.
    Returns: "UFR", "UFL", "UBR", "UBL", or None
    """
    # Check which corner position based on coordinates
    coord_set = set(corner_coords)
    
    if ("U", 2, 2) in coord_set:  # U face bottom-right
        return "UFR"
    elif ("U", 2, 0) in coord_set:  # U face bottom-left
        return "UFL"
    elif ("U", 0, 2) in coord_set:  # U face top-right
        return "UBR"
    elif ("U", 0, 0) in coord_set:  # U face top-left
        return "UBL"
    
    return None


def get_corner_orientation(cube, corner_coords, slot_name):
    """
    Determine corner orientation relative to the slot's perspective.
    """
    # Define which faces are 'Front' and 'Right' for each slot's perspective
    slot_faces = {
        "red-green":    {"front": "F", "right": "R"},
        "orange-green": {"front": "L", "right": "F"},
        "red-blue":     {"front": "R", "right": "B"},
        "orange-blue":  {"front": "B", "right": "L"},
    }
    
    faces = slot_faces.get(slot_name)
    
    for face, row, col in corner_coords:
        if cube[face][row][col] == 'Y':
            if face == "U":
                print(f"DEBUG: Corner piece has yellow on U face - orientation is 'yellow_up'")
                return "yellow_up"
            elif face == faces["front"]:
                print(f"DEBUG: Corner piece has yellow on front face ({face}) - orientation is 'yellow_front'")
                return "yellow_front"
            elif face == faces["right"]:
                print(f"DEBUG: Corner piece has yellow on right face ({face}) - orientation is 'yellow_right'")
                return "yellow_right"
    return None


def get_edge_u_position(edge_coords):
    """
    Determine which U layer edge position.
    Returns: "UF", "UR", "UB", "UL", or None
    """
    coord_set = set(edge_coords)
    
    if ("U", 2, 1) in coord_set:  # U face bottom edge
        return "UF"
    elif ("U", 1, 2) in coord_set:  # U face right edge
        return "UR"
    elif ("U", 0, 1) in coord_set:  # U face top edge
        return "UB"
    elif ("U", 1, 0) in coord_set:  # U face left edge
        return "UL"
    
    return None


def get_edge_orientation(cube, edge_coords, slot_name):
    """
    Determine edge orientation relative to the slot.
    """
    # For each slot, define which color is "front" and which is "right" 
    # from the slot's rotated perspective
    slot_color_map = {
        "red-green":    {"front": "G", "right": "R"},  # Green=front, Red=right
        "orange-green": {"front": "O", "right": "G"},  # Orange=front, Green=right (from rotated view)
        "red-blue":     {"front": "R", "right": "B"},  # Red=front, Blue=right (from rotated view)
        "orange-blue":  {"front": "B", "right": "O"},  # Blue=front, Orange=right (from rotated view)
    }
    
    target = slot_color_map.get(slot_name)
    if not target: return None
    
    for face, row, col in edge_coords:
        if face == "U":
            color = cube[face][row][col]
            if color == target["front"]:
                return "front_up"
            elif color == target["right"]:
                return "right_up"
    return None


def match_f2l_case(corner_pos, corner_orient, edge_pos, edge_orient):
    """
    Match the corner and edge configuration to one of the 24 F2L cases.
    Based on the descriptions in F2L_CASES.
    """
    # BASIC CASES
    if corner_orient == "yellow_right" and edge_pos == "UB" and edge_orient == "front_up":
        return "basic_1"
    
    if corner_orient == "yellow_front" and edge_pos == "UL" and edge_orient == "right_up":
        return "basic_2"
    
    if corner_orient == "yellow_front" and edge_pos == "UR" and edge_orient == "front_up":
        return "basic_3"
    
    if corner_orient == "yellow_right" and edge_pos == "UF" and edge_orient == "right_up":
        return "basic_4"
    
    # CORNER AND EDGE IN TOP
    if corner_pos == "UFR" and corner_orient == "yellow_right" and edge_pos == "UR" and edge_orient == "front_up":
        return "top_1"
    
    if corner_pos == "UFR" and corner_orient == "yellow_front" and edge_pos == "UF" and edge_orient == "right_up":
        return "top_2"
    
    if corner_pos == "UFR" and corner_orient == "yellow_right" and edge_pos == "UL" and edge_orient == "front_up":
        return "top_3"
    
    if corner_pos == "UFR" and corner_orient == "yellow_front" and edge_pos == "UB" and edge_orient == "right_up":
        return "top_4"
    
    if corner_pos == "UFR" and corner_orient == "yellow_right" and edge_pos == "UF" and edge_orient == "front_up":
        return "top_5"
    
    if corner_pos == "UFR" and corner_orient == "yellow_front" and edge_pos == "UR" and edge_orient == "right_up":
        return "top_6"
    
    if corner_pos == "UFR" and corner_orient == "yellow_right" and edge_pos == "UR" and edge_orient == "right_up":
        return "top_7"
    
    if corner_pos == "UFR" and corner_orient == "yellow_front" and edge_pos == "UF" and edge_orient == "front_up":
        return "top_8"
    
    if corner_pos == "UFR" and corner_orient == "yellow_right" and edge_pos == "UB" and edge_orient == "right_up":
        return "top_9"
    
    if corner_pos == "UFR" and corner_orient == "yellow_front" and edge_pos == "UL" and edge_orient == "front_up":
        return "top_10"
    
    if corner_pos == "UFR" and corner_orient == "yellow_right" and edge_pos == "UL" and edge_orient == "right_up":
        return "top_11"
    
    if corner_pos == "UFR" and corner_orient == "yellow_front" and edge_pos == "UB" and edge_orient == "front_up":
        return "top_12"
    
    # CORNER POINTING UP
    if corner_orient == "yellow_up" and edge_pos == "UR" and edge_orient == "front_up":
        return "corner_up_1"
    
    if corner_orient == "yellow_up" and edge_pos == "UF" and edge_orient == "right_up":
        return "corner_up_2"
    
    if corner_orient == "yellow_up" and edge_pos == "UB" and edge_orient == "front_up":
        return "corner_up_3"
    
    if corner_orient == "yellow_up" and edge_pos == "UL" and edge_orient == "right_up":
        return "corner_up_4"
    
    if corner_orient == "yellow_up" and edge_pos == "UL" and edge_orient == "front_up":
        return "corner_up_5"
    
    if corner_orient == "yellow_up" and edge_pos == "UB" and edge_orient == "right_up":
        return "corner_up_6"
    
    if corner_orient == "yellow_up" and edge_pos == "UF" and edge_orient == "front_up":
        return "corner_up_7"
    
    if corner_orient == "yellow_up" and edge_pos == "UR" and edge_orient == "right_up":
        return "corner_up_8"
    
    return None


def align_corner_to_ufr(corner_pos, slot_name):
    """
    Align corner to the target 'home' position for the specific slot.
    Red-Green home: UFR, Orange-Green home: UFL
    """
    # Define the target corner for each slot
    slot_targets = {
        "red-green": "UFR",
        "orange-green": "UFL",
        "red-blue": "UBR",
        "orange-blue": "UBL"
    }
    target = slot_targets.get(slot_name, "UFR")

    # Sequence: UFR -> UBR -> UBL -> UFL (with U moves)
    positions = ["UFR", "UBR", "UBL", "UFL"]
    start_idx = positions.index(corner_pos)
    target_idx = positions.index(target)
    
    # Calculate moves to reach target
    diff = (target_idx - start_idx) % 4
    # diff=1: target is 1 step forward (UBR->UFR needs to go back 3 = U)
    # diff=3: target is 3 steps forward (UFL->UFR needs to go back 1 = U')
    move_map = {0: [], 1: ["Uprime"], 2: ["U2"], 3: ["U"]}
    return move_map[diff]