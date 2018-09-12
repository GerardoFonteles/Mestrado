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
import timeit
import matplotlib.pyplot as plt
import pylab
import time

def PSO_regressao(N,Ng,k):
    start = timeit.default_timer()
    numVariables = k+1 # num de variables
    S = (N,numVariables)
    
    data = np.loadtxt('aerogerador.dat')
    #plt.plot(data[:,0],data[:,1],'o')
    volt = data[:,0]#Velocidade
    p = data[:,1]#Potência
    wInit = 0.9
    # Parâmetro de inércia final
    wFinal = 0.4
    # Parâmetros de alteração de velocidade
    c1 = 2.05
    c2 = 2.05
    #kp =c1 + c2
    #kx = 2/(abs(2 - kp - sqrt(kp^2 - 4*kp)));
    
    
    minValues = -100*np.ones(numVariables) 
    maxValues = 100*np.ones(numVariables)
    vellimit = 0.2*(maxValues - minValues)
    particles = np.zeros(S) #Enxame
    pbest = np.zeros(N)
    v = np.zeros(S)
    
                        
    for index in range(N): #Inicializacao das particulas
        particles[index,:] = minValues + (maxValues - minValues)*np.random.rand(1,numVariables)
    
    fitness = evaluateSolutions.evaluateSolutions(particles,volt,p,k)#calcula o fitness
    pbest = particles    #melhores posicoes atuais
    bestvalues = fitness #melhores resultados
    globalbest = math.inf
    gbest = particles[np.argmin(fitness),:]#melhor global encontrado
    iterationevolucion = np.zeros(Ng)
    
    w = wInit                 
    # calculo da velocidade e atualizacao da posicao                  
    for index in range (N):
        v[index] = w*v[index] + c1*np.random.rand(1)*(pbest[index] - particles[index]) + c2*np.random.rand(1)*(gbest-particles[index])
        
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
    
    #os.system("pause")
    #algoritmo sendo rodado Ng vezes
    for index in range (Ng):  
        fitness = evaluateSolutions.evaluateSolutions(particles,volt,p,k)
        for i in range (N):#atualiazacao do pbest, melhores fitness e global    
            if fitness[i] < bestvalues[i]:
                bestvalues[i] = fitness[i]
                pbest[i] = particles[i]
            if  fitness[i] < globalbest:
                globalbest = fitness[i]
                gbest = particles[np.argmin(bestvalues),:]
                #print("AQUI")
                #print(globalbest)
#                print(gbest)
#                print(globalbest)
#                print("Here")
        
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
        #os.system("pause")
#        plt.clf()    
#        for j in range(N):     
#            plt.plot(particles[j,0],particles[j,1],'o')
#            plt.plot(particles[np.argmin(bestvalues),0],particles[np.argmin(bestvalues),1],'r*')
#        axes = plt.gca()
#        axes.set_xlim([minValues[0],maxValues[1]])
#        axes.set_ylim([minValues[0],maxValues[1]])
#        plt.show() 
#        plt.pause(0.0001)
        iterationevolucion[index] = globalbest
        #print((Ng - index)/(Ng - 1))
    
   # plt.figure()
    #t = np.arange(0, Ng, 1)
    #plt.plot(t,iterationevolucion,'-b')
        #os.system("pause")
    stop = timeit.default_timer()
    tempo = stop - start
    print("tempo do PSO:")
    print(tempo)
    return gbest
        

    

  