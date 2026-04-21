## AI Assistant
Below is the Python equivalent of your UI code. This code uses the `tkinter` library to implement a window with text boxes, dropdowns, and a button, mimicking the described functionality in your original source.

```python
import tkinter as tk
from tkinter import messagebox, ttk

def show_instructions():
    instructions = """
    --------------------------------------------------------------------
    "Set Delay Counter (Sec.)" = This is a delay that only waits for a set amount of time. This is a flat wait.
    --------------------------------------------------------------------
    "Master Delay - Seconds" & "Run When Complete" Are delay settings that work together. 
    The master delay will run after the bot has completed the amount of actions on the site that is 
    filled out in the "Run When Complete" box. If you only want to like 100 images and then have the 
    software wait for a set amount of time, this is the setting you would use. Fill the delay time in 
    the "Master Delay - Seconds" and then tell the software when to run that delay in the 
    "Run When Complete" box.
    --------------------------------------------------------------------
    "Random Wait .1" and "Random Wait .2" work together. This will tell the software to wait a random 
    time between each action. Select a low wait time in the "Random Wait .1" drop-down and a high wait 
    time in the "Random Wait .2" drop-down, then the software will pick a random wait time 
    between each action.
    --------------------------------------------------------------------
    "Wait After Action Delay" - This delay will wait the set amount in seconds placed in the box after 
    the software has completed an action: Meaning after the follow, like, comment, or unfollow or whatever 
    action you are using has been completed, the software will wait that many seconds before continuing 
    to the next page.
    --------------------------------------------------------------------
    """
    messagebox.showinfo("Settings and Their Uses", instructions)

def delay_settings_ui():
    # Create the main window
    window = tk.Tk()
    window.title("Delay Settings")
    
    # Elements in the UI
    tk.Label(window, text="Set Delay Counter (Sec.):").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    delay_time = tk.Entry(window)
    delay_time.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(window, text="Stop The Software At:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    stop_bot_at = tk.Entry(window)
    stop_bot_at.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(window, text="Master Delay - Seconds:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    master_delay = tk.Entry(window)
    master_delay.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(window, text="Run When Complete:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
    run_when_complete = tk.Entry(window)
    run_when_complete.grid(row=3, column=1, padx=10, pady=5)

    # Random Wait .1 dropdown
    tk.Label(window, text="Random Wait .1:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
    random_wait_one_values = ["0", "1", "3", "9", "15", "21", "27", "33", "39", "45", "51", "57", "63", "69", "75", "81", "87", "93",
                              "99", "105", "111", "117", "123", "129", "135", "141", "147", "153", "159", "165", "171", "177", "183",
                              "189", "195", "201", "207", "213", "219", "225", "231", "237", "243", "249", "255", "261", "267", "273", "279",
                              "285", "291", "297"]
    random_wait_one = ttk.Combobox(window, values=random_wait_one_values)
    random_wait_one.grid(row=4, column=1, padx=10, pady=5)

    # Random Wait .2 dropdown
    tk.Label(window, text="Random Wait .2:").grid(row=5, column=0, padx=10, pady=5, sticky="w")
    random_wait_two_values = ["0", "6", "12", "18", "24", "30", "36", "42", "48", "54", "60", "66", "72", "78", "84", "90", "96", "102",
                              "108", "114", "120", "126", "132", "138", "144", "150", "156", "162", "168", "174", "180", "186", "192", "198",
                              "204", "210", "216", "222", "228", "234", "240", "246", "252", "258", "264", "270", "276", "282", "288", "294",
                              "300"]
    random_wait_two = ttk.Combobox(window, values=random_wait_two_values)
    random_wait_two.grid(row=5, column=1, padx=10, pady=5)

    tk.Label(window, text="Wait After Action Delay:").grid(row=6, column=0, padx=10, pady=5, sticky="w")
    wait_after = tk.Entry(window)
    wait_after.grid(row=6, column=1, padx=10, pady=5)

    # Button for showing instructions
    instructions_button = tk.Button(window, text="Settings Instructions & Uses", command=show_instructions)
    instructions_button.grid(row=7, column=0, columnspan=2, pady=10)

    # Start the Tkinter main loop
    window.mainloop()


# Run the UI
delay_settings_ui()
```

### Explanation
1. **UI Elements**: 
   - `Label` widgets for adding text labels to guide the user.
   - `Entry` widgets for user input fields (similar to "Text Box" in your original code).
   - `ttk.Combobox` for dropdown menus (similar to "Drop Down" in your UI code).
   - A `Button` widget to trigger the help/instructions popup.

2. **Show Instructions**: The `show_instructions` function displays the detailed instructions using the `messagebox.showinfo` function.

3. **Drop-down Values**: The lists for `Random Wait .1` and `Random Wait .2` dropdowns are created based on your provided constant values.

4. **Grid Layout**: The `grid` method organizes the UI elements in a structured grid format with proper padding for alignment.

Let me know if you need further clarification or adjustments!

