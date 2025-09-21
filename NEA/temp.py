def move_U(cube): # correct
    # Rotate the U face clockwise
    cube["U"] = rotate_face_cw(cube["U"])
    
    # Cycle the top rows of F, R, B, L
    f_top, r_top, b_top, l_top = cube["F"][0][:], cube["R"][0][:], cube["B"][0][:], cube["L"][0][:]
    
    cube["F"][0] = r_top
    cube["R"][0] = b_top
    cube["B"][0] = l_top
    cube["L"][0] = f_top