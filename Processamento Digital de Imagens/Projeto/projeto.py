# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 16:30:07 2018

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
from skimage.measure import compare_ssim as ssim
from sklearn.metrics import mean_squared_error
from copy import deepcopy
from glob import glob
from skimage import io
from scipy.misc import imsave 

pasta = 'Alprazolam'
pasta = 'Domino'
pasta = 'Tesla'
pasta = 'Medium cut'
pasta = 'Warner Bros'
imagens = glob('C:/Users/Labvis/Desktop/SIIM/'+pasta+'/*.jpg')
mask = glob('C:/Users/Labvis/Desktop/SIIM/'+pasta+'/*.png')
directory = 'C:/Users/Labvis/Desktop/SIIM/resultados_seg'+pasta
names = os.listdir('C:/Users/Labvis/Desktop/SIIM/'+pasta+'/')

n = len(imagens)

#Cria o diretorio de resultados
if not os.path.exists(directory):
    os.makedirs(directory)

#Leitura das imagens
for k in range(n):    
    im = imread(mask[k])
    im = im.astype('bool')
    im = im.astype('int')
    im2 = imread(imagens[k])
    seg = im*im2
    imsave(directory+'/'+names[2*k+1],seg)
    #print(mask[k],imagens[k],names[2*k+1])


#Converte as imagens emtons de cinzas
#grey_image = rgb2grey(im)
#grey_image2 = rgb2grey(im2)

#seg

#seg = seg.astype(int)
#plt.imshow(seg,cmap = 'gray')

