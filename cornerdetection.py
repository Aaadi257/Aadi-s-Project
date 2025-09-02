import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('1.png')
if img is not None:
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    corners = cv.goodFeaturesToTrack(gray, 40, 0.01, 10)
    corners = corners.astype(int)
    for corner in corners:
        x, y = corner.ravel()
        cv.circle(img, (x, y), 5, (0, 0, 255), -1) 
    # Converted BGR to RGB for matplotlib
    img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    plt.imshow(img_rgb)
    plt.title('Corners')
    plt.axis('off')
    print("About to show image...")
    plt.show()
    print("Image window closed.")
else:
    print("Error: Could not load image '1.png'. Please check the file path and format.")
