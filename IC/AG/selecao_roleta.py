# -*- coding: utf-8 -*-
"""
Created on Mon Apr 03 09:26:06 2017

@author: Labvis
"""

import numpy as np
import random
import os

def roda_roleta(Fn_acc,I):
    u = np.random.rand(1)
    indices(Fn_acc, lambda x: x > u)
    #J = np.where(Fn_acc > u)
    #print J
    
    os.system("pause")
    return I[J[1]]

def selecao_roleta(P,Fn):
    n = P.shape
    Fn_sort = np.sort(Fn,axis = None)
    I = np.argsort(Fn)
    Fn_acc = np.cumsum(Fn_sort)
    S = []
    for index in range (n[0]/2): 
        I1 = roda_roleta(Fn_acc,I)
        I2 = roda_roleta(Fn_acc,I)
        S.append(I1)
        S.append(I2)
    return S