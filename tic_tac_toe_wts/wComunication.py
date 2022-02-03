from selenium import webdriver
import time
from tic_tac_toe_bot import TTToeBot
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from bs4 import BeautifulSoup

class WhatsLyrBot:
    def __init__(self, actual_target, p2, status = False):
        srv = Service(r'./msedgedriver.exe')
        self.driver = webdriver.Edge(service = srv)
        self.actual_target = actual_target
        self.status = status
        self.whatsapp_link = "https://web.whatsapp.com/"
        self.game = TTToeBot(actual_target, p2)
        self.startWork()
        
    def onOffBot(self):
        if self.status : self.status = False
        else: self.status = True

    def callNewGm(self):
        self.wrMenss("Gerando novo jogo")
        self.wrMenss("3...")
        self.wrMenss("2...")
        self.wrMenss("1...")
        self.game.nwGame

    def startWork(self):
        intro_text = "Olá " + "*" + self.actual_target + "*" + ", eu sou Tyc" + '\n' + "Seu BOT de jogo da velha, para começarmos iremos selecionar aleatoriamente o primeiro jogador" + '\n' + "Quando for seu turno digite um número disponível para escolher a posição(_Digite_ 'OK' _para parar o jogo_)"+ '\n' + "Digite algo para começar"
        self.getToZapp()
        self.wrMenss(intro_text)
        self.wrMenss(self.game.generateBoard())
        old_mens = self.rdMenss()
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
                if mens in '123456789' :
                    if mens in self.game.board_st:
                        self.wrMenss(self.game.newMove(mens))
                        if self.game.game_status != "TIC-TAC-TOE":
                            self.wrMenss("Você deseja jogar uma nova partida? (S ou N)")
                            self.waitforNewGres()
                    else: self.wrMenss("Essa posição já foi selecionada por favor escolher outra")
                else: self.wrMenss('por favor digite uma posição de 1 a 9')

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
        messages = list()
        if self.game.actual_player == self.game.p1: p_turn = "message-in"
        else: p_turn = "message-out"
        #https://highontechs.com/chatbot/read-whatsapp-messages-using-python-selenium/ 
        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        for i in soup.find_all_next("div", class_= p_turn):
            message = i.find("span", class_="selectable-text")
            if message:
                message2 = message.find("span")
            if message2:
                messages.append(message2.text)
        messages = list(filter(None, messages))
        #-------------------------------------------------------------------------
        if len(messages) != 0: last_messages = messages[-1]
        else: last_messages = "."
        return last_messages
    
    def waitforNewGres(self):
        n_status = True
        old_mens = ""
        while n_status:
            mens = self.rdMenss()
            if mens in ["OK","Ok","ok","oK"]:
                    self.onOffBot()
                    self.wrMenss("Tchau :D")
            time.sleep(2.5)
            if (old_mens != mens) & (mens != "."):
                old_mens = mens
                print(mens)
                if mens in 'SN' :
                    if mens == "S": self.callNewGm()
                    else: 
                        self.onOffBot()
                else:  self.wrMenss("Por favor insira *S* para sim e *N* para não")

wt = WhatsLyrBot("Repositorio do Zap", "Luis F", True)