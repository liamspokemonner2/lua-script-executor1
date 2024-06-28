import os
import tkinter as tk
from tkinter import PhotoImage

# Define the path components relative to the script's location
script_dir = os.path.dirname(__file__)
image_path = os.path.join(script_dir, 'Farmingcutterui', 'Farmingcuttermainbackground.png')

# Print the base directory and image path for debugging
print(f"Script directory: {script_dir}")
print(f"Image path: {image_path}")

# Create the main application window
root = tk.Tk()

# Remove the window decorations (top bar)
root.overrideredirect(True)

# Function to make the window draggable
def start_drag(event):
    global x_offset, y_offset
    x_offset = event.x
    y_offset = event.y

def on_drag(event):
    x = root.winfo_pointerx() - x_offset
    y = root.winfo_pointery() - y_offset
    root.geometry(f"+{x}+{y}")

# Load the image
try:
    image = PhotoImage(file=image_path)
except tk.TclError as e:
    print(f"Error loading image: {e}")
    root.destroy()
    exit(1)

# Get the image size and set the window size accordingly
image_width = image.width()
image_height = image.height()
root.geometry(f"{image_width}x{image_height}")

# Create a label widget to display the image
label = tk.Label(root, image=image)
label.pack()

# Bind the mouse events to the label
label.bind("<Button-1>", start_drag)
label.bind("<B1-Motion>", on_drag)

# Run the application
root.mainloop()
