# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 09:30:02 2017

@author: Labvis
"""


import numpy as np
import os
import scipy.linalg


def power_method(A):
    n = A.shape[0]
    m = A.shape[1]
    if n !=m:
        print("Insert a square matrix")
    x = np.random.rand(A.shape[1])
    x = x/np.linalg.norm(x)
    
    while True:
        x1 = A@x
        x1norm = np.linalg.norm(x1)
        if (np.linalg.norm(x - x1/x1norm) < 0.00000001):
            break
        
        else:
            
            x = x1/x1norm
        #print(x)
        #os.system("pause")
    maxeigen = np.dot(A@x,x)/np.dot(x,x)
    
    return x,maxeigen

def power_method_inverse(A):
    x = np.random.rand(A.shape[0])
    
    while True:
        x1 = np.linalg.inv(A)@x
        x1norm = np.linalg.norm(x1)
        if (np.linalg.norm(x - x1/x1norm) < 0.00000001):
            break
        
        else:
            #print(np.linalg.inv(A)@x)
            x = x1/x1norm
        
    mineigenvalue = np.dot(A@x,x)/np.dot(x,x)
    
    return x,mineigenvalue

def power_method_shifted(A):
    _,maxeigenvalue = power_method(A)
    eigenvalues = []
    eigenvalues.append(maxeigenvalue)
    A1 = A - maxeigenvalue*np.eye(A.shape[0])
    aux = maxeigenvalue
    for k in range(A.shape[0]-2):
        _,aux2 = power_method(A1)
        print(aux2)
        eigenvalues.append(aux2)
        A1 = A - aux2*np.eye(A.shape[0])
        aux = aux2
#    _, mineigenvalue = power_method_inverse(A)
#    eigenvalues.append(mineigenvalue) 
    return eigenvalues