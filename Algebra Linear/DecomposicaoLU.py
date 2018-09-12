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
    '''
    
    Essa função recebe uma matriz 'A' e faz a pivotizacao dela retornando
    a matriz de pivo e inclusive a matriz de permutacao
    
    '''
    n = A.shape[0]
    m = A.shape[1]
    aux = A.copy()
    permutation = np.identity(n)
    
    
    if n == m or m > n:
        for j in range(m):#percorre toda a matriz pelas colunas
            if j == n:
                break
            #recebe o index maximo do valor máximo da coluna
            index = np.argmax(aux[:,j])         

            if index < j:
                #Indentificar se o index de valor máximo é da submatriz
                temporary = np.max(aux[j:n,j])
                #Encontra o index verdadeiro
                index = np.argwhere(aux[:,j] == temporary).flatten()
                
                if index.size > 1:#Se existir mais de um index igual seleciona o primeiro
                   index  = int(index[0].copy())
                else:#Se o valor máximo for diferente
                   index = int(np.argwhere(aux[:,j] == temporary).flatten())    
            
            if index >= j:# Se o index estiver na submatriz
                temp = aux[j,:].copy()#recebe a linha que sera deslocada
                aux[j,:] =  aux[index,:].copy()#linha que sera colocada acima
                aux[index,:] = temp.copy()#desloca a linha para baixo
                
                temp2 = permutation[j,:].copy()#matriz de permutacao
                permutation[j,:] = permutation[index,:]
                permutation[index,:] = temp2.copy()
            
    else:#Essa parte e para matrizes altas com n>m
        for j in range(n):
            if j == m:
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
                
                temp2 = permutation[j,:].copy()
                permutation[j,:] = permutation[index,:]
                permutation[index,:] = temp2.copy()
        
    return aux,permutation

def LU(A):
    
    '''
    Calcula a decomposicao LU de uma matriz A
    '''

    n = A.shape[0]
    m = A.shape[1]
   
    test,permutation = pivot_matrix(A)#recebe a matrix pivotizada
    matrix_pivot,_ = pivot_matrix(A)
    #print(matrix_pivot)
    if m > n:#essa matriz sera a matriz L
        t = min(m,n)
        mij = np.zeros((t,t))
    else:
        mij = np.zeros((n,m))
   
    if n == m or m > n: 
        
        for j in range(m):#percorre todas as colunas
            if j == m:#para na última coluna
                break
            for i in range(j,n):#percorre a linha, mas sempre para antes da ultima e inicia na diagonal
                    if i == n-1:
                        break
                    pivot = np.diag(test)[j]#atribui o pivot
                    mij[i+1,j] = test[i+1,j]/pivot #divida a linha pelo pivot
                    test[i+1,:] = test[i+1,:] - mij[i+1,j]*test[j,:]#a linha sera subitraida da abaixo dela zerando a coluna

        np.fill_diagonal(mij,1)#colca 1 na diagona de L
        return mij,test,permutation#retorna L U e P
    
    else:#mesmo algoritmo para matrizes altas
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

        np.fill_diagonal(mij,1)
        return mij,test[0:m,:],permutation
    