# -*- coding: utf-8 -*-
"""
Created on Mon Apr 03 09:23:25 2017

@author: Labvis
"""

import numpy as np
import os

def aptidao2(P):
    n = P.shape
    Xmin=-5
    Xmax=5
    a=1./((2**22) - 1)
    S = (n[0],2) 
        
    X = np.zeros(S)
    x2 = np.zeros(S)
    F = np.zeros(n[0])
    for index in range(int(n[0]),int(n[0]/2)):
        aux = P[index].astype(int)
        aux = ''.join(aux.astype(str))
        X[index] = int(aux,2)#convertido pra decimal
        #print (X[index])
        X[index]=Xmin + (Xmax-Xmin)*X[index]*a;
        print (X[index])
      #  print ("\n")
        #F[index]=X[index]*np.sin(10*np.pi*X[index])+1;
        #F[index] = X[index]*X[index]
        #print (F[index])
    for index range(int(n[0])/2,(int(n[0]))):
    Fn = F/sum(F)  #Aptidao normalizada
        
    #
    #print X[index]
    os.system("pause")
    return X,F,Fn