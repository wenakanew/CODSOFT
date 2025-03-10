import random
import string
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def generate_password_gui():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Length must be a positive integer")
        password = generate_password(length)
        result_label.config(text=f"Generated Password: {password}")
        copy_button.config(state=tk.NORMAL)
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))

def copy_to_clipboard():
    password = result_label.cget("text").replace("Generated Password: ", "")
    root.clipboard_clear()
    root.clipboard_append(password)
    #messagebox.showinfo("Copied", "Password copied to clipboard")

def exit_gui():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Password Generator")
height = 430
width = 530
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry(f'{width}x{height}+{x}+{y}')
root.overrideredirect(True)
root.config(background="white")

# Create and place the widgets
length_label = ttk.Label(root, text="Enter the desired length of the password:")
length_label.place(x=10, y=10)

length_entry = ttk.Entry(root)
length_entry.place(x=10, y=50)

generate_button = ttk.Button(root, text="Generate Password", command=generate_password_gui)
generate_button.place(x=10, y=100)

result_label = ttk.Label(root, text="")
result_label.place(x=10, y=150)

copy_button = ttk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, state=tk.DISABLED)
copy_button.place(x=10, y=200)

exit_button = ttk.Button(root, text="Exit", command=exit_gui)
exit_button.place(x=10, y=250)

# Start the GUI event loop
root.mainloop()