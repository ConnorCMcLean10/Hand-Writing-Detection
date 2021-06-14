import cv2
import numpy as np
from Utilities import *
from ImageParse import *

img = cv2.imread('handwriting.jpg')
img = refactor(img)

generateBoxes(img)

