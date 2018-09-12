# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 13:53:51 2017

@author: Labvis
"""

import random
import numpy as np

def mutacao(P,pm):
    n = P.shape
    Pnew=P;
    
    for index in range(n[0]):
        
        for k in range (n[1]):
            u = np.random.rand(n[1])
            if u[k] <= pm:
                if Pnew[index,k] == 0:
                    Pnew[index,k] = 1
                else:
                    Pnew[index,k] = 0
            else:
                Pnew[index,k] = Pnew[index,k]   
    return Pnew
