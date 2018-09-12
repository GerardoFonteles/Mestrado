# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 11:21:45 2017

@author: Labvis
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
import matplotlib.patches as mpatches
from normaliza import normaliza
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import timeit
from mpl_toolkits.mplot3d import Axes3D
import math
from numpy import genfromtxt
from pca import pca
import os


# Carrega dados
data = genfromtxt('haberman.data', delimiter=',')

data = genfromtxt('haberman.data', delimiter=',')
base = data[:,0:data.shape[1]-1]
#base = normaliza(base)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(base[:,0],base[:,1],base[:,2],c = 'r',marker = 'o')
ax.set_xlabel('1 Atributo')
ax.set_ylabel('2 Atributo')
ax.set_zlabel('3 Atributo')
plt.title('Base de dados')
plt.show()

resultados,Vq = pca(base,90)

plt.figure()
plt.title('As duas componentes principais')
plt.scatter(resultados[:,0],resultados[:,1])
plt.show()


#funceme = genfromtxt('dados_FUNCEME.txt', delimiter=',')
#t = np.arange(0,funceme.shape[1], 1)
#
#dados,autovetor = pca(funceme,100)
#
###Recuperados
#test = autovetor@dados

#for k in range(test.shape[0]):
#    plt.figure()
#    plt.plot(t,test[k])
#    plt.imshow
#
###autovalor de maior valor
##plt.figure()
##plt.plot(t,autovetores[:,0])
##plt.imshow
#
#
#for k in range(funceme.shape[0]):
#    plt.figure()
#    plt.plot(t,funceme[k])
#    plt.imshow
