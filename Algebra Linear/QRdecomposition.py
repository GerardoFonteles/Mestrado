# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 13:59:30 2017

@author: Labvis
"""

import numpy as np
import os
import scipy.linalg
from numpy.linalg import svd

def QRdecomposition(A):
    '''
    Essa funcao calcula a decomposicao QR de uma matriz A utilizando a matriz
    de householder retornando Q e R
    
    '''
    #copia de A
    test = A.copy()
    #dimensoes da matriz
    n = A.shape[0]
    m= A.shape[1]
    
    #percorre todas as colunas da matriz
    for i in range(m):
        #seleciona as colunas respeitando sendo o primeiro elemento o da diagonal
        c = test[i :,i]
        
        if i != 0:
            #adiciona zeros em c exemplo: c = [0 0 r33 ... rn3].T 
            zeros = np.zeros(i)
            c = np.concatenate((zeros,c),axis = 0)
        
        if c[i] >= 0:#verifica se o elemento do vetor "e"  deve ser positivo ou negativo
            aux = 1
        else: 
            aux = -1
        
        #calcula o vetor para o calculo da matriz de householder
        v = np.asarray((c + np.linalg.norm(c)*aux*np.eye(1,n,i))).reshape(-1)
        
        
        #calcula a matriz de householder segundo a formula
        H = np.eye(n)-2*(np.dot(v[:,None],v[None,:]))/np.dot(v,v)
        
        #calcula as matrizes Q e R
        if i == 0:
            Q = H
            R = H@A
        else:
            Q = Qant@H
            R = H@R
        
        if istriu(R) == True and m!=n:
            break;
        test = R.copy()
        Qant = Q.copy()
        
#    #multiplica the last colloum de Q e a ultima linha de R por -1
#    Q[:,-1] *= -1
#    R[-1,:] *= -1
        #retorno
    return Q,R 


def QReigenvalues(A):
    '''
    Essa funcao calcula os autovalores da matriz A utilizando a decomposicao QR
    aplicando RQ sucessivamente
    '''
    #calcula as dimensoes de A
    n,m = A.shape
    if n !=m:
        print("Insert a square matrix")
        return 0
   # while True:
    for i in range(1000):
        #calcula a decomposicao da nova matriz A
        Q,R = QRdecomposition(A)
        #Q,R = scipy.linalg.qr(A)
        Anew = R@Q
        
        #testa se A triangular superior
        if istriu(A) == True:
            return Anew
        else:
            A = Anew
        

def istriu(A):
    '''
    Essa funcao checa se o a matrix e triangulas superior retornando TRUE e FALSE
    '''
    
    n,m = A.shape
    s=[]
    #percorre toda a matriz
    for i in range(n):
       for j in range(m):
           if j < i :
               s.append(A[i][j])
    if np.sum(s) < 0.00000001:# testa se a soma dos elementos da matriz e menor
        B = True
    else:
        B = False
    return B


def nullspace(A, atol=1e-13, rtol=0.001):
    '''
    Calcula o espaço nulo de uma matriz utilizando a svd
    '''
    A = np.atleast_2d(A)
    u, s, vh = svd(A)
    tol = max(atol, rtol * s[0])
    nnz = (s >= tol).sum()
    ns = vh[nnz:].conj().T
    return ns

def QReigenvectors(A):
    '''
    Calcula o espaço nulo de uma matriz utilizando a QR 
    '''
    
    n,m = A.shape
    if n !=m:
        print("Insert a square matrix")
        return 0
    #calcula todos os autovalores de A
    eigvalues = np.diag(QReigenvalues(A))
    for i in range(len(eigvalues)):
        B = A - eigvalues[i]*np.eye(len(eigvalues))
        Q,R = QRdecomposition(B)
        
        if i == 0:
            vec=(Q[:,-1].T).reshape(A.shape[0],1)
        else:
            vec = np.concatenate((vec,(Q[:,-1].T).reshape(A.shape[0],1)),axis=1)

    return vec

def QReigenvec(A):
    '''
    Essa funcao calcula os autovetores estabilizando uma variavel
    '''
    #calcula os autovalores
    eigvalues = np.diag(QReigenvalues(A))
    for i in range(len(eigvalues)):
        #A2 e uma versao deslocada da matriz A
        A2 = A - eigvalues[i]*np.eye(len(eigvalues))
        
        #seleciona uma submatriz eliminando a primeira coluna e a primeira linha
        Atil = A2[1:None,1:None]
        
        #e a nossa primeira coluna da matriz
        b = -A2[1:None,0]
        
        #encontra o vetor x que e uma versao escalonada do nosso
        #vetor sem o pirmeiro elemento que 1 
        x = np.linalg.inv(Atil)@b
        
        #coloca um vetor                  
        v=np.insert(x,0,1)
        v = v/np.linalg.norm(v)
        v = v.reshape(len(eigvalues),1)
        
        
        if i == 0:
            vec=v
        else:
            vec = np.concatenate((vec,v),axis=1)
    return vec
                           