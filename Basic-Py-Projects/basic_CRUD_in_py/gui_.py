#Gui tkinter 
import _tkinter
from ast import And
from tkinter import *
from turtle import back
from btt_func import loginBtt, readBtt, regisBtt

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
                 [loginBtt(user_imput_lg, user_imput_ps, log_r), checkIflog(log_r, tk_screen, "menu")]
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
        log_r = Text(tk_screen, height= 2, width= 30, bg= 'white',state= DISABLED)
        widgets_list = [log_r, lab_title, lab, user_imput_lg, lab1, user_imput_ps, line, btt_lg, btt_rg, btt_ex]
        callScreen(widgets_list, tk_screen)

    elif screen == "regis":
        tk_screen.geometry("260x305" )
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
                 [regisBtt(r_user_imput_nm, r_user_imput_us, r_user_imput_pass, r_user_imput_cpass, r_log_r), checkIflog(r_log_r, tk_screen, "login")]
                 )
        r_btt_back = Button(tk_screen,
                 borderwidth = 0,
                 text ="back to the login screen.",
                 command = lambda:
                 [closeScreen(tk_screen), tkinterBox("login")])

        r_log_r = Text(tk_screen, height= 2, width= 30, bg= 'white', state= DISABLED)
        widgets_list_reg = [r_log_r, r_lab_title, r_lab, r_user_imput_nm, r_lab1, r_user_imput_us, r_lab2, r_user_imput_pass , r_lab3, r_user_imput_cpass , line, r_btt_cd, r_btt_back]
        callScreen(widgets_list_reg, tk_screen)

    elif screen == "menu":
        tk_screen.geometry("260x285" )
        tk_screen.title("Menu C.R.U.D")
        line_m = Label(text = "-------------------------------------------")
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
        widgets_list_reg = [m_lab_title, line_m, see_whoin_btt, config_btt, back_btt, line, exit_btt]
        callScreen(widgets_list_reg, tk_screen)
    
    elif screen == "see_user":
        tk_screen.geometry("260x285" )
        tk_screen.title("Read C.R.U.D")
        r_lab_title = Label(text = "Users",font =("Sans-serif", 13))
        back_btt = Button(tk_screen,
                 borderwidth = 1,
                 text ="Go back",
                 command = lambda:
                 [backTo(tk_screen ,"menu" )]
                 )
        r_lab_title.grid(column = 1, row = 0 )
        callNewread()
        back_btt.grid(column = 0, row = 0 )
        tk_screen.mainloop()

    elif screen == "update":
        tk_screen.geometry("360x285" )
        tk_screen.title("Read C.R.U.D")
        u_title = Label(text = "Update",font =("Sans-serif", 13))
        u_title.grid( column = 1, row= 0)
        back_btt = Button(tk_screen,
                 borderwidth = 1,
                 text ="Go back",
                 command = lambda:
                 [backTo(tk_screen ,"menu" )]
                 )
        back_btt.grid(column = 0, row = 0)
        line_m = Label(text = "-----------")
        line_m2 = Label(text = "-------------------------------------------")
        line_m.grid(column=0 , row= 1)
        line_m2.grid(column= 1 , row= 1)





def callScreen(widgets_s, tk):
    for widget in widgets_s:
        widget.pack()
    tk.mainloop()

def backTo(old_screen, new_screen):
    closeScreen(old_screen)
    tkinterBox(new_screen)

def callNewread():
    u_list = readBtt()
    line_u = Label(text = "-------------")
    line_u.grid(column = 0, row = 1 )
    line_u1 = Label(text = "----------------------------")
    line_u1.grid(column = 1, row = 1 )
    actual_row = 1
    for user in u_list:
         actual_row += 1
         name_lab = Label(text = "Name: ",font =("Arial bold", 8))
         name_lab.grid(column = 0, row = actual_row )
         name_lab_txt = Label(text = user.name ,font =("Sans-serif", 11))
         name_lab_txt.place(anchor= "w")
         name_lab_txt.grid(column = 1, row = actual_row )
         actual_row += 1
         username_lab = Label(text = "Username: ",font =("Arial bold", 8))
         username_lab.grid(column = 0, row = actual_row )
         username_lab_txt = Label(text = user.username ,font =("Sans-serif", 11))
         username_lab_txt.place(anchor= "w")
         username_lab_txt.grid(column = 1, row = actual_row )
         actual_row += 1
         line_u = Label(text = "-------------")
         line_u.grid(column = 0, row = actual_row )
         line_u1 = Label(text = "----------------------------")
         line_u1.grid(column = 1, row = actual_row )
    

def checkIflog(log_r, tk_screen, nw_screen):
    out_log = str(log_r.get("1.0", "end-1c"))
    if out_log == "Loged!":
        closeScreen(tk_screen)
        tkinterBox(nw_screen)

def closeScreen(screen):
    screen.destroy()

tkinterBox("login")