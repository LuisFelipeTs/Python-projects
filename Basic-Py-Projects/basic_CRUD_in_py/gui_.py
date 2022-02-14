#Gui tkinter 
import _tkinter
from ast import And
from subprocess import call
from tkinter import *
from wsgiref import validate
from btt_func import loginBtt, readBtt

def tkinterBox(screen, session_id = 0):
    tk_screen = Tk()
    line= Label(text = "-----------------------------------")

    if screen == "login":
        tk_screen.geometry("240x255" )
        tk_screen.title("Login C.R.U.D")
        lab_title = Label(text = "Logar-se",font =("Sans-serif", 13))
        lab = Label(text = "Username:",font =("Sans-serif", 10))
        user_imput_lg = Text(tk_screen, height= 1, width= 20, bg= 'white')
        lab1 = Label(text = "Password:",font =("Sans-serif", 10))
        user_imput_ps = Text(tk_screen, height= 1, width= 20, bg= 'white')
        #btt_img_lg = PhotoImage(file = "imgs/login_btt.png")
        btt_lg = Button(tk_screen,
                 borderwidth = 3,
                 text ="Login!",
                 command = lambda:
                 [closeScreen(tk_screen), tkinterBox("menu")]
                 #loginBtt(user_imput_lg, user_imput_ps), checkIflog(log_r, tk_screen)
                 )
        btt_rg = Button(tk_screen,
                 borderwidth = 0,
                 text ="Não possui conta? Registre-se",
                 command = lambda:
                 [closeScreen(tk_screen), tkinterBox("regis")], )
        btt_ex = Button(tk_screen,
                 borderwidth = 1,
                 text ="Exit!",
                 command = lambda:
                 closeScreen(tk_screen))
        log_r = Label(text = "",font =("Sans-serif", 15))
        widgets_list = [ log_r, lab_title, lab, user_imput_lg, lab1, user_imput_ps, line, btt_lg, btt_rg, btt_ex]
        callScreen(widgets_list, tk_screen)

    elif screen == "regis":
        tk_screen.geometry("260x285" )
        tk_screen.title("Registre-se C.R.U.D")
        r_lab_title = Label(text = "Register",font =("Sans-serif", 13))
        r_lab = Label(text = "Name:",font =("Sans-serif", 10))
        r_user_imput_nm = Text(tk_screen, height= 1, width= 20, bg= 'white')
        r_lab1 = Label(text = "Username:",font =("Sans-serif", 10))
        r_user_imput_us = Text(tk_screen, height= 1, width= 20, bg= 'white')
        r_lab2 = Label(text = "Password:",font =("Sans-serif", 10))
        r_user_imput_pass = Text(tk_screen, height= 1, width= 20, bg= 'white')
        r_lab3 = Label(text = "Confirm Password:",font =("Sans-serif", 10))
        r_user_imput_cpass = Text(tk_screen, height= 1, width= 20, bg= 'white')
        r_btt_cd = Button(tk_screen,
                 borderwidth = 3,
                 text ="Register",
                 command = lambda:
                 [loginBtt(user_imput_lg, user_imput_ps), checkIflog(log_r, tk_screen)]
                 )
        r_btt_back = Button(tk_screen,
                 borderwidth = 0,
                 text ="back to the login screen.",
                 command = lambda:
                 [closeScreen(tk_screen), tkinterBox("login")])
        r_log_r = Label(text = "",font =("Sans-serif", 15))
        widgets_list_reg = [ r_log_r, r_lab_title, r_lab, r_user_imput_nm, r_lab1, r_user_imput_us, r_lab2, r_user_imput_pass , r_lab3, r_user_imput_cpass , line, r_btt_cd, r_btt_back]
        callScreen(widgets_list_reg, tk_screen)

    elif screen == "menu":
        tk_screen.geometry("260x285" )
        tk_screen.title("Menu C.R.U.D")
        m_lab_title = Label(text = "Menu",font =("Sans-serif", 13))
        see_whoin_btt = Button(tk_screen,
                 borderwidth = 1,
                 text ="Show Users",
                 command = lambda:
                 [backTo(tk_screen, "see_user")]
                 )
        config_btt = Button(tk_screen,
                 borderwidth = 1,
                 text ="Configurations",
                 command = lambda:
                 [closeScreen(tk_screen), tkinterBox("login")])
        back_btt = Button(tk_screen,
                 borderwidth = 1,
                 text ="Go back",
                 command = lambda:
                 [loginBtt(user_imput_lg, user_imput_ps), checkIflog(log_r, tk_screen)]
                 )
        exit_btt = Button(tk_screen,
                 borderwidth = 2,
                 text ="Exit",
                 command = lambda:
                 [closeScreen(tk_screen), tkinterBox("login")])
        widgets_list_reg = [m_lab_title, see_whoin_btt, config_btt, back_btt, line, exit_btt]
        callScreen(widgets_list_reg, tk_screen)
    
    elif screen == "see_user":
        tk_screen.geometry("260x285" )
        tk_screen.title("Read C.R.U.D")
        r_lab_title = Label(text = "Users",font =("Sans-serif", 13))
        back_btt = Button(tk_screen,
                 borderwidth = 1,
                 text ="Go back",
                 command = lambda:
                 [backTo("see_user" ,"menu" )]
                 )
        r_lab_title.pack()
        callNewread()
        back_btt.pack()
        tk_screen.mainloop()

def callScreen(widgets_s, tk):
    for widget in widgets_s:
        widget.pack()
    tk.mainloop()

def backTo(old_screen, new_screen):
    closeScreen(old_screen)
    tkinterBox(new_screen)

def callNewread():
    u_list = readBtt()
    for user in u_list:
         name_lab = Label(text = "Name: ",font =("Sans-serif bold", 10))
         name_lab.pack()
         name_lab_txt = Label(text = user.name ,font =("Sans-serif", 10.5))
         name_lab_txt.pack()
         username_lab = Label(text = "Username: ",font =("Sans-serif bold", 10))
         username_lab.pack()
         username_lab_txt = Label(text = user.name ,font =("Sans-serif", 10.5))
         username_lab_txt.pack()
         line_u = Label(text = "-----------------------------------")
         line_u.pack()
    

def checkIflog(log_r, tk_screen):
    out_log = str(log_r.get("1.0", "end-1c"))
    if out_log == "Loged":
        closeScreen(tk_screen)
        tkinterBox("menu")

def closeScreen(screen):
    screen.destroy()

#def makeTxtbold(wid_txt):
#    wid_txt.tag_configure("boldtext",font=wid_txt.cget("font")+" bold")
#    wid_txt.tag_add("boldtext","sel.first","sel.last")

tkinterBox("login")