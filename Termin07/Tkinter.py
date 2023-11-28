import tkinter as tk

root = tk.Tk()
root.title("Moja prva aplikacija")
root.geometry("400x300")

label = tk.Label(root, text="Pozdravljeni!")
label.pack()

def on_button_click():
    label.config(text="Pritisnili ste gumb!")

button = tk.Button(root, text="Stisni me!", command=on_button_click)
button.pack()

root.mainloop()