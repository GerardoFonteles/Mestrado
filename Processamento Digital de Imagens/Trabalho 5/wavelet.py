# -*- coding: utf-8 -*-
"""
Created on Sun May  6 11:32:09 2018

@author: JoseGerardo
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 17:43:39 2018

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
from PIL import Image
import os

def Haar(normalizado):
    h = normalizado.shape[0]
    #normalizado = normalizado/np.sqrt(h)
    wavetransform2 = np.zeros(h)
    for i in range(int(h/2)):
        wavetransform2[i] =  (normalizado[2*i] + normalizado[2*i + 1])/(2)
        wavetransform2[int(h/2) + i] = (normalizado[2*i] - normalizado[2*i + 1])/(2)
#        os.system("Pause")
#        print(normalizado[2*i],normalizado[2*i + 1])
#        print(wavetransform2[i])
#        print(wavetransform2)
    return wavetransform2

def wavelet2D(img):
    h = img.shape[0]
    waveTransformlin = np.zeros((img.shape[0],img.shape[1]))
    waveTransformecol = np.zeros((img.shape[0],img.shape[1]))


    for i in range(img.shape[0]):
        waveTransformlin[i] = Haar(img[i,:])
    
    for i in range(img.shape[1]):
        waveTransformecol[i] = Haar(waveTransformlin[:,i])
    return waveTransformecol    

def wavelet(signal,nivel):
    h = signal.shape[0]
    wavetransform = np.zeros(h)

    #normalizado = signal/np.sqrt(h)
    normalizado = signal
    detales = np.zeros(1)
    
    while h > 1:
        wavetransform = Haar(normalizado)
        normalizado = wavetransform[0:h/2]
        aux = wavetransform[h/2:]
        detales = np.concatenate((aux,detales))
        print(normalizado)
        h = h/2
    
    detales = detales[:-1]
    wavelet = np.concatenate((normalizado,detales))
    return wavelet

def recomporHaar(normalizado):
    h = normalizado.shape[0]
    real = np.zeros(1)
    medias,detales = np.split(normalizado,2)

    for i in range(medias.shape[0]):
        aux = np.array([medias[i] -detales[i], medias[i] + detales[i]])
        real = np.concatenate((aux,real))
        #print(real,medias[i],detales[i])
        #os.system('Pause')
    real = real[:-1]
    real = real[::-1]
    return real

def recompor2D(img):
    h = img.shape[0]
    waveTransformlin = np.zeros((img.shape[0],img.shape[1]))
    waveTransformecol = np.zeros((img.shape[0],img.shape[1]))
   
    for i in range(img.shape[0]):
        waveTransformlin[i] = recomporHaar(img[i,:])
    
   # plt.imshow(waveTransformlin,cmap = 'gray')
    for i in range(img.shape[1]):
        waveTransformecol[i] = recomporHaar(waveTransformlin[:,i])
    return waveTransformecol  

def compress(x):
    medias,detales = np.split(x,2)
    #print(medias,detales,np.concatenate((medias,detales)))
   # os.system("Pause")
    for i in range(int(len(detales))):
        detales[i] = 0
    
    return np.concatenate((medias,detales))

def compress2D(img):
    h = img.shape[0]
    compressado = np.zeros((img.shape[0],img.shape[1]))
    for i in range(img.shape[0]):
        compressado[i] = compress(img[i,:])
    return compressado

    




