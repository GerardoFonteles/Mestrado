# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 14:53:38 2017

@author: Labvis
"""
import numpy as np

C1 = np.array([[1,-0.8,0.1],[-0.8,9,-0.1],[0.1,-0.3,4]])
C2 = np.array([[1,0,0],[0,1,0],[0.0,0,0]])
C3 = np.array([[4,-0.8,0.1],[-0.8,9,-0.1],[0.1,-0.1,16]])

determinantes = []

determinantes.append(np.linalg.det(C1))
determinantes.append(np.linalg.det(C2))
determinantes.append(np.linalg.det(C3))

w,v =np.linalg.eig(C1)
w2,v2 =np.linalg.eig(C2)
w3,v3 =np.linalg.eig(C3)

cholesky = np.linalg.cholesky(C3)