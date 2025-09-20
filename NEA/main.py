
# each gace is a 3x3 list of colours
# faces: U = up, D = down, F = front, B = black, L = left, R = right
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


# def move_U(cube): # wrong
#     # Rotate the U face clockwise
#     cube["U"] = rotate_face_cw(cube["U"])
    
#     # Cycle the top rows of F, R, B, L
#     f_top, r_top, b_top, l_top = cube["F"][0][:], cube["R"][0][:], cube["B"][0][:], cube["L"][0][:]
    
#     cube["F"][0] = l_top
#     cube["R"][0] = f_top
#     cube["B"][0] = r_top
#     cube["L"][0] = b_top

def move_U(cube): # correct
    # Rotate the U face clockwise
    cube["U"] = rotate_face_cw(cube["U"])
    
    # Cycle the top rows of F, R, B, L
    f_top, r_top, b_top, l_top = cube["F"][0][:], cube["R"][0][:], cube["B"][0][:], cube["L"][0][:]
    
    cube["F"][0] = r_top
    cube["R"][0] = b_top
    cube["B"][0] = l_top
    cube["L"][0] = f_top

print("Initial Cube State:", cube)
move_U(cube)
print("Cube State after U move:", cube)