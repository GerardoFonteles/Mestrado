# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 16:41:22 2017

@author: Labvis
"""

import numpy as np
from Estimacaomatrizconv import *
import timeit

X = np.array([[1.0,-1,1],[2,3,-1]])


tempo1 = np.zeros(1000)
tempo2 = np.zeros(1000)
tempo3 = np.zeros(1000)
tempo4 = np.zeros(1000)

for i in range(1000):
    
    start1 = timeit.default_timer()
    
    C1 = estimacaovetorial(X)
    
    stop1 = timeit.default_timer()
    
    tempo1[i] = stop1 - start1
    
    start2 = timeit.default_timer()
    C2 = estimacaorecursiva(X)
    stop2 = timeit.default_timer()
    
    tempo2[i] = stop2 - start2
    ######## Utilizando a biblioteca do python ##########
    
    start3 = timeit.default_timer()
    C3 = np.cov(X,bias = 'TRUE')
    stop3 = timeit.default_timer()
    tempo3[i] = stop3 - start3
    
    start4 = timeit.default_timer()
    C4 = estimacaoiterativa(X)
    stop4 = timeit.default_timer()
    tempo4[i] = stop4 - start4
          
tempomedio1 = np.mean(tempo1)
tempomedio2 = np.mean(tempo2)
tempomedio3 = np.mean(tempo3)
tempomedio4 = np.mean(tempo4)

