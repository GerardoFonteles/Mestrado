# -*- coding: utf-8 -*-
"""
Created on Sat May 19 09:22:09 2018

@author: JoseGerardo
"""

import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.color import rgb2grey 
from skimage import filters
import numpy as np
from scipy.fftpack import fft, ifft
import matplotlib.patches as mpatches
from scipy import  ndimage
from scipy import  signal
from PIL import Image
import os
from wavelet import *
from skimage.measure import compare_ssim as ssim
from sklearn.metrics import mean_squared_error
from copy import deepcopy

cameraman = imread('C:/Users/JoseGerardo/Dropbox/mestrado/Processamento Digital de Imagens/Trabalho1/lenna.jpg')
n=4

#mask = np.array([[1/4,0,0,0,0,0,0,1/2,0,0,0,0,0,0,1/4]])
mask = np.array([[1/4,0,0,1/2,0,0,1/4]])
mask = np.kron(mask,mask.T)

wavelet = signal.convolve2d(cameraman,mask)
#test = wavelet[1:-1,1:-1]
#wavelet = wavelet[len(cameraman),len(cameraman)]
#
#detalhes = cameraman-wavelet
#
detalhes,wavelet = Atrous(cameraman,n)


plt.figure(1)
plt.imshow(cameraman,cmap = 'gray')
plt.axis('off')

for i in range(n):
    plt.figure()
    plt.imshow(detalhes[:,:,i],cmap = 'gray')
    plt.axis('off')

plt.figure()
plt.imshow(wavelet[:,:],cmap = 'gray')

plt.title('Wavelet Atrou.')
plt.axis('off')

recons = reconstruir(wavelet,detalhes)

test = recons.astype('uint8')
mse = mean_squared_error(test,cameraman)
ssim = ssim(test,cameraman)


