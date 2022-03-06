from email import message
from tkinter import *
from RfromCrud import *
from CfromCRUD import *
import os

from UfromCRUD import updateName, updatePassword

def checkIfconnectedtobase():
    if ~(os.path.exists("data/user_data.xlsx")):
        return True
    else: return False

def loginBtt(username_imp, password_imp, out_log):
    username = str(username_imp.get("1.0", "end-1c"))
    password = password_imp.get()
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
    password = password.get()
    confirm_password = confirm_password.get()
    validate = False
    message_log = ""
    if name == "" or (len(name) < 3): message_log = "The name must have at least 3 letters"
    elif username == "" or (len(name) < 4): message_log = "The username must have at least 4 letters"
    elif password == "" or (len(name) < 3): message_log = "The password must have at least 4 letters"
    elif confirm_password != password: message_log = "The Confirm password must be equal to the password"        
    else:
        validate, message_log = registerUser(User(getNewid(), name, username, password, "white"))
    if message_log == "Loged!": 
        print("...")
        changeLog(out_log, "Loged!")
    return validate

def updateElement(user, attr, new_attr, log, password,  confirm_pas = 0):
    if attr == "Name":
        name = str(new_attr.get("1.0", "end-1c"))
        password_ = str(password.get("1.0", "end-1c"))
        validate, message_ = updateName(user , name, password_)
    elif attr == "Pass":
        password_ = str(new_attr.get("1.0", "end-1c"))
        if confirm_pas == 0:
            message_ = "Confirm you password before update"
        else:
            password_c = str(confirm_pas.get("1.0", "end-1c"))
            validate, message_ = updatePassword(user, password, password_, password_c)
    
    if validate: changeLog(log, "Ok")
    else: changeLog(log, message_)

def changeLog(out_log, log_txt):
    out_log["state"] = NORMAL
    out_log.delete("1.0","end")
    out_log.insert(END, log_txt)
    out_log["state"] = DISABLED

def readBtt():
    list_of_users = callAlluser()
    return list_of_users

