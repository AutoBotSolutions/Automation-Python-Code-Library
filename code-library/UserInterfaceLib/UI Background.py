import tkinter as tk
from tkinter import ttk  # Optional, for styled widgets

# Create the main window
window = tk.Tk()CSS UI Background
window.title("Application with Background Image")

# Set the size of the window
window.geometry("800x600")  # Adjust window size as needed

# Load the background image
bg_image = tk.PhotoImage(file="background.png")  # Replace with your image path

# Create a Canvas to place the image as a background
canvas = tk.Canvas(window, width=800, height=600)  # Adjust size as needed
canvas.pack(fill="both", expand=True)

# Place the image on the Canvas
canvas.create_image(0, 0, image=bg_image, anchor="nw")

# Create consistent UI layering: frame for other widgets
frame = tk.Frame(window, bg="transparent")  # Use appropriate background for transparency
frame.place(relwidth=1, relheight=1)

# Add UI elements into the frame (they'll appear over the image)
follow_label = tk.Label(frame, text="Follow:")
follow_label.pack(pady=10)

follow_entry = tk.Entry(frame)
follow_entry.pack(pady=10)

start_button = tk.Button(frame, text="Start", command=lambda: print("Started"))
start_button.pack(pady=10)

stop_button = tk.Button(frame, text="Stop", command=lambda: print("Stopped"))
stop_button.pack(pady=10)

# Run the application
window.mainloop()

