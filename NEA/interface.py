from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark") # Modes: system (default), dark, light
customtkinter.set_default_color_theme("blue") # Themes: blue (default), dark-blue, green

# root = tk()
root = customtkinter.CTk()

root.title("Rubik's Cube Solver")
root.iconbitmap("NEA/icon.ico")
root.geometry("1920x1080")
root.attributes('-fullscreen', True)


# Title
title_label = customtkinter.CTkLabel(
    root,
    text="Rubik's Cube Solver",
    font=("Arial", 28, "bold")
)
title_label.pack(pady=20)


# Cube Display Frame
cube_frame = customtkinter.CTkFrame(root, corner_radius=10)
cube_frame.pack(pady=20)

cube_label = customtkinter.CTkLabel(
    cube_frame,
    text="Cube Display Area",
    font=("Arial", 18)
)
cube_label.pack(pady=10)

cube_canvas = customtkinter.CTkCanvas(
    cube_frame,
    width=800,
    height=600,
    bg="#222222",
    highlightthickness=0
)
cube_canvas.pack()


# Control Buttons Frame
buttons_frame = customtkinter.CTkFrame(root, corner_radius=10, width=800, height=200)
buttons_frame.pack(pady=50)


# Solve Button in Frame
solve_button = customtkinter.CTkButton(
    buttons_frame,
    width=150,
    height=50,
    text="Solve Cube",
    font=("Arial", 16)
)
solve_button.grid(row=0, column=0, padx=20, pady=20)


# Scramble Button in Frame
scramble_button = customtkinter.CTkButton(
    buttons_frame,
    width=150,
    height=50,
    text="Scramble Cube",
    font=("Arial", 16)
)
scramble_button.grid(row=0, column=1, padx=20, pady=20)


# Reset Button in Frame
reset_button = customtkinter.CTkButton(
    buttons_frame,
    width=150,
    height=50,
    text="Reset Cube",
    font=("Arial", 16)
)
reset_button.grid(row=0, column=2, padx=20, pady=20)


# Exit Button in Frame
exit_button = customtkinter.CTkButton(
    buttons_frame,
    width=150,
    height=50,
    text="Exit",
    font=("Arial", 16),
    command=root.destroy
)
exit_button.grid(row=0, column=3, padx=20, pady=20)




# # Solve Button
# solve_button = customtkinter.CTkButton(
#     root,
#     width=150,
#     height=50,
#     text="Solve Cube",
#     font=("Arial", 16)
# )
# solve_button.pack(side=LEFT, pady=100, padx=900)


# # Scramble Button
# scramble_button = customtkinter.CTkButton(
#     root,
#     width=150,
#     height=50,
#     text="Scramble Cube",
#     font=("Arial", 16)
# )
# scramble_button.pack(pady=100, padx=30)


# # Reset Button
# reset_button = customtkinter.CTkButton(
#     root,
#     width=150,
#     height=50,
#     text="Reset Cube",
#     font=("Arial", 16)
# )
# reset_button.pack(side=LEFT, pady=100, padx=30)


# # Exit Button
# exit_button = customtkinter.CTkButton(
#     root,
#     width=150,
#     height=50,
#     text="Exit",
#     font=("Arial", 16),
#     command=root.destroy
# )
# exit_button.pack(side=LEFT, pady=100, padx=30)


root.mainloop()