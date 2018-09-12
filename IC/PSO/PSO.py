# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 09:37:27 2017

@author: Labvis
"""

import numpy as np
import sys
import math
import evaluateSolutions
import matplotlib.pyplot as plt
import timeit
import matplotlib.patches as mpatches

start = timeit.default_timer()
N=100 # Tamanho da populacao
Ng=50  # Iterações
numVariables = 2 # num de variables
S = (N,numVariables)

wInit = 0.9
# Parâmetro de inércia final
wFinal = 0.4
# Parâmetros de alteração de velocidade
c1 = 2.05
c2 = 2.05
kp =c1 + c2
#kx = 2/(abs(2 - kp - sqrt(kp^2 - 4*kp)));


minValues = -5*np.ones(numVariables) 
maxValues = 5*np.ones(numVariables)
vellimit = 0.2*(maxValues - minValues)
particles = np.zeros(S) #Enxame
pbest = np.zeros(N)
v = np.zeros(S)
media = np.zeros(Ng)
minimo = np.zeros(Ng)
                    
for index in range(N): #Inicializacao das particulas
    particles[index,:] = minValues + (maxValues - minValues)*np.random.rand(1,numVariables)

fitness = evaluateSolutions.evaluateSolutions(particles)#calcula o fitness
pbest = particles    #melhores posicoes atuais
bestvalues = fitness #melhores resultados
#globalbest = np.argmin(fitness)
globalbest = math.inf
gbest = particles[np.argmin(fitness),:]#melhor global encontrado

auxiliar = (Ng,N)                  
iterationevolucion = np.zeros(auxiliar)

w = wInit                 
# calculo da velocidade e atualizacao da posicao                  
for index in range (N):
    v[index] = v[index] + c1*np.random.rand(1)*(pbest[index] - particles[index]) + c2*np.random.rand(1)*(gbest-particles[index])
    
    for t in range(numVariables):
            if v[index,t] > vellimit[t]:
                v[index,t] = vellimit[t]
            if v[index,t] < -vellimit[t]:
                v[index,t] = -vellimit[t]
    particles[index] = particles[index] + v[index]
    
    for t in range(numVariables):
            if particles[index,t] > maxValues[t]:
                particles[index,:] = minValues + (maxValues - minValues)*np.random.rand(1,numVariables)                  
            if particles[index,t] < vellimit[t]:
                particles[index,:] = minValues + (maxValues - minValues)*np.random.rand(1,numVariables) 
#algoritmo sendo rodado Ng vezes
for index in range (Ng):  
    fitness = evaluateSolutions.evaluateSolutions(particles)
    for k in range (N):#atualiazacao do pbest, melhores fitness e global    
        if fitness[k] < bestvalues[k]:
            bestvalues[k] = fitness[k]
            pbest[k] = particles[k]
        if  fitness[k] < globalbest:
            globalbest = fitness[k]
            gbest = particles[np.argmin(bestvalues),:]
    
    for j in range (N):
        v[j] = w*v[j] + c1*np.random.rand(1)*(pbest[j] - particles[j]) + c2*np.random.rand(1)*(gbest-particles[j])
        for t in range(numVariables):
            if v[j,t] > vellimit[t]:
                v[j,t] = vellimit[t]
            if v[j,t] < -vellimit[t]:
                v[j,t] = -vellimit[t]
    particles = particles + v
    for j in range (N):
        for t in range(numVariables):
            if particles[j,t] > maxValues[t]:
                particles[j,:] = minValues + (maxValues - minValues)*np.random.rand(1,numVariables)                  
            if particles[j,t] < minValues[t]:
                particles[j,:] = minValues + (maxValues - minValues)*np.random.rand(1,numVariables)   
    w = wFinal + (wInit - wFinal)*(Ng - index)/(Ng - 1);
    plt.clf()    
    for j in range(N):     
        plt.plot(particles[j,0],particles[j,1],'o')
        plt.plot(particles[np.argmin(bestvalues),0],particles[np.argmin(bestvalues),1],'k*')
    axes = plt.gca()
    axes.set_xlim([minValues[0],maxValues[1]])
    axes.set_ylim([minValues[0],maxValues[1]])
    plt.show() 
    plt.pause(0.05)
    iterationevolucion[index] = fitness
    
    media[index] = np.mean(fitness)
    minimo[index] = globalbest
    print(globalbest)
    
plt.figure()
t = np.arange(0, Ng, 1)

for p in range(N):
    plt.plot(t,np.sort(iterationevolucion[:,p])[::-1])   
axes = plt.gca()
axes.set_xlim(0,Ng)


plt.figure()
blue_patch = mpatches.Patch(color='blue', label='Aptidão média')
orange_patch = mpatches.Patch(color='orange', label='Melhor Indivíduo')
plt.legend(handles=[blue_patch,orange_patch])
line1 = plt.plot(t,np.sort(media)[::-1],color = 'blue')
line2 = plt.plot(t,minimo,color = 'orange')
axes = plt.gca()
axes.set_xlim(0,Ng)

stop = timeit.default_timer()

tempo =  stop - start 