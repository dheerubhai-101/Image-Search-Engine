# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 17:28:22 2021

@author: tech crusaders
"""

import cv2 as cv
import matplotlib.image as img
import matplotlib.pyplot as plt

import numpy as np

a1=np.array([1,2])
a2=np.array([2])
a3=np.array([3])

image=img.imread('sp1.jpg')

def rgb_histo(image):
 
    histo= cv.calcHist([image],[0],None,[256],[0,256])
    fv=np.array(histo)
    for i in range(1,3):
        histo= cv.calcHist([image],[i],None,[256],[0,256])
        fv=np.append(fv,histo,0)    
    return fv


vector=rgb_histo(image)
print(vector.shape)
plt.plot(vector)
plt.show()

image2=img.imread('sp6.jpg')
vector2=rgb_histo(image2)
p = cv.compareHist(vector, vector2 ,cv.HISTCMP_BHATTACHARYYA)
 
 
if p<0.3 :
     print(p)
     print("same")
    
 
p = cv.compareHist(vector, vector2 ,cv.HISTCMP_CORREL)
print(p)
 
