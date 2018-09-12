# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 14:45:02 2017

@author: Labvis
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from mpl_toolkits.mplot3d import Axes3D
import timeit
from copy import deepcopy
import math
from numpy import genfromtxt
import os
from sklearn import metrics
from sklearn.metrics import pairwise_distances
from kmedias import *
from normaliza import normaliza
from DBindex import *

data = genfromtxt('haberman.data', delimiter=',')
base = data[:,0:data.shape[1]-1]
base = normaliza(base)

k=2
r = 9
x = []
x.append(k)
DB = []
CH = []
Cs = []
labelsopt = []
ssdresultsopt = []

for i in range(r):
    points,labels,C,ssdresults = kmedias(data,k)
    if check(C):
        while check(C):
            points,labels,C,ssdresults = kmedias(data,k)
    #print(C)
    aux = compute_DB_index(base, labels, C, k)
    aux2 = metrics.calinski_harabaz_score(base,labels)
    ssdresultsopt.append(ssdresults)
    Cs.append(C)
    labelsopt.append(labels)
    DB.append(aux)
    CH.append(aux2)
    plt.close("all")
    k = k + 1
    x.append(k)
#distancias,C,clusters = kmediasseq(data,5)
#points,labels,C,ssdresults = kmedias(data,k)
#labels2,C2,ssdresults2 = kmediasseq(data,k)

x = x[:-1]
ssdresultsopt[0] = np.asanyarray(ssdresultsopt[0])/100000
CH = np.asanyarray(CH)
DB = np.asanyarray(DB)
x = np.asanyarray(x)


plt.figure()
plt.title('Gráfico de SSD')
plt.plot(ssdresultsopt[0])
plt.xlabel('Iterações')
plt.ylabel('SSD')



plt.figure()
plt.title('Gráfico de DB')
plt.plot(x,DB)
plt.xlabel('Quantidade de Grupos')
plt.ylabel('DB(K)')

plt.figure()
plt.title('Gráfico de CH')
plt.plot(x,CH)
plt.xlabel('Quantidade de Grupos')
plt.ylabel('CH(K)')



for j in range(len(labelsopt)):
    print(np.sum(np.sum(labelsopt[j] == j)))
    for i in range(3):
        print('Clurster {0} '.format(j))
        print('Míximo: {0}'.format(np.min(base[labelsopt[j] == 0][:,i])))
        print('Máximo: {0}'.format(np.max(base[labelsopt[j] == 0][:,i])))
        print('Médio: {0}'.format(np.mean(base[labelsopt[j] == 0][:,i])))
        print('Médiana: {0}'.format(np.median(base[labelsopt[j] == 0][:,i])))
        print('STD: {0}'.format(np.std(base[labelsopt[j] == 0][:,i])))
    