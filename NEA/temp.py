#cfop.py
from main import apply_move



def solve_cfop(cube):
    moves = []

    moves += solve_cross(cube)
    moves += solve_f2l(cube)
    moves += solve_oll(cube)
    moves += solve_pll(cube)

    return moves



def solve_cross(cube):
    moves = []

    if is_cross_solved(cube):
        return moves

    # Placeholder logic for solving the cross
    return moves

def is_cross_solved(cube, face="U"):
    centre=cube[face][1][1]
    edges = [
        (0, 1),
        (1, 0),
        (1, 2),
        (2, 1)
    ]

    for r, c in edges:
        if cube[face][r][c] != centre:
            return False
    
    return True



def solve_f2l(cube):
    pass




def solve_oll(cube):
    pass




def solve_pll(cube):
    pass