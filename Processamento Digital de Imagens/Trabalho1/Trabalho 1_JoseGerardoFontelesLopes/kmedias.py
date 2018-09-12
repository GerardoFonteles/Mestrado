# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 08:52:58 2017

@author: Labvis
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial.distance import chebyshev
import timeit
from copy import deepcopy
import math
from numpy import genfromtxt
import os


def kmedias(data,k,distance,iteration):
    
    base = data
      
    C_1 = np.random.randint(np.min(base), np.max(base), size=k)
    
    C = np.array(list(zip(C_1)), dtype=np.uint8)
    #print(C)
    
    #clusters anteriores
    C_ant = np.zeros(C.shape)
    #error
    error = np.linalg.norm(C - C_ant , axis=1)
    #clusters
    clusters = np.zeros(len(base))
    
    aux = math.inf
    
    test = 0
    while aux >= 0.001:
        if test > iteration:
            break;
        
        for i in range(len(base)):
            if distance == 'euclidean':    
                distancias = np.linalg.norm(base[i] - C , axis=1)  
            else:
                distancias = np.zeros(k)
                for w in range(k):
                    distancias[w] = chebyshev(base[i],C[w])
                #print(distancias)
                
            cluster = np.argmin(distancias)
            clusters[i] = cluster
                 
        C_ant = deepcopy(C)
        
    
        clusters = np.reshape(clusters,(clusters.shape[0],1))
        for i in range(k):
            points = [base[j] for j in range(len(base)) if clusters[j] == i]
            C[i] = np.mean(points, axis=0)
        #print(points.shape)
        if distance == 'euclidean':    
            error = np.linalg.norm(C - C_ant,axis = 1)    
        else:
            error = chebyshev(C,C_ant)
        aux = np.sum(error)
        print(aux)
        test = test + 1
        print(test)
        
    return points,clusters,C

