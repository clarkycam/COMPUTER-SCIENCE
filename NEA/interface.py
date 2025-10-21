from tkinter import *
import customtkinter
from PIL import Image

# --- Window Setup ---
customtkinter.set_appearance_mode("dark") # Modes: system (default), dark, light
customtkinter.set_default_color_theme("blue") # Themes: blue (default), dark-blue, green


root = customtkinter.CTk()
root.title("Rubik's Cube Solver")
root.iconbitmap("NEA/IMAGES/icon.ico")
root.geometry("1280x920")


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
        cube_canvas.configure(bg="#E5E5E5") # light grey for light mode
    else:
        customtkinter.set_appearance_mode("dark")
        theme_button.configure(image=light_mode_icon)
        cube_canvas.configure(bg="#222222") # dark grey for dark mode


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


# --- Canvas Background Colour Based on Theme ---
# appearance_mode = customtkinter.get_appearance_mode()

# if appearance_mode == "Dark":
#     canvas_bg = "#222222" # dark grey for dark mode
# else:
#     canvas_bg = "#E5E5E5" # light grey for light mode

cube_canvas = customtkinter.CTkCanvas(
    cube_frame,
    width=700,
    height=500,
    bg="#222222",
    highlightthickness=0
)
cube_canvas.pack()


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


# --- Solve Button in Frame ---
solve_button = customtkinter.CTkButton(buttons_frame, width=150, height=50, text="Solve Cube", font=("Arial", 16))
solve_button.grid(row=0, column=0, padx=20, pady=20)


# --- Scramble Button in Frame ---
scramble_button = customtkinter.CTkButton(buttons_frame, width=150, height=50, text="Scramble Cube", font=("Arial", 16))
scramble_button.grid(row=0, column=1, padx=20, pady=20)


# --- Reset Button in Frame ---
reset_button = customtkinter.CTkButton(buttons_frame, width=150, height=50, text="Reset Cube", font=("Arial", 16))
reset_button.grid(row=0, column=2, padx=20, pady=20)


# --- Exit Button in Frame ---
exit_button = customtkinter.CTkButton(buttons_frame, width=150, height=50, text="Exit", font=("Arial", 16), command=root.destroy)
exit_button.grid(row=0, column=3, padx=20, pady=20)


root.mainloop()