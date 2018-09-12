# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 10:44:15 2017

@author: Labvis
"""

import random
import math
import numpy as np
import os
from numpy.linalg import inv

def evaluateSolutions(particles,v,p,k):
    T,n = particles.shape
    y = np.zeros(T)
    
    
    for index in range(T):
        #y[index] = rosenbrock(particles[index])
        #y[index] = seq(particles[index],v,p,k)
        y[index] = seq_reg(particles[index],v,p,k)
        #y[index] = rastringin(particles[index])
#        print(particles[index,:])
#        print(particles[index])
#        print(y)
#        os.system("pause")
    #print (y)
    return y
        

def rosenbrock(x):
    
    y = ((1 - x[0])**2) + 100*((x[1] - ((x[0])**2))**2)
   
    return y

def rastringin(x):
    
    y = 20 + x[0]**2 + x[1]**2 -10*(math.cos(2*math.pi*x[0]) + math.cos(2*math.pi*x[1]))
    
    return y

def seq(B,v,p,k):#ordem do polinomio
    n = len(v)
    y = p#vetor de observações
    S = (n,k+1)
    X = np.zeros(S)
    aux = []
    for j in range(k+1):
        aux = np.power(v,j)
        X[:,j] = aux
        
    #print (X)  
    ypred = np.dot(X,B)
    erro = y - ypred
    SEQ = np.sum((np.power(erro,2)))
    ymed = np.mean(y)
    Syy = sum(np.power(y-ymed,2))
    #print(1/SEQ)
    #print (SEQ)
    #os.system("pause")
    return SEQ

def seq_reg(B,v,p,k):#ordem do polinomio
    n = len(v)
    y = p#vetor de observações
    S = (n,k+1)
    lamda = 0.1
    X = np.zeros(S)
    fit = np.zeros(len(v))
    auxiliar = (len(v),2)
    z = np.zeros(auxiliar)
    z[:,0] = v
    z[:,1] = p        

    aux = []
    for j in range(k+1):
        aux = np.power(v,j)
        X[:,j] = aux
        
    #print (X)  
    ypred = np.dot(X,B)
    erro = y - ypred
    #for k in range(len(v)):
     #   fit[k] =  1*(z[k,0]**2 + z[k,1]**2)
    #fit = np.sum(np.power(z[:,0],2) + np.power(z[:,1],2))
    fit = np.sum(np.power(B,2))
    SEQ = np.sum(np.power(erro,2)) + lamda*fit
    #SEQ = np.sum((np.power(erro,2))) +  0.1*np.dot(np.transpose(z), z)
    #print(np.sum((np.power(erro,2))))
    #print('\n')
    #print(np.sum(t*np.linalg.norm(X)))
    #print(1/SEQ)
    #print (SEQ)
    #os.system("pause")
    return SEQ