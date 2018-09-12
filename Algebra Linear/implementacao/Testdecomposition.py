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
from power_method import power_method_shifted
from QRdecomposition import QRdecomposition
from QRdecomposition import QReigenvalues

import numpy as np
import os
import scipy.linalg

#A = np.asarray([[6.0, 3, 4, 8], [3, 6, 5,1], [4, 5, 10, 7], [8, 1, 7, 25]])
#A = np.asarray([ [7.0, 3, -1, 2], [3, 8, 1, -4], [9, 9, 4, -1], [2, 10, -1, 6] ])
#A = np.asarray([ [7.0, 3, -1, 2], [3, 8, 1, -4], [-1, 1, 4, -1]])
#A = np.asarray([ [7.0, 3, -1, 2, 5], [3, 8, 1, -4,6], [-1,8, 1, 4, -1]])
#A = np.asarray([[4.0, 1, -1], [3, 2, -3], [1, 3, 0]])
A = np.asarray([[6.0, 3, 4, 8], [3, 6, 5, 1], [4, 5, 10, 7], [8, 1, 7, 25]])
#A = np.asarray([[0,1.0],[-2,-3]])
L,U,P = LU(A)


C,Ct = DecomposicaoCholesky.cholesky(A)
eigenvectormax,maxeigenvalue = power_method(A)
#eigenvalues = power_method_shifted(A)

eigenvectormin,mineigenvalue = power_method_inverse(A)

Q,R = QRdecomposition(A)
eigenvaluesA = QReigenvalues(A)
