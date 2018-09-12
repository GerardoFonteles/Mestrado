# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 14:49:06 2017

@author: Labvis
"""

import numpy as np
import os
import scipy.linalg
from math import sqrt

#def cholesky(A):
#    L = [[0.0] * len(A) for _ in range(len(A))]
#    for i, (Ai, Li) in enumerate(zip(A, L)):
#        for j, Lj in enumerate(L[:i+1]):
#            s = sum(Li[k] * Lj[k] for k in range(j))
#            Li[j] = sqrt(Ai[i] - s) if (i == j) else \
#                      (1.0 / Lj[j] * (Ai[j] - s))
#    return L
#
#def cholesky2(A):
#    
#    n = len(A)
#
#    # Create zero matrix for L
#    L = [[0.0] * n for i in range(n)]
#    aux = []
#    # Perform the Cholesky decomposition
#    for i in range(n):
#        for k in range(i+1):
#            tmp_sum = sum(L[i][j] * L[k][j] for j in range(k))
#            aux.append(tmp_sum)
#            if (i == k): # Diagonal elements
#                # LaTeX: l_{kk} = \sqrt{ a_{kk} - \sum^{k-1}_{j=1} l^2_{kj}}
#                L[i][k] = sqrt(A[i][i] - tmp_sum)
#            else:
#                # LaTeX: l_{ik} = \frac{1}{l_{kk}} \left( a_{ik} - \sum^{k-1}_{j=1} l_{ij} l_{kj} \right)
#                L[i][k] = (1.0 / L[k][k] * (A[i][k] - tmp_sum))
    #return L,aux
#

#A = np.asarray([ [7.0, 3, -1, 2], [3, 8, 1, -4], [9, 9, 4, -1], [2, 10, -1, 6] ])
#A = np.asarray([[6, 3, 4, 8], [3, 6, 5, 1], [4, 5, 10, 7], [8, 1, 7, 25]])
def cholesky(A):
    
    n = A.shape[0]
    m = A.shape[1]
    
    if n !=m:
        print("Insert a square matrix")
        return 0
        
    test = A.copy()
    L = np.zeros((n,m))
    aux = []
    for i in range(n):
        for k in range(i+1):
            s = 0
            for j in range(k):
                s += L[i,j]*L[k,j]
                aux.append(s)
                #print(s,(L[i,j]*L[k,j]))
                
            if i == k:
                L[i,k] = sqrt(test[i,i] - s)
            else:   
                L[i,k] = ((1.0 / L[k,k])*(test[i,k] - s))
                #os.system("pause")
    return L,np.transpose(L)
