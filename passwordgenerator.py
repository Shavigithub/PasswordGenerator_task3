import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(entry_length.get())
        if length <= 0:
            raise ValueError

        chars = ""
        if var_upper.get():
            chars += string.ascii_uppercase
        if var_lower.get():
            chars += string.ascii_lowercase
        if var_digits.get():
            chars += string.digits
        if var_symbols.get():
            chars += string.punctuation

        if not chars:
            messagebox.showwarning("Selection Missing", "Select at least one character type.")
            return

        password = ''.join(random.choice(chars) for _ in range(length))
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
    
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid password length.")

def copy_to_clipboard():
    password = entry_password.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")


def update_tickmarks():
    lbl_upper.config(text="✔️" if var_upper.get() else "")
    lbl_lower.config(text="✔️" if var_lower.get() else "")
    lbl_digits.config(text="✔️" if var_digits.get() else "")
    lbl_symbols.config(text="✔️" if var_symbols.get() else "")

root = tk.Tk()
root.title(" Password Generator")
root.geometry("400x400")
root.config(bg="black")

tk.Label(root, text="Password Generator", font=("Arial", 18), fg="white", bg="black").pack(pady=10)

tk.Label(root, text="Password Length:", font=("Arial", 12), fg="white", bg="black").pack()
entry_length = tk.Entry(root, width=10, font=("Arial", 12))
entry_length.pack(pady=5)

var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)

frame_checks = tk.Frame(root, bg="black")
frame_checks.pack(pady=5)

tk.Checkbutton(frame_checks, text="Uppercase", variable=var_upper, fg="white", bg="black",
               command=update_tickmarks).grid(row=0, column=0, sticky="w", padx=5)
lbl_upper = tk.Label(frame_checks, text="✔️", bg="black", fg="lightgreen", font=("Arial", 12))  
lbl_upper.grid(row=0, column=1)

tk.Checkbutton(frame_checks, text="Lowercase", variable=var_lower, fg="white", bg="black",
               command=update_tickmarks).grid(row=1, column=0, sticky="w", padx=5)
lbl_lower = tk.Label(frame_checks, text="✔️", bg="black", fg="lightgreen", font=("Arial", 12)) 
lbl_lower.grid(row=1, column=1)

tk.Checkbutton(frame_checks, text="Digits", variable=var_digits, fg="white", bg="black",
               command=update_tickmarks).grid(row=2, column=0, sticky="w", padx=5)
lbl_digits = tk.Label(frame_checks, text="✔️", bg="black", fg="lightgreen", font=("Arial", 12)) 
lbl_digits.grid(row=2, column=1)

tk.Checkbutton(frame_checks, text="Symbols", variable=var_symbols, fg="white", bg="black",
               command=update_tickmarks).grid(row=3, column=0, sticky="w", padx=5)
lbl_symbols = tk.Label(frame_checks, text="✔️", bg="black", fg="lightgreen", font=("Arial", 12))  
lbl_symbols.grid(row=3, column=1)


tk.Button(root, text="Generate Password", font=("Arial", 12), bg="lightblue", command=generate_password).pack(pady=10)
entry_password = tk.Entry(root, width=35, font=("Arial", 14), justify="center")
entry_password.pack(pady=10)
tk.Button(root, text="Copy to Clipboard", font=("Arial", 12), bg="lightgreen", command=copy_to_clipboard).pack(pady=5)

update_tickmarks()  
root.mainloop()
