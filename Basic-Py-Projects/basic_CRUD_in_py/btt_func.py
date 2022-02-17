from sre_parse import State
from tkinter import *
from validateRels import *

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
 
def changeLog(out_log, log_txt):
    out_log["state"] = NORMAL
    out_log.delete("1.0","end")
    out_log.insert(END, log_txt)
    out_log["state"] = DISABLED

def readBtt():
    list_of_users = callAlluser()
    return list_of_users

