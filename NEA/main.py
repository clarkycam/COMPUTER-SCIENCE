
# each face is a 3x3 list of colours
# faces: U = up, D = down, F = front, B = back, L = left, R = right
# colours: W = white, Y = yellow, R = red, O = orange, G = green, B = blue
cube = {
    "U": [["W", "W", "W"],
          ["W", "W", "W"],
          ["W", "W", "W"]],
        
    "D": [["Y", "Y", "Y"],
          ["Y", "Y", "Y"],
          ["Y", "Y", "Y"]],
    
    "F": [["G", "G", "G"],
          ["G", "G", "G"],
          ["G", "G", "G"]],
    
    "B": [["B", "B", "B"],
          ["B", "B", "B"],
          ["B", "B", "B"]],
    
    "L": [["O", "O", "O"],
          ["O", "O", "O"],
          ["O", "O", "O"]],
    
    "R": [["R", "R", "R"],
          ["R", "R", "R"],
          ["R", "R", "R"]]
}



def rotate_face_cw(face): # rotates a face clockwise

      # reverse the rows (top to bottom)
      reversed_rows = face[::-1]

      # transpose (swap rows with columns)
      transposed = []
      for collumn in range(3):
            new_row = [reversed_rows[row][collumn] for row in range(3)]
            transposed.append(new_row)

      return transposed

def rotate_face_acw(face): # rotates face anticlockwise

      # transpose (swap rows with columns)
      transposed = []
      for collumn in range(3):
            new_row = [face[row][collumn] for row in range(3)]
            transposed.append(new_row)
      
      # reverse the rows (top to bottom)
      reversed_rows = transposed[::-1]

      return reversed_rows



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


def move_B(cube):
    cube["B"] = rotate_face_cw(cube["B"])
    u_top = cube["U"][0][:]
    r_col = [cube["R"][i][2] for i in range(3)]
    d_bot = cube["D"][2][:]
    l_col = [cube["L"][i][0] for i in range(3)]
    cube["R"][0][2], cube["R"][1][2], cube["R"][2][2] = d_bot
    cube["D"][2] = l_col[::-1]
    cube["L"][0][0], cube["L"][1][0], cube["L"][2][0] = u_top
    cube["U"][0] = r_col[::-1]


def move_L(cube):
    cube["L"] = rotate_face_cw(cube["L"])
    u_col = [cube["U"][i][0] for i in range(3)]
    f_col = [cube["F"][i][0] for i in range(3)]
    d_col = [cube["D"][i][0] for i in range(3)]
    b_col = [cube["B"][2-i][2] for i in range(3)]  # reversed
    for i in range(3): cube["F"][i][0] = u_col[i]
    for i in range(3): cube["D"][i][0] = f_col[i]
    for i in range(3): cube["B"][2-i][2] = d_col[i]
    for i in range(3): cube["U"][i][0] = b_col[i]


def move_R(cube):
    cube["R"] = rotate_face_cw(cube["R"])
    u_col = [cube["U"][i][2] for i in range(3)]
    f_col = [cube["F"][i][2] for i in range(3)]
    d_col = [cube["D"][i][2] for i in range(3)]
    b_col = [cube["B"][2-i][0] for i in range(3)]  # reversed
    for i in range(3): cube["B"][2-i][0] = u_col[i]
    for i in range(3): cube["U"][i][2] = f_col[i]
    for i in range(3): cube["F"][i][2] = d_col[i]
    for i in range(3): cube["D"][i][2] = b_col[i]



# Example usage

print("Initial Cube State:", cube)
move_R(cube)
print("Cube State after move:", cube)