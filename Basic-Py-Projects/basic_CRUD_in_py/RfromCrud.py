from ast import Return
from operator import index
from User import User
import pandas as pd

user_data = pd.read_excel("data/user_data.xlsx")

def checkIfesxists(user):
    if user not in list(user_data["username"]): return False
    else: return True

def getLogin(username, password):
    if checkIfesxists(username):
        ind = list(user_data["username"]).index(username)
        passw_ = user_data["password"][ind]
        if str(passw_) == str(password):
            index_ = user_data["user_id"][ind]
            return True, index_
        else: return False, "p"
    else: return False, "u"

def callUserinbase(user_id):
    name = user_data["name"][user_id]
    username = user_data["username"][user_id]
    password = user_data["password"][user_id]
    ux = user_data["UX"][user_id]
    new_u = User(user_id, name, username, password, ux)
    return new_u

def callAlluser():
    list_of_users = []
    for u_id in user_data["user_id"]:
        list_of_users.append(callUserinbase(u_id))
    return list_of_users
    
def getNewid():
    id_list = user_data["user_id"]
    new_id = len(id_list)
    return new_id

#user_data = pd.read_excel("user_data.xlsx")
#print(list(user_data["username"]))