# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 12:38:01 2018

@author: Labvis
"""

import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.color import rgb2grey 
from skimage import filters
import numpy as np
from scipy.ndimage.filters import gaussian_laplace

cameraman = imread('C:/Users/Labvis/Dropbox/mestrado/Processamento Digital de Imagens/Trabalho1/crowd1.jpg')
cameraman = imread('C:/Users/Labvis/Dropbox/mestrado/Processamento Digital de Imagens/Trabalho1/original.jpg')


lena = rgb2grey(np.asarray(cameraman))*np.max(cameraman)
lena_frenquencia = np.fft.fft2(lena)
lena_frenquencia2  = np.fft.fftshift(lena_frenquencia)

plt.figure()
plt.title("Crowd Original")
plt.axis('off')
plt.imshow(lena,cmap = "gray")

lenafft = np.fft.fft2(lena)
medio = np.mean(lena)
medio2 = np.abs(lenafft[0,0])/(lena.shape[0]*lena.shape[1])

plt.figure()
plt.title("Valor Absoluto")
plt.axis('off')
plt.imshow(np.log10(np.abs(lena_frenquencia2)),cmap = "gray")

