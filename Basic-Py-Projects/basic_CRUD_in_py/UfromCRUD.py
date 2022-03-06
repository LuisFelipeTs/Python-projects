from tkinter import messagebox
import User 
import pandas as pd

def updateName(user, new_name, password):
    user_data = call_u_database()
    if user.name != new_name:
        password_u = str(user.password)
        if password_u == password:
            user_data.loc[user_data['name'] ==  user.name, 'name'] = new_name
            saveU(user_data)
            return True, ""
        else: return False, "The password is not correct"
    else: return False, "The new name is equal to the old one"

def updatePassword(user, password, new_password, new_password_cf):
    user_data = call_u_database()
    if user.password != password:
        if password != new_password:
                if new_password == new_password_cf:
                    user_data.loc[user_data['user_id'] ==  user.user_id, 'password'] = new_password
                    saveU(user_data)
                    return True, ""
                else: return False, "The confirmation is not equal to the new password"
        else: return False, "The password is equal to the old one"
    else: return False, "The actual password is incorrect"

def updateUx(user, new_ux):
    user_data = call_u_database()
    ux_guide = pd.read_excel("data/UX_guide.xlsx")
    '''if add_del:
        if new_ux not in user.UX_:
            if new_ux in list(ux_guide["ux_id"]):
                old_ux += new_ux
                user_data.loc[user_data['user_id'] ==  user.user_id, 'UX'] = old_ux
                return True, ""
            else: return False, "ne"
        else: return False, "ai"
    else:'''
    
    user_data.loc[user_data['user_id'] ==  user.user_id, 'UX'] = str(new_ux)
    alert("Color Update", "Color updated!")
    saveU(user_data)

    #alert("Color Update", "Update error!", "error")
    
        
def alert(title, message, kind='info'):
    show_method = getattr(messagebox, 'show{}'.format(kind))
    show_method(title, message)

def saveU(user_data):
    with pd.ExcelWriter("data/user_data.xlsx") as writer:
        user_data.to_excel(writer, index= False)

def call_u_database():
    return pd.read_excel("data/user_data.xlsx")