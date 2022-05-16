
from tkinter import LEFT, X, Y, YES, Frame, Label, Button, Text, Tk
import logging


class doorLock():

    def __init__(self):
        self.tk_screen = Tk()
        self.line = Label(text = "-----------------------------------")
        self.txt_visor = ""
        self.actual_pass = ""
        self.generateScreen()

    def generateScreen(self):
        self.tk_screen.geometry("200x190" )
        self.tk_screen.title("Door Lock Simulator")
        self.top_frame = Frame(self.tk_screen) 
        lab_title = Label(self.top_frame,text = "Door Lock",font =("Sans-serif", 13))
        lab_title.pack( expand = YES, fill = X)
        self.visor = Text(self.top_frame, self.txt_visor, width = 16, height = 3,)
        self.visor.pack(expand = YES, fill = X) 
        self.top_frame.pack (expand=YES, fill = X)       

        pass_btt_op = ["123", "456", "789", "X0O"]          
        for pass_btt in pass_btt_op:
            self.btt_frame = Frame(self.tk_screen)                       
            for char in pass_btt:
                if char == "O":
                    btt_op = Button (self.btt_frame, text="C", bg = 'green',
                                    command = lambda:[self.removeLastVisor()])
                elif char == "X":
                    btt_op = Button (self.btt_frame, text=char, bg = 'red',
                                    command = lambda:[self.removeLastVisor()])
                else:
                    btt_op = Button (self.btt_frame, text=char, bg = 'white',
                                    command = lambda s = self, y = char: s.insertVisor(y))

                btt_op.pack (side=LEFT, expand=YES, fill = X)
            self.btt_frame.pack (expand=YES, fill = X)
        self.tk_screen.mainloop()
        

        
#    def callScreen(self):
#        for widget in self.widgets_list:
#            widget.pack(expand = YES, fill = X)
        

    def insertVisor (self, text):
        self.actual_pass = self.actual_pass + text
        self.txt_visor = self.txt_visor + "*"
        print(self.actual_pass)
    
    def removeLastVisor(self):
        if self.actual_pass != "": 
            self.actual_pass = self.actual_pass[:-1]
            self.txt_visor = self.txt_visor[:-1]

    def closeScreen(self):
        self.tk_screen.destroy()

door_lock = doorLock()
