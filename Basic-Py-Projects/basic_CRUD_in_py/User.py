
from numpy import True_


class User:
    def __init__(self, user_id, name, username, password):
        self.user_id = user_id
        self.name = name
        self.username = username
        self.password = password
        self.UX_ = ""

    def __str__(self):
        return self.name

    def checkPassword(self, pass_try):
        if pass_try == self.password: return True
        else: return False
    
    def updateUX(self, new_ux, del_ = False):
        if del_:
            if new_ux in self.UX_: self.UX_ -= new_ux
            else: return False
        else:
            self.UX_ += new_ux
    
    def updateName(self, new_name):
        if (len(new_name) > 0):
            self.name = new_name
            return True
        else: return False

    def updatePassword(self, curr_password, new_password):
        if curr_password == self.password:
            if self.password == new_password:
                self.password = new_password
                return True
            else: return False
        else: return False
        
    def updateUsername(self, new_username):
#datab = pd.read_excel("user_data.xlsx")
        if new_username != self.username & len(new_username):
            self.username = new_username
            return True
        else: return False

        
