# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 16:46:44 2018

@author: ZZ
"""

import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import time
X=[]
Y=[]
ID=[]
Date=[]
a=0
b=90
cap = cv2.VideoCapture("rtsp://admin:pjesfs;sn@192.168.11.221/streaming/channels/101")

dictionary_name = cv2.aruco.DICT_4X4_250
dictionary = cv2.aruco.getPredefinedDictionary(dictionary_name)

while True:
    a=a+1
    ret,frame = cap.read()
    ret,frame = cap.read()
    ret,frame = cap.read()
    ret,frame = cap.read()
    ret,frame = cap.read()
    ret,frame = cap.read()
    ret,frame = cap.read()
    if(np.shape(frame)[0]!=0):
        
        corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(frame, dictionary)
        frame = cv2.aruco.drawDetectedMarkers(frame, corners, ids)
        if corners and ids[0]==1:
            #print(corners[0][0][0][0])
            X.append(corners[0][0][0][0])
            Y.append(corners[0][0][0][1])
            ID.append(ids[0])
            Date.append(time.ctime())
        cv2.namedWindow("1",0)
        cv2.resizeWindow("1",1280,720)
        cv2.imshow('1', frame)
        if a==50:
            plt.xlim(0,1920)  
            plt.ylim(0,1080)  
            plt.plot(X,Y)
            plt.axis('off')
            plt.savefig("d:/position/1/pic/"+str(b)+".jpg")
            plt.close()
            temp={"Time":Date,"ID":ID,"X":X,"Y":Y}
            data=pd.DataFrame(temp)
            data.to_csv("d:/position/1/csv/"+str(b)+".csv",index="False")
            b=b+1
            a=0
            X=[]
            Y=[]
            Date=[]
            ID=[]
        if b==100:
            break;
        k = cv2.waitKey(1)
        if k == 27:
            break
cap.release()
cv2.destroyAllWindows()