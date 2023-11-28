import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = name_entry.get()
    birth_year_input = birth_year_entry.get()  
    favorite_color = color_var.get()

    if not birth_year_input.isdigit():
        messagebox.showerror("Napačen vnose", "Leto rojstva mora biti številka.")
        return

    age = 2023 - int(birth_year_input)

    info_window = tk.Toplevel(root)
    info_window.title("Submitted Information")
    tk.Label(info_window, text=f"Name: {name}").pack()
    tk.Label(info_window, text=f"Age: {age}").pack()
    tk.Label(info_window, text=f"Favorite Color: {favorite_color}").pack()

root = tk.Tk()
root.title("Personal Information Form")
root.geometry("300x200")

tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Leto rojstva:").pack()
birth_year_entry = tk.Entry(root)  # Corrected widget name
birth_year_entry.pack()

tk.Label(root, text="Favorite Color:").pack()
color_var = tk.StringVar(root)
color_var.set("Red")  # default value
color_menu = tk.OptionMenu(root, color_var, "Red", "Green", "Blue", "Yellow", "Orange", "Purple", "Pink")
color_menu.pack()


submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.pack()

root.mainloop()