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

# face colours and hover colours
face_colours = {
    "U": {"main": "#FFFFFF", "hover": "#CCCCCC"},
    "L": {"main": "#FF5900", "hover": "#CC4700"},
    "F": {"main": "#009B48", "hover": "#007C3A"},
    "R": {"main": "#B90000", "hover": "#940000"},
    "B": {"main": "#0045AD", "hover": "#00378A"},
    "D": {"main": "#FFD500", "hover": "#CCAA00"}
}

# --- Colour Selection ---
cycle_mode = False
active_colour = {"main": "#FFFFFF", "hover": "#CCCCCC"}
# track picker buttons and which is active
colour_buttons = []
active_picker_button = None

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
colour_picker_frame = customtkinter.CTkFrame(main_frame, corner_radius=10, width=200, height=400) # height=320
colour_picker_frame.grid_propagate(False)
colour_picker_frame.grid(row=0, column=0, padx=20, pady=0, sticky="w")

# two equal columns
colour_picker_frame.grid_columnconfigure((0, 1), weight=1)

# colour picker label
colour_picker_label = customtkinter.CTkLabel(
    colour_picker_frame,
    text="Colour Picker",
    font=("Arial", 18),
    height=20
)
colour_picker_label.grid(row=0, column=0, padx=0, pady=(10, 0), sticky="n", columnspan=2)

# colour cycle functionality
def cycle_colours(button):
    global cycle_mode, face_colours, active_colour, active_picker_button
    cycle_mode = True

    for btn in colour_buttons:
        btn.configure(border_width=2)  # reset border of all buttons

    button.configure(border_width=4)  # highlight cycle button
    while cycle_mode:
        for i in range(1,6):
            active_colour = {"main": face_colours[i]["main"], "hover": face_colours[i]["hover"]}


# colour cycle button
cycle_button = customtkinter.CTkButton(
    colour_picker_frame,
    width=150,
    height=40,
    text="Cycle Colours",
    font=("Arial", 14),
    border_width=4,
    border_color="#000000",
    command=lambda: cycle_colours(cycle_button)
)
cycle_button.grid(row=2, column=0, padx=10, pady=(10,0), sticky="n", columnspan=2)

# --- Colour Buttons Frame ---
colour_buttons_frame = customtkinter.CTkFrame(colour_picker_frame, corner_radius=10, fg_color="transparent")
colour_buttons_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
colour_buttons_frame.grid_propagate(True)

# set active colour
def set_active_colour(main, hover, button):
    global active_colour, active_picker_button, cycle_mode
    active_colour = {"main": main, "hover": hover}

    # reset border for all picker buttons
    for btn in colour_buttons:
        btn.configure(border_width=2)
    cycle_button.configure(border_width=2)
    cycle_mode = False

    # make the clicked button look selected
    if button is not None:
        button.configure(border_width=4)
        active_picker_button = button


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
    border_color="#000000",
    command=lambda b=None: set_active_colour("#FFFFFF", "#CCCCCC", white_button)
)
white_button.grid(row=0, column=0, padx=5, pady=5)
colour_buttons.append(white_button)


orange_button = customtkinter.CTkButton(
    colour_buttons_frame,
    width=tile_width,
    height=tile_height,
    fg_color="#FF5900",
    text="",
    hover_color="#cc4700",
    border_width=2,
    border_color="#000000",
    command=lambda b=None: set_active_colour("#FF5900", "#CC4700", orange_button)
)
orange_button.grid(row=0, column=1, padx=5, pady=5)
colour_buttons.append(orange_button)


# green button
green_button = customtkinter.CTkButton(
    colour_buttons_frame,
    width=tile_width,
    height=tile_height,
    fg_color="#009B48",
    text="",
    hover_color="#007c3a",
    border_width=2,
    border_color="#000000",
    command=lambda b=None: set_active_colour("#009B48", "#007C3A", green_button)
)
green_button.grid(row=1, column=0, padx=5, pady=5)
colour_buttons.append(green_button)

# red button
red_button = customtkinter.CTkButton(
    colour_buttons_frame,
    width=tile_width,
    height=tile_height,
    fg_color="#B90000",
    text="",
    hover_color="#940000",
    border_width=2,
    border_color="#000000",
    command=lambda b=None: set_active_colour("#B90000", "#940000", red_button)
)
red_button.grid(row=1, column=1, padx=5, pady=5)
colour_buttons.append(red_button)

# blue button
blue_button = customtkinter.CTkButton(
    colour_buttons_frame,
    width=tile_width,
    height=tile_height,
    fg_color="#0045AD",
    text="",
    hover_color="#00378a",
    border_width=2,
    border_color="#000000",
    command=lambda b=None: set_active_colour("#0045AD", "#00378A", blue_button)
)
blue_button.grid(row=2, column=0, padx=5, pady=5)
colour_buttons.append(blue_button)

# yellow button
yellow_button = customtkinter.CTkButton(
    colour_buttons_frame,
    width=tile_width,
    height=tile_height,
    fg_color="#FFD500",
    text="",
    hover_color="#ccaa00",
    border_width=2,
    border_color="#000000",
    command=lambda b=None: set_active_colour("#FFD500", "#CCAA00", yellow_button)
)
yellow_button.grid(row=2, column=1, padx=5, pady=5)
colour_buttons.append(yellow_button)



# --- Cube Display Frame ---
cube_frame = customtkinter.CTkFrame(main_frame, corner_radius=10)
cube_frame.grid(row=0, column=1, padx=0, pady=20)
# cube label
cube_label = customtkinter.CTkLabel(cube_frame, text="Cube Display", font=("Arial", 18))
cube_label.grid(row=0, column=0, padx=0, pady=(10, 0))
# cube grid frame
cube_grid = customtkinter.CTkFrame(cube_frame, width=800, height=500, corner_radius=10)
cube_grid.grid(row=1, column=0, padx=10, pady=10)

# --- Cube Faces ---
frame_width = 150
faces = ["U", "L", "F", "R", "B", "D"]
# dictionary to hold each face
face_frames = {}

# define grid positions for each face
face_positions = {
    "U": (0, 1),
    "L": (1, 0),
    "F": (1, 1),
    "R": (1, 2),
    "B": (1, 3),
    "D": (2, 1)
}

# create frames for each face
for face in faces:
    r, c = face_positions[face]
    frame = customtkinter.CTkFrame(cube_grid, width=frame_width, height=frame_width, corner_radius=10, fg_color="transparent")
    frame.grid(row=r, column=c, padx=5, pady=5)
    face_frames[face] = frame

# --- Paint Function---
def paint_tile(tile):
    tile.configure(
        fg_color=active_colour["main"],
        hover_color=active_colour["hover"]
    )

# --- Cube Tiles ---
cube_size = 3
tile_padding = 3
tile_size = 50

# dictionary to hold button references
face_tiles = {}

for face, frame in face_frames.items():
    face_tiles[face] = [] # store each face's 9 buttons here
    
    for row in range(cube_size):
        for col in range(cube_size):
            tile = customtkinter.CTkButton(
                frame,
                width=tile_size,
                height=tile_size,
                text="",
                fg_color=face_colours[face]["main"],
                border_width=1,
                border_color="#000000",
                hover_color=face_colours[face]["hover"],
                command=lambda t=None: None  # placeholder for click action
            )

            tile.configure(command=lambda t=tile: paint_tile(t))
            tile.grid(row=row, column=col, padx=tile_padding, pady=tile_padding)
            face_tiles[face].append(tile)
    




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

# --- Reset Functionality ---
def reset_cube():
    for face, tiles in face_tiles.items():
        for tile in tiles:
            tile.configure(
                fg_color=face_colours[face]["main"],
                hover_color=face_colours[face]["hover"]
            )
# reset button
reset_button = customtkinter.CTkButton(
    buttons_frame,
    width=150,
    height=50,
    text="Reset Cube",
    font=("Arial", 16),
    command=reset_cube
)
reset_button.grid(row=0, column=2, padx=20, pady=20)

# exit button
exit_button = customtkinter.CTkButton(buttons_frame, width=150, height=50, text="Exit", font=("Arial", 16), command=root.destroy)
exit_button.grid(row=0, column=3, padx=20, pady=20)



# --- Main Loop ---
root.mainloop()