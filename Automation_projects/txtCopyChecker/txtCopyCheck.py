
from turtle import bgcolor
import pyautogui
import time
import tkinter as tk
from tkinter import *
from entryBox import boxE

tktk_v = tk.Tk()
tktk_v.geometry("500x500" )
tktk_v.title("Answer validation!")
#text_gene = Text(tktk_v, height = 10, width = 82)
#tktk_v.withdraw()
lab = Label(text = "Add the answer:",font =("Sans-serif", 18))
lab1 = Label(text = "--------------------------------------------------------------")
lab2= Label(text = "https://github.com/LuisFelipeTs", font=("Arial", 6))
user_imput = Text(tktk_v, height= 12, width= 50, bg= 'light gray')
calc_output = Text(tktk_v, height= 12, width= 50, bg= 'light green')
 

btt_img = PhotoImage(file = "image_btt.png")
btt = Button(tktk_v,
                 image= btt_img,
                 borderwidth = 0,
                 text ="Check!",
                 command = lambda:boxE(user_imput , calc_output))

lab.pack(side= TOP, anchor="n")
lab1.pack()
user_imput.pack()
btt.pack()
calc_output.pack()
lab2.pack()

tk.mainloop()

'''
options = simpledialog.askstring(
    title="Random choice", prompt="Add your options?(Like: opt1, opt2, opt3)\n      https://github.com/LuisFelipeTs"
)
link_choice =options.split(",")
webchoice = random.choice(link_choice)  '''