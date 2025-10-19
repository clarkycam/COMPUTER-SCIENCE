from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("system") # Modes: system (default), dark, light
customtkinter.set_default_color_theme("blue") # Themes: blue (default), dark-blue, green

# root = tk()
root = customtkinter.CTk()

root.title("Rubik's Cube Solver")
root.iconbitmap("NEA/icon.ico")
root.geometry("1280x720")

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
    width=400,
    height=400,
    bg="#222222",
    highlightthickness=0
)
cube_canvas.pack()

root.mainloop()