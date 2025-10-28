from tkinter import *
import customtkinter
from PIL import Image

# --- Window Setup ---
customtkinter.set_appearance_mode("dark") # Modes: system (default), dark, light
customtkinter.set_default_color_theme("dark-blue") # Themes: "blue" (default), dark-blue, green, "NEA/THEMES/breeze.json"

root = customtkinter.CTk()
root.title("Rubik's Cube Solver")
root.iconbitmap("NEA/IMAGES/icon.ico")
root.geometry("1400x950")

# --- Main Frame ---
main_frame = customtkinter.CTkFrame(root, corner_radius=10, width=1300, height=700, fg_color="#00FF00")
main_frame.pack(pady=20, padx=20)






#version 1





# version 2
# --- Colour Picker Frame ---
colour_picker_frame = customtkinter.CTkFrame(main_frame, corner_radius=10, width=200, height=300)
colour_picker_frame.grid_propagate(False)
colour_picker_frame.grid(row=0, column=0, padx=20, pady=0, sticky="w")

# two equal columns for buttons
colour_picker_frame.grid_columnconfigure((0, 1), weight=1)

# colour picker label
colour_picker_label = customtkinter.CTkLabel(
    colour_picker_frame,
    text="Colour Picker",
    font=("Arial", 18)
)
colour_picker_label.grid(row=0, column=0, padx=0, pady=10, sticky="n", columnspan=2)

# --- Colour Buttons ---
tile_width = 70
tile_height = 70

# white button
white_button = customtkinter.CTkButton(
    colour_picker_frame,
    width=tile_width,
    height=tile_height,
    fg_color="#FFFFFF",
    text="",
    hover_color="#DDDDDD", 
    border_width=2, 
    border_color="#000000"
)
white_button.grid(row=1, column=0, padx=0, pady=0)

# orange button
orange_button = customtkinter.CTkButton(
    colour_picker_frame,
    width=tile_width,
    height=tile_height,
    fg_color="#FFA500",
    text="",
    hover_color="#FF8C00",
    border_width=2,
    border_color="#000000"
)
orange_button.grid(row=1, column=1, padx=0, pady=0)

# green button
green_button = customtkinter.CTkButton(
    colour_picker_frame,
    width=tile_width,
    height=tile_height,
    fg_color="#008000",
    text="",
    hover_color="#006400",
    border_width=2,
    border_color="#000000"
)
green_button.grid(row=2, column=0, padx=0, pady=0)

# red button
red_button = customtkinter.CTkButton(
    colour_picker_frame,
    width=tile_width,
    height=tile_height,
    fg_color="#FF0000",
    text="",
    hover_color="#B22222",
    border_width=2,
    border_color="#000000"
)
red_button.grid(row=2, column=1, padx=0, pady=0)

# blue button
blue_button = customtkinter.CTkButton(
    colour_picker_frame,
    width=tile_width,
    height=tile_height,
    fg_color="#0000FF",
    text="",
    hover_color="#0000CD",
    border_width=2,
    border_color="#000000"
)
blue_button.grid(row=3, column=0, padx=0, pady=0)

# yellow button
yellow_button = customtkinter.CTkButton(
    colour_picker_frame,
    width=tile_width,
    height=tile_height,
    fg_color="#FFFF00",
    text="",
    hover_color="#FFD700",
    border_width=2,
    border_color="#000000"
)
yellow_button.grid(row=3, column=1, padx=0, pady=0)
