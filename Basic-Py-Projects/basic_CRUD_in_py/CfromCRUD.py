
import numpy as np
import pandas as pd
import RfromCrud

user_data = pd.read_excel("data/user_data.xlsx")
ux_guide = pd.read_excel("data/UX_guide.xlsx")

def registerUser(user):
    if RfromCrud.checkIfesxists(user.username): 
        return False, "The Username is already in use"
    new_u = pd.DataFrame([[
        user.user_id,
        user.name,
        user.username,
        user.password,
        user.UX_]], columns=['user_id', 'name', 'username', 'password', 'UX'])
    
    union_frames = [user_data, new_u]
    new_user_base = pd.concat(union_frames, sort = False, ignore_index= True)
    
    with pd.ExcelWriter("data/user_data.xlsx") as writer:
        new_user_base.to_excel(writer)
    return True, "Loged!"
    
    
