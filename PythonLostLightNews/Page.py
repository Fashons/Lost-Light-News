import requests
from bs4 import BeautifulSoup
import translators as ts

url = 'https://www.lostlight.game/news/'
response = requests.get(url).text

data = BeautifulSoup(response, 'html.parser')
for article in data.find_all('ul', class_ = 'lbnr'):
    for article in data.find_all('li'):
        title = article.a['title']
        link = 'https:'+article.a['href']
        titlefinal = title.replace('â', ' - ')
        titlefinal = title.replace('-', ' - ')
        final = ts.translate_text(titlefinal, from_language='en', to_language='ru',translator='yandex')
        print(final," - ", link)
