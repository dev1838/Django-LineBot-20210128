#superpix.py

import cv2
import numpy as np 

domain = 'https://c74f160c6d3f.ngrok.io'#這邊需要置換成自己的ngrok domain

#SLIC運算法
def SLIC(image_name,image_path):

    img = cv2.imread(image_path)
    #設定SLIC初始化設定，超像素平均尺寸20(默認為10)，平滑參數為20
    slic = cv2.ximgproc.createSuperpixelSLIC(img,region_size=20,ruler = 20.0) 
    slic.iterate(10)     #迭代次數，跌代越多次，則超像素分離的效果越好
    mask_slic = slic.getLabelContourMask() #建立超像素的遮罩，mask_slic數值為1
    label_slic = slic.getLabels()        #獲得超像素的標籤
    number_slic = slic.getNumberOfSuperpixels()  #獲得超項素的數量
    mask_inv_slic = cv2.bitwise_not(mask_slic)  
    img_slic = cv2.bitwise_and(img,img,mask =  mask_inv_slic) #在原圖中繪製超像素邊界
    cv2.imwrite('./static/SLIC.png',img_slic)    #將繪製邊界的圖片儲存
    return domain+'/static/SLIC.png'

#SEEDS運算法
def SEEDS(image_name,image_path):
    img = cv2.imread(image_path)
    #建立SEEDS初始化設定
    seeds = cv2.ximgproc.createSuperpixelSEEDS(img.shape[1],img.shape[0],img.shape[2],2000,15,3,5,True)
    seeds.iterate(img,10)  #以原圖進行SEEDS處理，設定迭代次數為10次
    mask_seeds = seeds.getLabelContourMask()
    label_seeds = seeds.getLabels()
    number_seeds = seeds.getNumberOfSuperpixels()
    mask_inv_seeds = cv2.bitwise_not(mask_seeds)
    img_seeds = cv2.bitwise_and(img,img,mask =  mask_inv_seeds)
    cv2.imwrite('./static/SEED.png',img_seeds)
    return domain+'/static/SEED.png'

#LSC運算法
def LSC(image_name,image_path):
    img = cv2.imread(image_path)
    #設定LSC初始化設定
    lsc = cv2.ximgproc.createSuperpixelLSC(img)
    lsc.iterate(10)#設定迭代次數
    mask_lsc = lsc.getLabelContourMask()
    label_lsc = lsc.getLabels()
    number_lsc = lsc.getNumberOfSuperpixels()
    mask_inv_lsc = cv2.bitwise_not(mask_lsc)
    img_lsc = cv2.bitwise_and(img,img,mask = mask_inv_lsc)
    cv2.imwrite('./static/LSC.png',img_lsc)
    return domain+'/static/LSC.png'