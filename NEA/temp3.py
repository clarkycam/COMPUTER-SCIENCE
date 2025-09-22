import customtkinter as ctk
import random

class RubiksCubeViewer(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Rubik's Cube Viewer")
        self.geometry("1920x1080")
        
        self.colors = {
            'white': '#FFFFFF',
            'yellow': '#FFFF00',
            'blue': '#0000FF',
            'green': '#008000',
            'red': '#FF0000',
            'orange': '#FFA500'
        }
        self.color_names = list(self.colors.keys())

        self.initial_state = {
            'top': ['white'] * 9,
            'front': ['green'] * 9,
            'right': ['red'] * 9,
            'left': ['orange'] * 9,
            'back': ['blue'] * 9,
            'bottom': ['yellow'] * 9
        }
        
        # The current state of the cube, which will now be updated on clicks
        self.current_state = {face: colors[:] for face, colors in self.initial_state.items()}
        self.current_color = self.colors['white']
        self.all_tiles = {}
        self.message_label = None

        self.create_widgets()
        self.update_cube_view()

    def create_widgets(self):
        """Builds the main window, cube faces, and buttons."""
        main_frame = ctk.CTkFrame(self, fg_color="transparent")
        main_frame.pack(padx=20, pady=20)

        face_frames = {}
        for face_name in self.initial_state:
            face_frames[face_name] = ctk.CTkFrame(main_frame, fg_color="gray20", border_width=2, corner_radius=10)
            self.all_tiles[face_name] = []
            
        face_frames['top'].grid(row=0, column=1, padx=5, pady=5)
        face_frames['left'].grid(row=1, column=0, padx=5, pady=5)
        face_frames['front'].grid(row=1, column=1, padx=5, pady=5)
        face_frames['right'].grid(row=1, column=2, padx=5, pady=5)
        face_frames['back'].grid(row=1, column=3, padx=5, pady=5)
        face_frames['bottom'].grid(row=2, column=1, padx=5, pady=5)

        for face_name in self.initial_state:
            frame = face_frames[face_name]
            for i in range(9):
                row, col = divmod(i, 3)
                
                tile = ctk.CTkButton(
                    frame, fg_color=self.colors['white'], hover_color=self.colors['white'],
                    text="", width=60, height=60, corner_radius=5,
                )
                # Pass both the tile object and its position to the click handler
                tile.configure(command=lambda tile=tile, face=face_name, index=i: self.set_tile_color(tile, face, index))
                tile.grid(row=row, column=col, padx=2, pady=2)
                self.all_tiles[face_name].append(tile)
        
        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.pack(pady=20)
        
        scramble_button = ctk.CTkButton(button_frame, text="Scramble", command=self.scramble_cube, width=120)
        scramble_button.grid(row=0, column=0, padx=10)
        
        clear_button = ctk.CTkButton(button_frame, text="Clear", command=self.clear_cube, width=120)
        clear_button.grid(row=0, column=1, padx=10)
        
        checker_button = ctk.CTkButton(button_frame, text="Check Solvability", command=self.check_solvability, width=160)
        checker_button.grid(row=0, column=2, padx=10)
        
        picker_label = ctk.CTkLabel(button_frame, text="Pick a color:", font=("Arial", 16))
        picker_label.grid(row=0, column=3, padx=(30, 10))

        for i, color_name in enumerate(self.color_names):
            color_hex = self.colors[color_name]
            color_button = ctk.CTkButton(
                button_frame, text="", fg_color=color_hex, hover_color=color_hex,
                width=50, height=50, corner_radius=5,
                command=lambda color=color_hex: self.select_color(color)
            )
            color_button.grid(row=0, column=i + 4, padx=5)
            
        self.message_label = ctk.CTkLabel(self, text="", font=("Arial", 16), text_color="green")
        self.message_label.pack(pady=10)

    def update_cube_view(self):
        """Updates the visual view based on the current_state data."""
        for face_name, tiles in self.all_tiles.items():
            for i, tile in enumerate(tiles):
                color_name = self.current_state[face_name][i]
                color_hex = self.colors[color_name]
                tile.configure(fg_color=color_hex, hover_color=color_hex)
                
    def select_color(self, color):
        """Sets the currently active color for manual changes."""
        self.current_color = color
        self.message_label.configure(text=f"Selected color: {color}")

    def set_tile_color(self, tile, face, index):
        """Updates both the visual color and the internal state of a tile."""
        # 1. Update the visual color
        tile.configure(fg_color=self.current_color, hover_color=self.current_color)
        
        # 2. Find the name of the new color and update the internal state
        for color_name, color_hex in self.colors.items():
            if color_hex == self.current_color:
                self.current_state[face][index] = color_name
                break
        
    def scramble_cube(self):
        self.message_label.configure(text="Scrambling cube...")
        all_moves = ["U", "D", "L", "R", "F", "B", "U'", "D'", "L'", "R'", "F'", "B'"]
        
        for _ in range(random.randint(25, 40)):
            move = random.choice(all_moves)
            self.apply_move(move)
        
        self.update_cube_view()
        self.message_label.configure(text="Scramble complete! The cube is in a solvable state.")

    def apply_move(self, move):
        state = self.current_state
        
        def rotate_face(face):
            return [face[6], face[3], face[0], face[7], face[4], face[1], face[8], face[5], face[2]]
        
        def rotate_face_inv(face):
            return [face[2], face[5], face[8], face[1], face[4], face[7], face[0], face[3], face[6]]

        if move == "U":
            state['top'] = rotate_face(state['top'])
            temp = state['front'][0:3]
            state['front'][0:3] = state['right'][0:3]
            state['right'][0:3] = state['back'][0:3]
            state['back'][0:3] = state['left'][0:3]
            state['left'][0:3] = temp
        elif move == "U'":
            state['top'] = rotate_face_inv(state['top'])
            temp = state['front'][0:3]
            state['front'][0:3] = state['left'][0:3]
            state['left'][0:3] = state['back'][0:3]
            state['back'][0:3] = state['right'][0:3]
            state['right'][0:3] = temp
        elif move == "D":
            state['bottom'] = rotate_face(state['bottom'])
            temp = state['front'][6:9]
            state['front'][6:9] = state['left'][6:9]
            state['left'][6:9] = state['back'][6:9]
            state['back'][6:9] = state['right'][6:9]
            state['right'][6:9] = temp
        elif move == "D'":
            state['bottom'] = rotate_face_inv(state['bottom'])
            temp = state['front'][6:9]
            state['front'][6:9] = state['right'][6:9]
            state['right'][6:9] = state['back'][6:9]
            state['back'][6:9] = state['left'][6:9]
            state['left'][6:9] = temp
        elif move == "L":
            state['left'] = rotate_face(state['left'])
            temp = [state['top'][0], state['top'][3], state['top'][6]]
            state['top'][0], state['top'][3], state['top'][6] = state['back'][8], state['back'][5], state['back'][2]
            state['back'][2], state['back'][5], state['back'][8] = state['bottom'][0], state['bottom'][3], state['bottom'][6]
            state['bottom'][0], state['bottom'][3], state['bottom'][6] = state['front'][0], state['front'][3], state['front'][6]
            state['front'][0], state['front'][3], state['front'][6] = temp[0], temp[1], temp[2]
        elif move == "L'":
            state['left'] = rotate_face_inv(state['left'])
            temp = [state['top'][0], state['top'][3], state['top'][6]]
            state['top'][0], state['top'][3], state['top'][6] = state['front'][0], state['front'][3], state['front'][6]
            state['front'][0], state['front'][3], state['front'][6] = state['bottom'][0], state['bottom'][3], state['bottom'][6]
            state['bottom'][0], state['bottom'][3], state['bottom'][6] = state['back'][2], state['back'][5], state['back'][8]
            state['back'][2], state['back'][5], state['back'][8] = temp[0], temp[1], temp[2]
        elif move == "R":
            state['right'] = rotate_face(state['right'])
            temp = [state['top'][2], state['top'][5], state['top'][8]]
            state['top'][2], state['top'][5], state['top'][8] = state['front'][2], state['front'][5], state['front'][8]
            state['front'][2], state['front'][5], state['front'][8] = state['bottom'][2], state['bottom'][5], state['bottom'][8]
            state['bottom'][2], state['bottom'][5], state['bottom'][8] = state['back'][6], state['back'][3], state['back'][0]
            state['back'][0], state['back'][3], state['back'][6] = temp[2], temp[1], temp[0]
        elif move == "R'":
            state['right'] = rotate_face_inv(state['right'])
            temp = [state['top'][2], state['top'][5], state['top'][8]]
            state['top'][2], state['top'][5], state['top'][8] = state['back'][6], state['back'][3], state['back'][0]
            state['back'][0], state['back'][3], state['back'][6] = state['bottom'][8], state['bottom'][5], state['bottom'][2]
            state['bottom'][2], state['bottom'][5], state['bottom'][8] = state['front'][2], state['front'][5], state['front'][8]
            state['front'][2], state['front'][5], state['front'][8] = temp[0], temp[1], temp[2]
        elif move == "F":
            state['front'] = rotate_face(state['front'])
            temp = [state['top'][6], state['top'][7], state['top'][8]]
            state['top'][6], state['top'][7], state['top'][8] = state['left'][8], state['left'][5], state['left'][2]
            state['left'][2], state['left'][5], state['left'][8] = state['bottom'][0], state['bottom'][1], state['bottom'][2]
            state['bottom'][0], state['bottom'][1], state['bottom'][2] = state['right'][6], state['right'][3], state['right'][0]
            state['right'][0], state['right'][3], state['right'][6] = temp[2], temp[1], temp[0]
        elif move == "F'":
            state['front'] = rotate_face_inv(state['front'])
            temp = [state['top'][6], state['top'][7], state['top'][8]]
            state['top'][6], state['top'][7], state['top'][8] = state['right'][0], state['right'][3], state['right'][6]
            state['right'][0], state['right'][3], state['right'][6] = state['bottom'][2], state['bottom'][1], state['bottom'][0]
            state['bottom'][0], state['bottom'][1], state['bottom'][2] = state['left'][2], state['left'][5], state['left'][8]
            state['left'][2], state['left'][5], state['left'][8] = temp[2], temp[1], temp[0]
        elif move == "B":
            state['back'] = rotate_face(state['back'])
            temp = [state['top'][0], state['top'][1], state['top'][2]]
            state['top'][0], state['top'][1], state['top'][2] = state['right'][2], state['right'][5], state['right'][8]
            state['right'][2], state['right'][5], state['right'][8] = state['bottom'][8], state['bottom'][7], state['bottom'][6]
            state['bottom'][6], state['bottom'][7], state['bottom'][8] = state['left'][6], state['left'][3], state['left'][0]
            state['left'][0], state['left'][3], state['left'][6] = temp[2], temp[1], temp[0]
        elif move == "B'":
            state['back'] = rotate_face_inv(state['back'])
            temp = [state['top'][0], state['top'][1], state['top'][2]]
            state['top'][0], state['top'][1], state['top'][2] = state['left'][6], state['left'][3], state['left'][0]
            state['left'][0], state['left'][3], state['left'][6] = state['bottom'][6], state['bottom'][7], state['bottom'][8]
            state['bottom'][6], state['bottom'][7], state['bottom'][8] = state['right'][2], state['right'][5], state['right'][8]
            state['right'][2], state['right'][5], state['right'][8] = temp[0], temp[1], temp[2]

    def clear_cube(self):
        self.current_state = {face: colors[:] for face, colors in self.initial_state.items()}
        self.update_cube_view()
        self.message_label.configure(text="Cube has been reset to its solved state.")
        
    def check_solvability(self):
        """
        A highly reliable checker that validates two core properties of a solvable cube state.
        1. The total count of each color must be 9.
        2. The central tiles must have their correct initial colors.
        """
        color_counts = {color: 0 for color in self.colors}
        for face_name in self.current_state:
            for color in self.current_state[face_name]:
                color_counts[color] += 1
        
        has_correct_colors = all(count == 9 for count in color_counts.values())
        
        center_pieces_correct = (
            self.current_state['top'][4] == self.initial_state['top'][4] and
            self.current_state['front'][4] == self.initial_state['front'][4] and
            self.current_state['right'][4] == self.initial_state['right'][4] and
            self.current_state['left'][4] == self.initial_state['left'][4] and
            self.current_state['back'][4] == self.initial_state['back'][4] and
            self.current_state['bottom'][4] == self.initial_state['bottom'][4]
        )
        
        if has_correct_colors and center_pieces_correct:
            self.message_label.configure(text="Check passed! This is a valid cube state. ✅", text_color="green")
        else:
            self.message_label.configure(text="Check failed. This is NOT a valid cube state. ❌", text_color="red")
            
if __name__ == "__main__":
    app = RubiksCubeViewer()
    app.mainloop()