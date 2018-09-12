# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 09:32:35 2017

@author: Labvis
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
import matplotlib.patches as mpatches
from Estimacaomatrizconv import *
from normaliza import normaliza
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import timeit
import math
from numpy import genfromtxt
from pca import pca
import os

data = genfromtxt('haberman.data', delimiter=',')
#data = genfromtxt('david.data', delimiter=' ')

#Separa os atributos das classes
classes = data[:,data.shape[1]-1]
base = data[:,0:data.shape[1]-1]

test1 = base[:,0].reshape(base.shape[0],1)
test2 = base[:,2].reshape(base.shape[0],1)

test1 = base[:,1].reshape(base.shape[0],1)
test2 = base[:,2].reshape(base.shape[0],1)

test1 = base[:,0].reshape(base.shape[0],1)
test2 = base[:,1].reshape(base.shape[0],1)

base = np.concatenate((test1,test2),axis=1)

Y = pca(base,95)
base = Y

classe1 = []
classe2 = []

##Separa as amostra em duas classes
for k in range(base.shape[0]):
    if (classes[k] == 1):
        classe1.append(base[k])
    elif(classes[k] == 2):
        classe2.append(base[k])   

    
        
classe1 = np.asarray(classe1, dtype=np.float32)
classe2 = np.asarray(classe2, dtype=np.float32)

#Y = pca(base,800)
#base = Y

tx_acerto = np.zeros(100)

for i in range(100):
    #separa treino e test
    X_train, X_test, y_train, y_test = train_test_split(base,classes.T,
    test_size=20,stratify = classes.T)
    
    
    index1 = [i for i, x in enumerate(list(y_train)) if x == 1]
    index2 = [i for i, x in enumerate(list(y_train)) if x == 2]
    m,n = X_train.shape
    
    #Calcula todas as matrizes de de covariância para todos os classificadores
    C1 = estimacaovetorial(X_train[index1].T)
    C2 = estimacaovetorial(X_train[index2].T)
    Cp = (X_train[index1].shape[0]/m)*C1 + (X_train[index2].shape[0]/m)*C2
    Cn = np.diag(np.diag(C1))
 
    
    PC1 = classe1.shape[0]/classes.shape[0]
    PC2 = classe2.shape[0]/classes.shape[0]
    
     #classes preditas
    y_pred = np.zeros(X_test.shape[0])

    #classes preditas
        
    ############## Equacao completa #############
    for k in range(X_test.shape[0]):
            xn = X_test[k,:].reshape(base.shape[1],1)
            media = np.mean(X_train[index1],axis=0).reshape(base.shape[1],1)
            media2 = np.mean(X_train[index2],axis=0).reshape(base.shape[1],1)
            
            Q1 = (xn-media).T@np.linalg.inv(C1)@(xn-media)
            g1 = -0.5*Q1 -0.5*math.log(np.linalg.det(C1))+math.log(PC1)
            
            Q2 = (xn-media2).T@np.linalg.inv(C2)@(xn-media2)
            g2 = -0.5*Q2 -0.5*math.log(np.linalg.det(C2))+math.log(PC2)
            
            index = np.argmax(np.asanyarray([g1,g2]))
            if index == 0:
                y_pred[k] = 1
            elif index == 1:
                y_pred[k] = 2
          
    tx_acerto[i] = np.sum(y_pred==y_test)/y_pred.shape[0]

mediacertos = np.mean(tx_acerto)
maximo = np.max(tx_acerto)  
minimo = np.min(tx_acerto)
mediana = np.median(tx_acerto)  
std = np.std(tx_acerto)

for j in range(base.shape[0]):     
        plt.plot(base[j,0],base[j,1],'o')

 