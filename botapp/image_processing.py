#image_processing.py

import cv2 as cv
import numpy as np

def image_processing_1(image_name,image_path):
    #讀取照片原圖
    img = cv.imread(image_path)
    
    #將原圖轉為灰階圖
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    
    #將灰階圖進行二值化處理
    ret,binary=cv.threshold(gray,200,255,cv.THRESH_BINARY)

    #將二值化的圖片放到
    contours,hierarchy = cv.findContours(binary,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)  

    #首先複製原圖
    copy = img.copy()

    #建立空白圖片
    empty = np.ones(img.shape,dtype=np.uint8)*255

    total_area = img.shape[0]*img.shape[1]
    font = cv.FONT_HERSHEY_DUPLEX #text type
    n = len(contours)
    for i in range(n):
        M = cv.moments(contours[i])
        area = M['m00']
        if area/total_area>0.15 and area/total_area<0.50:#若面積大於總面積的15%且小於50%
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            center = tuple((cx,cy))
            if cx>img.shape[1]*0.25 and cx<img.shape[1]*0.75:
                cv.putText(empty,'. no.='+str(i),center,font,2,(0,0,255),1)
                print('輪廓編號%d，面積大小%d，中心點%s'%(i,area,str(center)))      
                #將輪廓描繪在複製圖上
                copy = cv.drawContours(empty,contours[i],-1,(255,0,0),2)

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