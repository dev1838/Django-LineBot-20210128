#image_morphology.py

import cv2 as cv 
import numpy as np 

# V1
# img = cv.imread('apple2.jpg')
# kernel = np.ones((3,3),dtype=np.uint8)
# erosion = cv.erode(img,kernel)

# cv.imwrite('./erosion.jpg',erosion)

# V2
# img = cv.imread('apple2.jpg')
# kernel = np.ones((6,6),dtype=np.uint8)
# erosion = cv.erode(img,kernel)

# cv.imwrite('./erosion.jpg',erosion)

# V3
# img = cv.imread('apple2.jpg')
# kernel = np.ones((4,4),dtype=np.uint8)
# erosion = cv.erode(img,kernel)
# dilation = cv.dilate(erosion,kernel)

# cv.imwrite('./erosion.jpg',erosion)
# cv.imwrite('./dilation.jpg',dilation)

# V4
#讀取待處理圖片
img = cv.imread('grape.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret,binary = cv.threshold(gray,200,255,cv.THRESH_BINARY_INV)

#建立核結構
kernel = np.ones((8,8),dtype=np.uint8)

#開運算處理
opening = cv.morphologyEx(binary,cv.MORPH_OPEN,kernel)

#閉運算處理
closing = cv.morphologyEx(binary,cv.MORPH_CLOSE,kernel)

#梯度運算處理
gradient = cv.morphologyEx(binary,cv.MORPH_GRADIENT,kernel)

#禮帽運算處理
tophat = cv.morphologyEx(binary,cv.MORPH_TOPHAT,kernel)

#黑帽運算處理
blackhat = cv.morphologyEx(binary,cv.MORPH_BLACKHAT,kernel)

#禮帽+黑帽
twohat = cv.add(tophat,blackhat)

cv.imwrite('./binary.jpg',binary)
cv.imwrite('./opening.jpg',opening)
cv.imwrite('./closing.jpg',closing)
cv.imwrite('./gradient.jpg',gradient)
cv.imwrite('./tophat.jpg',tophat)
cv.imwrite('./blackhat.jpg',blackhat)
cv.imwrite('./twohat.jpg',twohat)

