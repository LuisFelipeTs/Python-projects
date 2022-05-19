
from tkinter import LEFT, X, Y, YES, Frame, Label, Button, Text, Tk, messagebox

import logging
logging.basicConfig(filename='logs\general_log.log', level=logging.DEBUG, format='%(asctime)s.%(msecs)03d %(levelname)s ====: %(message)s =;',
    datefmt='%Y-%m-%d %H:%M:%S',)
logging.info("Door's Lock simulator is ready to Start...")

class doorLock():
    def __init__(self):
        self.tk_screen = Tk()
        self.line = Label(text = "-----------------------------------")
        self.txt_visor = ""
        self.actual_pass = ""
        self.visor_color = "white"
        self.security_pass = "54321"
        logging.debug("Initiating Door's Lock simulator...")
        self.generateScreen()

    def generateScreen(self):
        self.tk_screen.geometry("200x190" )
        self.tk_screen.title("Door Lock Simulator")
        self.top_frame = Frame(self.tk_screen) 
        lab_title = Label(self.top_frame,text = "Door Lock",font = ("Sans-serif", 13))
        lab_title.pack( expand = YES, fill = X)
        self.visor = Text(self.top_frame, self.txt_visor, width = 16, height = 3, bg = self.visor_color)
        self.visor.pack(expand = YES, fill = X) 
        self.top_frame.pack (expand=YES, fill = X)       

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
                                    command = lambda s = self, y = char: s.insertVisor(y))

                btt_op.pack (side=LEFT, expand=YES, fill = X)
            self.btt_frame.pack (expand=YES, fill = X)
        self.callScreen(self.tk_screen)
        

    def __str__(self):
        pass

    def callScreen(self, tk):
         tk.mainloop()
        

    def insertVisor (self, text):
        self.actual_pass = self.actual_pass + text
        self.txt_visor = self.txt_visor + "*"
        print(self.actual_pass)
    
    def removeLastVisor(self):
        if self.actual_pass != "": 
            self.actual_pass = self.actual_pass[:-1]
            self.txt_visor = self.txt_visor[:-1]

    def checkPassword(self):
        if self.actual_pass == self.security_pass:
            self.visor_color = 'green'
            alert("Acesso Liberado!", "A sua entrada foi liberada com sucesso" , "info")
            logging.warning("Door's was opened by {}.".format("Owner"))
            print("ok")
        else:
            self.visor_color = 'red'
            alert("Acesso Bloqueado!", "A senha está incorreta!", "warning")
            logging.warning("Someone is trying to acess your front door")

    def closeScreen(self):
        self.tk_screen.destroy()

#https://www.foxinfotech.in/2019/01/alert-message-box-in-python-using-tkinter.html
def alert(title, message, kind):
    if kind not in ('error', 'warning', 'info'):
        raise ValueError('Unsupported alert kind.')
    show_method = getattr(messagebox, 'show{}'.format(kind))
    show_method(title, message)
#---------------------------------------------------------------------------------

door_lock = doorLock()
 