# WIKIPEDIA 

import requests
from parsel import Selector
import re
import pickle

class Letra(object):
    def __init__(self, letra, desc):
        self.letra = letra
        self.desc = desc

    @property
    def chave(self):
        return self.letra

    def __str__(self):
        return '{0} {1} {0}\n{2}\n'.format('*' * 10, self.letra, self.desc)

lista = []
for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    r = requests.get('https://pt.wikipedia.org/wiki/' + letter)
    sel = Selector(r.text)
    text_parts = sel.xpath('*//div[@id="mw-content-text"]/div/p[1]//text()').extract()
    text = ' '.join(text_parts)
    text = re.sub('\s+', ' ', text, re.UNICODE)
    letra = Letra(letter , text)
    print(letra)
    lista.append(letra)


with open('./alfabeto.pkl', 'bw') as f:
    pickle.dump(lista, f)
