
import tkinter as tk
from tkinter import *
from entryBox import boxE

tktk_v = tk.Tk()
 
tktk_v.geometry("500x415" )
tktk_v.title("Answer validation!")
#text_gene = Text(tktk_v, height = 10, width = 82)
#tktk_v.withdraw()
lab = Label(text = "Add the Word:",font =("Sans-serif", 18))
lab1 = Label(text = "--------------------------------------------------------------")
lab2= Label(text = "https://github.com/LuisFelipeTs", font=("Arial", 5))
lab3= Label(text = "https://pt.wikipedia.org/", font=("Arial", 5))
lab4= Label(text = "https://www.dicionarioinformal.com.br/", font=("Arial", 5))
user_imput = Text(tktk_v, height= 2, width= 30, bg= 'white')
calc_output = Text(tktk_v, height= 8, width= 50, bg= 'light gray')


btt_img = PhotoImage(file = "image_btt.png")
btt = Button(tktk_v,
                 image= btt_img,
                 borderwidth = 0,
                 text ="Check!",
                 command = lambda:
                 boxE((user_imput) , calc_output))

lab.pack(side= TOP, anchor="n")
lab1.pack()
user_imput.pack()
btt.pack()
calc_output.pack()
lab2.pack()
lab3.pack()
lab4.pack()

tk.mainloop()
 