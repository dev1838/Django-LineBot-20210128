#image_read.py
import cv2 as cv 
import numpy as np 

#version A
img = cv.imread('./test.jpg')
print(img)

#version B
a = img[0,0]
b = img[1,1]
c = img[2,0:3]

print('a=\n',a)
print('b=\n',b)
print('c=\n',c)