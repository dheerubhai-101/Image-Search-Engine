# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 11:34:35 2021

@author: tech crusaders
"""

import cv2 
import os
import matplotlib.image as img
import matplotlib.pyplot as plt
import csv
import numpy as np



image=img.imread('sp1.jpg')
#image = plt.imread('sp1.jpg') #reads image data
#image= cv.imread('sp1.jpg',0)


def rgb_histo(image):
    fv=[]
    for i in range(0,3): 
        histo= cv2.calcHist([image],[i],None,[256],[0,256])
        print(histo.shape)
        fv.append(histo)
    fv=np.array(fv)
    np.concatenate(fv,)
    return fv
    
    
    
vector=rgb_histo(image)
for i in range(0,3):    
    plt.plot(vector[i])
    plt.show()

image2=img.imread('sp1.jpg')
vector2=rgb_histo(image2)

p = cv2.compareHist(vector[0], vector2[0] ,cv2.HISTCMP_BHATTACHARYYA)


if p>0.9 :

 print("same")
   

img_template_probability_match = cv2.matchTemplate(vector[0],vector2[0], cv2.TM_CCOEFF_NORMED)[0][0]
print(p)

# show the plotting graph of an image
plt.plot(vector[0])
plt.show
#plt.imshow(img)
plt.plot(vector2[0])
plt.show()