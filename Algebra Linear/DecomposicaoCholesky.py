# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 14:49:06 2017

@author: Labvis
"""

import numpy as np
import os
import scipy.linalg
from math import sqrt

def cholesky(A):
    '''
    Calcula a decomposicao cholesky para uma matriz A caso nao seja quadrada retorna 0
    '''
    #dimensoes da matriz
    n = A.shape[0]
    m = A.shape[1]
    
    #retorna zero se nao for quadrada
    if n !=m:
        print("Insert a square matrix")
        return 0,0
        
    #copia de A
    test = A.copy()
    #cria a matriz L como zeros
    L = np.zeros((n,m))
    #auxilia no calculo da choleskyy
    aux = []
    
    #percorre todas as linhas
    for i in range(n):
        #laco para o calculo da matriz de cholesky
        for k in range(i+1):
            s = 0
            for j in range(k):
                s += L[i,j]*L[k,j]
                aux.append(s)
               
                
            if i == k:#para a diagonal
                L[i,k] = sqrt(test[i,i] - s)
            else:#restante dos elementos
                L[i,k] = ((1.0 / L[k,k])*(test[i,k] - s))
                #os.system("pause")
    return L