import numpy as np
import pandas as pd
import RfromCrud

def registerUser(user):
    user_data = pd.read_excel("data/user_data.xlsx")
    if RfromCrud.checkIfesxists(user.username): 
        return False, "The Username is already in use"
    new_u = pd.DataFrame([[
        user.user_id,
        user.name,
        user.username,
        user.password,
        user.UX_]], columns=['user_id', 'name', 'username', 'password', 'UX'])
    
    union_frames = [user_data, new_u]
    conc_np = np.concatenate(union_frames, axis = 0)
    new_user_base = pd.DataFrame(conc_np, columns= ['user_id', 'name', 'username', 'password', 'UX'])
    #new_user_base = pd.concat(union_frames, sort = False, axis = 0, ignore_index= True)

    with pd.ExcelWriter("data/user_data.xlsx") as writer:
        new_user_base.to_excel(writer, index= False)

    return True, "Loged!"
    
    
