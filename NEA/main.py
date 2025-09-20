
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


# test face
face = [
    [1, 2, 3],   # top row
    [4, 5, 6],   # middle row
    [7, 8, 9]    # bottom row
]

newface=face
print(face)
for i in range(1,5): # checking through all possible turns
      newface=rotate_face_cw(newface)
      print(f"\nRotation {i}")
      for j in newface:
            print(j)