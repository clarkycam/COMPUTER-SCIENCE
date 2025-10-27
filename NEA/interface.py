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
    
    # Update frame colours manually to match new theme
    cube_frame.configure(fg_color=customtkinter.ThemeManager.theme["CTkFrame"]["fg_color"])
    buttons_frame.configure(fg_color=customtkinter.ThemeManager.theme["CTkFrame"]["fg_color"])


# --- Title ---
title_label = customtkinter.CTkLabel(
    root,
    text="Rubik's Cube Solver",
    font=("Arial", 28, "bold")
)
title_label.pack(pady=20)


# --- Main Frame ---
main_frame = customtkinter.CTkFrame(root, corner_radius=10)
main_frame.pack(pady=20)

# --- Cube Display Frame ---
cube_frame = customtkinter.CTkFrame(main_frame, corner_radius=10)
cube_frame.pack(pady=20)

cube_label = customtkinter.CTkLabel(
    cube_frame,
    text="Cube Display",
    font=("Arial", 18)
)
cube_label.pack(pady=10)


# --- Cube Grid Frame ---
cube_grid = customtkinter.CTkFrame(cube_frame, width=800, height=500, fg_color="transparent")
cube_grid.pack(padx=20, pady=20)


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


# --- Control Buttons ---
solve_button = customtkinter.CTkButton(buttons_frame, width=150, height=50, text="Solve Cube", font=("Arial", 16))
solve_button.grid(row=0, column=0, padx=20, pady=20)

scramble_button = customtkinter.CTkButton(buttons_frame, width=150, height=50, text="Scramble Cube", font=("Arial", 16))
scramble_button.grid(row=0, column=1, padx=20, pady=20)

reset_button = customtkinter.CTkButton(buttons_frame, width=150, height=50, text="Reset Cube", font=("Arial", 16))
reset_button.grid(row=0, column=2, padx=20, pady=20)

exit_button = customtkinter.CTkButton(buttons_frame, width=150, height=50, text="Exit", font=("Arial", 16), command=root.destroy)
exit_button.grid(row=0, column=3, padx=20, pady=20)


# --- Main Loop ---
root.mainloop()