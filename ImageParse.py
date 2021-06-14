import cv2
import numpy as np
from PIL import Image
from Utilities import *
import pytesseract
from pytesseract import Output
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def generateBoxes(img):
    result = pytesseract.image_to_boxes(img, lang='eng', nice=0, output_type=pytesseract.Output.DICT)
    print(result)
    left = result['left'][0]
    bottom = result['bottom'][0]
    right = result['right'][0]
    top = result['top'][0]

    d = pytesseract.image_to_data(img, output_type=Output.DICT)
    n_boxes = len(d['level'])
    for i in range(n_boxes):
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        showImg(cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2))

    # showImg(img_box)
