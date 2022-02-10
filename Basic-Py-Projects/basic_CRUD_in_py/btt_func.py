from tkinter import *
from validateRels import *

def loginBtt(username_imp, password_imp, out_log):
    out_log = out_log.get("1.0", "end-1c")
    username = str(username_imp.get("1.0", "end-1c"))
    password = str(password_imp.get("1.0", "end-1c"))
    lg_validation, lg_response = getLogin(username, password)
    if lg_validation:
        print("lg")
    elif lg_response == "u":  
        out_log.insert(END, "The Username is not in the database")
    elif lg_response == "p":
        out_log.insert(END, "The Password is not correct")
 

