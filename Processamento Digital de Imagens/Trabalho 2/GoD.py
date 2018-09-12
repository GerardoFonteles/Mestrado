# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 09:49:56 2018

@author: JoseGerardo
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 15:44:05 2018

@author: Labvis
"""

# -*- coding: utf-8 -*-
"""
Created on Tue May 16 13:23:32 2017

@author: Labvis
"""
import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.color import rgb2grey 
from skimage import filters
import numpy as np
from scipy.ndimage.filters import gaussian_laplace
from scipy.ndimage.filters import gaussian_filter



#Leitura das imagens
cameraman = imread('C:/Users/Labvis/Dropbox/mestrado/Processamento Digital de Imagens/Trabalho1/crowd1.jpg')

#Converte a imagem para níveis de cinza
lena = rgb2grey(np.asarray(cameraman))*np.max(cameraman)

i = 6
lena_filtrada = np.zeros((lena.shape[0],lena.shape[1],i))
lena_filtrada2 = np.zeros((lena.shape[0],lena.shape[1],i)) 

for k in range(6):  
    lena_filtrada[:,:,k] = lena - gaussian_filter(lena, 1*k)
    plt.figure(k)
    plt.axis('off')
    plt.imshow(lena_filtrada[:,:,k],cmap = "gray")
    


