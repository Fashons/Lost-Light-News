import requests
from bs4 import BeautifulSoup
import translators as ts
import textwrap

from tkinter import *
import tkinter as tk
from tkinter import ttk

counter = 1
linkk = ''

root = Tk()

def linki(counter):
    global links
    links = []
    url = 'https://www.lostlight.game/news/'
    response = requests.get(url).text

    data = BeautifulSoup(response, 'html.parser')
    for article in data.find_all('ul', class_ = 'lbnr'):
        for article in data.find_all('li'):
            title = article.a['title']
            link = 'https:'+article.a['href']
            titlefinal = title.replace('â', ' - ')
            titlefinal = title.replace('-', ' - ')
            final = ts.translate_text(titlefinal, from_language='en', to_language='ru', translator='yandex')
            # print(f"{counter}.{final} - {link}")
            counter = counter + 1
            links.append(link)
    print("Ссылки готовы!")
    counter = str(counter)
    # Файл
    config = open('settings.txt', 'w+', encoding='utf8')
    config.write(counter)
    config.close()
    return links

def sublinki(linkk):
    global TextX
    TextX = ""

    #Файл
    file = open('lostlight.txt', 'w+', encoding='utf8')

    url = linkk
    response = requests.get(url).text

    data = BeautifulSoup(response, 'html.parser')
    article = data.find('div', class_ = 'artText')
    title = article.text
    a = textwrap.wrap(title, 5000)
    for i in a:
        final = ts.translate_text(i, from_language='en', to_language='ru', translator='yandex')
        #нумерация
        final = final.replace('1.', '\n1.')
        final = final.replace('2.', '\n2.')
        final = final.replace('3.', '\n3.')
        final = final.replace('4.', '\n4.')
        final = final.replace('5.', '\n5.')
        final = final.replace('6.', '\n6.')
        final = final.replace('7.', '\n7.')
        final = final.replace('8.', '\n8.')
        final = final.replace('9.', '\n9.')
        final = final.replace('10.', '\n10.')
        final = final.replace('11.', '\n11.')
        final = final.replace('12.', '\n12.')
        final = final.replace('13.', '\n13.')
        final = final.replace('14.', '\n14.')
        final = final.replace('15.', '\n15.')
        final = final.replace('16.', '\n16.')
        final = final.replace('17.', '\n17.')
        final = final.replace('18.', '\n18.')
        final = final.replace('19.', '\n19.')
        final = final.replace('20.', '\n20.')
        final = final.replace('[', '\n\n[')
        final = final.replace(']', ']\n\n')
        final = final.replace('\n \n', '\n\n')
        final = final.replace('\n\n\n\n', '\n\n')
        final = final.replace('\n\n\n', '\n')
        final = final.replace('\n ', '\n')
        file.write(final)
    print("Готово!")
    print("Текст сохранён в файл lostlight.txt")

    file.close()
    file = open('lostlight.txt', 'r+', encoding='utf8')
    TextX = file.read()
    file.close()

def but1():
    def update_wraplength(_event):
        label.configure(wraplength=label.winfo_width())

    linkk = links[0]
    sublinki(linkk)
    window = Tk()
    window.title("Новое окно")
    window.geometry("1000x700")
    window.iconbitmap(default="Lost_Light_Ico_Full.ico")
    window.resizable(False, False)
    window.attributes("-alpha", 0.9)
    label = ttk.Label(window, text=TextX, font=('JetBrains Mono', 10), justify='left')
    label.pack(side="left", fill="x", expand=True)
    window.bind("<Configure>", update_wraplength)
def but2():
    def update_wraplength(_event):
        label.configure(wraplength=label.winfo_width())

    linkk = links[1]
    sublinki(linkk)
    window = Tk()
    window.title("Новое окно")
    window.geometry("1000x700")
    window.iconbitmap(default="Lost_Light_Ico_Full.ico")
    window.resizable(False, False)
    window.attributes("-alpha", 0.9)
    label = ttk.Label(window, text=TextX, font=('JetBrains Mono', 10), justify='left')
    label.pack(side="left", fill="x", expand=True)
    window.bind("<Configure>", update_wraplength)
def but3():
    def update_wraplength(_event):
        label.configure(wraplength=label.winfo_width())

    linkk = links[2]
    sublinki(linkk)
    window = Tk()
    window.title("Новое окно")
    window.geometry("1000x700")
    window.iconbitmap(default="Lost_Light_Ico_Full.ico")
    window.resizable(False, False)
    window.attributes("-alpha", 0.9)
    label = ttk.Label(window, text=TextX, font=('JetBrains Mono', 10), justify='left')
    label.pack(side="left", fill="x", expand=True)
    window.bind("<Configure>", update_wraplength)
def but4():
    def update_wraplength(_event):
        label.configure(wraplength=label.winfo_width())

    linkk = links[3]
    sublinki(linkk)
    window = Tk()
    window.title("Новое окно")
    window.geometry("1000x700")
    window.iconbitmap(default="Lost_Light_Ico_Full.ico")
    window.resizable(False, False)
    window.attributes("-alpha", 0.9)
    label = ttk.Label(window, text=TextX, font=('JetBrains Mono', 10), justify='left')
    label.pack(side="left", fill="x", expand=True)
    window.bind("<Configure>", update_wraplength)
def but5():
    def update_wraplength(_event):
        label.configure(wraplength=label.winfo_width())

    linkk = links[4]
    sublinki(linkk)
    window = Tk()
    window.title("Новое окно")
    window.geometry("1000x700")
    window.iconbitmap(default="Lost_Light_Ico_Full.ico")
    window.resizable(False, False)
    window.attributes("-alpha", 0.9)
    label = ttk.Label(window, text=TextX, font=('JetBrains Mono', 10), justify='left')
    label.pack(side="left", fill="x", expand=True)
    window.bind("<Configure>", update_wraplength)
def but6():
    def update_wraplength(_event):
        label.configure(wraplength=label.winfo_width())

    linkk = links[5]
    sublinki(linkk)
    window = Tk()
    window.title("Новое окно")
    window.geometry("1000x700")
    window.iconbitmap(default="Lost_Light_Ico_Full.ico")
    window.resizable(False, False)
    window.attributes("-alpha", 0.9)
    label = ttk.Label(window, text=TextX, font=('JetBrains Mono', 10), justify='left')
    label.pack(side="left", fill="x", expand=True)
    window.bind("<Configure>", update_wraplength)
def but7():
    def update_wraplength(_event):
        label.configure(wraplength=label.winfo_width())

    linkk = links[6]
    sublinki(linkk)
    window = Tk()
    window.title("Новое окно")
    window.geometry("1000x700")
    window.iconbitmap(default="Lost_Light_Ico_Full.ico")
    window.resizable(False, False)
    window.attributes("-alpha", 0.9)
    label = ttk.Label(window, text=TextX, font=('JetBrains Mono', 10), justify='left')
    label.pack(side="left", fill="x", expand=True)
    window.bind("<Configure>", update_wraplength)
def but8():
    def update_wraplength(_event):
        label.configure(wraplength=label.winfo_width())

    linkk = links[7]
    sublinki(linkk)
    window = Tk()
    window.title("Новое окно")
    window.geometry("1000x700")
    window.iconbitmap(default="Lost_Light_Ico_Full.ico")
    window.resizable(False, False)
    window.attributes("-alpha", 0.9)
    label = ttk.Label(window, text=TextX, font=('JetBrains Mono', 10), justify='left')
    label.pack(side="left", fill="x", expand=True)
    window.bind("<Configure>", update_wraplength)
def but9():
    def update_wraplength(_event):
        label.configure(wraplength=label.winfo_width())

    linkk = links[8]
    sublinki(linkk)
    window = Tk()
    window.title("Новое окно")
    window.geometry("1000x700")
    window.iconbitmap(default="Lost_Light_Ico_Full.ico")
    window.resizable(False, False)
    window.attributes("-alpha", 0.9)
    label = ttk.Label(window, text=TextX, font=('JetBrains Mono', 10), justify='left')
    label.pack(side="left", fill="x", expand=True)
    window.bind("<Configure>", update_wraplength)
def but10():
    def update_wraplength(_event):
        label.configure(wraplength=label.winfo_width())

    linkk = links[9]
    sublinki(linkk)
    window = Tk()
    window.title("Новое окно")
    window.geometry("1000x700")
    window.iconbitmap(default="Lost_Light_Ico_Full.ico")
    window.resizable(False, False)
    window.attributes("-alpha", 0.9)
    label = ttk.Label(window, text=TextX, font=('JetBrains Mono', 10), justify='left')
    label.pack(side="left", fill="x", expand=True)
    window.bind("<Configure>", update_wraplength)

def graphic():
    #Настройки окна
    root.title('Lost Light News')
    root.geometry('1000x700')
    root.iconbitmap(default="Lost_Light_Ico_Full.ico")
    root.resizable(False, False)
    root.attributes("-alpha", 0.9)

    #Рамки
    frame1 = Frame(root)
    frame1.pack()
    frame2 = Frame(root)
    frame2.pack()
    frame3 = Frame(root)
    frame3.pack()
    #Текст
    label1 = ttk.Label(frame1, text="Это приложение для просмотра новостей игры", font=("DacikPush", 20), justify='center')
    label1.pack()
    label2 = ttk.Label(frame1, text='Lost Light', font=('DacikPush', 30), justify='center')
    label2.pack()
    label3 = ttk.Label(frame3, text='Выберите одну из новостей', font=('JetBrains Mono', 40), justify='center')
    label3.pack()
    #Кнопки
    btn1 = ttk.Button(frame2, text="Новость 1", command=but1)
    btn1.pack(expand=True, padx=5, pady=5, ipadx=5, ipady=5, side=tk.LEFT)
    btn2 = ttk.Button(frame2, text="Новость 2", command=but2)
    btn2.pack(expand=True, padx=5, pady=5, ipadx=5, ipady=5, side=tk.LEFT)
    btn3 = ttk.Button(frame2, text="Новость 3", command=but3)
    btn3.pack(expand=True, padx=5, pady=5, ipadx=5, ipady=5, side=tk.LEFT)
    btn4 = ttk.Button(frame2, text="Новость 4", command=but4)
    btn4.pack(expand=True, padx=5, pady=5, ipadx=5, ipady=5, side=tk.LEFT)
    btn5 = ttk.Button(frame2, text="Новость 5", command=but5)
    btn5.pack(expand=True, padx=5, pady=5, ipadx=5, ipady=5, side=tk.LEFT)
    btn6 = ttk.Button(frame2, text="Новость 6", command=but6)
    btn6.pack(expand=True, padx=5, pady=5, ipadx=5, ipady=5, side=tk.LEFT)
    btn7 = ttk.Button(frame2, text="Новость 7", command=but7)
    btn7.pack(expand=True, padx=5, pady=5, ipadx=5, ipady=5, side=tk.LEFT)
    btn8 = ttk.Button(frame2, text="Новость 8", command=but8)
    btn8.pack(expand=True, padx=5, pady=5, ipadx=5, ipady=5, side=tk.LEFT)
    btn9 = ttk.Button(frame2, text="Новость 9", command=but9)
    btn9.pack(expand=True, padx=5, pady=5, ipadx=5, ipady=5, side=tk.LEFT)
    btn10 = ttk.Button(frame2, text="Новость 10", command=but10)
    btn10.pack(expand=True, padx=5, pady=5, ipadx=5, ipady=5, side=tk.LEFT)

    root.mainloop()

linki(counter)
graphic()