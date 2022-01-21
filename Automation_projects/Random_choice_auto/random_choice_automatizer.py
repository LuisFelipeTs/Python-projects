import random
import pyautogui
import time
import tkinter as tk
from tkinter import simpledialog

tktk_v = tk.Tk()
tktk_v.withdraw()
options = simpledialog.askstring(title="Random choice",
                                  prompt="What's your options?(Like: opt1, opt2, opt3)")
link_choice =options.split(",")
webchoice = random.choice(link_choice)  
print(webchoice)
pyautogui.press('winleft')
time.sleep(1)
pyautogui.write('edge')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.hotkey('alt','space')
pyautogui.press('x')
time.sleep(1.5)
pyautogui.write(webchoice)
pyautogui.press('enter')
time.sleep(2)

