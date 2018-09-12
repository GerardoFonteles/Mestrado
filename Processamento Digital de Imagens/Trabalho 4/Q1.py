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
from sklearn.metrics import mean_squared_error
from pca import pca
import os


# Carrega dados
data = genfromtxt('haberman.data', delimiter=',')
#data = genfromtxt('david.data', delimiter=' ')

data = genfromtxt('haberman.data', delimiter=',')
base = data[:,0:data.shape[1]-1]
base = normaliza(base)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(base[:,0],base[:,1],base[:,2],c = 'r',marker = 'o')
ax.set_xlabel('1 Atributo')
ax.set_ylabel('2 Atributo')
ax.set_zlabel('3 Atributo')
plt.title('Base de dados')
plt.show()



#dados,autovetor = pca(funceme,100)
Y,Vq = pca(base,90)

reconstrução = Y@Vq.T + np.mean(base,axis=0)

mse = mean_squared_error(base,reconstrução)



##Funceme
funceme = np.asanyarray(genfromtxt('dados_FUNCEME.txt', delimiter=','))
t = np.arange(0,funceme.shape[1], 1)

Yfunc,Vqfunc = pca(funceme,100)

reconstruçãofunc = Yfunc@Vqfunc.T + np.mean(funceme,axis=0)
msefunc = mean_squared_error(funceme,reconstruçãofunc)

test = Yfunc

plt.figure()
plt.scatter(Yfunc[:,0],Yfunc[:,1])
plt.title("Componentes Principais para os dados da Funceme")
plt.imshow
#
###autovalor de maior valor
#plt.figure()
#plt.plot(t,autovetor[:,0])
#plt.imshow
##
#
plt.figure()
for k in range(funceme.shape[0]):
    plt.subplot(5,6,k+1)
    plt.plot(t,funceme[k])
    plt.imshow
