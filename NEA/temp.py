# def move_U(cube): # wrong
#     # Rotate the U face clockwise
#     cube["U"] = rotate_face_cw(cube["U"])
    
#     # Cycle the top rows of F, R, B, L
#     f_top, r_top, b_top, l_top = cube["F"][0][:], cube["R"][0][:], cube["B"][0][:], cube["L"][0][:]
    
#     cube["F"][0] = l_top
#     cube["R"][0] = f_top
#     cube["B"][0] = r_top
#     cube["L"][0] = b_top

def move_U(cube):
    
    # Rotate the U face clockwise
    cube["U"] = rotate_face_cw(cube["U"])

    # Cycle the top rows of F, R, B, L
    f_top, r_top, b_top, l_top = cube["F"][0][:], cube["R"][0][:], cube["B"][0][:], cube["L"][0][:]
    cube["F"][0] = r_top
    cube["L"][0] = f_top
    cube["B"][0] = l_top
    cube["R"][0] = b_top


def move_D(cube):
    cube["D"] = rotate_face_cw(cube["D"])
    f_bot, r_bot, b_bot, l_bot = cube["F"][2][:], cube["R"][2][:], cube["B"][2][:], cube["L"][2][:]
    cube["F"][2] = l_bot
    cube["R"][2] = f_bot
    cube["B"][2] = r_bot
    cube["L"][2] = b_bot


def move_F(cube):
    cube["F"] = rotate_face_cw(cube["F"])
    u_bot = cube["U"][2][:]
    r_col = [cube["R"][i][0] for i in range(3)]
    d_top = cube["D"][0][:]
    l_col = [cube["L"][i][2] for i in range(3)]
    cube["R"][0][0], cube["R"][1][0], cube["R"][2][0] = u_bot
    cube["D"][0] = r_col[::-1]
    cube["L"][0][2], cube["L"][1][2], cube["L"][2][2] = d_top
    cube["U"][2] = l_col[::-1]


# def move_B(cube): # wrong
#     cube["B"] = rotate_face_cw(cube["B"])
#     u_top = cube["U"][0][:]
#     r_col = [cube["R"][i][2] for i in range(3)]
#     d_bot = cube["D"][2][:]
#     l_col = [cube["L"][i][0] for i in range(3)]
#     cube["R"][0][2], cube["R"][1][2], cube["R"][2][2] = u_top
#     cube["D"][2] = r_col[::-1]
#     cube["L"][0][0], cube["L"][1][0], cube["L"][2][0] = d_bot
#     cube["U"][0] = l_col[::-1]

def move_B(cube): # correct
    cube["B"] = rotate_face_cw(cube["B"])
    u_top = cube["U"][0][:]
    r_col = [cube["R"][i][2] for i in range(3)]
    d_bot = cube["D"][2][:]
    l_col = [cube["L"][i][0] for i in range(3)]
    cube["R"][0][2], cube["R"][1][2], cube["R"][2][2] = d_bot
    cube["D"][2] = l_col[::-1]
    cube["L"][0][0], cube["L"][1][0], cube["L"][2][0] = u_top
    cube["U"][0] = r_col[::-1]


def move_L(cube): # correct
    cube["L"] = rotate_face_cw(cube["L"])
    u_col = [cube["U"][i][0] for i in range(3)]
    f_col = [cube["F"][i][0] for i in range(3)]
    d_col = [cube["D"][i][0] for i in range(3)]
    b_col = [cube["B"][2-i][2] for i in range(3)]  # reversed
    for i in range(3): cube["F"][i][0] = u_col[i]
    for i in range(3): cube["D"][i][0] = f_col[i]
    for i in range(3): cube["B"][2-i][2] = d_col[i]
    for i in range(3): cube["U"][i][0] = b_col[i]

# def move_L(cube): # wrong
#     cube["L"] = rotate_face_cw(cube["L"])
#     u_col = [cube["U"][i][0] for i in range(3)]
#     f_col = [cube["F"][i][0] for i in range(3)]
#     d_col = [cube["D"][i][0] for i in range(3)]
#     b_col = [cube["B"][i][0] for i in range(3)]
#     for i in range(3): cube["F"][i][0] = u_col[i]
#     for i in range(3): cube["D"][i][0] = f_col[i]
#     for i in range(3): cube["B"][i][0] = d_col[i]
#     for i in range(3): cube["U"][i][0] = b_col[i]


def move_R(cube): # correct
    cube["R"] = rotate_face_cw(cube["R"])
    u_col = [cube["U"][i][2] for i in range(3)]
    f_col = [cube["F"][i][2] for i in range(3)]
    d_col = [cube["D"][i][2] for i in range(3)]
    b_col = [cube["B"][2-i][0] for i in range(3)]  # reversed
    for i in range(3): cube["B"][2-i][0] = u_col[i]
    for i in range(3): cube["U"][i][2] = f_col[i]
    for i in range(3): cube["F"][i][2] = d_col[i]
    for i in range(3): cube["D"][i][2] = b_col[i]

# def move_R(cube): # wrong
#     cube["R"] = rotate_face_cw(cube["R"])
#     u_col = [cube["U"][i][2] for i in range(3)]
#     f_col = [cube["F"][i][2] for i in range(3)]
#     d_col = [cube["D"][i][2] for i in range(3)]
#     b_col = [cube["B"][i][2] for i in range(3)]
#     for i in range(3): cube["B"][i][2] = u_col[i]
#     for i in range(3): cube["U"][i][2] = f_col[i]
#     for i in range(3): cube["F"][i][2] = d_col[i]
#     for i in range(3): cube["D"][i][2] = b_col[i]