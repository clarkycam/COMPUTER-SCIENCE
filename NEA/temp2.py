import customtkinter as ctk

class RubiksCubeViewer(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Rubik's Cube Viewer")
        self.geometry("800x650")
        
        # Define the colors and their corresponding hex codes
        self.colors = {
            'white': '#FFFFFF',
            'yellow': '#FFFF00',
            'blue': '#0000FF',
            'green': '#008000',
            'red': '#FF0000',
            'orange': '#FFA500'
        }
        self.color_names = list(self.colors.keys())

        # Define the initial state of the cube's faces
        self.face_layouts = {
            'top': ['white'] * 9,
            'front': ['green'] * 9,
            'right': ['red'] * 9,
            'left': ['orange'] * 9,
            'back': ['blue'] * 9,
            'bottom': ['yellow'] * 9
        }
        
        # Initialize the current selected color
        self.current_color = self.colors['white']

        self.create_widgets()

    def create_widgets(self):
        """Builds the main window, cube faces, and color picker."""
        main_frame = ctk.CTkFrame(self, fg_color="transparent")
        main_frame.pack(padx=20, pady=20)

        # Create frames for each cube face
        face_frames = {}
        for face_name in self.face_layouts:
            face_frames[face_name] = ctk.CTkFrame(main_frame, fg_color="gray20", border_width=2, corner_radius=10)
            
        # Position the faces to resemble a cube net
        face_frames['top'].grid(row=0, column=1, padx=5, pady=5)
        face_frames['left'].grid(row=1, column=0, padx=5, pady=5)
        face_frames['front'].grid(row=1, column=1, padx=5, pady=5)
        face_frames['right'].grid(row=1, column=2, padx=5, pady=5)
        face_frames['back'].grid(row=1, column=3, padx=5, pady=5)
        face_frames['bottom'].grid(row=2, column=1, padx=5, pady=5)

        # Draw the 3x3 grid of tiles for each face
        for face_name, face_layout in self.face_layouts.items():
            frame = face_frames[face_name]
            for i in range(9):
                row, col = divmod(i, 3)
                initial_color_name = face_layout[i]
                
                # Use a helper function to create and configure the button
                tile = self.create_tile_button(frame, initial_color_name)
                tile.grid(row=row, column=col, padx=2, pady=2)
        
        # Create a frame for the color picker
        color_picker_frame = ctk.CTkFrame(self, fg_color="transparent")
        color_picker_frame.pack(pady=10)
        
        # Create a button for each color
        for i, color_name in enumerate(self.color_names):
            color_hex = self.colors[color_name]
            
            color_button = ctk.CTkButton(
                color_picker_frame, 
                text="",
                fg_color=color_hex,
                hover_color=color_hex,
                width=50,
                height=50,
                corner_radius=5,
                command=lambda color=color_hex: self.select_color(color)
            )
            color_button.grid(row=0, column=i, padx=5)

    def create_tile_button(self, frame, initial_color_name):
        """Helper function to create and configure a single tile button."""
        tile = ctk.CTkButton(
            frame, 
            fg_color=self.colors[initial_color_name], 
            hover_color=self.colors[initial_color_name],
            text="", 
            width=60, 
            height=60, 
            corner_radius=5,
        )
        # Bind the command after the button is created
        tile.configure(command=lambda: self.set_tile_color(tile))
        return tile

    def select_color(self, color):
        """Sets the current active color."""
        self.current_color = color
        print(f"Selected color: {color}")

    def set_tile_color(self, tile):
        """Changes the color of a tile to the currently selected color."""
        tile.configure(fg_color=self.current_color, hover_color=self.current_color)

if __name__ == "__main__":
    app = RubiksCubeViewer()
    app.mainloop()