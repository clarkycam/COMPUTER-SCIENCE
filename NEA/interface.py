from tkinter import *
import customtkinter
from PIL import Image

# --- Window Setup ---
customtkinter.set_appearance_mode("dark") # Modes: system (default), dark, light
customtkinter.set_default_color_theme("dark-blue") # Themes: "blue" (default), "dark-blue", "green", "NEA/THEMES/breeze.json"

root = customtkinter.CTk()
root.title("Rubik's Cube Solver")
root.iconbitmap("NEA/IMAGES/icon.ico")
root.geometry("1400x950")



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


# --- Light/Dark Mode Toggle Functionality ---
def toggle_appearance_mode():
    current_mode = customtkinter.get_appearance_mode()

    if current_mode == "Dark":
        customtkinter.set_appearance_mode("light")
        theme_button.configure(image=dark_mode_icon)
    else:
        customtkinter.set_appearance_mode("dark")
        theme_button.configure(image=light_mode_icon)



# --- Title ---
title_label = customtkinter.CTkLabel(
    root,
    text="Rubik's Cube Solver",
    font=("Arial", 28, "bold")
)
title_label.pack(pady=20)



# --- Main Frame ---
main_frame = customtkinter.CTkFrame(root, corner_radius=10, width=1300, height=700)
main_frame.pack(pady=20, padx=20)


# --- Colour Picker Frame ---
colour_picker_frame = customtkinter.CTkFrame(main_frame, corner_radius=10, width=200, height=350)
colour_picker_frame.grid_propagate(True)
colour_picker_frame.grid(row=0, column=0, padx=20, pady=0, sticky="w")

# two equal columns
colour_picker_frame.grid_columnconfigure((0, 1), weight=1)

# colour picker label
colour_picker_label = customtkinter.CTkLabel(
    colour_picker_frame,
    text="Colour Picker",
    font=("Arial", 18)
)
colour_picker_label.grid(row=0, column=0, padx=0, pady=(10, 0), sticky="n", columnspan=2)

# --- Colour Buttons Frame ---
colour_buttons_frame = customtkinter.CTkFrame(colour_picker_frame, corner_radius=10)
colour_buttons_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
colour_buttons_frame.grid_propagate(True)

# colour buttons
tile_width = 80
tile_height = 80

# white button
white_button = customtkinter.CTkButton(
    colour_buttons_frame,
    width=tile_width,
    height=tile_height,
    fg_color="#FFFFFF",
    text="",
    hover_color="#cccccc",
    border_width=2,
    border_color="#000000"
)
white_button.grid(row=0, column=0, padx=5, pady=5)

# orange button
orange_button = customtkinter.CTkButton(
    colour_buttons_frame,
    width=tile_width,
    height=tile_height,
    fg_color="#FF5900",
    text="",
    hover_color="#cc4700",
    border_width=2,
    border_color="#000000"
)
orange_button.grid(row=0, column=1, padx=5, pady=5)

# green button
green_button = customtkinter.CTkButton(
    colour_buttons_frame,
    width=tile_width,
    height=tile_height,
    fg_color="#009B48",
    text="",
    hover_color="#007c3a",
    border_width=2,
    border_color="#000000"
)
green_button.grid(row=1, column=0, padx=5, pady=5)

# red button
red_button = customtkinter.CTkButton(
    colour_buttons_frame,
    width=tile_width,
    height=tile_height,
    fg_color="#B90000",
    text="",
    hover_color="#940000",
    border_width=2,
    border_color="#000000"
)
red_button.grid(row=1, column=1, padx=5, pady=5)

# blue button
blue_button = customtkinter.CTkButton(
    colour_buttons_frame,
    width=tile_width,
    height=tile_height,
    fg_color="#0045AD",
    text="",
    hover_color="#00378a",
    border_width=2,
    border_color="#000000"
)
blue_button.grid(row=2, column=0, padx=5, pady=5)

# yellow button
yellow_button = customtkinter.CTkButton(
    colour_buttons_frame,
    width=tile_width,
    height=tile_height,
    fg_color="#FFD500",
    text="",
    hover_color="#ccaa00",
    border_width=2,
    border_color="#000000"
)
yellow_button.grid(row=2, column=1, padx=5, pady=5)



# # --- Colour Buttons ---
# tile_width = 70
# tile_height = 70

# # white button
# white_button = customtkinter.CTkButton(
#     colour_picker_frame,
#     width=tile_width,
#     height=tile_height,
#     fg_color="#FFFFFF",
#     text="",
#     hover_color="#DDDDDD", 
#     border_width=2, 
#     border_color="#000000"
# )
# white_button.grid(row=1, column=0, padx=0, pady=0)

# # orange button
# orange_button = customtkinter.CTkButton(
#     colour_picker_frame,
#     width=tile_width,
#     height=tile_height,
#     fg_color="#FFA500",
#     text="",
#     hover_color="#FF8C00",
#     border_width=2,
#     border_color="#000000"
# )
# orange_button.grid(row=1, column=1, padx=0, pady=0)

# # green button
# green_button = customtkinter.CTkButton(
#     colour_picker_frame,
#     width=tile_width,
#     height=tile_height,
#     fg_color="#008000",
#     text="",
#     hover_color="#006400",
#     border_width=2,
#     border_color="#000000"
# )
# green_button.grid(row=2, column=0, padx=0, pady=0)

# # red button
# red_button = customtkinter.CTkButton(
#     colour_picker_frame,
#     width=tile_width,
#     height=tile_height,
#     fg_color="#FF0000",
#     text="",
#     hover_color="#B22222",
#     border_width=2,
#     border_color="#000000"
# )
# red_button.grid(row=2, column=1, padx=0, pady=0)

# # blue button
# blue_button = customtkinter.CTkButton(
#     colour_picker_frame,
#     width=tile_width,
#     height=tile_height,
#     fg_color="#0000FF",
#     text="",
#     hover_color="#0000CD",
#     border_width=2,
#     border_color="#000000"
# )
# blue_button.grid(row=3, column=0, padx=0, pady=0)

# # yellow button
# yellow_button = customtkinter.CTkButton(
#     colour_picker_frame,
#     width=tile_width,
#     height=tile_height,
#     fg_color="#FFFF00",
#     text="",
#     hover_color="#FFD700",
#     border_width=2,
#     border_color="#000000"
# )
# yellow_button.grid(row=3, column=1, padx=0, pady=0)


# --- Cube Display Frame ---
cube_frame = customtkinter.CTkFrame(main_frame, corner_radius=10)
cube_frame.grid(row=0, column=1, padx=0, pady=20)
# cube label
cube_label = customtkinter.CTkLabel(cube_frame, text="Cube Display", font=("Arial", 18))
cube_label.grid(row=0, column=0, padx=0, pady=(10, 0))
# cube grid frame
cube_grid = customtkinter.CTkFrame(cube_frame, width=800, height=500)
cube_grid.grid(row=1, column=0, padx=10, pady=10)


# --- Options Frame ---
options_frame = customtkinter.CTkFrame(main_frame, corner_radius=10, width=200, height=300)
options_frame.grid(row=0, column=2, padx=20, pady=20, sticky="e")



# --- Load Icons ---
fullscreen_icon = customtkinter.CTkImage(Image.open("NEA/IMAGES/fullscreen.png"), size=(30, 30))
windowed_icon = customtkinter.CTkImage(Image.open("NEA/IMAGES/windowed.png"), size=(30, 30))
light_mode_icon = customtkinter.CTkImage(Image.open("NEA/IMAGES/light_mode.png"), size=(30, 30))
dark_mode_icon = customtkinter.CTkImage(Image.open("NEA/IMAGES/dark_mode.png"), size=(30, 30))


# --- Fullscreen Toggle Button ---
fullscreen_button = customtkinter.CTkButton(
    root,
    text="",
    image=windowed_icon,
    width=40,
    height=45,
    fg_color="transparent",
    hover_color=customtkinter.ThemeManager.theme["CTkButton"]["hover_color"],  # hover colour from theme
    command=toggle_fullscreen
)
fullscreen_button.place(relx=0.99, rely=0.985, anchor="se")


# --- Theme Toggle Button ---
theme_button = customtkinter.CTkButton(
    root,
    text="",
    image=light_mode_icon,
    width=40,
    height=45,
    fg_color="transparent",
    hover_color=customtkinter.ThemeManager.theme["CTkButton"]["hover_color"],
    command=toggle_appearance_mode
)
theme_button.place(relx=0.01, rely=0.985, anchor="sw")



# --- Control Buttons Frame ---
buttons_frame = customtkinter.CTkFrame(root, corner_radius=10, width=800, height=200)
buttons_frame.pack(pady=50)

# solve button
solve_button = customtkinter.CTkButton(buttons_frame, width=150, height=50, text="Solve Cube", font=("Arial", 16))
solve_button.grid(row=0, column=0, padx=20, pady=20)

# scramble button
scramble_button = customtkinter.CTkButton(buttons_frame, width=150, height=50, text="Scramble Cube", font=("Arial", 16))
scramble_button.grid(row=0, column=1, padx=20, pady=20)

# reset button
reset_button = customtkinter.CTkButton(buttons_frame, width=150, height=50, text="Reset Cube", font=("Arial", 16))
reset_button.grid(row=0, column=2, padx=20, pady=20)

# exit button
exit_button = customtkinter.CTkButton(buttons_frame, width=150, height=50, text="Exit", font=("Arial", 16), command=root.destroy)
exit_button.grid(row=0, column=3, padx=20, pady=20)



# --- Main Loop ---
root.mainloop()