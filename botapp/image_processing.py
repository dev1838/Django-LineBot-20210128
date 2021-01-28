#image_processing.py

import cv2 as cv
import numpy as np

def image_processing_1(image_name,image_path):
    #讀取照片原圖
    img = cv.imread(image_path)
    
    #將原圖轉為灰階圖
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    
    #將灰階圖進行二值化處理
    ret,binary=cv.threshold(gray,220,255,cv.THRESH_BINARY)

    #將二值化的圖片放到
    contours,hierarchy = cv.findContours(binary,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)

    #首先複製原圖
    copy = img.copy()

    #建立空白圖片
    empty = np.ones(img.shape,dtype=np.uint8)*255

    total_area = img.shape[0]*img.shape[1]
    font = cv.FONT_HERSHEY_PLAIN #設定cv字型

    n = len(contours)
    for i in range(n):
        M = cv.moments(contours[i])
        area = M['m00']
        if area/total_area>0.001 and area/total_area<0.800:#若面積大於總面積的15%且小於50%
            #將輪廓描繪在複製圖上
            mask = np.zeros(gray.shape,dtype=np.uint8)
            cv.drawContours(mask,contours[i],-1,(255,255,255),-1)
            meanVal = cv.mean(img,mask=mask) #mask是一個區域，所以必須是單通道的
            if meanVal[2]>meanVal[1] and meanVal[2]>meanVal[1]:
                print(meanVal)#將輪廓中的平均數值print出來
                if abs(meanVal[2]-meanVal[1])>20:#若紅色與綠色絕對值差20以上
                    copy = cv.drawContours(img,contours[i],-1,(0,0,255),2)#將輪廓繪製到空白底圖中

    #將複製圖存實體檔案
    contour_image_path = './static/contour.png'
    cv.imwrite(contour_image_path,copy)

    #將灰階圖與二值化處理圖存為實體檔案
    gray_path = './static/gray_'+image_name
    binary_path = './static/binary_'+image_name

    cv.imwrite(gray_path,gray)
    cv.imwrite(binary_path,binary)

    return gray_path, binary_path, contour_image_path