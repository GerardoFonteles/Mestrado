# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 11:21:45 2017

@author: Labvis
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
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


# Carrega dados
data = genfromtxt('haberman.data', delimiter=',')
#data = genfromtxt('david.data', delimiter=' ')

#Separa os atributos das classes
classes = data[:,data.shape[1]-1]
base = data[:,0:data.shape[1]-1]


test1 = base[:,0].reshape(base.shape[0],1)
test2 = base[:,2].reshape(base.shape[0],1)

#test1 = base[:,1].reshape(base.shape[0],1)
#test2 = base[:,2].reshape(base.shape[0],1)

#test1 = base[:,0].reshape(base.shape[0],1)
#test2 = base[:,1].reshape(base.shape[0],1)

base = np.concatenate((test1,test2),axis=1)
#
#Y = pca(base,800)
#base = Y

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

p = 100

#declara as tacas de acertos
tx_acerto = np.zeros(p)
tx_acertoid = np.zeros(p)
tx_acertop = np.zeros(p)
tx_acerton = np.zeros(p)
tx_acertosvm = np.zeros(p)

y_predt = []
y_predidt = []
y_predpt = []
y_prednt = []
y_testt = []
y_predtsvm = []

resultados = []
resultadosmax = []
resultadosmin = []


treino = np.asanyarray([0.90,0.80,0.60,0.50,0.40,0.10])
#treino = np.asanyarray([0.20])

for j in range(treino.shape[0]):
    
#Simula 100 vezes as taxas para os classificadores
    for u in range(p):
        #separa treino e test
        X_train, X_test, y_train, y_test = train_test_split(base,classes.T,
        test_size=treino[j],stratify = classes.T)
        
        
        index1 = [i for i, x in enumerate(list(y_train)) if x == 1]
        index2 = [i for i, x in enumerate(list(y_train)) if x == 2]
        m,n = X_train.shape
        
        #Calcula todas as matrizes de de covariância para todos os classificadores
        C1 = estimacaovetorial(X_train[index1].T)
        C2 = estimacaovetorial(X_train[index2].T)
        Cp = (X_train[index1].shape[0]/m)*C1 + (X_train[index2].shape[0]/m)*C2
        Cn = np.diag(np.diag(C1))
     
        #print(X_train[index1].shape[0])
        PC1 = classe1.shape[0]/classes.shape[0]
        PC2 = classe2.shape[0]/classes.shape[0]
    
        #classes preditas
        y_pred = np.zeros(X_test.shape[0])
        y_predid = np.zeros(X_test.shape[0])
        y_predp = np.zeros(X_test.shape[0])
        y_predn = np.zeros(X_test.shape[0])
        y_predsvm = np.zeros(X_test.shape[0])
        
        ############## SVM #############
        clf = svm.SVC()

        clf = svm.SVC(gamma=0.001, C=100)
        clf.fit(X_train,y_train)
        y_predsvm = clf.predict(X_test)
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
              
        ############## sendo a indetidade #############
        
        for k in range(X_test.shape[0]):
                xn = X_test[k,:].reshape(base.shape[1],1)
                Q1 = (xn-media).T@np.linalg.inv(np.eye(base.shape[1]))@(xn-media)
                g1 = -0.5*Q1 -0.5*math.log(np.linalg.det(np.eye(base.shape[1])))+math.log(PC1)
                
                Q2 = (xn-media2).T@np.linalg.inv(np.eye(base.shape[1]))@(xn-media2)
                g2 = -0.5*Q2 -0.5*math.log(np.linalg.det(np.eye(base.shape[1])))+math.log(PC2)
                  
                index = np.argmax(np.asanyarray([g1,g2]))
                if index == 0:
                    y_predid[k] = 1
                elif index == 1:
                    y_predid[k] = 2
              
        ########## pooled ###############
        for k in range(X_test.shape[0]):
                xn = X_test[k,:].reshape(base.shape[1],1)
                Q1 = (xn-media).T@np.linalg.inv(Cp)@(xn-media)
                g1 = -0.5*Q1 -0.5*math.log(np.linalg.det(Cp))+math.log(PC1)
                
                Q2 = (xn-media2).T@np.linalg.inv(Cp)@(xn-media2)
                g2 = -0.5*Q2 -0.5*math.log(np.linalg.det(Cp))+math.log(PC2)
                        
                index = np.argmax(np.asanyarray([g1,g2]))
                if index == 0:
                    y_predp[k] = 1
                elif index == 1:
                    y_predp[k] = 2
            
          ########## naive ############### 
        for k in range(X_test.shape[0]):
                xn = X_test[k,:].reshape(base.shape[1],1)
                Q1 = (xn-media).T@np.linalg.inv(Cn)@(xn-media)
                g1 = -0.5*Q1 -0.5*math.log(np.linalg.det(Cn))+math.log(PC1)
                
                Q2 = (xn-media2).T@np.linalg.inv(Cn)@(xn-media2)
                g2 = -0.5*Q2 -0.5*math.log(np.linalg.det(Cn))+math.log(PC1)
                    
                index = np.argmax(np.asanyarray([g1,g2]))
                if index == 0:
                    y_predn[k] = 1
                elif index == 1:
                    y_predn[k] = 2
        
        y_predt.append(y_pred)
        y_predidt.append(y_predid)
        y_predpt.append(y_predp)
        y_prednt.append(y_predn)
        y_testt.append(y_test)
        y_predtsvm.append(y_predsvm)
        
           
        tx_acerto[u] = np.sum(y_pred==y_test)/y_pred.shape[0]
        tx_acertoid[u] = np.sum(y_predid==y_test)/y_pred.shape[0]
        tx_acertop[u] = np.sum(y_predp==y_test)/y_pred.shape[0]
        tx_acerton[u] = np.sum(y_predn==y_test)/y_pred.shape[0]
        tx_acertosvm[u] = np.sum(y_predsvm==y_test)/y_pred.shape[0]
        
    ### Calcula o máximo o mínimo e a mediana e o desvio padrao
    mediaacertos = []
    mediaacertos.append([np.mean(tx_acerto),np.mean(tx_acertoid),np.mean(tx_acertop),np.mean(tx_acerton)])
    
    maximo = []
    maxindices = []
    maximo.append([np.max(tx_acerto),np.max(tx_acertoid),np.max(tx_acertop),np.max(tx_acerton)])
    maxindices.append([np.argmax(tx_acerto),np.argmax(tx_acertoid),np.argmax(tx_acertop),np.argmax(tx_acerton)])
    
    minimo = []
    minindices = []
    minimo.append([np.min(tx_acerto),np.min(tx_acertoid),np.min(tx_acertop),np.min(tx_acerton)])
    minindices.append([np.argmin(tx_acerto),np.argmin(tx_acertoid),np.argmin(tx_acertop),np.argmin(tx_acerton)])
    
    mediana = []
    mediana.append([np.median(tx_acerto),np.median(tx_acertoid),np.median(tx_acertop),np.median(tx_acerton)])
    
    std = []
    std.append([np.std(tx_acerto),np.std(tx_acertoid),np.std(tx_acertop),np.std(tx_acerton)])
    
    ###Box plots
    f, axarr = plt.subplots(2, 2)
    bplot1 = axarr[0, 0].boxplot(tx_acertoid)  # will be used to label x-ticks)
    axarr[0, 0].set_title('Caso 1')
    bplot2 = axarr[0, 1].boxplot(tx_acertop)
    axarr[0, 1].set_title('Caso 2')
    bplot3 = axarr[1, 0].boxplot(tx_acerto)
    axarr[1, 0].set_title('Caso 3')
    bplot4 = axarr[1, 1].boxplot(tx_acerton)
    axarr[1, 1].set_title('Caso 4')
    
    
    # Fine-tune figure; hide x ticks for top plots and y ticks for right plots
    plt.setp([a.get_xticklabels() for a in axarr[0, :]], visible=False)
    plt.setp([a.get_yticklabels() for a in axarr[:, 1]], visible=False)
    
    #### Matriz de Confusao Equacao Completa
    cmatrixmin1 = confusion_matrix(y_testt[int(minindices[0][0])],y_predt[minindices[0][0]])
    #### Identidade
    cmatrixmin2 = confusion_matrix(y_testt[int(minindices[0][1])],y_predidt[minindices[0][1]])
    #### Pooled
    cmatrixmin3 = confusion_matrix(y_testt[int(minindices[0][2])],y_predpt[minindices[0][2]])
    #### Naive
    cmatrixmin4 = confusion_matrix(y_testt[int(minindices[0][3])],y_prednt[minindices[0][3]])
    
    #### Matriz de Confusao Equacao Completa
    cmatrixmax1 = confusion_matrix(y_testt[int(maxindices[0][0])],y_predt[maxindices[0][0]])
    #### Identidade
    cmatrixmax2 = confusion_matrix(y_testt[int(maxindices[0][1])],y_predidt[maxindices[0][1]])
    #### Pooled
    cmatrixmax3 = confusion_matrix(y_testt[int(maxindices[0][2])],y_predpt[maxindices[0][2]])
    #### Naive
    cmatrixmax4 = confusion_matrix(y_testt[int(maxindices[0][3])],y_prednt[maxindices[0][3]])
    
    resultados.append(mediaacertos[0][0])
    resultadosmax.append(maximo[0][0])
    resultadosmin.append(minimo[0][0])
    
t = np.arange(0, 6, 1)
plt.figure()
blue_patch = mpatches.Patch(color='blue', label='Média')
orange_patch = mpatches.Patch(color='orange', label='Valor Mínimo')
red_patch = mpatches.Patch(color='red', label='Valor Máximo')
plt.legend(handles=[blue_patch,orange_patch,red_patch])
line1 = plt.plot(t,resultados,color = 'blue')
line2 = plt.plot(t,resultadosmin,color = 'orange')
line3 = plt.plot(t,resultadosmax,color = 'red')
axes = plt.gca()
my_xticks = [90,80,60,50,40,10]
plt.xticks(t, my_xticks)
plt.ylabel('Taxa de Acerto')
plt.xlabel('Procentagem de teste')
plt.title('Classificador caso 3')


