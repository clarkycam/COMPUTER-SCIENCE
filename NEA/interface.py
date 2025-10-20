from tkinter import *
import customtkinter
from PIL import Image

# --- Window Setup ---
customtkinter.set_appearance_mode("dark") # Modes: system (default), dark, light
customtkinter.set_default_color_theme("blue") # Themes: blue (default), dark-blue, green


root = customtkinter.CTk()
root.title("Rubik's Cube Solver")
root.iconbitmap("NEA/icon.ico")
root.geometry("1920x1080")


# --- Fullscreen Toggle Functionality ---
is_fullscreen = False


def toggle_fullscreen():
    global is_fullscreen
    if is_fullscreen:
        root.attributes("-fullscreen", False)
        fullscreen_button.configure(image=windowed_icon)
        is_fullscreen = False
    else:
        root.attributes("-fullscreen", True)
        fullscreen_button.configure(image=fullscreen_icon)
        is_fullscreen = True


# --- Title ---
title_label = customtkinter.CTkLabel(
    root,
    text="Rubik's Cube Solver",
    font=("Arial", 28, "bold")
)
title_label.pack(pady=20)


# --- Cube Display Frame ---
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


# --- Load Fullscreen and Windowed Icons ---
fullscreen_icon = customtkinter.CTkImage(Image.open("NEA/fullscreen.png"), size=(30, 30))
windowed_icon = customtkinter.CTkImage(Image.open("NEA/windowed.png"), size=(30, 30))


# --- Fullscreen Toggle Button ---
fullscreen_button = customtkinter.CTkButton(
    root,
    text="",
    image=fullscreen_icon,
    width=40,
    height=40,
    fg_color="transparent",
    hover_color=("#1f1f1f", "#dcdcdc"),
    command=toggle_fullscreen
)
fullscreen_button.place(relx=0.99, rely=0.99, anchor="se")


# Control Buttons Frame
buttons_frame = customtkinter.CTkFrame(root, corner_radius=10, width=800, height=200)
buttons_frame.pack(pady=50)


# Solve Button in Frame
solve_button = customtkinter.CTkButton(buttons_frame, width=150, height=50, text="Solve Cube", font=("Arial", 16))
solve_button.grid(row=0, column=0, padx=20, pady=20)


# Scramble Button in Frame
scramble_button = customtkinter.CTkButton(buttons_frame, width=150, height=50, text="Scramble Cube", font=("Arial", 16))
scramble_button.grid(row=0, column=1, padx=20, pady=20)


# Reset Button in Frame
reset_button = customtkinter.CTkButton(buttons_frame, width=150, height=50, text="Reset Cube", font=("Arial", 16))
reset_button.grid(row=0, column=2, padx=20, pady=20)


# Exit Button in Frame
exit_button = customtkinter.CTkButton(buttons_frame, width=150, height=50, text="Exit", font=("Arial", 16), command=root.destroy)
exit_button.grid(row=0, column=3, padx=20, pady=20)


root.mainloop()