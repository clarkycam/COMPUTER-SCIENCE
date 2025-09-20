# representation of the cube
# faces: up, front, right, back, left, down
# colours: white, green, red, blue, orange, yellow
cube = {
    "U": [["W", "W", "W"],
          ["W", "W", "W"],
          ["W", "W", "W"]],
    
    "F": [["G", "G", "G"],
          ["G", "G", "G"],
          ["G", "G", "G"]],
    
    "R": [["R", "R", "R"],
          ["R", "R", "R"],
          ["R", "R", "R"]],
    
    "B": [["B", "B", "B"],
          ["B", "B", "B"],
          ["B", "B", "B"]],

    "L": [["O", "O", "O"],
          ["O", "O", "O"],
          ["O", "O", "O"]],
    
    "D": [["Y", "Y", "Y"],
          ["Y", "Y", "Y"],
          ["Y", "Y", "Y"]]
}

def rotate_face(face): # rotate face clockwise-

    reversed_face = face[::-1] # reverses order of rows
    print("reversed: ", reversed_face)

    #transposing
    ROWS = 3 # constant
    COLUMNS = 3 #constant

    #initialisng the matrix with 0
    transposed = [[0 for _ in range(ROWS)] for _ in range(COLUMNS)]

    #transpose new values 
    for i in range(ROWS):
        for j in range(COLUMNS):
            transposed[j][i] = reversed_face[i][j]
    print("transposed: ", transposed)




face = [["W", "O", "Y"],
        ["R", "G", "W"],
        ["W", "R", "B"]]

rotate_face(face)
