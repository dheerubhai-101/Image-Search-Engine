# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 11:04:32 2021

@author: tech crusaders
"""

import cv2 as cv
import os
import numpy as np
import csv
import matplotlib.pyplot as plt
import matplotlib.image as img
def rgb_histo(image):
 
    histo= cv.calcHist([image],[0],None,[256],[0,256])
    fv=np.array(histo)
    for i in range(1,3):
        histo= cv.calcHist([image],[i],None,[256],[0,256])
        fv=np.append(fv,histo,0)    
    return fv

file="Images.csv"
def load_images_from_folder(folder):
    images=[]
    for filename in os.listdir(folder):
        image = img.imread(os.path.join(folder,filename))
        if image is not None:
            images.append(image)
    return images



folder='Task 2 Image Dataset'
images=load_images_from_folder(folder)
plt.imshow(images[0])
plt.show()

database="Database2.csv"

def histo_data(folder):
    for filename in os.listdir(folder):
        image = cv.imread(os.path.join(folder,filename))
        if image is not None:
            fv=rgb_histo(image)
            np.save(database,fv)
        
    


#histo_data(folder)
def csv_database(folder):
    with open(database,'w') as csvfile:
        for filename in os.listdir(folder):
            image = img.imread(os.path.join(folder,filename)) 
            loc = (os.path.join(folder,filename))
            fv=rgb_histo(image)
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(fv)
            

csv_database(folder)


    

