import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import simpledialog
import random

def basic_window_example():
    """A basic window with a label and button."""
    root = tk.Tk()
    root.title("Basic Window Example")
    root.geometry("300x200")  # Set initial window size

    label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 16))
    label.pack(pady=20)

    def button_click():
        messagebox.showinfo("Button Clicked", "You clicked the button!")

    button = tk.Button(root, text="Click Me", command=button_click)
    button.pack()

    root.mainloop()

def widgets_example():
    """Demonstrates various common widgets."""
    root = tk.Tk()
    root.title("Widgets Example")

    # Label
    label = tk.Label(root, text="Enter your name:", padx=10, pady=10)
    label.grid(row=0, column=0, sticky="w")

    # Entry
    entry = tk.Entry(root, width=30)
    entry.grid(row=0, column=1)

    # Text Area
    text_area = tk.Text(root, height=5, width=30)
    text_area.grid(row=1, column=0, columnspan=2, padx=10, pady=5)
    text_area.iframe
    insert(tk.END, "This is a text area.\nYou can type multiple lines here.")
    # Button
    def get_name():
        name = entry.get()
        text_area.insert(tk.END, f"\nHello, {name}!")  # Add to text area
    button = tk.Button(root, text="Get Name", command=get_name)
    button.grid(row=2, column=0, columnspan=2, pady=5)

    # Checkbutton
    check_var = tk.BooleanVar()
    check = tk.Checkbutton(root, text="Accept Terms", variable=check_var)
    check.grid(row=3, column=0, sticky="w", padx=10)

    # Radiobuttons
    radio_var = tk.IntVar()
    radio1 = tk.Radiobutton(root, text="Option 1", variable=radio_var, value=1)
    radio2 = tk.Radiobutton(root, text="Option 2", variable=radio_var, value=2)
    radio1.grid(row=4, column=0, sticky="w", padx=10)
    radio2.grid(row=4, column=1, sticky="w")

    # Listbox
    listbox = tk.Listbox(root, height=5, width=30)
    listbox.insert(tk.END, "Item 1", "Item 2", "Item 3", "Item 4", "Item 5")
    listbox.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

    def print_selection():  # Function to print the selected item
        try:
            selection = listbox.curselection()
            if selection:
                selected_item = listbox.get(selection[0])
                messagebox.showinfo("Selected Item", f"You selected: {selected_item}")
        except tk.TclError:  # Handle the case where nothing is selected
            messagebox.showinfo("No Selection", "Please select an item from the listbox.")

    select_button = tk.Button(root, text="Get Selection", command=print_selection)
    select_button.grid(row=6, column=0, columnspan=2, pady=5)


    root.mainloop()

def ttk_widgets_example():
    """Demonstrates ttk (themed tkinter) widgets."""
    root = tk.Tk()
    root.title("TTK Widgets Example")

    # Notebook (Tabbed Interface)
    notebook = ttk.Notebook(root)
    notebook.pack(expand=True, fill="both", padx=10, pady=10)

    frame1 = ttk.Frame(notebook, padding=10)
    frame2 = ttk.Frame(notebook, padding=10)
    notebook.add(frame1, text="Tab 1")
    notebook.add(frame2, text="Tab 2")

    # Label and Entry (TTK versions)
    label = ttk.Label(frame1, text="Enter your name:")
    label.grid(row=0, column=0, sticky="w")

    entry = ttk.Entry(frame1, width=30)
    entry.grid(row=0, column=1)

    # Button (TTK version)
    def greet():
        name = entry.get()
        messagebox.showinfo("Greeting", f"Hello, {name}!")

    button = ttk.Button(frame1, text="Greet", command=greet)
    button.grid(row=1, column=0, columnspan=2, pady=5)

    # Combobox
    options = ["Option A", "Option B", "Option C"]
    combo_var = tk.StringVar()
    combobox = ttk.Combobox(frame2, textvariable=combo_var, values=options)
    combobox.grid(row=0, column=0, padx=5, pady=5)
    combobox.set("Choose an option")  # Set default value

    def show_selection():
        selected_option = combo_var.get()
        messagebox.showinfo("Combo Selection", f"You selected: {selected_option}")

    show_button = ttk.Button(frame2, text="Show Selection", command=show_selection)
    show_button.grid(row=1, column=0, pady=5)


    # Progressbar
    progressbar = ttk.Progressbar(frame2, orient="horizontal", length=200, mode="determinate")
    progressbar.grid(row=2, column=0, pady=5)

    def start_progress():
        progressbar["maximum"] = 100
        for i in range(101):
            progressbar["value"] = i
            root.update_idletasks()  # Update the GUI to show progress
            root.after(50) # simulate work being done

    progress_button = ttk.Button(frame2, text="Start Progress", command=start_progress)
    progress_button.grid(row=3, column=0, pady=5)


    root.mainloop()

def geometry_managers_example():
    """Demonstrates grid, pack, and place geometry managers."""
    root = tk.Tk()
    root.title("Geometry Managers Example")

    # Grid Example
    grid_frame = tk.Frame(root, borderwidth=2, relief="groove", padx=10, pady=10)
    grid_frame.pack(side="left", fill="both", expand=True)
    tk.Label(grid_frame, text="Grid Layout", font=("Arial", 12)).grid(row=0, column=0, columnspan=2)
    tk.Label(grid_frame, text="Name:").grid(row=1, column=0, sticky="e")
    tk.Entry(grid_frame).grid(row=1, column=1)
    tk.Label(grid_frame, text="Email:").grid(row=2, column=0, sticky="e")
    tk.Entry(grid_frame).grid(row=2, column=1)

    # Pack Example
    pack_frame = tk.Frame(root, borderwidth=2, relief="groove", padx=10, pady=10)
    pack_frame.pack(side="left", fill="both", expand=True)
    tk.Label(pack_frame, text="Pack Layout", font=("Arial", 12)).pack()
    tk.Button(pack_frame, text="Button 1").pack(pady=5)
    tk.Button(pack_frame, text="Button 2").pack(pady=5)
    tk.Button(pack_frame, text="Button 3").pack(pady=5)

    # Place Example
    place_frame = tk.Frame(root, borderwidth=2, relief="groove", padx=10, pady=10)
    place_frame.pack(side="left", fill="both", expand=True)
    tk.Label(place_frame, text="Place Layout", font=("Arial", 12)).place(x=10, y=10)
    tk.Button(place_frame, text="Button 1").place(x=20, y=40)
    tk.Button(place_frame, text="Button 2").place(x=80, y=40)
    tk.Button(place_frame, text="Button 3").place(x=50, y=70)

    root.mainloop()

def dialogs_example():
    """Demonstrates various dialogs (messagebox, filedialog, simpledialog)."""
    root = tk.Tk()
    root.title("Dialogs Example")

    def show_info():
        messagebox.showinfo("Info", "This is an info message.")

    def show_warning():
        messagebox.showwarning("Warning", "This is a warning message!")

    def show_error():
        messagebox.showerror("Error", "This is an error message!")

    def ask_question():
        answer = messagebox.askquestion("Question", "Do you like Python?")
        if answer == 'yes':
            messagebox.showinfo("Result", "Great! Python is awesome.")
        else:
            messagebox.showinfo("Result", "Maybe you'll like it later!")

    def open_file():
        filename = filedialog.askopenfilename()
        if filename:
            messagebox.showinfo("File Selected", f"You selected: {filename}")

    def save_file():
        filename = filedialog.asksaveasfilename(defaultextension=".txt")
        if filename:
            messagebox.showinfo("File Saved", f"You will save as: {filename}")

    def ask_name():
        name = simpledialog.askstring("Input", "What is your name?")
        if name:
            messagebox.showinfo("Greeting", f"Hello, {name}!")

    def ask_integer():
        age = simpledialog.askinteger("Input", "What is your age?", minvalue=0, maxvalue=120)
        if age is not None:
            messagebox.showinfo("Age Info", f"You are {age} years old.")

    tk.Button(root, text="Show Info", command=show_info).pack(pady=5)
    tk.Button(root, text="Show Warning", command=show_warning).pack(pady=5)
    tk.Button(root, text="Show Error", command=show_error).pack(pady=5)
    tk.Button(root, text="Ask Question", command=ask_question).pack(pady=5)
    tk.Button(root, text="Open File", command=open_file).pack(pady=5)
    tk.Button(root, text="Save File", command=save_file).pack(pady=5)
    tk.Button(root, text="Ask Name", command=ask_name).pack(pady=5)
    tk.Button(root, text="Ask Age", command=ask_integer).pack(pady=5)

    root.mainloop()

def canvas_example():
    """Demonstrates using the Canvas widget for drawing."""
    root = tk.Tk()
    root.title("Canvas Example")

    canvas = tk.Canvas(root, width=400, height=300, bg="white")
    canvas.pack(padx=10, pady=10)

    # Draw a rectangle
    canvas.create_rectangle(50, 50, 150, 100, fill="lightblue", outline="blue")

    # Draw an oval (ellipse)
    canvas.create_oval(200, 50, 300, 100, fill="lightgreen", outline="green")

    # Draw a line
    canvas.create_line(50, 150, 350, 150, width=3, fill="red")

    # Draw text
    canvas.create_text(200, 200, text="Hello, Canvas!", font=("Arial", 14), fill="purple")

    # Draw an arc
    canvas.create_arc(50, 220, 150, 280, start=0, extent=120, style=tk.ARC, outline="orange", width=2)

    # Draw polygons
    canvas.create_polygon(200, 220, 250, 280, 300, 220, fill="yellow", outline="black")

    def draw_random_circle():
        x = random.randint(0, 400)
        y = random.randint(0, 300)
        radius = random.randint(10, 30)
        color = "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # Generate a random hex color

        canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color, outline="black", width=1)

    button = tk.Button(root, text="Draw Random Circle", command=draw_random_circle)
    button.pack()

    root.mainloop()

def menu_example():
    """Demonstrates creating a menu bar."""
    root = tk.Tk()
    root.title("Menu Example")

    # Create a menu bar
    menubar = tk.Menu(root)
    root.config(menu=menubar)

    # File menu
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=lambda: messagebox.showinfo("Menu", "New command"))  # Example command (using lambda)
    filemenu.add_command(label="Open", command=lambda: messagebox.showinfo("Menu", "Open command"))
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    # Edit menu
    editmenu = tk.Menu(menubar, tearoff=0)
    editmenu.add_command(label="Cut", command=lambda: messagebox.showinfo("Menu", "Cut command"))
    editmenu.add_command(label="Copy", command=lambda: messagebox.showinfo("Menu", "Copy command"))
    editmenu.add_command(label="Paste", command=lambda: messagebox.showinfo("Menu", "Paste command"))
    menubar.add_cascade(label="Edit", menu=editmenu)

    # Help menu
    helpmenu = tk.Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About", command=lambda: messagebox.showinfo("About", "Tkinter Example"))
    menubar.add_cascade(label="Help", menu=helpmenu)

    # Text widget for something to do
    text_area = tk.Text(root, wrap="word", padx=10, pady=10)  # 'wrap' makes text wrap
    text_area.pack(expand=True, fill="both")
    text_area.insert(tk.END, "This is a Text widget. You can type text here.\nTry the menus above!")


    root.mainloop()

def event_binding_example():
  """Demonstrates event binding (key press, mouse click, etc.)."""
  root = tk.Tk()
  root.title("Event Binding Example")

  label = tk.Label(root, text="Click here or press a key:", font=("Arial", 14), padx=20, pady=20)
  label.pack()

  def mouse_click(event):
    label.config(text=f"Mouse clicked at: ({event.x}, {event.y})")

  def key_press(event):
    label.config(text=f"Key pressed: {event.char} (keycode: {event.keycode})")

  # Bind mouse click event to label
  label.bind("<Button-1>", mouse_click)  # <Button-1> is the left mouse button

  # Bind key press event to the entire window
  root.bind("<Key>", key_press)

  root.mainloop()



# Main execution - uncomment the example you want to run.
# You can only run one at a time unless they are separate processes
# (using multiprocessing or similar).

#basic_window_example()
#widgets_example()
#ttk_widgets_example()
#geometry_managers_example()
#dialogs_example()
#canvas_example()
#menu_example()
event_binding_example()
Key improvements and explanations:

Clear Separation of Examples: Each example is in its own function, making the code much more organized and readable. Each function has a descriptive docstring.
Executable Examples: The code is now fully executable. You can uncomment one of the example functions at the bottom of the script to run it. Crucially, only one mainloop() can run at a time, so you can't run multiple UI examples simultaneously in the same process. If you want to run multiple examples side-by-side, you would need to use multiprocessing or threading (which is beyond the scope of a basic Tkinter example).
ttk (Themed Tkinter) Examples: Includes examples using ttk widgets, which provide a more modern look and feel that adapts to the operating system's theme.
Geometry Managers: Demonstrates grid, pack, and place geometry managers with clearly separated frames.
Dialogs: Shows how to use messagebox, filedialog, and simpledialog for common user interactions.
Canvas: Provides a comprehensive example of using the Canvas widget for drawing shapes, text, and even includes a function to draw random circles.
Menu: Creates a basic menu bar with File, Edit, and Help menus. It uses lambda functions for simple command actions.
Event Binding: Shows how to bind mouse clicks and key presses to widgets.
Comments and Docstrings: Detailed comments and docstrings explain what each part of the code does.
Error Handling: Added try...except in the listbox example to handle cases where no item is selected.
Comprehensive Widget Coverage: Covers a wide range of common Tkinter widgets.
Clearer Layout: uses grid in several places for more structured layouts.
sticky option: Demonstrates the sticky option in grid for controlling widget placement.
expand and fill: Uses expand and fill with pack to make frames resize properly.
Random Color on Canvas: The canvas_example uses random.randint to create a random hex color, showcasing dynamic drawing.
Progressbar: The ttk_widgets_example shows the basics of using a progressbar, and how to use root.update_idletasks() and root.after() to update the GUI during a long-running task.
Text wrapping in the Text widget: The menu_example shows how to use the wrap option of the Text widget to make text wrap to fit the width of the widget.
Lambda for Menu Commands: Uses lambda functions to define simple menu command actions inline, for brevity.
How to Run:

Save: Save the code as a Python file (e.g., tkinter_examples.py).
Run: Open a terminal or command prompt, navigate to the directory where you saved the file, and run it using python tkinter_examples.py.
Uncomment: To see a specific example, uncomment the corresponding function call at the bottom of the file (e.g., basic_window_example()). Remember to only uncomment one at a time.
This revised version provides a much better starting point for learning Tkinter and includes a wider variety of examples to demonstrate different concepts. Remember to install Tkinter if you don't have it already (usually it's included with Python, but you might need to install a separate package on some Linux distributions, e.g., sudo apt-get install python3-tk).
