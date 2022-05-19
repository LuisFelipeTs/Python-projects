import cv2
import time

import logging
logging.basicConfig(filename='logs\general_log.log', level=logging.DEBUG, format='%(asctime)s.%(msecs)03d %(levelname)s ====: %(message)s =;',
    datefmt='%Y-%m-%d %H:%M:%S',)



def getPic(img_name):
    cam = cv2.VideoCapture(0)
    logging.info("Uma foto foi registrada pelo equipamento")
    #cv2.namedWindow("test")
        
    ret, frame = cam.read()
    time.sleep(1)
    cv2.imwrite(img_name, img = frame)
    cam.release()

    cv2.destroyAllWindows()

getPic("img/first_img_test.png")
