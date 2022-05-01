import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def getImg(display=False, size=[480, 320]):
    _,Img = cap.read()
    Img = cv2.resize(Img, (480, 320))
    if display:
        cv2.imshow('VID', Img)
    return Img

if __name__ == '__main__':
    while True:
        Img = getImg(True)
        cv2.waitKey(1)