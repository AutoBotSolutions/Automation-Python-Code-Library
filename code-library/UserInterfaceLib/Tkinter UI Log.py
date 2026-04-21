import tkinter
from tkinter import messagebox

# Function to simulate adding logs
def add_log(message):
    log_area.insert(tkinter.END, f"{message}\n")  # Insert the log message at the end
    log_area.see(tkinter.END)  # Scroll to the latest log

window = tkinter.Tk()
window.title("Insta Promoter v 4.0")
window.geometry('800x540')
window.configure(bg='#333333', bd='2', relief='sunken')
window.resizable(False, False)

def show_selection():
    add_log(f"Checkbox 1: {var1.get()}")
    add_log(f"Checkbox 2: {var2.get()}")
    add_log(f"Checkbox 3: {var3.get()}")
    add_log(f"Checkbox 4: {var4.get()}")

def start():
    username = "johnsmith"
    password = "12345"
    add_log("Start button clicked.")  # Log the event
    if follow_entry.get() == username and unfollow_entry.get() == password:
        messagebox.showinfo(title="Start Success", message="You successfully logged in.")
        add_log("Successfully logged in.")
    else:
        messagebox.showerror(title="Error", message="Invalid Start.")
        add_log("Login attempt failed.")

def stop():
    username = "johnsmith"
    password = "12345"
    add_log("Stop button clicked.")  # Log the event
    if follow_entry.get() == username and unfollow_entry.get() == password:
        messagebox.showinfo(title="Stop Success", message="You Stopped")
        add_log("Software Stopped")
    else:
        messagebox.showerror(title="Error", message="Invalid Stop.")
        add_log("Stop attempt failed.")

def pause():
    username = "johnsmith"
    password = "12345"
    add_log("Pause button clicked.")  # Log the event
    if follow_entry.get() == username and unfollow_entry.get() == password:
        messagebox.showinfo(title="Pause Success", message="You Paused")
        add_log("Software Paused")
    else:
        messagebox.showerror(title="Error", message="Invalid Pause.")
        add_log("Pause attempt failed.")

def close():
    username = "johnsmith"
    password = "12345"
    add_log("Close button clicked.")  # Log the event
    if follow_entry.get() == username and unfollow_entry.get() == password:
        messagebox.showinfo(title="Close Success", message="You successfully Closed")
        add_log("Successfully Close")
    else:
        messagebox.showerror(title="Error", message="Invalid Close.")
        add_log("Close attempt failed.")

var1 = tkinter.BooleanVar()
var2 = tkinter.BooleanVar()
var3 = tkinter.BooleanVar()
var4 = tkinter.BooleanVar()

frame = tkinter.Frame(bg='#333333')

# Creating widgets
follow_label = tkinter.Label(frame, width=19, text="Follow Per Keyword", bg='#333333', fg="#FFFFFF", font=("Cantrell", 12))
follow_entry = tkinter.Entry(frame, width=19, bg='#b9b4b3', font=("Cantrell", 12))
unfollow_label = tkinter.Label(frame, width=18, text="Number To Unfollow", bg='#333333', fg="#FFFFFF", font=("Cantrell", 12))
unfollow_entry = tkinter.Entry(frame, width=18, bg='#b9b4b3', font=("Cantrell", 12))
comment_label = tkinter.Label(frame, width=19, text="Comment Per Key", bg='#333333', fg="#FFFFFF", font=("Cantrell", 12))
comment_entry = tkinter.Entry(frame, width=19, bg='#b9b4b3',font=("Cantrell", 12))
likes_entry = tkinter.Entry(frame, width=18, bg='#b9b4b3',font=("Cantrell", 12))
likes_label = tkinter.Label(frame, width=18, text="Likes Per Keyword", bg='#333333', fg="#FFFFFF", font=("Cantrell", 12))

# Creating widgets
checkbox1 = tkinter.Checkbutton(frame, text="Follows", bg="#333333", fg="#FFFFFF", bd=0, highlightthickness=0, height=1, font=("Cantrell", 12),
variable=var1, onvalue=True, offvalue=False, command=show_selection)
checkbox2 = tkinter.Checkbutton(frame, text="Likes", bg="#333333", fg="#FFFFFF", bd=0, highlightthickness=0, height=1, font=("Cantrell", 12),
variable=var2, onvalue=True, offvalue=False, command=show_selection)
checkbox3 = tkinter.Checkbutton(frame, text="Unfollows", bg="#333333", fg="#FFFFFF", bd=0, highlightthickness=0, height=1, font=("Cantrell", 12),
variable=var3, onvalue=True, offvalue=False, command=show_selection)
checkbox4 = tkinter.Checkbutton(frame, text="Comments", bg="#333333", fg="#FFFFFF", bd=0, highlightthickness=0, height=1, font=("Cantrell", 12),
variable=var4, onvalue=True, offvalue=False, command=show_selection)

# Creating widgets
follow_stat_label = tkinter.Label(frame, width=19, text="(F) Stat:", bg='#333333', fg="#FFFFFF", font=("Cantrell", 12))
likes_stat_label = tkinter.Label(frame, width=19, text="(L) Stat:", bg='#333333', fg="#FFFFFF", font=("Cantrell", 12))
unfollow_stat_label = tkinter.Label(frame, width=19, text="(U) Stat:", bg='#333333', fg="#FFFFFF", font=("Cantrell", 12))
comment_stat_label = tkinter.Label(frame, width=19, text="(C) Stat:", bg='#333333', fg="#FFFFFF", font=("Cantrell", 12))


# Creating widgets
start_button = tkinter.Button(frame, width=5, height=1, text="Start", bg="#FF3399", fg="#FFFFFF", font=("Cantrell", 12), command=start)
stop_button = tkinter.Button(frame, width=5, height=1, text="Stop", bg="#FF3399", fg="#FFFFFF", font=("Cantrell", 12), command=stop)
pause_button = tkinter.Button(frame, width=5, height=1, text="Pause", bg="#FF3399", fg="#FFFFFF", font=("Cantrell", 12), command=pause)
close_button = tkinter.Button(frame, width=5, height=1, text="Close", bg="#FF3399", fg="#FFFFFF", font=("Cantrell", 12), command=close)




# Adding a text area for verbose log
log_label = tkinter.Label(window, bg='#333333', fg="#FFFFFF", font=("Cantrell", 12))
log_area = tkinter.Text(window, height=35, width=95, bg="#222222", fg="#FFFFFF", font=("Cantrell", 12), wrap=tkinter.WORD)
log_scroll = tkinter.Scrollbar(window, command=log_area.yview, bg="#333333")
log_area.configure(yscrollcommand=log_scroll.set)

# Placing widgets on the screen
follow_label.grid(row=0, column=0, columnspan=1, padx=1, pady=1)
follow_entry.grid(row=1, column=0, columnspan=1, padx=13, pady=5)
likes_label.grid(row=0, column=1, columnspan=1, padx=1, pady=1)
likes_entry.grid(row=1, column=1, columnspan=1, padx=13, pady=5)
unfollow_label.grid(row=0, column=2, columnspan=1, padx=1, pady=1)
unfollow_entry.grid(row=1, column=2, columnspan=1, padx=13, pady=5)
comment_label.grid(row=0, column=3, columnspan=1, padx=1, pady=1)
comment_entry.grid(row=1, column=3, columnspan=1, padx=13, pady=5)
# Placing widgets on the screen
checkbox1.grid(row=3, column=0, columnspan=2, padx=13, pady=5, sticky="w")
checkbox2.grid(row=3, column=1, columnspan=2, padx=13, pady=5, sticky="w")
checkbox3.grid(row=3, column=2, columnspan=2, padx=13, pady=5, sticky="w")
checkbox4.grid(row=3, column=3, columnspan=2, padx=13, pady=5, sticky="w")
# Placing widgets on the screen
start_button.grid(row=5, column=0, columnspan=1, padx=10, pady=1, sticky="w")
stop_button.grid(row=5, column=1, columnspan=1, padx=3, pady=0, sticky="w")
pause_button.grid(row=5, column=2, columnspan=1, padx=1, pady=0, sticky="w")
close_button.grid(row=5, column=3, columnspan=1, padx=10, pady=1, sticky="w")
# Placing widgets on the screen
follow_stat_label.grid(row=5, column=0, columnspan=1, padx=1, pady=5, sticky="e")
likes_stat_label.grid(row=5, column=1, columnspan=1, padx=0, pady=0, sticky="e")
unfollow_stat_label.grid(row=5, column=2, columnspan=1, padx=0, pady=0, sticky="e")
comment_stat_label.grid(row=5, column=3, columnspan=1, padx=1, pady=5, sticky="e")

frame.pack()

# Placing the log area at the bottom
log_label.pack(pady=5)
log_area.pack(side=tkinter.LEFT, padx=10, pady=5)
log_scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)

window.mainloop()
