#image_processing.py

import cv2 as cv
import numpy as np

def image_processing_1(image_name,image_path):
    #讀取照片原圖
    img = cv.imread(image_path)
    
    #將原圖轉為灰階圖
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    
    #將灰階圖進行二值化處理
    ret,binary=cv.threshold(gray,127,255,cv.THRESH_BINARY)

    #將二值化的圖片放到
    contours,hierarchy = cv.findContours(binary,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)

    #首先複製原圖
    copy = img.copy()

    #建立空白圖片
    empty = np.ones(img.shape,dtype=np.uint8)*255

    #將輪廓描繪在複製圖上
    # copy = cv.drawContours(copy,contours,-1,(255,0,0),2)
    copy = cv.drawContours(empty,contours,-1,(255,0,0),2)

    #將複製圖存實體檔案
    contour_image_path = './static/contour.png'
    cv.imwrite(contour_image_path,copy)

    #將灰階圖與二值化處理圖存為實體檔案
    gray_path = './static/gray_'+image_name
    binary_path = './static/binary_'+image_name

    cv.imwrite(gray_path,gray)
    cv.imwrite(binary_path,binary)

    return gray_path, binary_path, contour_image_path