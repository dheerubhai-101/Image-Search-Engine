# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 08:03:07 2021

@author: tech crusaders
"""

import cv2 as cv
import matplotlib.image as img
import matplotlib.pyplot as plt
import csv
import numpy as np
import os

#histogram feature vector
def rgb_histo(image):
 
    histo= cv.calcHist([image],[0],None,[256],[0,256])
    fv=np.array(histo)
    for i in range(1,3):
        histo= cv.calcHist([image],[i],None,[256],[0,256])
        fv=np.append(fv,histo,0)    
    return fv

folder='Task 2 Image Dataset'

def load_paths_from_folder(folder):
    images=[]
    for filename in os.listdir(folder):
        path = (os.path.join(folder,filename))
        if path is not None:
            images.append(path)
    return images


location="Locations.csv"



print("Input name of the image to be searched: ")
name=input()+'.jpg'
q_img= img.imread(name)
plt.imshow(q_img)
plt.show()

q_vec=rgb_histo(q_img)

plt.plot(q_vec)
plt.show()
print(q_vec[0])


with open(location,'r') as csvlocation:
    with open("Database.csv",'r') as csvfile:
         sim_im={}
         csvreader= csv.reader(csvfile)
         csvloc= csv.reader(csvlocation)
         c_vec= next(csvreader)
         path= next(csvloc)
         images=[]
         for row in csvreader :
             
             c_vec=row
             c_vec=[float(s[1:-1]) for s in c_vec]
             c_vec=np.array(c_vec)
             c_vec=c_vec.astype(np.float32)
             c_vec.shape=(768,1)
             p = cv.compareHist(c_vec, q_vec ,cv.HISTCMP_BHATTACHARYYA)
             q = cv.compareHist(q_vec, c_vec ,cv.HISTCMP_CORREL)
             path= next(csvloc)
             if p<0.238 or q>0.88:
                 
                 images.append(path[0])
                 sim_im[q]=c_vec
                 
         
csvfile.close()
#dictionary of similar images
print(sim_im.keys())


for s in images:
    pic= img.imread(s)
    plt.imshow(pic)
    plt.show()
         
         
    
 
     
    
 
     
     
         
         
         
         
         
         
         
         
         
         
         
         
         
         
   