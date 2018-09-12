# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 13:59:30 2017

@author: Labvis
"""

import numpy as np
import os
import scipy.linalg

#A = np.asarray([[6.0, 3, 4, 8], [3, 6, 5, 1], [4, 5, 10, 7], [8, 1, 7, 25]])
#A = np.asarray([[12.0, -51.0, 4], [6,167,-68], [-4, 24, -41]])

def QRdecomposition(A):

    test = A.copy()
    n = A.shape[0]
    m= A.shape[1]

    Qant = 0
    
    for i in range(m):
        c = test[i :,i]
        #        if c.size == 0:
#                return Qant,Rant
        if i != 0:
            zeros = np.zeros(i)
            c = np.concatenate((zeros,c),axis = 0)
            
        v = np.asarray((c - np.dot(np.linalg.norm(c),np.eye(1,n,i)))).reshape(-1)
        #print(np.eye(1,n,i))
        H = np.eye(n)-2/np.dot(v,v)*(np.dot(v[:,None],v[None,:]))
        if i == 0:
            Q = H
            R = Q@A
        else:
            Q = Qant@H
            R = H@R
        #os.system("pause")
        if istriu(R) == True and m!=n:
            break;
        test = R.copy()
        Qant = Q.copy()
        Rant = R.copy()
    Q = -1*Q
    R = -1*R        
    return Q,R 

def QReigenvalues(A): 
    n,m = A.shape
    if n !=m:
        print("Insert a square matrix")
        return 0
    while True:
        Q,R = QRdecomposition(A)
        Anew = R@Q
        
        if istriu(A) == True:
            return Anew
        else:
            A = Anew
        

def istriu(A):
    n,m = A.shape
    s=[]
    for i in range(n):
       for j in range(m):
           if j < i :
               s.append(A[i][j])
    if np.sum(s) < 0.0001:
        B = True
    else:
        B = False
    #print(s)
    return B

#def QReigenvectors(A):
    