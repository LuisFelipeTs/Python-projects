#Function adapted from https://www.foxinfotech.in/2019/01/alert-message-box-in-python-using-tkinter.html
from tkinter import messagebox

def alert(title, message, kind):
    if kind not in ('error', 'warning', 'info'):
        raise ValueError('Unsupported alert kind.')
    show_method = getattr(messagebox, 'show{}'.format(kind))
    show_method(title, message)
#---------------------------------------------------------------------------------