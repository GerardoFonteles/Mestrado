# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 09:37:27 2017

@author: Labvis
"""

import numpy as np
import sys
import os
import time
import random
import math
import evaluateSolutions
import matplotlib.pyplot as plt
import pylab
import time
import matplotlib.patches as mpatches
import timeit

N=100  # Tamanho da populacao
Ng=50   # Iterações
numVariables = 2 # num de variables
S = (N,numVariables)
F = 0.8
CR = 0.2

start = timeit.default_timer()

#kx = 2/(abs(2 - kp - sqrt(kp^2 - 4*kp)));
minValues = -5*np.ones(numVariables) 
maxValues = 5*np.ones(numVariables)
vellimit = 0.2*(maxValues - minValues)
particles = np.zeros(S) #Enxame
pbest = np.zeros(N)
v = np.zeros(S)
u = np.zeros(S)
globalbest = np.zeros(Ng)

minimo = np.zeros(Ng)
media = np.zeros(Ng)
auxiliar = (Ng,N)
iterationevolucion = np.zeros(auxiliar)

                    
for index in range(N): #Inicializacao das particulas
    particles[index,:] = minValues + (maxValues - minValues)*np.random.rand(1,numVariables)  

fitness = evaluateSolutions.evaluateSolutions(particles)

for index in range(Ng):
    fitness = evaluateSolutions.evaluateSolutions(particles)   
    for j in range(N):
        for k in range(1000):
            data1 = random.choice (particles)
            if (data1 != particles[k]).all():
                break
        
        for k in range(1000):
            data2 = random.choice (particles)
            if ((data2 != particles[k]).all() and (data2 != data1).all()):
                break
            
        for k in range(1000):
            data3 = random.choice(particles)
            if (((data3 != particles[k])).all() and (data3 != data1).all() and (data3 != data2).all()):
                break
            
        v[j] = data1 + F*(data3 - data2)#mutacao
        u[j] = particles[j]
        aux = random.random()
        if aux >= CR:
            u[j] = v[j]#cros
    fitness_u = evaluateSolutions.evaluateSolutions(u) 
    #os.system("pause")
    for i in range(N):
        if fitness_u[i] < fitness[i]:
            particles[i] = u[i]
    #print(particles[0,0])
   #os.system("pause")
    #if np.argmin(fitness) < globalbest[index]:
    globalbest[index] = fitness[np.argmin(fitness)]
#    plt.clf()
#   plt.figure() 
#    for j in range(N):     
#        plt.plot(particles[j,0],particles[j,1],'o')
#    axes = plt.gca()
#    axes.set_xlim([minValues[0],maxValues[1]])
#    axes.set_ylim([minValues[0],maxValues[1]])
#    plt.show() 
#    plt.pause(0.05)
    iterationevolucion[index] = fitness 
    minimo[index] = globalbest[index]
    media[index] = np.mean(fitness)

t = np.arange(0, Ng, 1)
plt.figure()
for p in range(N):
    plt.plot(t,np.sort(iterationevolucion[:,p])[::-1])

plt.figure()
blue_patch = mpatches.Patch(color='blue', label='Aptidão média')
orange_patch = mpatches.Patch(color='orange', label='Melhor Indivíduo')
plt.legend(handles=[blue_patch,orange_patch])
plt.plot(t,minimo,color = 'orange')
plt.plot(t,media,color = 'blue')
print(minimo[index])

stop = timeit.default_timer()

tempo =  stop - start 
    
    #os.system("pause")
    
    
    
       
    