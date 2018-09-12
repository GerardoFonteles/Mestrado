# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 11:11:41 2017

@author: Labvis
"""

import numpy as np
import os
import scipy.linalg
#from pivot_matrix import pivot_matrix


def pivot_matrix(A):
    #troca as linhas da matriz
    n = A.shape[0]
    m = A.shape[1]
    aux = A.copy()
    permutation = np.identity(n)
    k=0
    #percorre toda a matriz
    for j in range(m):
        if j == n:
            break
        #recebe o index maximo do valor máximo da coluna
        index = np.argmax(aux[:,j])         
        #print(index)
        if index < j:
            #Indentificar se o index de valor máximo é da submatriz
            temporary = np.max(aux[j:n,j])
            #Encontra o index verdadeiro
            index = np.argwhere(aux[:,j] == temporary).flatten()
            if index.size > 1:
               index  = int(index[0].copy())
            else:
               index = int(np.argwhere(aux[:,j] == temporary).flatten())    
        if index >= j:
            temp = aux[j,:].copy()
            aux[j,:] =  aux[index,:].copy()
            aux[index,:] = temp.copy()
            #print(aux,j,index,temp,test2)   
            temp2 = permutation[j,:].copy()
            permutation[j,:] = permutation[index,:]
            permutation[index,:] = temp2.copy()
        #print(permutation)
    
    return aux,permutation

#Matriz A
#A = np.asarray([ [7.0, 3, -1, 2], [3, 8, 1, -4], [9, 9, 4, -1], [2, 10, -1, 6] ])
#A = np.array([[0,2,1,2,-1],[1,4,2,3,-1],[1,2,1,1,0]])
#A = np.asarray([ [7.0, 3, -1, 2], [3, 8, 1, -4], [-1, 1, 4, -1]])
#A = np.asarray([[6 , 3],[4,3],[2,3],[5,6]])

def LU(A):

    n = A.shape[0]
    m = A.shape[1]
    #test = np.asarray([[7.0,8,9],[6,3,6],[4 , 3,5]])
    #test = np.asarray([ [7.0, 3, -1, 2], [3, 8, 1, -4], [-1, 1, 4, -1], [2, -4, -1, 6] ])
    #test = np.asarray([ [7.0, 3, -1, 2], [3, 8, 1, -4], [-1, 1, 4, -1]])
    #test = np.asarray([[6 , 3],[4,3],[2,3],[5,6]])
    #A = np.transpose(A)
    
    
    test,permutation = pivot_matrix(A)
    matrix_pivot,_ = pivot_matrix(A)
    
    pivot =matrix_pivot[0,0]
    
    if m != n:
        t = min(m,n)
        mij = np.zeros((t,t))
    else:
        mij = np.zeros((n,m))
    
    
    for j in range(m):
        if j == m:
            break
        for i in range(j,n):
                if i == n-1:
                    break
                pivot = np.diag(test)[j]
                mij[i+1,j] = test[i+1,j]/pivot 
                test[i+1,:] = test[i+1,:] - mij[i+1,j]*test[j,:]
                #print(mij[i+1,j],test[i+1,:],test[j,:])
                #os.system("pause")
    
    np.fill_diagonal(mij,1)
    return mij,test,permutation