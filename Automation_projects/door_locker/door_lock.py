import time
from tkinter import DISABLED, END, LEFT, X, Y, YES, Entry, Frame, Label, Button, Text, Tk, messagebox
#import cam_res
import logging
logging.basicConfig(filename='logs\general_log.log', level=logging.DEBUG, format='%(asctime)s.%(msecs)03d %(levelname)s ====: %(message)s =;',
    datefmt='%Y-%m-%d %H:%M:%S',)
logging.info("Door's Lock simulator is ready to Start...")

class doorLock():
    def __init__(self):
        self.tk_screen = Tk()
        self.actual_pass = ""
        self.visor_color = "white"
        self.security_pass = "54321"
        self.try_pass = 0
        logging.debug("Initiating Door's Lock simulator...")

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
                                    command = lambda s = self, y = char: s.insertVisor(y))

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
        #img_path, who, permition = cam_res.getPic()
        permition = True
        if self.actual_pass == self.security_pass:
            if permition == True:
                self.visor_color = 'green'
                alert("Acesso Liberado!", "A sua entrada foi liberada com sucesso" , "info")
                logging.warning("Door's was opened by {}.".format("Owner"))
            else:
                self.visor_color = 'yellow'
                alert("Acesso Liberado!", "A sua entrada foi liberada com sucesso" , "info")
                logging.warning("Door's was opened by {}.".format("Owner"))

        else:
            alert("Acesso Bloqueado!", "A senha está incorreta!", "error")
            self.actual_pass = ""
            self.try_pass += 1
            if self.try_pass == 3:
                logging.warning("Someone is trying to acess your front door")
                self.try_pass = 0


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
 
