print("HELLO DEBUG")
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

print("Image loaded, displaying window...")
img = cv.imread('1.png', cv.IMREAD_COLOR)
if img is not None:
   cv.line(img, (0, 0), (200, 200), (0, 0, 0), 5)
   cv.rectangle(img, (0, 0), (200, 200), (0, 0, 0), 5)
   font = cv.FONT_HERSHEY_SIMPLEX
   cv.putText(img, 'Hello' , (0,200), font, 5, (255,0,0), 10 , cv.LINE_AA)
   plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
   plt.title('UAV')
   plt.show()
   cv.destroyAllWindows()
