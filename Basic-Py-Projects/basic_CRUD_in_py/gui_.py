#Gui tkinter 
from tkinter import RIGHT, Y, Grid, messagebox, Tk, Label, Button, Text, DISABLED, ttk
import tkinter as tk
from RfromCrud import callUserinbase, getUid
from btt_func import loginBtt, readBtt, regisBtt, updateElement

def tkinterBox(screen):
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
                 [loginBtt(user_imput_lg, user_imput_ps, log_r), checkIflog(log_r, tk_screen, "menu", user_imput_lg)]
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
                 [regisBtt(r_user_imput_nm, r_user_imput_us, r_user_imput_pass, r_user_imput_cpass, r_log_r), checkIflog(r_log_r, tk_screen, "menu", r_user_imput_us, True)]
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
                 [closeScreen(tk_screen), tkinterBox("update")])
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
        tk_screen.grid_rowconfigure(0, weight=1)
        tk_screen.columnconfigure(0, weight=1)
        frameM = tk.Frame(tk_screen)
        frameM.grid(sticky='news')

        r_lab_title = Label(frameM, text = "Users",font =("Sans-serif", 13))
        back_btt = Button(frameM,
                 borderwidth = 1,
                 text ="Go back",
                 command = lambda:
                 [backTo(tk_screen ,"menu" )]
                 )
        
        r_lab_title.grid(column = 1, row = 0 )
        callNewread(frameM)
        back_btt.grid(column = 0, row = 0 )
        canvas = tk.Canvas(frameM)
        canvas.grid(row = 0, column=0, sticky="news")
        cv_scroll = tk.Scrollbar(frameM, orient="vertical", command=canvas.yview)
        cv_scroll.grid(row=0, column=1, sticky='ns')
        canvas.config(scrollregion = canvas.bbox("all"))
        tk_screen.mainloop()

    elif screen == "update":
        session_u = callUserinbase(changeSession(False))
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
        name_lab = Label(text = "Name: " + session_u.name ,font =("Arial bold", 8))
        name_lab.grid(column = 1, row = 2 )
        ch_n_btt = Button(tk_screen,
                 borderwidth = 1,
                 text ="Change Name",
                 command = lambda:
                 [backTo(tk_screen ,"update+N" )]
                 )
        ch_n_btt.grid(column = 0 , row = 2)
        pass_lab = Label(text = "Password: " + len(str(session_u.password)) * '*' ,font =("Arial bold", 8))
        pass_lab.grid(column = 1, row = 3 )
        ch_p_btt = Button(tk_screen,
                 borderwidth = 1,
                 text ="Change Pass",
                 command = lambda:
                 [backTo(tk_screen ,"update+P" )]
                 )
        ch_p_btt.grid(column = 0 , row = 3)
        pass_lab = Label(text = "color: " + session_u.name ,font =("Arial bold", 8))
        pass_lab.grid(column = 1, row = 4 )
    
    elif screen == 'update+N':
        session_u = callUserinbase(changeSession(False))
        tk_screen.geometry("260x130")
        tk_screen.title("Update Name")
        back_btt = Button(tk_screen,
                 borderwidth = 1,
                 text ="Go back",
                 command = lambda:
                 [backTo(tk_screen ,"update")]
                 )
        back_btt.grid(column = 0, row = 0)
        u_title = Label(text = "Update Name",font =("Sans-serif", 13))
        u_title.grid(column = 1, row= 0)
        n_actual1 = Label(text = "Actual Name:",font =("Sans-serif", 8))
        n_actual1.grid(column = 0, row= 1)
        n_actual2 = Label(text = session_u.name ,font =("Sans-serif", 9))
        n_actual2.grid(column = 1, row= 1)
        n_new = Label(text = "New Name:",font =("Sans-serif", 8))
        n_new.grid(column = 0, row= 2)
        up_user_imput_nm = Text(tk_screen, height= 1, width= 20, bg= 'white')
        up_user_imput_nm.grid(column = 1, row = 2)
        up_pass = Label(text = "Password:",font = ("Sans-serif", 8))
        up_pass.grid(column = 0, row= 3)
        up_user_imput_pass = Text(tk_screen, height= 1, width= 20, bg= 'white')
        up_user_imput_pass.grid(column = 1, row = 3)
        up_btt = Button(tk_screen,
                 borderwidth = 1,
                 text ="Update!",
                 command = lambda:
                 [updateElement(session_u, "Name", up_user_imput_nm, log_u, up_user_imput_pass), checkIfup(log_u, tk_screen)]
                 )
        up_btt.grid(column = 1, row= 4)
        log_u = Text(tk_screen)


    elif screen == 'update+P':
        tk_screen.geometry("260x130" )
        tk_screen.title("Update Password")
        session_u = callUserinbase(changeSession(False))
        back_btt = Button(tk_screen,
                 borderwidth = 1,
                 text ="Go back",
                 command = lambda:
                 [backTo(tk_screen ,"update")]
                 )
        back_btt.grid(column = 0, row = 0)
        u_title = Label(text = "Update Password",font =("Sans-serif", 13))
        u_title.grid(column = 1, row= 0)
        n_actual1 = Label(text = "Actual Password:",font =("Sans-serif", 8))
        n_actual1.grid(column = 0, row= 1)
        up_user_imput_o_pass = Text(tk_screen, height= 1, width= 20, bg= 'white')
        up_user_imput_o_pass.grid(column = 1, row= 1)
        n_new = Label(text = "New Password:",font =("Sans-serif", 8))
        n_new.grid(column = 0, row= 2)
        up_user_imput_n_pass = Text(tk_screen, height= 1, width= 20, bg= 'white')
        up_user_imput_n_pass.grid(column = 1, row = 2)
        up_pass = Label(text = "Confirm Password:",font = ("Sans-serif", 8))
        up_pass.grid(column = 0, row= 3)
        up_user_imput_pass = Text(tk_screen, height= 1, width= 20, bg= 'white')
        up_user_imput_pass.grid(column = 1, row = 3)
        up_btt = Button(tk_screen,
                 borderwidth = 1,
                 text ="Update!",
                 command = lambda:
                 [updateElement(session_u, "Pass", up_user_imput_n_pass, log_u, up_user_imput_o_pass, up_user_imput_pass), checkIfup(log_u, tk_screen)]
                 )
        up_btt.grid(column = 1, row= 4)
        log_u = Text(tk_screen)

def callScreen(widgets_s, tk):
    for widget in widgets_s:
        widget.pack()
    tk.mainloop()

def backTo(old_screen, new_screen):
    closeScreen(old_screen)
    tkinterBox(new_screen)

def callNewread(frame):
    u_list = readBtt()
    line_u = Label(frame,text = "-------------")
    line_u.grid(column = 0, row = 1 )
    line_u1 = Label(frame, text = "----------------------------")
    line_u1.grid(column = 1, row = 1 )
    actual_row = 1
    for user in u_list:
         actual_row += 1
         name_lab = Label(frame, text = "Name: ",font =("Arial bold", 8))
         name_lab.grid(column = 0, row = actual_row )
         name_lab_txt = Label(frame, text = user.name ,font =("Sans-serif", 11))
         name_lab_txt.place(anchor= "w")
         name_lab_txt.grid(column = 1, row = actual_row )
         actual_row += 1
         username_lab = Label(frame, text = "Username: ",font =("Arial bold", 8))
         username_lab.grid(column = 0, row = actual_row )
         username_lab_txt = Label(frame, text = user.username ,font =("Sans-serif", 11))
         username_lab_txt.place(anchor= "w")
         username_lab_txt.grid(column = 1, row = actual_row )
         actual_row += 1
         line_u = Label(frame, text = "-------------")
         line_u.grid(column = 0, row = actual_row )
         line_u1 = Label(frame, text = "----------------------------")
         line_u1.grid(column = 1, row = actual_row )
    

def checkIflog(log_r, tk_screen, nw_screen, username, register = False):
    out_log = str(log_r.get("1.0", "end-1c"))
    username = str(username.get("1.0", "end-1c"))
    if out_log == "Loged!":
        if register: alert("Register Info!", "Registered!")
        else: alert("Login Info!", "Loged!")
        changeSession(True, getUid(username))
        closeScreen(tk_screen)
        tkinterBox(nw_screen)
    else: alert("Login Info!", "Error: " + out_log, kind= 'error')


def checkIfup(log, tk_screen):
    out_log = str(log.get("1.0", "end-1c"))
    if out_log == "Ok":
        alert("Update Status!", "Update successfully!", kind= "info")
        closeScreen(tk_screen)
        tkinterBox("update")
    else:

        alert("Update Status!", out_log , kind= "error")

def closeScreen(screen):
    screen.destroy()

def changeSession(ch , new_id = 0):
    global session_id
    if ch == True: session_id = new_id
    return session_id

#https://www.foxinfotech.in/2019/01/alert-message-box-in-python-using-tkinter.html
def alert(title, message, kind='info', hidemain=True):
    if kind not in ('error', 'warning', 'info'):
        raise ValueError('Unsupported alert kind.')
    show_method = getattr(messagebox, 'show{}'.format(kind))
    show_method(title, message)
#---------------------------------------------------------------------------------

tkinterBox("login")