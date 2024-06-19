import requests
from bs4 import BeautifulSoup
import translators as ts
import textwrap

from tkinter import *
import tkinter as tk
from tkinter import ttk

counter = 1
links = []
linkk = ''

root = Tk()

def linki(links, counter):
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
            print(f"{counter}.{final} - {link}")
            counter = counter + 1
            links.append(link)
    # print(links)
    return links

def sublinki(links, linkk):
    #Файл
    file = open('lostlight.txt', 'w+', encoding='utf8')

    url = linkk
    response = requests.get(url).text

    data = BeautifulSoup(response, 'html.parser')
    article = data.find('div', class_ = 'artText')
    title = article.text
    a = textwrap.wrap(title, 5000)
    for i in a:
        final = ts.translate_text(i, from_language='en', to_language='ru',translator='yandex')
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

def graphic(counter, links, linkk):
    n = 0
    files = []
    btn = []
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

    for i in links:
        files.append("Button" + str(counter))
        counter += 1

    for i in range(len(files)):
        # linkk = links[n]
        btn.append(Button(frame, text=files[i], command=lambda c=i: print(btn[c].cget("text")))) # print(btn[c].cget("text"))/sublinki(links, linkk)
        btn[i].pack(expand=True, padx=5, pady=5, ipadx=5, ipady=5, side=tk.LEFT)
        # n += 1
    root.mainloop()

linki(links, counter)
graphic(counter, links, linkk)