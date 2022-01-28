from ast import And
from tkinter import *
from wsgiref import validate
from checker import checkText_wk , checkText_dc
import time

def boxE(user_imput, calc_output):
    calc_output.delete("1.0", "end")
    INPUT = user_imput.get("1.0", "end-1c")
    u_imp = str(INPUT)
    out_wk , validation_wk = checkText_wk(u_imp)
    out_dc , validation_dc = checkText_dc(u_imp)
    print(validation_wk)
    print(validation_dc)

    if not (validation_wk and validation_dc ):
        calc_output.insert(END, "The Word that was added is incorrect or doesn't exists")
    else:
        out_end = genStrOut(u_imp , out_wk, validation_wk, out_dc, validation_dc)
        calc_output.insert(END, out_end)
    
def genStrOut(u_imp, out_wk, validation_wk, out_dc, validation_dc):
    if validation_wk == False: out_wk = "Nenhum resultado do Wikipedia"
    if validation_dc == False: out_dc = "Nenhum resultado do Dicio.com"

    out = '-------- {0} --------   \n *** WIKIPEDIA *** \n \n {1} \n\n *** Dicio.com *** \n \n {2} \n --------------------'.format(u_imp, out_wk, out_dc)
    return out


