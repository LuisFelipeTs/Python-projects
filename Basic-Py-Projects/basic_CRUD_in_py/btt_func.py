from sre_parse import State
from tkinter import *
from RfromCrud import *
import os

def checkIfconnected():
    if ~(os.path.exists("data/user_data.xlsx")):
        return True
    else: return False

def loginBtt(username_imp, password_imp, out_log):
    username = str(username_imp.get("1.0", "end-1c"))
    password = str(password_imp.get("1.0", "end-1c"))
    lg_validation, lg_response = getLogin(username, password)
    if lg_validation:
        changeLog(out_log, "Loged!")
    elif lg_response == "u":  
        changeLog(out_log, "The Username is not in the database")
    elif lg_response == "p":
        changeLog(out_log, "The Password is not correct")   

def regisBtt(name, username, password, confirm_password, out_log):
    name = str(name.get("1.0", "end-1c"))
    username = str(username.get("1.0", "end-1c"))
    password = str(password.get("1.0", "end-1c"))
    confirm_password = str(confirm_password.get("1.0", "end-1c"))
    if name == "" or (len(name) < 3):
        changeLog(out_log, "The name must have at least 3 letters")
    elif username == "" or (len(name) < 4):
        changeLog(out_log, "The username must have at least 4 letters")
    elif password == "" or (len(name) < 3):
        changeLog(out_log, "The password must have at least 4 letters")
    elif confirm_password != password:
        changeLog(out_log, "The Confirm password must be equal to the password")
    else:
        registerUser(name, username, password, confirm_password)


def changeLog(out_log, log_txt):
    out_log["state"] = NORMAL
    out_log.delete("1.0","end")
    out_log.insert(END, log_txt)
    out_log["state"] = DISABLED

def readBtt():
    list_of_users = callAlluser()
    return list_of_users

