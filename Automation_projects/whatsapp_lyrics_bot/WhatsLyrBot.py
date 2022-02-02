from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from get_music_lyr import *
from bs4 import BeautifulSoup

class WhatsLyrBot:
    def __init__(self, actual_target, status = False):
        srv = Service(r'./msedgedriver.exe')
        self.driver = webdriver.Edge(service = srv)
        self.actual_target = actual_target
        self.status = status
        #self.cypher_origin_link = "https://www.cifraclub.com.br/"
        self.whatsapp_link = "https://web.whatsapp.com/"
        self.startWork()
        
    def onOffBot(self):
        if self.status : self.status = False
        else: self.status = True

    def startWork(self):
        self.intro_text = "Olá " + "*" + self.actual_target + "*" + ", eu sou Lyra" + '\n' + "Seu BOT de cifras musicais," + " para receber uma cifra insira um texto nesse formato" + '\n' + "(ex: Yesterday - The Beatles)" + '\n' + '_Para sair digite_ "OK"'
        self.getToZapp()
        self.wrMenss(self.intro_text)
        old_mens = ""
        while (self.status):
            mens = self.rdMenss()
            if mens in ["OK","Ok","ok","oK"]:
                self.onOffBot()
                self.wrMenss("Tchau :D")
                break
            time.sleep(2.5)
            if (old_mens != mens) & (mens != "."):
                old_mens = mens
                print(mens)
                if " - " in mens :
                    
                    song_n, singer = mens.split(" - ")
                    text_to_res = getMusicLyr(song_n, singer)
                    print(text_to_res)
                    if text_to_res == "NSF": self.wrMenss("Tal autor/musica não existe ou está escrito incorretamente")
                    else: self.wrMenss(text_to_res)
                        
                else: self.wrMenss('por favor lembrar de separar o cantor da música com " - "')


    def getToZapp(self):
        self.driver.get(self.whatsapp_link)
        time.sleep(15) 
        find_target = self.driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
        find_target.click()
        time.sleep(2)
        find_target.send_keys(self.actual_target + Keys.ENTER)

    def wrMenss(self, msg): 
        txt_entry = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
        time.sleep(0.5)
        txt_entry.click()
        time.sleep(1)
        #self.song_name + " - " + self.song_artist + "\n" + "\n"  
        txt_entry.send_keys(msg + Keys.ENTER)

    def rdMenss(self):
        #https://highontechs.com/chatbot/read-whatsapp-messages-using-python-selenium/ 
        messages = list()
        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        for i in soup.find_all("div", class_="message-in"):
            message = i.find("span", class_="selectable-text")
            if message:
                message2 = message.find("span")
            if message2:
                messages.append(message2.text)
        messages = list(filter(None, messages))
        if len(messages) != 0: last_messages = messages[-1]
        else: last_messages = "."
        return last_messages


wt = WhatsLyrBot("BILIO", True)