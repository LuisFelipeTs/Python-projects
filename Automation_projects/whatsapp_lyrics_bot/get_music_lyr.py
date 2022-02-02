import requests
import re
from parsel import Selector
  
#//*[@id="js-w-content"]/div[3]/div[1]/div[1]/div[1]/div/div/pre
 
def getMusicLyr(music_name, music_singer):
    nw_music_name = re.sub('\s', '-', music_name)
    nw_music_singer = re.sub('\s', '-', music_singer)
    b_link = 'https://www.cifraclub.com.br/' + nw_music_singer + '/' + nw_music_name + '/'
    print(b_link)
    link = requests.get(b_link)
    sel = Selector(link.text)
    text_parts = sel.xpath('//*[@id="js-w-content"]/div[3]/div[1]/div[1]/div[1]/div/div/pre').extract()
    song = ' '.join(text_parts)
    
    song = re.sub('<b>', '', song)
    song = re.sub('</b>', '', song)

    if song == "": return "NSF" #No song was found
    else: 
        return(music_name + " - " + music_singer + "\n" + "\n" + song + "\n" + "\n" + "Para tocar no Cifra club : " + b_link) 


#def getYoutLink(music_name, music_singer):

print(getMusicLyr("pet sematary", "ramones"))
 

 