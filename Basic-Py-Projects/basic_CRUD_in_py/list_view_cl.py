from msilib.schema import ListBox
from tkinter import DISABLED, END, EXTENDED, Button, Grid, Label, Text, Tk, Listbox
import pandas as pd
import UfromCRUD

class ColorList:
    def __init__(self, tk_screen, user_s):
        self.user = user_s
        self.color_data = pd.read_excel("data/UX_guide.xlsx")
        m_lab_title = Label(text = "Menu color", font =("Sans-serif", 13))
        m_lab_title.grid(row = 0, column = 1)
        r_log_r = Text(tk_screen, height= 8, width= 3, bg= user_s.UX_ , state= DISABLED)
        self.list_c = Listbox(tk_screen, selectmode = EXTENDED)
        self.list_c.grid(row = 1, column = 1)
        self.getColors()
        self.select_button = Button(tk_screen, text="Change color!", command = self.changeToSelectColor)
        self.select_button.grid(row = 2, column = 1)

    def getColors(self):
        for i in self.color_data['color']:
            self.list_c.insert(END, str(i))

    def changeToSelectColor(self):
        selectedCol = self.list_c.curselection()
        selec = ",".join([self.list_c.get(i) for i in selectedCol])
        print(selec)
        UfromCRUD.updateUx(self.user, str(selec))
