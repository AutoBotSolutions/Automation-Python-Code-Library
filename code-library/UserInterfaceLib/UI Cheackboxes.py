import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.title("Login form")
window.geometry('800x540')
window.configure(bg='#333333')
window.resizable(False, False)
window.font = ("Cantrell", 12)

def show_selection():
    print(f"Checkbox 1: {var1.get()}")
    print(f"Checkbox 2: {var2.get()}")
    print(f"Checkbox 3: {var3.get()}")
    print(f"Checkbox 4: {var4.get()}")

def start():
    username = "johnsmith"
    password = "12345"
    if follow_entry.get()==username and unfollow_entry.get()==password:
        messagebox.showinfo(title="Start Success", message="You successfully logged in.")
    else:
        messagebox.showerror(title="Error", message="Invalid Start.")


var1 = tkinter.BooleanVar()
var2 = tkinter.BooleanVar()
var3 = tkinter.BooleanVar()
var4 = tkinter.BooleanVar()

frame = tkinter.Frame(bg='#333333')

# Creating widgets
follow_label = tkinter.Label(frame, width=18, text="Follow Per Keyword", bg='#333333', fg="#FFFFFF", font=("Cantrell", 12))
follow_entry = tkinter.Entry(frame, width=18, bg='#b9b4b3', font=("Cantrell", 12))
unfollow_label = tkinter.Label(frame, width=18, text="Number To Unfollow", bg='#333333', fg="#FFFFFF", font=("Cantrell", 12))
unfollow_entry = tkinter.Entry(frame, width=18, bg='#b9b4b3', font=("Cantrell", 12))
comment_label = tkinter.Label(frame, width=18, text="Comment Per Key", bg='#333333', fg="#FFFFFF", font=("Cantrell", 12))
comment_entry = tkinter.Entry(frame, width=18, bg='#b9b4b3',font=("Cantrell", 12))
likes_entry = tkinter.Entry(frame, width=18, bg='#b9b4b3',font=("Cantrell", 12))
likes_label = tkinter.Label(frame, width=18, text="Likes Per Keyword", bg='#333333', fg="#FFFFFF", font=("Cantrell", 12))

# Creating widgets
checkbox1 = tkinter.Checkbutton(frame, text="Follows", bg="#333333", fg="#FFFFFF", font=("Cantrell", 12),
variable=var1, onvalue=True, offvalue=False, command=show_selection)
checkbox2 = tkinter.Checkbutton(frame, text="Likes", bg="#333333", fg="#FFFFFF", font=("Cantrell", 12),
variable=var2, onvalue=True, offvalue=False, command=show_selection)
checkbox3 = tkinter.Checkbutton(frame, text="Unfollows", bg="#333333", fg="#FFFFFF", font=("Cantrell", 12),
variable=var3, onvalue=True, offvalue=False, command=show_selection)
checkbox4 = tkinter.Checkbutton(frame, text="Comments", bg="#333333", fg="#FFFFFF", font=("Cantrell", 12),
variable=var4, onvalue=True, offvalue=False, command=show_selection)
start_button = tkinter.Button(frame, width=18, text="Start Software", bg="#FF3399", fg="#FFFFFF", font=("Cantrell", 12), command=start)

# Placing widgets on the screen
follow_label.grid( row=0, column=0, columnspan=1, padx=5, pady=5)
follow_entry.grid(row=1, column=0, columnspan=1, padx=5, pady=5)
likes_label.grid(row=0, column=1, columnspan=1, padx=5, pady=5)
likes_entry.grid(row=1, column=1, columnspan=1, padx=5, pady=5)
unfollow_label.grid(row=0, column=2, columnspan=1, padx=5, pady=5)
unfollow_entry.grid(row=1, column=2, columnspan=1, padx=5, pady=5)
comment_label.grid(row=0, column=3, columnspan=1, padx=5, pady=5)
comment_entry.grid(row=1, column=3, columnspan=1, padx=5, pady=5)
# Placing widgets on the screen
checkbox1.grid(row=3, column=0, padx=5, pady=5, sticky="w")
checkbox2.grid(row=3, column=1, padx=5, pady=5, sticky="w")
checkbox3.grid(row=3, column=2, padx=5, pady=5, sticky="w")
checkbox4.grid(row=3, column=3, padx=5, pady=5, sticky="w")

start_button.grid(row=4, column=0, columnspan=3, pady=30)
frame.pack()
window.mainloop()
