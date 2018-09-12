# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 09:55:25 2017

@author: Labvis
"""
from DecomposicaoLU import LU
from DecomposicaoLU import pivot_matrix
import DecomposicaoCholesky
from power_method import power_method
from power_method import power_method_inverse
from QRdecomposition import QRdecomposition
from QRdecomposition import *
from sympy import *

import numpy as np
import os
import scipy.linalg

#A = np.asarray([ [7.0, 3, -1, 2], [3, 8, 1, -4], [9, 9, 4, -1], [2, 10, -1, 6] ])
#A = np.asarray([ [7.0, 3, -1, 2, 5], [3, 8, 1, -4,6], [-1,8, 1, 4, -1]])
A = np.asarray([[6.0, 3, 4, 8], [3, 6, 5, 1], [4, 5, 10, 7], [8, 1, 7, 25]])
#A = np.asarray([[8.0, 3, 4,], [3, 6, 1], [4, 5, 10]])
#A = np.random.rand(3,3)
#A = A + A.T
#A = np.asarray([[1.0,3],[1,2],[1,-1],[2,1]])

print('Matrix:')
print(A)
L,U,P = LU(A)
print('LU decomposition:')
print(L)
print(U)
print(P)


#C = DecomposicaoCholesky.cholesky(A)
print('Cholesky decomposition:')
print(C)

print('Power methods:')
eigenvectormax,maxeigenvalue = power_method(A)
eigenvectormin,mineigenvalue = power_method_inverse(A)
print(maxeigenvalue)
print(mineigenvalue)
#
#print('QR decomposiotion:')
Q,R = QRdecomposition(A)
eigenvaluesA = np.diag(QReigenvalues(A))
#vec = QReigenvectors(A)
vecs = QReigenvec(A)
#print(Q)
#print(R)
#print(eigenvaluesA)
#print(vecs)
#
######m>n
#A2 = np.random.rand(3,5)
#A2 = np.asarray([ [7.0, 3, -1, 2,5], [3, 4, 1, 8,9], [-1, 1, -4, -1,10]])
#L2,U2,P2 = LU(A2)
##
######n>m
#A3 = np.random.rand(5,3)
#L3,U3,P3 = LU(A3)