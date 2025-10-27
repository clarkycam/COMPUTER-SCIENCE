from tkinter import *
import customtkinter
from PIL import Image

# --- Window Setup ---
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.title("Rubik's Cube Solver")
root.iconbitmap("NEA/IMAGES/icon.ico")
root.geometry("1280x950")

# --- Fullscreen Toggle ---
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


# --- Theme Toggle ---
def toggle_appearance_mode():
    current_mode = customtkinter.get_appearance_mode()

    if current_mode == "Dark":
        customtkinter.set_appearance_mode("light")
        theme_button.configure(image=dark_mode_icon)
    else:
        customtkinter.set_appearance_mode("dark")
        theme_button.configure(image=light_mode_icon)

    # Refresh frame colours when switching mode
    cube_frame.configure(fg_color=customtkinter.ThemeManager.theme["CTkFrame"]["fg_color"])
    buttons_frame.configure(fg_color=customtkinter.ThemeManager.theme["CTkFrame"]["fg_color"])


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

# --- Cube Grid Frame ---
cube_grid = customtkinter.CTkFrame(cube_frame, fg_color="transparent")
cube_grid.pack(padx=20, pady=20)

# --- Cube Data ---
test_cube = {
    "U": [["white"] * 3 for _ in range(3)],
    "L": [["orange"] * 3 for _ in range(3)],
    "F": [["green"] * 3 for _ in range(3)],
    "R": [["red"] * 3 for _ in range(3)],
    "B": [["blue"] * 3 for _ in range(3)],
    "D": [["yellow"] * 3 for _ in range(3)]
}

# --- Colours in Cycle Order ---
colour_order = ["white", "yellow", "red", "orange", "green", "blue"]

# --- Sticker Buttons Dictionary ---
sticker_buttons = {}


# --- Change Colour Function ---
def change_colour(face, row, col):
    current_colour = test_cube[face][row][col]
    next_index = (colour_order.index(current_colour) + 1) % len(colour_order)
    next_colour = colour_order[next_index]
    test_cube[face][row][col] = next_colour

    # Update button colour
    button = sticker_buttons[(face, row, col)]
    button.configure(fg_color=next_colour, hover_color=next_colour)


# --- Draw Cube ---
def draw_cube():
    for widget in cube_grid.winfo_children():
        widget.destroy()

    size = 50
    padding = 5

    # Define where each face goes (row offset, column offset)
    face_positions = {
        "U": (0, 3),
        "L": (3, 0),
        "F": (3, 3),
        "R": (3, 6),
        "B": (3, 9),
        "D": (6, 3)
    }

    # Draw each face separately
    for face in face_positions:
        start_row = face_positions[face][0]
        start_col = face_positions[face][1]

        for r in range(3):
            for c in range(3):
                colour = test_cube[face][r][c]

                # Create a button for each sticker
                sticker = customtkinter.CTkButton(
                    cube_grid,
                    width=size,
                    height=size,
                    text="",
                    fg_color=colour,
                    hover_color=colour,
                    corner_radius=0,
                    command=lambda f=face, row=r, col=c: change_colour(f, row, col)
                )
                sticker.grid(row=start_row + r, column=start_col + c, padx=padding, pady=padding)

                # Save a reference to the button
                sticker_buttons[(face, r, c)] = sticker


# --- Load Icons ---
fullscreen_icon = customtkinter.CTkImage(Image.open("NEA/IMAGES/fullscreen.png"), size=(30, 30))
windowed_icon = customtkinter.CTkImage(Image.open("NEA/IMAGES/windowed.png"), size=(30, 30))
light_mode_icon = customtkinter.CTkImage(Image.open("NEA/IMAGES/light_mode.png"), size=(30, 30))
dark_mode_icon = customtkinter.CTkImage(Image.open("NEA/IMAGES/dark_mode.png"), size=(30, 30))

# --- Draw Cube at Startup ---
draw_cube()

# --- Fullscreen Toggle Button ---
fullscreen_button = customtkinter.CTkButton(
    root,
    text="",
    image=windowed_icon,
    width=40,
    height=45,
    fg_color="transparent",
    hover_color=customtkinter.ThemeManager.theme["CTkButton"]["hover_color"],
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

# --- Control Buttons ---
solve_button = customtkinter.CTkButton(buttons_frame, width=150, height=50, text="Solve Cube", font=("Arial", 16))
solve_button.grid(row=0, column=0, padx=20, pady=20)

scramble_button = customtkinter.CTkButton(buttons_frame, width=150, height=50, text="Scramble Cube", font=("Arial", 16))
scramble_button.grid(row=0, column=1, padx=20, pady=20)

reset_button = customtkinter.CTkButton(buttons_frame, width=150, height=50, text="Reset Cube", font=("Arial", 16))
reset_button.grid(row=0, column=2, padx=20, pady=20)

exit_button = customtkinter.CTkButton(buttons_frame, width=150, height=50, text="Exit", font=("Arial", 16), command=root.destroy)
exit_button.grid(row=0, column=3, padx=20, pady=20)

root.mainloop()
