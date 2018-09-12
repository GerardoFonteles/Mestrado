# -*- coding: utf-8 -*-
"""
Created on Mon May  7 09:48:55 2018

@author: Labvis
"""

import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.color import rgb2grey 
from skimage import filters
import numpy as np
from scipy.fftpack import fft, ifft
import matplotlib.patches as mpatches
from scipy import  ndimage
from PIL import Image
import os
from wavelet import *
from skimage.measure import compare_ssim as ssim
from sklearn.metrics import mean_squared_error
from copy import deepcopy


cameraman = imread('C:/Users/Labvis/Dropbox/mestrado/Processamento Digital de Imagens/Trabalho1/cameraman.jpg')
#cameraman = imread('C:/Users/Labvis/Dropbox/mestrado/Processamento Digital de Imagens/Trabalho1/lenna.jpg')




plt.figure()
plt.title("Original")
plt.imshow(cameraman,cmap='gray')
plt.axis('off')

h = cameraman.shape[0]

cameraman = cameraman/h
#
test = wavelet2D(np.copy(cameraman))
reconstruido = recompor2D(np.copy(test))


#
plt.figure()
plt.title("Wavelet Test")
plt.axis('off')
plt.imshow(test.T,cmap = "gray")
#
plt.figure()
plt.title("Reconstruido")
plt.axis('off')
plt.imshow(reconstruido,cmap = "gray")

compressado = compress2D(np.copy(test))

reconstruido_comp = recompor2D(np.copy(compressado))

plt.figure()
plt.title("Reconstruido")
plt.axis('off')
plt.imshow(reconstruido_comp,cmap = "gray")

error = mean_squared_error(cameraman,reconstruido)
#ssim = ssim(cameraman,reconstruido)


###########################################
plt.figure()
plt.title("Nível 1")
plt.axis('off')
plt.imshow(test.T,cmap = "gray")

decomp = test
h = int(h/2)
decomp2 = wavelet2D(test[0:h,0:h])


plt.figure()
plt.title("Nível 2")
plt.axis('off')
plt.imshow(decomp2,cmap = "gray")
#
h = int(h/2)
decomp3 = wavelet2D(decomp2[0:h,0:h])

plt.figure()
plt.title("Nível 3")
plt.axis('off')
plt.imshow(decomp3.T,cmap = "gray")
#
h = int(h/2)
decomp4 = wavelet2D(decomp3[0:h,0:h])

plt.figure()
plt.title("Nível 4")
plt.axis('off')
plt.imshow(decomp4,cmap = "gray")

#########################################
recupe4 = compress(decomp4)
recuperar2D = recompor2D(recupe4)

decomp3[0:h,0:h] = recuperar2D
       
plt.figure()
plt.title("Nível 5")
plt.axis('off')
plt.imshow(decomp3.T,cmap = "gray")
       
recuperar2D = recompor2D(decomp3)    

decomp2[0:2*h,0:2*h] = recuperar2D
       
plt.figure()
plt.title("Nível 6")
plt.axis('off')
plt.imshow(decomp2,cmap = "gray")
       
recuperar2D = recompor2D(decomp2) 

decomp[0:4*h,0:4*h] = recuperar2D
      
decomp = recompor2D(decomp)

plt.figure()
plt.title("Truncado")
plt.axis('off')
plt.imshow(decomp,cmap = "gray")

error2 = mean_squared_error(cameraman,decomp)
ssim2 = ssim(cameraman,decomp)


########################################
      


#########################################

#########################################

signal = np.array([9.0,7,3,5])
aux = Haar(signal)
Haar2 = Haar(signal)
teste = recomporHaar(np.copy(aux))
