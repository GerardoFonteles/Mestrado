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
import timeit

def DE_regressao(N,Ng,k):
    start = timeit.default_timer()
    numVariables = k+1 # num de variables
    S = (N,numVariables)
    F = 0.2
    CR = 0.5
    
    #kx = 2/(abs(2 - kp - sqrt(kp^2 - 4*kp)));
    data = np.loadtxt('aerogerador.dat')
    #plt.plot(data[:,0],data[:,1],'o')
    volt = data[:,0]#Velocidade
    p = data[:,1]#Potência
    minValues = -100*np.ones(numVariables) 
    maxValues = 100*np.ones(numVariables)
    particles = np.zeros(S) #Enxame
    v = np.zeros(S)
    u = np.zeros(S)
    globalbest = np.zeros(Ng)
                        
    for index in range(N): #Inicializacao das particulas
        particles[index,:] = minValues + (maxValues - minValues)*np.random.rand(1,numVariables)  
    
    fitness = evaluateSolutions.evaluateSolutions(particles,volt,p,k)
    
    for index in range(Ng):
        fitness = evaluateSolutions.evaluateSolutions(particles,volt,p,k)   
        for j in range(N):
            for i in range(1000):
                data1 = random.choice (particles)
                if (data1 != particles[i]).all():
                    break
            
            for i in range(1000):
                data2 = random.choice (particles)
                if ((data2 != particles[i]).all() and (data2 != data1).all()):
                    break
                
            for i in range(1000):
                data3 = random.choice(particles)
                if (((data3 != particles[i])).all() and (data3 != data1).all() and (data3 != data2).all()):
                    break
                
            v[j] = data1 + F*(data3 - data2)#mutacao
            u[j] = particles[j]
            aux = random.random()
            if aux >= CR:
                u[j] = v[j]#cros
        fitness_u = evaluateSolutions.evaluateSolutions(u,volt,p,k) 
        #os.system("pause")
        for i in range(N):
            if fitness_u[i] < fitness[i]:
                particles[i] = u[i]
        #print(particles[0,0])
       #os.system("pause")
        #if np.argmin(fitness) < globalbest[index]:
        globalbest[index] = fitness[np.argmin(fitness)]
       # print((Ng - index)/(Ng - 1))
        #print(globalbest[index])
        #plt.clf()
    #   plt.figure() 
    #    for j in range(N):     
    #        plt.plot(particles[j,0],particles[j,1],'o')
    #    axes = plt.gca()
    #    axes.set_xlim([minValues[0],maxValues[1]])
    #    axes.set_ylim([minValues[0],maxValues[1]])
    #    plt.show() 
    #    plt.pause(0.05)
    #    print(globalbest[index])
        #print(particles[np.argmin(fitness)])

    #plt.figure()
    #t = np.arange(0, Ng, 1)
    #plt.plot(t,globalbest,'-b')
    stop = timeit.default_timer()
    tempo = stop - start
    print("tempo do De:")
    print(tempo)    
    return particles[np.argmin(fitness)]
        
        #os.system("pause")
        
        
        
           
    