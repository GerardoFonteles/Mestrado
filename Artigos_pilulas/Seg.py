# -*- coding: utf-8 -*-
"""
Created on Thu May 17 09:43:03 2018

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


mascara = imread('C:/Users/Labvis/Desktop/SIIM/Alprazolam/3283_lg.png')
real = imread('C:/Users/Labvis/Desktop/SIIM/Alprazolam/3283_lg.jpg')

mascara = rgb2grey(mascara)
real = rgb2grey(real)

seg = mascara*real

plt.figure()
plt.imshow(seg,cmap='gray')