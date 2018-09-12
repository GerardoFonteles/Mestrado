# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 11:28:14 2018

@author: Labvis
"""

import numpy as np
import cv2
from skimage.color import rgb2grey
from skimage.feature import greycomatrix, greycoprops,local_binary_pattern
from skimage.io import imread, show, imshow
import glob as g
import matplotlib.pyplot as plt
import os
from scipy.stats import itemfreq




def descritor():

    Alprazolam = g.glob("C:/Users/Labvis/Desktop/SIIM/resultados_segAlprazolam/*.png")
    Domino = g.glob("C:/Users/Labvis/Desktop/SIIM/resultados_segDomino/*.png")
    Medium = g.glob("C:/Users/Labvis/Desktop/SIIM/resultados_segMedium cut/*.png")
    Tesla = g.glob("C:/Users/Labvis/Desktop/SIIM/resultados_segTesla/*.png")
    Warner = g.glob("C:/Users/Labvis/Desktop/SIIM/resultados_segWarner Bros/*.png")   
    
    radius = 3
    no_points = 8*radius
    #d = 1
    #l = []
    for i, value in enumerate(Alprazolam):
        image = cv2.imread(value, 0)
        im_gray = rgb2grey(image)
        
        lbp = local_binary_pattern(im_gray, no_points, radius, method='uniform')
        x = itemfreq(lbp.ravel())
        hist = x[:, 1]/sum(x[:, 1])
        
        file_save(hist, '0')
        
        print('Alprazolam ->', hist)

    for i, value in enumerate(Domino):
        image = cv2.imread(value, 0)
        im_gray = rgb2grey(image)
        
        lbp = local_binary_pattern(im_gray, no_points, radius, method='uniform')
        x = itemfreq(lbp.ravel())
        hist = x[:, 1]/sum(x[:, 1])
        
        file_save(hist, '1')
        
        print('Domino ->', hist)
      
    for i, value in enumerate(Medium):
        image = cv2.imread(value, 0)
        im_gray = rgb2grey(image)
        
        lbp = local_binary_pattern(im_gray, no_points, radius, method='uniform')
        x = itemfreq(lbp.ravel())
        hist = x[:, 1]/sum(x[:, 1])
        
        file_save(hist, '2')  # one
        print('Medium ->', hist)
        
    for i, value in enumerate(Tesla):
        image = cv2.imread(value, 0)
        im_gray = rgb2grey(image)
        
        lbp = local_binary_pattern(im_gray, no_points, radius, method='uniform')
        x = itemfreq(lbp.ravel())
        hist = x[:, 1]/sum(x[:, 1])
        
        file_save(hist, '3')  # one
        print('Tesla ->', hist)  

    for i, value in enumerate(Warner):
        image = cv2.imread(value, 0)
        im_gray = rgb2grey(image)
        
        lbp = local_binary_pattern(im_gray, no_points, radius, method='uniform')
        x = itemfreq(lbp.ravel())
        hist = x[:, 1]/sum(x[:, 1])
        
        file_save(hist, '4')  # one
        print('Warner ->', hist)
    

    return lbp

def file_save(vetor, label):

    file = open('validation_001_lbp.libsvm', 'a+')
    file.write(str(label)+" "+" ".join(str(i+1)+":"+str(pix) for i, pix in enumerate(vetor))+"\n")
    file.close()


if __name__ == '__main__':
    lbp = descritor()
    print("arroz");
