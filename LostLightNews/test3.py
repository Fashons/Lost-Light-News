import tkinter as tk

file = open('lostlight.txt', 'r+', encoding='utf8')
TextX = file.read()
file.close()

root = tk.Tk()

def update_wraplength(_event):
    label.configure(wraplength=label.winfo_width())

# Настройки окна
root.geometry('1000x700')
root.resizable(False, False)

label = tk.Label(root, text=TextX, justify='left')
label.pack(side="left", fill="x", expand=True)

root.bind("<Configure>", update_wraplength)

root.mainloop()