import tkinter as tk
from tkinter import messagebox
import random
import string

# --------------------- FUNCTIONS --------------------- #
def generate_password():
    length = length_var.get()
    if length < 6:
        messagebox.showwarning("Warning", "Password length should be at least 6!")
        return
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_chars) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# ---------------------- GUI ---------------------- #
root = tk.Tk()
root.title("Password Generator ")
root.geometry("500x300")
root.configure(bg="#1a1a1a")  # Dark background for cool look
root.resizable(False, False)

# Title Label
title_label = tk.Label(root, text='Password Generator',font=("Arial Black", 12), fg="#ff6666", bg="#1a1a1a")
title_label.pack(pady=10)

# Password Entry
password_entry = tk.Entry(root, font=("Consolas", 14), width=30, justify='center', bg="#333333", fg="#00ff00", bd=0)
password_entry.pack(pady=20)

# Length Slider
length_var = tk.IntVar(value=6)
length_slider = tk.Scale(root, from_=6, to=20, orient='horizontal', label="    Digits ",
                         variable=length_var, bg="#1a1a1a", fg="#ffcc00", troughcolor="#333333",
                         highlightbackground="#1a1a1a")
length_slider.pack()

# Buttons Frame
button_frame = tk.Frame(root, bg="#1a1a1a")
button_frame.pack(pady=20)

generate_btn = tk.Button(button_frame, text="Generate ", command=generate_password,
                         font=("Arial", 10), bg="#ff6666", fg="white", width=10, bd=0, activebackground="#ff3333")
generate_btn.grid(row=0, column=0, padx=10)

copy_btn = tk.Button(button_frame, text="Copy ", command=copy_password,
                     font=("Arial", 10), bg="#66ff66", fg="black", width=10, bd=0, activebackground="#33ff33")
copy_btn.grid(row=0, column=1, padx=10)

# Footer
footer_label = tk.Label(root, text="Created by PRANAV RAO", font=("Arial", 10), fg="#888888", bg="#1a1a1a")
footer_label.pack(side='bottom', pady=5)

# Run GUI
root.mainloop()