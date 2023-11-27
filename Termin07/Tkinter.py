import tkinter as tk

root = tk.Tk()
root.title("Moja prva aplikacija")
root.geometry("300x200")

label = tk.Label(root, text="Pozdravljeni!")
label.pack()

def on_button_click():
    label.config(text="Pritisnili ste gumb!")

button = tk.Button(root, text="Stisni me", command=on_button_click)
button.pack()


root.mainloop()
