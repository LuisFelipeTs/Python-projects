from tkinter import *
from wsgiref import validate
from checker import checkText_wk , checkText_dc
import time

def boxE(user_imput, calc_output):
    calc_output.delete("1.0", "end")
    INPUT = user_imput.get("1.0", "end-1c")
    u_imp = str(INPUT)
    output_txt, validation = checkText_wk(u_imp)
    
    if(validation):
        calc_output.insert(END, output_txt)
    else:
        calc_output.insert(END, "The Word that was added is incorrect or doesn't exists")
    
