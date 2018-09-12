# -*- coding: utf-8 -*-
"""
Created on Mon May  8 09:11:21 2017

@author: Labvis
"""
import numpy as np
import sys
import os
import time
import random
import math
import matplotlib.pyplot as plt
import pylab
import time
from numpy.linalg import inv
from PSO_regressao import PSO_regressao
from DE_regressao import DE_regressao
import matplotlib.patches as mpatches

data = np.loadtxt('aerogerador.dat')
plt.plot(data[:,0],data[:,1],'o')
v = data[:,0]#Velocidade
p = data[:,1]#Potência
N=100# Tamanho da populacao
Ng=125 # Iterações
k=4#ordem do polinomio
T = []
A = np.zeros(k+1)
n = len(v)
y = p#vetor de observações
S = (n,k+1)
X = np.zeros(S)

aux = []

#Método Utilizando a fórmula direto da inversão de matrizes
for j in range(k+1):
    aux = np.power(v,j)
    X[:,j] = aux #Matriz 

B = np.dot(np.dot(inv(np.dot((np.transpose(X)),X)),np.transpose(X)),y)#vetor de coeficientes 
print(B)

ypred = np.dot(X,B)
erro = y - ypred
SEQ = sum(np.power(erro,2))
ymed = np.mean(y)
Syy = sum(np.power(y-ymed,2))
R = 1 - SEQ/Syy
#print(R)


for t in range(1000):
    A = PSO_regressao(N,Ng,k)#metodo para o calculo do PSO
    print(A)
    ypred = np.dot(X,A)
    erro = y - ypred
    SEQ1 = sum(np.power(erro,2))
    ymed = np.mean(y)
    Syy = sum(np.power(y-ymed,2))
    R1 = 1 - SEQ1/Syy
    if R1 > 0.97:
        break

print(SEQ1)

for m in range(1000):    
    C = DE_regressao(N,Ng,k)#metodo para o calculo do DE
    print(C)
    ypred = np.dot(X,C)
    erro = y - ypred
    SEQ2 = sum(np.power(erro,2))
    ymed = np.mean(y)
    Syy = sum(np.power(y-ymed,2))
    R2 = 1 - SEQ2/Syy
    if R2 > 0.97:
        break

print(SEQ2)

Z = np.polyfit(v,p,k)#Funcao polyfit do phyton
F = np.poly1d(Z)
erro = F(v) - p
SEQ3 = sum(np.power(erro,2))
ymed = np.mean(y)
Syy = sum(np.power(y-ymed,2))
R3 = 1 - SEQ3/Syy
print(SEQ3)

vv = np.arange(v[np.argmin(v)],v[np.argmax(v)],0.1)
vv = np.transpose(vv)
T = (len(vv),k+1)
XX = np.zeros(T)
for j in range(k+1):
        aux = np.power(vv,j)
        XX[:,j] = aux

ypred2 = np.dot(XX,A)
plt.plot(vv,ypred2,'r-')

plt.plot(vv,F(vv),'y-')
#plt.show()
#Plot dos graficos
ypred2 = np.dot(XX,C)
plt.plot(vv,ypred2,'k-')
red_patch = mpatches.Patch(color='red', label='PSO')
yellow_patch = mpatches.Patch(color='yellow', label='Polifit')
black_patch =  mpatches.Patch(color='black', label='DE')
plt.legend(handles=[red_patch,yellow_patch,black_patch])
plt.xlabel('Velocidade do vento')
plt.ylabel('Potência')
plt.title('Regressão')
plt.show()

#Dados do aerogerador
plt.figure()
plt.plot(data[:,0],data[:,1],'o')
plt.xlabel('Velocidade do vento')
plt.ylabel('Potência')

print((np.sum(np.power(A,2)))**0.5)
print((np.sum(np.power(C,2)))**0.5)
