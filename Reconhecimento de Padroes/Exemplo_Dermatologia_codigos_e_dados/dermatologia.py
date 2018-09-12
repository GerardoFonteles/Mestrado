# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 08:29:08 2017

@author: Labvis
"""

import numpy as np
from numpy.linalg import inv
from io import StringIO
from scipy.spatial.distance import pdist

#Carrega asrquivos
x = np.loadtxt('pacientes.txt')
y = np.loadtxt('patologias.txt')

lines,colluns = x.shape

#Permutar dadods
I = np.random.permutation(colluns)
x = x[:,I] 
y = y[:,I] 

#Separa o modelo
Xmodel = x[:,0:300]
Ymodel = y[:,0:300]

#Qualidade do modelo
Xtest = x[:,301:358]
Ytest = y[:,301:358]

#Construção do modelos (matriz A)
A = np.dot(np.dot(Ymodel,np.transpose(Xmodel)),inv(np.dot(Xmodel,np.transpose(Xmodel))))

#Testa o modelo
Ypred = np.dot(A,Xtest)

#Index dos elementos maximos preditos
Imax_pred = np.argmax(Ypred,axis = 0)

#Index dos elemsntos maximos de test
Imax_test = np.argmax(Ytest,axis = 0)

# porcentagem de Erro
aux = np.vstack((Imax_pred,Imax_test))
Perro=100*pdist(aux,'hamming')
Pacerto = 100-Perro


