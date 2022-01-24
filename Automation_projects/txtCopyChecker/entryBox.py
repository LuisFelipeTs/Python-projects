from tkinter import *

def boxE(user_imput, calc_output):
    INPUT = user_imput.get("1.0", "end-1c")
    if(INPUT == "120"):
        calc_output.insert(END, 'Correct')
    else:
        calc_output.insert(END, "Wrong answer")
