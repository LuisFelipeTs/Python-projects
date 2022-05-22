from ast import Try
import imp
import time
from tkinter import DISABLED, END, LEFT, X, Y, YES, Entry, Frame, Label, Button, Text, Tk, messagebox
from urllib import response
#import cam_res
from whatsappComunicator import WhatsComunic
import logging
from alert import alert
#import aws_connection
logging.basicConfig(filename='logs\general_log.log', level=logging.DEBUG, format='%(asctime)s.%(msecs)03d %(levelname)s ====: %(message)s =;',
    datefmt='%Y-%m-%d %H:%M:%S')
logging.info("Door's Lock simulator is ready to Start...")

class doorLock():
    def __init__(self):
        self.tk_screen = Tk()
        self.actual_pass = ""
        self.visor_color = "white"
        self.security_pass = "54321"
        self.try_pass = 0
        self.wtsapp_connect = WhatsComunic() 
        logging.debug("Initiating Door's Lock simulator...")
        self.generateScreen()

    def generateScreen(self):
        self.tk_screen.geometry("200x190" )
        self.tk_screen.title("Door Lock Simulator")
        lab_title = Label(self.tk_screen,text = "Door Lock",font = ("Sans-serif", 13))
        lab_title.pack( fill = X)
        self.visor = Text(self.tk_screen, width = 16, height = 2, bg= self.visor_color)
        self.visor.pack(fill = X)        

        pass_btt_op = ["123", "456", "789", "X0O"]          
        for pass_btt in pass_btt_op:
            self.btt_frame = Frame(self.tk_screen)                       
            for char in pass_btt:
                if char == "O":
                    btt_op = Button (self.btt_frame, text="C", bg = 'green',
                                    command = lambda:[self.checkPassword()])
                elif char == "X":
                    btt_op = Button (self.btt_frame, text=char, bg = 'red',
                                    command = lambda:[self.removeLastVisor()])
                else:
                    btt_op = Button (self.btt_frame, text=char, bg = 'white',
                                    command = lambda:[self.insertVisor(char)])

                btt_op.pack (side=LEFT, expand=YES, fill = X)
            self.btt_frame.pack (expand=YES, fill = X)
        self.callScreen(self.tk_screen)
        

    def callScreen(self, tk):
        tk.mainloop()
        

    def insertVisor (self, text):
        self.actual_pass = self.actual_pass + text
        self.visor.insert(END, "*")
        

    def removeLastVisor(self):
        if self.actual_pass != "": 
            self.actual_pass = self.actual_pass[:-1]
            self.visor.delete('end-2c' , END)
            

    def checkPassword(self):
        if self.actual_pass == self.security_pass:
            #response1, response2 = cam_res.getPic(True)
            response2 = True 
            if response2 == True:
                self.visor_color = 'green'
                alert("Acesso Liberado!", "Bem vindo atual vendedor" , "info")
                self.wtsapp_connect.wrMenss("Bem Vindo! Porta aberta.")
                #aws_connection.sendImgS3(response1 , "Resident__")
                logging.warning("Door's was opened by {}.".format("Owner"))
            else:
                self.visor_color = 'yellow'
                alert("Acesso Postergado!", "Não o reconhecemos por favor aguarde a liberação pelo dono" , "info")
                quest_req = self.wtsapp_connect.getResponse("Alguem que não reconhecemos com a senha está tentando acessar a porta, você deseja abrir a porta?\nResponda S - para Sim e N - para não")
                if quest_req:
                    logging.warning("Door's was opened by {}.".format("Visitant"))
                    #aws_connection.sendImgS3(response1 , "Visitant")
                else:
                    logging.warning("Door's was protected from suspect {}.".format("Visitant"))
                    #aws_connection.sendImgS3(response1 , "Suspect")
        else:
            alert("Acesso Bloqueado!", "A senha está incorreta!", "error")
            self.actual_pass = ""
            self.visor.delete('1.0' , END)
            self.try_pass += 1
            if self.try_pass == 4:
                permition = True
                #name_sus, suspect = cam_res.getPic(False)
                self.wtsapp_connect.wrMenss("Cuidado, alguêm está tentando acessar a porta")
                #aws_connection.sendImgS3(name_sus, "Suspect")
                logging.warning("Someone is trying to acess your front door")
                self.try_pass = 0

    def closeScreen(self):
        self.tk_screen.destroy()

door_lock = doorLock()
 
