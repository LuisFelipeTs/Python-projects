from msilib.schema import ListBox
from tkinter import END, EXTENDED, Button, Grid, Tk, Listbox
import pandas as pd
import UfromCRUD

class ColorList:
    def __init__(self, tk_screen, user_s):
        self.user = user_s
        self.color_data = pd.read_excel("data/UX_guide.xlsx")
        self.list_c = Listbox(tk_screen, selectmode = EXTENDED)
        self.list_c.grid(row = 1, column = 1)
        self.getColors()
        self.select_button = Button(tk_screen, text="Change color!", command=self.changeToSelectColor)
        self.select_button.pack()

    def getColors(self):
        for i in self.color_data['color']:
            self.list_c.insert(END, str(i))

    def changeToSelectColor(self):
        selectedCol = self.list_c.curselection()
        UfromCRUD.updateUx(self.user, selectedCol)
