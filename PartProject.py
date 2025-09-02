import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

#  Priority list and colours
shape_priority = {'star' : 3 , 'triangle' : 2 , 'square' : 1}
emergency_priority = {'red' : 3, 'yellow' : 2, 'green' : 1}
camp_colors_bgr = {'blue': (136,176,255), 'pink':(230,161,255), 'gray':(221,218,218)}
camp_capacity = {'blue':4, 'pink':3, 'gray':2}

# -----------x---------------x-----------x------------x----------x-----------------
img = cv.imread('1.png')
if img is not None: 
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# ocean and land
ocean_mask = cv.inRange(hsv, (100, 60, 60), (130, 255, 255))
land_mask = cv.inRange(hsv, (35, 50, 50), (90, 255, 255))
segmented = img.copy()
segmented[ocean_mask > 0] = (255, 140, 80)
segmented[land_mask > 0] = (50, 255, 150)
cv.imwrite("segmented_1.png", segmented)

cv.imshow('segemented', segmented)
cv.waitKey(0)
cv.destroyAllWindows()
