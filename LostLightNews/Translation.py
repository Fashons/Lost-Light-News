# from translate import Translator

# trans = Translator(from_lang='en', to_lang='ru')
# text = 'Lost Light'

# final = trans.translate(text)
# print(final)

import translators as ts
text = 'lost ' * 5000

def chunks(s, n):
    """Produce `n`-character chunks from `s`."""
    for start in range(0, len(s), n):
        yield s[start:start+n]

for chunk in chunks(text, 5000):
    print(chunk)



params = {
    'query_text': chunk,
    'from_language': 'en',
    'to_language': 'ru',
    'update_session_after_freq': 1,
    'if_show_time_stat' : True,
}

print(ts.translate_text(**params,translator='yandex'))
