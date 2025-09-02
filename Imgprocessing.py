import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('1.png', cv.IMREAD_COLOR)
if img is not None:
   rows, cols, channels = img.shape
   imggray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
   ret, mask = cv.threshold(imggray, 100, 150, cv.THRESH_BINARY_INV)
   plt.imshow(mask, cmap='gray')
   plt.title('UAV Mask')
   plt.show()
else:
   print("Error: Could not load image '1.png'. Please check the file path and format.")
