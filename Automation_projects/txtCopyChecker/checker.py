
import requests
from parsel import Selector
import re
import pickle

class Textr(object):
    bol = True

    def __init__(self, text):
        self.text = text
        if text == "": self.val = False
        else: self.val = True 

    @property
    def chave(self):
        return self.text
   
    def __str__(self):
        return '{0} {1} {0}\n{2}\n'.format('*' * 10, self.text, self.desc)

def checkText_wk(text_to_check):
    link_w = 'https://pt.wikipedia.org/wiki/' + text_to_check
    r = requests.get(link_w)
    sel = Selector(r.text)
    text_parts = sel.xpath('//*[@id="mw-content-text"]/div[1]/p[1]//text()').extract()
    #//span[@class="hgKElc"]//text()[last()]
    textt = ' '.join(text_parts)
    text_t = re.sub('\s', ' ', textt, re.UNICODE)
    letra = Textr(text_t )
    
    return letra.text, letra.val

def checkText_dc(text_to_check):
    link_w = 'https://www.dicionarioinformal.com.br/' + text_to_check
    r = requests.get(link_w)
    sel = Selector(r.text)
    text_parts = sel.xpath('//*[@id="main-feed"]/div[3]/div[2]/p/text()').extract()
    #//span[@class="hgKElc"]//text()[last()]
    textt = ' '.join(text_parts)
    print(textt)
    text_t1 = re.sub('\s', ' ', textt, re.UNICODE)
    letra1 = Textr(text_t1)
    
    return letra1.text, letra1.val
#print(checkText("bola")[1])