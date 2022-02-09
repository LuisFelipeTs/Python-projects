#Gui tkinter 
import _tkinter
from ast import And
from tkinter import *
from wsgiref import validate
from btt_func import loginBtt

def tkinterBox(screen):
    tk_screen = Tk()
    if screen == "login":
        tk_screen.geometry("400x315" )
        tk_screen.title("CRUD in Py")
        lab = Label(text = "Login:",font =("Sans-serif", 15))
        user_imput_lg = Text(tk_screen, height= 2, width= 25, bg= 'white')
        lab = Label(text = "Password:",font =("Sans-serif", 15))
        user_imput_ps = Text(tk_screen, height= 2, width= 25, bg= 'white')
        btt_img_lg = PhotoImage("imgs/login_btt.png")
        btt_lg = Button(tk_screen,
                 image= btt_img_lg,
                 borderwidth = 0,
                 text ="Login!",
                 command = lambda:
                 loginBtt(user_imput_lg, user_imput_ps))
        btt_img_rg = PhotoImage("imgs/gotoreg_btt.png")
        btt_rg = Button(tk_screen,
                 image= btt_img_rg,
                 borderwidth = 0,
                 text ="Registre-se!",
                 command = lambda:
                 boxE((user_imput) , calc_output))
        log_r = Label(text = "",font =("Sans-serif", 15), _Color = "red")


