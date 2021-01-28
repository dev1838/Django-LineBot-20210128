#image_calculator.py
from cv2 import cv2 as cv 
import numpy as np

# Day 17

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

# Version 2
# img = cv.imread('./Mcdonald.jpg')
# img2 = cv.imread('./burgerking.jpg')
# img3 = cv.add(img,img2)
# cv.imwrite('./V2.png',img)
# cv.imwrite('./V2.2.png',img2)
# cv.imwrite('./V2.3.png',img3)

# Version 3
# img = cv.imread('./Mcdonald.jpg')
# img2 = cv.imread('./burgerking.jpg')
# img3 = cv.addWeighted(img,0.8,img2,0.2,0)
# cv.imwrite('./V3.png',img)
# cv.imwrite('./V3.2.png',img2)
# cv.imwrite('./V3.3.png',img3)

# Day 18

# version 1 cv2.bitwise_and()
# img = cv.imread('./apple.jpg')
# img2 = cv.imread('./android.jpg')
# img3 = cv.bitwise_and(img,img2) #逐位元and邏輯運算
# cv.imwrite('./Day18v1.png',img)
# cv.imwrite('./Day18v1.2.png',img2)
# cv.imwrite('./Day18v1.3.png',img3)

# version 2 cv2.bitwise_or()
# img = cv.imread('./apple.jpg')
# img2 = cv.imread('./android.jpg')
# img3 = cv.bitwise_or(img,img2)  #逐位元or邏輯運算
# cv.imwrite('./Day18v2.png',img)
# cv.imwrite('./Day18v2.2.png',img2)
# cv.imwrite('./Day18v2.3.png',img3)

# version 3 cv2.bitwise_not()
# img = cv.imread('./apple.jpg')
# img2 = cv.imread('./android.jpg')
# img3 = cv.bitwise_not(img)#逐位元not邏輯運算1
# img4 = cv.bitwise_not(img2)#逐位元not邏輯運算2
# cv.imwrite('./Day18v3.png',img)
# cv.imwrite('./Day18v3.2.png',img2)
# cv.imwrite('./Day18v3.3.png',img3)
# cv.imwrite('./Day18v3.4.png',img4)

# version 4 cv2.bitwise_xor()
# img = cv.imread('./apple.jpg')
# img2 = cv.imread('./android.jpg')
# img3 = cv.bitwise_xor(img,img2)#逐位元xor邏輯運算
# cv.imwrite('./Day18v4.png',img)
# cv.imwrite('./Day18v4.2.png',img2)
# cv.imwrite('./Day18v4.3.png',img3)

#version 5
img = cv.imread('./apple.jpg')
img2 = cv.imread('./android.jpg')
mask = np.zeros((img.shape[0],img.shape[1]),dtype=np.uint8)
mask[40:60,40:60]=255
img3 = cv.bitwise_and(img,img2,mask=mask)#逐位元and邏輯運算1
cv.imwrite('./Day18v5.png',img)
cv.imwrite('./Day18v5.2.png',img2)
cv.imwrite('./Day18v5.3.png',img3)
