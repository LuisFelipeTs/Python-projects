
import requests
from parsel import Selector
import re
import pickle

class Textr(object):
    def __init__(self, text, desc):
        self.text = text
        self.desc = desc

    @property
    def chave(self):
        return self.text

    def __str__(self):
        return '{0} {1} {0}\n{2}\n'.format('*' * 10, self.text, self.desc)

def checkText(text_to_check):
    link_r = 'https://www.google.com.br/search?q=' + text_to_check
    r = requests.get(link_r)
    sel = Selector(r.text)
    text_parts = sel.xpath('')
    text = ' '.join(text_parts)
    print(text)
    text_t = re.sub('\s+', ' ', text, re.UNICODE)
    letra = Textr(text_to_check , text_t)

    print(letra)


    #return n_output, validation

checkText("Queijo")