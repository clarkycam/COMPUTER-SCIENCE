# F2L Cases - All for Front-Right (F-R) slot
# These will be translated for other slots as needed

F2L_CASES = {
    # description relative to being in FR slot
    # ===== SECTION 1: BASIC CASES (4 cases) =====
    "basic_1": {
        "description": "corner: yellow facing right, edge: U(r0,c1) front colour facing up",
        "algorithm": ["R", "U", "Rprime"]
    },
    
    "basic_2": {
        "description": "corner: yellow facing front, edge: U(r1,c0) right colour facing up",
        "algorithm": ["Fprime", "Uprime", "F"]
    },
    
    "basic_3": {
        "description": "corner: yellow facing front, edge: U(r1,c2) front colour facing up",
        "algorithm": ["U", "R", "Uprime", "Rprime"]
    },
    
    "basic_4": {
        "description": "corner: yellow facing right, edge: U(r2,c1) right colour facing up",
        "algorithm": ["Uprime", "Fprime", "U", "F"]
    },
    
    # ===== SECTION 2: CORNER AND EDGE IN TOP (12 cases) =====
    "top_1": {
        "description": "corner: yellow facing right, edge: U(r1,c2) front colour facing up",
        "algorithm": ["Uprime", "R", "Uprime", "Rprime", "U", "R", "U", "Rprime"]
    },
    
    "top_2": {
        "description": "corner: yellow facing front, edge: U(r2,c1) right colour facing up",
        "algorithm": ["U", "Fprime", "U", "F", "Uprime", "Fprime", "Uprime", "F"]
    },
    
    "top_3": {
        "description": "corner: yellow facing right, edge: U(r1,c0) front colour facing up",
        "algorithm": ["Uprime", "R", "U", "Rprime", "U", "R", "U", "Rprime"]
    },
    
    "top_4": {
        "description": "corner: yellow facing front, edge: U(r0,c1) right colour facing up",
        "algorithm": ["U", "Fprime", "Uprime", "F", "Uprime", "Fprime", "Uprime", "F"]
    },
    
    "top_5": {
        "description": "corner: yellow facing right, edge: U(r2,c1) front colour facing up",
        # d (R' U2 R) d' (R U R') => U' (B' U2 B) U (R U R')
        "algorithm": ["Rprime", "U2", "R2", "U", "R2", "U", "R"]
    },
    
    "top_6": {
        "description": "corner: yellow facing front, edge: U(r1,c2) right colour facing up",
        # U' R U2 R' d (R' U' R) => U' R U2 R' U' (B' U' B)
        "algorithm": ["Uprime", "R", "U2", "Rprime", "Uprime", "Bprime", "Uprime", "B"]
    },
    
    "top_7": {
        "description": "corner: yellow facing right, edge: U(r1,c2) right colour facing up",
        # R U' R' U d (R' U' R) => R U' R' U U' (B' U' B)
        "algorithm": ["R", "Uprime", "Rprime", "U", "Uprime", "Bprime", "Uprime", "B"]
    },
    
    "top_8": {
        "description": "corner: yellow facing front, edge: U(r2,c1) front colour facing up",
        # F' U F U' d' (F U F') => F' U F U' U (L U L')
        "algorithm": ["Fprime", "U", "F", "Uprime", "U", "L", "U", "Lprime"]
    },
    
    "top_9": {
        "description": "corner: yellow facing right, edge: U(r0,c1) right colour facing up",
        "algorithm": ["U", "Fprime", "U2", "F", "U", "Fprime", "U2", "F"]
    },
    
    "top_10": {
        "description": "corner: yellow facing front, edge: U(r1,c0) front colour facing up",
        "algorithm": ["Uprime", "R", "U2", "Rprime", "Uprime", "R", "U2", "Rprime"]
    },
    
    "top_11": {
        "description": "corner: yellow facing right, edge: U(r1,c0) right colour facing up",
        "algorithm": ["U", "Fprime", "Uprime", "F", "U", "Fprime", "U2", "F"]
    },
    
    "top_12": {
        "description": "corner: yellow facing front, edge: U(r0,c1) front colour facing up",
        "algorithm": ["Uprime", "R", "U", "Rprime", "Uprime", "R", "U2", "Rprime"]
    },
    
    # ===== SECTION 3: CORNER POINTING UP, EDGE IN TOP (8 cases) =====
    "corner_up_1": {
        "description": "corner: facing up, edge: U(r1,c2) front colour facing up",
        "algorithm": ["R", "U2", "Rprime", "Uprime", "R", "U", "Rprime"]
    },
    
    "corner_up_2": {
        "description": "corner: facing up, edge: U(r2,c1) right colour facing up",
        "algorithm": ["Fprime", "U2", "F", "U", "Fprime", "Uprime", "F"]
    },
    
    "corner_up_3": {
        "description": "corner: facing up, edge: U(r0,c1) front colour facing up",
        "algorithm": ["U", "R", "U2", "Rprime", "U", "R", "Uprime", "Rprime"]
    },
    
    "corner_up_4": {
        "description": "corner: facing up, edge: U(r1,c0) right colour facing up",
        "algorithm": ["Uprime", "Fprime", "U2", "F", "Uprime", "Fprime", "U", "F"]
    },
    
    "corner_up_5": {
        "description": "corner: facing up, edge: U(r1,c0) front colour facing up",
        "algorithm": ["U2", "R", "U", "Rprime", "U", "R", "Uprime", "Rprime"]
    },
    
    "corner_up_6": {
        "description": "corner: facing up, edge: U(r0,c1) right colour facing up",
        "algorithm": ["U2", "Fprime", "Uprime", "F", "Uprime", "Fprime", "U", "F"]
    },
    
    "corner_up_7": {
        "description": "corner: facing up, edge: U(r2,c1) front colour facing up",
        # (R U R' U') U' (R U R' U') (R U R')
        "algorithm": ["R", "U", "Rprime", "Uprime", "Uprime", "R", "U", "Rprime", "Uprime", "R", "U", "Rprime"]
    },
    
    "corner_up_8": {
        "description": "corner: facing up, edge: U(r1,c2) right colour facing up",
        # y' (R' U' R U) U (R' U' R U) (R' U' R)
        # y' rotation makes this: L' U' L U U L' U' L U L' U' L
        "algorithm": ["Lprime", "Uprime", "L", "U", "U", "Lprime", "Uprime", "L", "U", "Lprime", "Uprime", "L"]
    }
}

# Move translation tables for each slot
MOVE_TRANSLATION = {
    "red-green": {  # F-R slot (no translation needed)
        "R": "R", "Rprime": "Rprime", "R2": "R2",
        "L": "L", "Lprime": "Lprime", "L2": "L2",
        "F": "F", "Fprime": "Fprime", "F2": "F2",
        "B": "B", "Bprime": "Bprime", "B2": "B2",
        "U": "U", "Uprime": "Uprime", "U2": "U2",
        "D": "D", "Dprime": "Dprime", "D2": "D2"
    },
    "orange-green": {  # F-L slot (mirror R to L)
        "R": "L", "Rprime": "Lprime", "R2": "L2",
        "L": "R", "Lprime": "Rprime", "L2": "R2",
        "F": "F", "Fprime": "Fprime", "F2": "F2",
        "B": "B", "Bprime": "Bprime", "B2": "B2",
        "U": "U", "Uprime": "Uprime", "U2": "U2",
        "D": "D", "Dprime": "Dprime", "D2": "D2"
    },
    "red-blue": {  # B-R slot (rotate 180°: F to B)
        "R": "R", "Rprime": "Rprime", "R2": "R2",
        "L": "L", "Lprime": "Lprime", "L2": "L2",
        "F": "B", "Fprime": "Bprime", "F2": "B2",
        "B": "F", "Bprime": "Fprime", "B2": "F2",
        "U": "U", "Uprime": "Uprime", "U2": "U2",
        "D": "D", "Dprime": "Dprime", "D2": "D2"
    },
    "orange-blue": {  # B-L slot (rotate 180° + mirror)
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