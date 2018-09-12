# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 17:18:37 2018

@author: JoseGerardo
"""
import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.color import rgb2grey 
from skimage import filters
import numpy as np
from scipy.fftpack import fft, ifft
import matplotlib.patches as mpatches

x = np.array([0, 0, 0,0,0,0,0, 2.0, 2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0])
y = fft(x)
yinv = ifft(y)

plt.figure()
blue_patch = mpatches.Patch(color='blue', label='Portão no tempo')
plt.title("Portão no tempo")
line1 = plt.plot(x)

##Plota o valor absoluto do da fft
plt.figure()
blue_patch = mpatches.Patch(color='blue', label='FFT')
plt.title("FFT do portão")
line2 = plt.plot(np.angle(y))


##Teste da formula inversa
z = np.conjugate(fft(np.conjugate(y)))
plt.figure()
blue_patch = mpatches.Patch(color='blue', label='FFT')
plt.title("Portão no tempo")
line2 = plt.plot(np.abs(z))