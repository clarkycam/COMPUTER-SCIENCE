from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark") # Modes: system (default), dark, light
customtkinter.set_default_color_theme("blue") # Themes: blue (default), dark-blue, green

# root = tk()
root = customtkinter.CTk()

root.title("Rubik's Cube Solver")
root.iconbitmap("NEA/icon.ico")
root.geometry("1280x720")

root.mainloop()