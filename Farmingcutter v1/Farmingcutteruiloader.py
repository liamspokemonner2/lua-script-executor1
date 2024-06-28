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
root.title("Image Viewer")

# Load the image
try:
    image = PhotoImage(file=image_path)
except tk.TclError as e:
    print(f"Error loading image: {e}")
    root.destroy()
    exit(1)

# Create a label widget to display the image
label = tk.Label(root, image=image)
label.pack()

# Run the application
root.mainloop()