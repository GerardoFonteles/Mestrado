# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 15:45:32 2017

@author: Labvis
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from Estimacaomatrizconv import *
import timeit
from numpy import genfromtxt

#data = np.loadtxt('haberman.data')
data = genfromtxt('haberman.data', delimiter=',')
classes = data[:,3]
atributos = data[:,0:3]

start1 = timeit.default_timer()
C = np.cov(atributos.T,bias = 'TRUE')
stop1 = timeit.default_timer()

####### Métodos implementados #######
####### Estimacao vetorial #######
start2 = timeit.default_timer()
C2 = estimacaovetorial(atributos.T)
stop2 = timeit.default_timer()

###### Estimação recursiva #######
start3 = timeit.default_timer()
C3 = estimacaorecursiva(atributos.T)
stop3 = timeit.default_timer()

###### Estimação recursiva ######
start4 = timeit.default_timer()
C4 = estimacaoiterativa(atributos.T)
stop4 = timeit.default_timer()

classe1 = []
classe2 = []

for k in range(data.shape[0]):
    if (data[k,3] == 1):
        classe1.append(data[k])
    else:
        classe2.append(data[k])    
    
        
classe1 = np.asarray(classe1, dtype=np.float32)
classe2 = np.asarray(classe2, dtype=np.float32)

C_classe1 = np.cov(classe1[:,0:3].T)
C_classe2 = np.cov(classe2[:,0:3].T)

####### Tempo de Execução ########
tempo1 = stop1 - start1
tempo2 = stop2 - start2
tempo3 = stop3 - start3
tempo4 = stop4 - start4

rank_matricial =  np.linalg.matrix_rank(C2)
cond =  np.linalg.cond(C2,2)

rank_matricial_C1 = np.linalg.matrix_rank(C_classe1)
rank_matricial_C2 = np.linalg.matrix_rank(C_classe2)

cond_C1 = np.linalg.cond(C_classe1,2)
cond_C2 = np.linalg.cond(C_classe2,2)