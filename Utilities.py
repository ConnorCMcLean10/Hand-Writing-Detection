import cv2
from win32api import GetSystemMetrics
from PIL import Image
import numpy as np

def refactor(writing):
    print("Priming Image...")
    image = cv2.cvtColor(writing, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image, (GetSystemMetrics(0), GetSystemMetrics(1)))
    se = cv2.getStructuringElement(cv2.MORPH_RECT, (8, 8))
    bg = cv2.morphologyEx(image, cv2.MORPH_DILATE, se)
    out_gray = cv2.divide(image, bg, scale=255)
    ret,img = cv2.threshold(out_gray, 125, 255,cv2.THRESH_BINARY) #125 works better for pen, 175 for pencil

    showImg(img)
    #drawHoriLines(img)

    return img

def showImg(img):       #testing method
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def drawHoriLines(writing):
    img = cv2.cvtColor(writing, cv2.COLOR_BGR2RGB)
    PIL_img = Image.fromarray(img)

    pixArray = np.asarray(writing)
    for row in range(len(pixArray)):
        if(not search(pixArray[row], 0)):
            for i in range(len(pixArray[row])):
                pixArray[row][i] = 0
    showImg(pixArray)


def search(array, value):
    for i in array:
        if (i == value):
            return True
    return False
