# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 09:50:19 2017

@author: Labvis
"""

import numpy as np
from numpy.linalg import inv
from io import StringIO
from scipy.spatial.distance import pdist
import os


def estimacaovetorial(X):
####### Estimação da Matriz de Covariância - Forma Vetorial ##########
#X = np.array([[1.0,-1,1],[2,3,-1]])
    Xmedia = np.mean(X,axis=1)
    Xmedia = Xmedia.reshape(X.shape[0],1)
    N = X.shape[1]

    Rx = 1/N*X@X.T
    C = (Rx - Xmedia@Xmedia.T)


    return C

def estimacaoiterativa(X):
    Xmedia = np.mean(X,axis=1)
    Xmedia = Xmedia.reshape(X.shape[0],1)
    N = X.shape[1]
    M = X.shape[0]
    S = (M,M)
    C = np.zeros(S)
    for k in range(N):
            aux = X[:,k].reshape(1,M)
            A = (aux.T - Xmedia).copy()
            C = C + A@A.T
            aux=0
    return C/N

############ Estimação da Covariância - Forma Recursiva ####################
def estimacaorecursiva(X):
    N = X.shape[1]
    x = np.zeros(2)
    for k in range(N):
        if k == 0:
            x = X[:,k]
        elif k == 1:
            x = ((x + X[:,k])/(k+1))
        else:
            x = k*x/(k+1) + X[:,k]/(k+1)
    
    x = x.reshape(X.shape[0],1)        
    
    for n in range(N):
        if n == 0:
            aux = X[:,n].reshape(X.shape[0],1)
            aux1 = aux.T 
            Rx1 = aux@aux1
        elif n==1:
            aux = X[:,n].reshape(X.shape[0],1)
            aux1 = aux.T 
            Rx1 = ((Rx1 + aux@aux1)/(n+1))
        else:
            aux = X[:,n].reshape(X.shape[0],1)
            aux1 = aux.T 
            Rx1 = n*Rx1/(n+1) +  aux@aux1/(n+1)
    #    print(Rx1)
    #    os.system("pause")
    
    C3 = Rx1 - x@x.T  
    return C3
    