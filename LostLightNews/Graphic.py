from tkinter import *
import tkinter as tk
from tkinter import ttk

counter = 1
s = 10

root = Tk()

#Настройки окна
root.title('Lost Light News')
root.geometry('1000x700')
root.iconbitmap(default="Lost_Light_Ico_Full.ico")
root.resizable(False, False)
root.attributes("-alpha", 0.9)

#Текст
label = ttk.Label(text="Это приложение для просмотра новостей игры", font=("DacikPush", 20), justify='center')
label.pack()
label1 = ttk.Label(text='Lost Light', font=('DacikPush', 30), justify='center')
label1.pack()

frame = Frame(root)
frame.pack()

for i in range(s):
    btn = ttk.Button(frame, text=f"Новость {counter}")
    btn.pack(expand=True, padx=5, pady=5, ipadx=5, ipady=5, side=tk.LEFT)
    counter += 1

root.mainloop()