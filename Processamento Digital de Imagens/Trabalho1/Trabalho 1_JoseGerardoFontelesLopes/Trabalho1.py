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
from sklearn.cluster import KMeans
from nltk.cluster.kmeans import KMeansClusterer
from skimage import exposure
from kmedias import kmedias


#Leitura das imagens
cameraman = imread('C:/Users/Labvis/Dropbox/mestrado/Processamento Digital de Imagens/Trabalho1/cameraman512.jpg')

#Converte a imagem para níveis de cinza
lena = rgb2grey(np.asarray(cameraman))*np.max(cameraman)



#Vetoriza a Imagem
image_vector = np.reshape(lena, (1,lena.shape[0]*lena.shape[1]))

#Plota o Histograma
plt.figure(1)
plt.xlabel('Níveis de Cinza')
plt.ylabel('Frequência de Ocorrência')
plt.title('Histograma')

hist, bins_center = exposure.histogram(lena)
plt.plot(bins_center, hist)


#Calcula o kmedias
points,clusters,C = kmedias(image_vector.T,2,'euclidean',10)


vector_seg2 = clusters.T

#Transforma o vetor de labels na imagem segmentada
image_seg2 = np.reshape(vector_seg2,(lena.shape[0],lena.shape[1]))

#plota a Imagem segmentada pelo kmedias
plt.figure(2)
plt.axis('off')
plt.imshow(image_seg2,cmap = "gray")


#Calula o limiar do Otsu
val = filters.threshold_otsu(lena)

#Plota a imagem segmentada pelo otsu
plt.figure(3)
plt.axis('off')
plt.imshow(lena<val,cmap="gray")


test = lena < val

test2 = test.astype(int)

result = np.sum(test2  - image_seg2)


#plt.figure(2)
#plt.imshow(cameram,cmap="gray")
#plt.axis('off')


