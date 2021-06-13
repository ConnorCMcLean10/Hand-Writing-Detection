import cv2
import numpy as np
from Utilities import *

img = cv2.imread('handwriting.jpg')
img = refactor(img)
