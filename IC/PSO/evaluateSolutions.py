# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 10:44:15 2017

@author: Labvis
"""

import random
import math
import numpy as np
import os

def evaluateSolutions(particles):
    T,n = particles.shape
    y = np.zeros(T)
    
    for index in range(T):
        #y[index] = rosenbrock(particles[index])
        y[index] = rastringin(particles[index])
#        print(particles[index,:])
#        print(particles[index])
#        print(y)
#        os.system("pause")
    return y
        

def rosenbrock(x):
    
    y = ((1 - x[0])**2) + 100*((x[1] - ((x[0])**2))**2)
   
    return y

def rastringin(x):
    
    y = 20 + x[0]**2 + x[1]**2 -10*(math.cos(2*math.pi*x[0]) + math.cos(2*math.pi*x[1]))
    #print(y)
    
    return y