import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img1 = cv.imread('1.png')
img2 = cv.imread('2.png')
if img2 is not None:
    orb = cv.ORB_create()
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)
    bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1,des2)
    matches = sorted(matches, key = lambda x:x.distance)
    img3 = cv.drawMatches(img1,kp1,img2,kp2,matches[:5],None,flags=2)
    plt.imshow(img3)
    plt.title('MATCHES')
    plt.axis('off')
    print("About to show image...")
    plt.show()
    print("Image window closed.")
else:
    print("Error: Could not load image '1.png'. Please check the file path and format.")
