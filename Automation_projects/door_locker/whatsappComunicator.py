from selenium import webdriver
import time
from alert import alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from bs4 import BeautifulSoup

import logging
logging.basicConfig(filename='logs\general_log.log', level=logging.DEBUG, format='%(asctime)s.%(msecs)03d %(levelname)s ====: %(message)s =;',
    datefmt='%Y-%m-%d %H:%M:%S')
logging.info("Estabelecendo conexão com o Whatsapp...")

class WhatsComunic:
    def __init__(self):
        alert("Info", "Para comerçarmos conecte-se ao whatsapp com o QR_CODE que surgirá na tela", "info")
        srv = Service(r'./msedgedriver.exe')
        self.driver = webdriver.Edge(service = srv)
        self.wt_bot = "Door lock"
        self.status = True
        self.intro_text = "Olá , eu sou o Door Lock bot" + '\n' + "Seu BOT de segurança, trarei qualquer atualização no status de sua porta."
        self.whatsapp_link = "https://web.whatsapp.com/"
        self.startWork()

    def onOffBot(self):
        if self.status : self.status = False
        else: self.status = True

    def startWork(self):
        self.getToZapp()
        self.wrMenss(self.intro_text)
    
    def getResponse(self, question_txt):
        self.wrMenss(question_txt)
        old_mens = self.rdMenss()
        while (self.status):
            mens = self.rdMenss()
            time.sleep(2.5)
            if (old_mens != mens) & (mens != "."):
                old_mens = mens
                if mens in 'SN' : 
                    if mens == "S": return(True)
                    else: return(False)
                else: self.wrMenss('Por Favor responda apenas com "S" para Sim e "N" para não')

    def getToZapp(self):
        self.driver.get(self.whatsapp_link)
        time.sleep(5)
        while True:
            try:
                find_target = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[1]/div/div/div[2]/div/div[2]')
                logging.info("Conectado...")
                print(123)
                break 
            except:
                logging.info("Tentando estabelecer conexão...")
            time.sleep(3)
        time.sleep(3)
        find_target.click()
        time.sleep(3)
        find_target.send_keys(self.wt_bot)
        time.sleep(1)
        find_target.send_keys(Keys.ENTER)
        

    def wrMenss(self, msg): 
        try:
            txt_entry = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
        except:
            alert("Reconnect-se","Por favor reconnect-se","error")
            self.getToZapp()
            txt_entry = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')

        time.sleep(0.5)
        txt_entry.click()
        time.sleep(1)
        txt_entry.send_keys(msg + Keys.ENTER)

    def rdMenss(self):
        messages = list()
        try:
            soup = BeautifulSoup(self.driver.page_source, "html.parser")
            for i in soup.find_all("div", class_="message-out"): #alternar sobre quem manda as msgs
                message = i.find("span", class_="selectable-text")
                if message:
                    message2 = message.find("span")
                if message2:
                    messages.append(message2.text)
            messages = list(filter(None, messages))
            if len(messages) != 0: last_messages = messages[-1]
            else: last_messages = "."
            return last_messages
        except:
            alert("Reconnect-se","Por favor reconnect-se","alert")
            self.getToZapp()
            return self.rdMenss()

