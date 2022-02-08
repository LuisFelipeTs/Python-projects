from operator import index
import User
import pandas as pd

user_data = pd.read_excel("user_data.xlsx")

def checkIfesxists(user):
    if user not in list(user_data["username"]): return False
    else: return True

def getLogin(username, password):
    if checkIfesxists(username):
        ind = index(user_data["username"][username])
        if user_data["password"][ind] == password:
            index_ = user_data["user_id"][ind]
            return True, index_
        else: return False, "p"
    else: return False, "u"

def callUserinbase(user_id):
    name = user_data["name"][user_id]
    username = user_data["username"][user_id]
    password = user_data["password"][user_id]
    ux = name = user_data["UX"][user_id]
    return User(user_id, name, username, password, ux)


    


#user_data = pd.read_excel("user_data.xlsx")
#print(list(user_data["username"]))