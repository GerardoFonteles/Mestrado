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

#cameraman = imread('C:/Users/JoseGerardo/Dropbox/mestrado/Processamento Digital de Imagens/Trabalho1/crowd1.jpg')
lena = ndimage.imread('C:/Users/Labvis/Dropbox/mestrado/Processamento Digital de Imagens/Trabalho1/cameraman.jpg', flatten=True)

#Converte a imagem para níveis de cinza
#lena = rgb2grey(np.asarray(cameraman))*np.max(cameraman)

#plota a imagem
plt.figure()
plt.title("Imagem Original")
plt.axis('off')
plt.imshow(lena,cmap = "gray")

##Transformada fft para imagens e coloca o eixo no centro
lena_frenquencia = np.fft.fft2(lena)
lena_frenquencia2  = np.fft.fftshift(lena_frenquencia)

##Valor absoluto da transformada
plt.figure()
plt.title("Valor Absoluto")
plt.axis('off')
plt.imshow(np.log10(np.abs(lena_frenquencia2)),cmap = "gray")

##Frenquencia
plt.figure()
plt.title("Angulo ")
plt.axis('off')
plt.imshow(np.angle(lena_frenquencia2),cmap = "gray")

##Teste da formula inversa
z = np.conjugate(np.fft.fft2(np.conjugate(lena_frenquencia)))
plt.figure()
plt.title("Aplicada a propriedade")
plt.axis('off')
plt.imshow(np.abs(z),cmap = "gray")

##Propriedades
img = Image.open("C:/Users/Labvis/Dropbox/mestrado/Processamento Digital de Imagens/Trabalho1/cameraman.jpg")
img = img.rotate(-45)
img = np.asanyarray(img)
img_fft = np.fft.fft2(img)
img_fft2  = np.fft.fftshift(img_fft)

plt.figure()
plt.axis('off')
plt.imshow(np.log10(np.abs(img_fft2)),cmap = "gray")

plt.figure()
plt.axis('off')
plt.imshow(np.angle(img_fft2),cmap = "gray")

plt.figure()
plt.title("Rotacionada")
plt.axis('off')
plt.imshow(img,cmap = "gray")





