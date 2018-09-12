# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 12:45:51 2017

@author: Labvis
"""


import random
import math
import numpy as np
import os


def cruzamento(P,S,pc):
    n = P.shape
    #Pnew = np.empty([n[0], n[1]])
    Pnew = []
    for index in range(int(n[0]/2)):
        u = random.random()
        if u <= pc:
            r = random.random()
            cut = math.floor(((float(n[1]) - 1)*r)) + 1 
            #Determina os filhos
            F1 = np.concatenate((P[S[index,0],0:cut],P[S[index,1],cut:])) 
            F2 = np.concatenate((P[S[index,1],0:cut],P[S[index,0],cut:]))
            
            Pnew.append(F1)
            Pnew.append(F2)
           
        else:
            F1 = P[S[index,0],:]
            F2 = P[S[index,1],:]
            Pnew.append(F1)
            Pnew.append(F2)
#        print("u %f, cut %d" % (u,cut))
#        print index
#        print S
#        print S[index,0]
#        print S[index,1]
#        print P[S[index,0],0:cut]
#        print P[S[index,1],cut:]
#        print F1
#        print F2
#        print P
#        
    Pnew = np.array(Pnew)
#    print Pnew
#    
#    os.system("pause")
#    print "\n"
    return Pnew
#    os.system("pause")
                     
    