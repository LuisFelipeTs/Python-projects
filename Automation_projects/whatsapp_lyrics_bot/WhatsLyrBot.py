from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from get_music_lyr import *
from bs4 import BeautifulSoup

class WhatsLyrBot:
    def __init__(self, song_name, song_artist, actual_target):
        srv = Service(r'./msedgedriver.exe')
        self.driver = webdriver.Edge(service = srv)
        self.song_name = song_name
        self.song_artist = song_artist
        self.actual_target = actual_target
        #self.cypher_origin_link = "https://www.cifraclub.com.br/"
        self.whatsapp_link = "https://web.whatsapp.com/"
        
    def startProcess(self):
        self.getToZapp()
        self.wrMenss()

    def getToZapp(self):
        self.driver.get(self.whatsapp_link)
        time.sleep(25)
        find_target = self.driver.find_element('//*[@id="side"]/div[1]/div/label/div/div[2]')
        find_target.click()
        time.sleep(2)
        find_target.send_keys(self.actual_target)
        time.sleep(1)
        find_target.send_keys(Keys.ENTER)

    def wrMenss(self): 
        txt_entry = self.driver.find_element('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
        time.sleep(1)
        txt_entry.click()
        time.sleep(1)
        song_msg = self.song_name + " - " + self.song_artist + "\n" + "\n"  
        txt_entry.send_keys(song_msg + Keys.ENTER)
        return

    def rdMenss(self): 

        
        

        return
    #//*[@id="main"]/div[3]/div/div[2]/div[3]/div[17]
    #//*[@id="main"]/div[3]/div/div[2]/div[3]/div[18]/div
    #//*[@id="main"]/div[3]/div/div[2]/div[3]/div[19]/div/div/div/div[1]/div/span[1]/span
wt = WhatsLyrBot("teste", "cantor do test", "REPOSITORIO DO ZAP")