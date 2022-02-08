import User 
import pandas as pd
import validateRels
user_data = pd.read_excel("user_data.xlsx")
ux_guide = pd.read_excel("UX_guide.xlsx")

def updateName(user, new_name, password):
    if user.name != new_name:
        if user.password == password:
            user_data.loc[user_data['name'] ==  user.name, 'name'] = new_name
            return True, ""
        else: return False, "p"
    else: return False, "i"

def updatePassword(user, password, new_password, new_password_cf):
    if user.password != password:
        if password != new_password:
                if new_password == new_password_cf:
                    user_data.loc[user_data['user_id'] ==  user.user_id, 'password'] = new_password
                    return True, ""
                else: return False, "ni"
        else: return False, "ip"
    else: return False, "wp"

def updateUx(user, new_ux, add_del):
    if add_del:
        if new_ux not in user.UX:
            if new_ux in list(ux_guide["ux_id"]):
                old_ux = user._UX
                old_ux += new_ux
                user_data.loc[user_data['user_id'] ==  user.user_id, 'UX'] = old_ux
                return True, ""
            else: return False, "ne"
        else: return False, "ai"
    else:
        pass
