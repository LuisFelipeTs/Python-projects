import cv2
from aws_connection import *
import time
import datetime  
import logging
logging.basicConfig(filename='logs\general_log.log', level=logging.DEBUG, format='%(asctime)s.%(msecs)03d %(levelname)s ====: %(message)s =;',
    datefmt='%Y-%m-%d %H:%M:%S')

def getPic(analyse):
    try:
        cam = cv2.VideoCapture(0) 
        now = datetime.datetime.now()
        actual_time = "{}-{}-{}_{}-{}-{}".format(now.year, now.month, now.day, now.hour, now.minute, now.second)
        img_name = "img/{}.png".format(actual_time)   
        ret, frame = cam.read()
        
        cv2.imwrite(img_name, img = frame)
        time.sleep(1)
        cam.release()
        cv2.destroyAllWindows()
        if analyse:
            res1, res2 = getReckres(img_name)
            if res2:
                logging.info("Análise realizada.")
                return(img_name, res1)
                
            else:
                logging.info("Ninguém foi reconhecido em câmera")
                return(img_name, False)
        sendImgS3(img_name, 'test')
        return(img_name, False)
    except:
        print(9)
        logging.info("Um erro ocorreu na câmera")
        return("error", False)

#getPic(False)
