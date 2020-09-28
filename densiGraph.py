# -*- coding: utf-8 -*-
"""
Created on Mon July 28 16:58:15 2020

@author: 周财霖
"""

import gdal
import numpy as np
import matplotlib.pyplot as plt

#Read Img
densi_img=gdal.Open('H:/FILE/luojia/shp/tk7.tif')
samples1=densi_img.RasterXSize
lines1=densi_img.RasterYSize
bands1=densi_img.RasterCount

#Convert to array
densi_arr=np.zeros([lines1,samples1])
densi_data=densi_img.GetRasterBand(1)
densi_arr[:,:]=densi_data.ReadAsArray(0,0,samples1,lines1)

#Set pixel area
pixel_area=2500
#Set the init threshold of Density
kd=1001

#first step
Num=np.size(densi_arr[densi_arr>kd])
area=Num*pixel_area
s1=pow(area,0.5)

#Main loop
i=0
d=kd
D=np.zeros([1001])
S=np.zeros([1001])
delta=np.zeros([1001])
while d>0:
    D[i]=d
    Num=np.size(densi_arr[densi_arr>d])
    area=Num*pixel_area
    S[i]=pow(area,0.5)
    
    if i==1:
        delta[i]=S[i]-s1;
    if i!=1:
        delta[i]=S[i]-S[i-1]
    i=i+1
    
    #the decreament could set greater to reduce loop times
    d=d-1

#Plot figure
plt.figure(figsize=(8,8))
plt.scatter(D,delta,marker=".",alpha=0.2)
plt.xlim(0,1000)
plt.ylim(0,100)
plt.tick_params(labelsize=20)
plt.xlabel('Kernel Density',{'size': 20})
plt.ylabel('Increment',{'size': 20})
plt.style.use('ggplot')
plt.show()

