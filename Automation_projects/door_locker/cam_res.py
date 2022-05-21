from tkinter import image_names
import cv2
from aws_connection import *
import time
import datetime  
import logging
logging.basicConfig(filename='logs\general_log.log', level=logging.DEBUG, format='%(asctime)s.%(msecs)03d %(levelname)s ====: %(message)s =;',
    datefmt='%Y-%m-%d %H:%M:%S',)

def getPic():
    try:
        cam = cv2.VideoCapture(0) 
        now = datetime.datetime.now()
        actual_time = "{}-{}-{}_{}-{}-{}".format(now.year, now.month, now.day, now.hour, now.minute, now.second)
        img_name = "img\{}.png".format(actual_time)   
        ret, frame = cam.read()
        
        cv2.imwrite(img_name, img = frame)
        time.sleep(1)
        cam.release()
        cv2.destroyAllWindows()
        if getReckres(actual_time):
            return(True)

        logging.info("Uma foto foi registrada pelo equipamento")
        name = "NM"
        permition = True
        return(img_name, name, permition)
    except:
        logging.info("Um erro ocorreu na câmera")
        return(False)

getPic()
