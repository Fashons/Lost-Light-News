import requests
from bs4 import BeautifulSoup
import translators as ts
import textwrap

#Файл
file = open('lostlight.txt', 'w+', encoding='utf8')

url = 'https://www.lostlight.game/news/update/20240521/34301_1156226.html'
response = requests.get(url).text

data = BeautifulSoup(response, 'html.parser')
article = data.find('div', class_ = 'artText')
title = article.text
a = textwrap.wrap(title, 5000)
for i in a:
    final = ts.translate_text(i, from_language='en', to_language='ru',translator='yandex')
    if (final.find('[')):
        final = final.replace('[', '\n[')
    if (final.find('[')):
        final = final.replace(']', ']\n')
    file.write(final)
print("Готово!")

file.close()
