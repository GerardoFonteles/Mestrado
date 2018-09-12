# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 08:29:19 2017

@author: Labvis
"""

import numpy as np
from sklearn import preprocessing
import matplotlib.patches as mpatches
from Estimacaomatrizconv import *
from numpy import genfromtxt
import os

def pca(data,tol):
#data = genfromtxt('haberman.data', delimiter=',')

    X = data
    
    media = np.mean(X,axis = 0)
    
    X = X - media
    
    Cx = np.cov(X.T)    
    
    autovalores,autovetores = np.linalg.eig(Cx)
  
    VT = np.sum(autovalores)
    
    for k in range(autovalores.shape[0]):
        if k == 0:
            aux = 100*(autovalores[0].sum())/VT
        else:
            aux = 100*(autovalores[:k].sum())/VT
            print(aux,tol)
            if aux >= tol:
                Vq = autovetores[:,np.arange(k)]
                break;
            elif k == autovalores.shape[0]-1:
                Vq =  autovetores
    Y = Vq.T@X.T
    Y = Y.T
    
    return Y