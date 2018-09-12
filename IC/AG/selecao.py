# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 11:44:56 2017

@author: Labvis
"""

import numpy as np
import random
import os

def selecao_torneio(P,Fn): 
    T,n = P.shape
    a = int(T/2)
    S = np.empty([T, T])
    for index in range (a):     
        I =np.random.permutation((T)); #Gerar valor uniform 

        I1 = I[1]
        I2 = I[2]
        
        if Fn[I1] > Fn[I2]:
            Pai = I1
        else:
            Pai = I2
#        print I1
#        print I2
#        print Pai
#        print Fn
#        print "\n"
        # Seleciona 1o. individuo do par (PAI)
        
        I =np.random.permutation((T)); #Gerar valor uniform 

        I1 = I[1]
        I2 = I[2]
        
        if Fn[I1] > Fn[I2]:
            Mae = I1
        else:
            Mae = I2
            
        S[index ,0] = Pai
        S[index ,1] = Mae   
    

    return S
       