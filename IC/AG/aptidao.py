# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 09:08:22 2017

@author: Labvis
"""
#Funcao que calcula a aptidao
import numpy as np
import math
import os
    

def aptidao(P):
    n = P.shape
    Xmin=-5
    Xmax=5
    #a=1./((2**(P.shape[1])/2) - 1)
    a = 1./2047
    #a = 1
    S = (P.shape[0])
    X1 = np.zeros(S)
    X2 = np.zeros(S)
    X = np.zeros(n[0])
    F = np.zeros(n[0])
    
    
    for index in range(int(n[0])):
        aux = P[index,0:P.shape[1]/2].astype(int)
        aux = ''.join(aux.astype(str))
        X[index] = int(aux,2)#convertido pra decimal
        X1[index]=Xmin + (Xmax-Xmin)*X[index]*a;
        #print(X[index])
          
        aux = P[index,P.shape[1]/2:].astype(int)
        aux = ''.join(aux.astype(str))
        X[index] = int(aux,2)#convertido pra decimal
        X2[index]=Xmin + (Xmax-Xmin)*X[index]*a;
        #print (X1[index])
        #print (X2[index])
        #print(X1[index])
        #print(X2[index])
        #print (a)
        #print (X[index])
      #  print ("\n")
        #F[index]=X[index]*np.sin(10*np.pi*X[index])+1;
        #F[index] = X[index]*X[index]
        F[index] = 20 + X1[index]**2 + X2[index]**2 -10*(math.cos(2*math.pi*X1[index]) + math.cos(2*math.pi*X1[index]))
        #os.system("pause")
        print (F[index])
    Fn = F/sum(F)  #Aptidao normalizada
    
    #print X[index]
    #os.system("pause")
    return X,F,1/Fn
        
    
    