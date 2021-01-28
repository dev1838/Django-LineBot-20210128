#image_calculator.py
from cv2 import cv2 as cv 
import numpy as np

# Version 1
# image_path = './test.png'
# img = cv.imread(image_path,0)
# print(img)
# img2 = np.ones(img.shape,dtype=np.uint8)*30
# print(img2)
# img3 = cv.add(img,img2)
# print(img3)
# cv.imwrite('./V1.png',img)
# cv.imwrite('./V1.2.png',img2)
# cv.imwrite('./V1.3.png',img3)

#Version 2
# img = cv.imread('./Mcdonald.jpg')
# img2 = cv.imread('./burgerking.jpg')
# img3 = cv.add(img,img2)
# cv.imwrite('./V2.png',img)
# cv.imwrite('./V2.2.png',img2)
# cv.imwrite('./V2.3.png',img3)

#Version 3
img = cv.imread('./Mcdonald.jpg')
img2 = cv.imread('./burgerking.jpg')
img3 = cv.addWeighted(img,0.8,img2,0.2,0)
cv.imwrite('./V3.png',img)
cv.imwrite('./V3.2.png',img2)
cv.imwrite('./V3.3.png',img3)