# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 08:52:58 2017

@author: Labvis
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from mpl_toolkits.mplot3d import Axes3D
import timeit
from copy import deepcopy
import math
from numpy import genfromtxt
from normaliza import normaliza
import os


def kmedias(data,k):
#data = genfromtxt('haberman.data', delimiter=',')
    base = data[:,0:data.shape[1]-1]
    
    #base = normaliza(base)
    
    colors = ['r', 'g', 'b', 'y', 'c', 'm']
    # Number of cluster
    
    C_1 = np.random.randint(np.min(base[:,0]), np.max(base[:,0]), size=k)
    
    C_2 = np.random.randint(np.min(base[:,1]), np.max(base[:,1]), size=k)
    
    C_3 = np.random.randint(np.min(base[:,2]), np.max(base[:,2]), size=k)
    
    
    C = np.array(list(zip(C_1, C_2,C_3)), dtype=np.float32)
    #print(C)
    
#    fig = plt.figure()
#    ax = fig.add_subplot(111, projection='3d')
##    
#    ax.scatter(base[:,0],base[:,1],base[:,2],c = 'r',marker = 'o')
#    
#    ax.set_xlabel('1 Atributo')
#    ax.set_ylabel('2 Atributo')
#    ax.set_zlabel('3 Atributo')
#    plt.title('Base de dados')
#    plt.show()
#    
    #clusters anteriores
    C_ant = np.zeros(C.shape)
    #error
    error = np.linalg.norm(C - C_ant , axis=1)
    #clusters
    clusters = np.zeros(len(base))
    ssdresults = []
    aux = math.inf
    test = 0
    while aux >= 0.001:

        for i in range(len(base)):
            distancias = np.linalg.norm(base[i,:] - C , axis=1)
            cluster = np.argmin(distancias)
            clusters[i] = cluster 
        C_ant = deepcopy(C)
        ssdresults.append(ssd(base,C))
       
#        fig = plt.figure()
#        ax1 = fig.add_subplot(111, projection='3d')
#        for i in range(k):
#            points = np.array([base[j,:] for j in range(len(base)) if clusters[j] == i])
#            ax1.scatter(points[:, 0], points[:, 1],points[:,2], s=7, c=colors[i])
#        ax1.scatter(C[:, 0], C[:, 1],C[:,2], marker='*', s=200, c='#050505')
#        ax1.set_xlabel('1 Atributo')
#        ax1.set_ylabel('2 Atributo')
#        ax1.set_zlabel('3 Atributo')
#        plt.title('Base de dados')
#        red_patch = mpatches.Patch(color='r', label='Grupo 1')
#        green_patch = mpatches.Patch(color='g', label='Grupo 2')
#        plt.legend(handles=[red_patch,green_patch])  
#        plt.show()
        for i in range(k):
            points = [base[j,:] for j in range(len(base)) if clusters[j] == i]
            C[i] = np.mean(points, axis=0)
        error = np.linalg.norm(C - C_ant,axis = 1)
        aux = np.sum(error)
            
            
    
   
    
    if k != 1:
        if all(x==clusters[0] for x in clusters):
            points,clusters,C,ssdresults = kmedias(data,k)
            return points,clusters,C,ssdresults
        
#    for i in range(k):
#            points = np.array([base[j,:] for j in range(len(base)) if clusters[j] == i])
#            ax.scatter(points[:, 0], points[:, 1],points[:,2], s=7, c=colors[i])
                 
#    ax.scatter(C[:, 0], C[:, 1],C[:,2], marker='*', s=200, c='#050505')
#    ax.set_xlabel('1 Atributo')
#    ax.set_ylabel('2 Atributo')
#    ax.set_zlabel('3 Atributo')
#    red_patch = mpatches.Patch(color='r', label='Grupo 1')
#    green_patch = mpatches.Patch(color='g', label='Grupo 2')
#    plt.legend(handles=[red_patch,green_patch])  
#    plt.title('Base de dados')
#    plt.show()
###    

    
    return points,clusters,C,ssdresults


def kmediasseq(data,k):
    
    base = np.array(data[:,0:data.shape[1]-1],dtype=np.float32)
    
    # Number of clusters
    C_1 = np.random.randint(np.min(base[:,0]), np.max(base[:,0]), size=k)
    
    C_2 = np.random.randint(np.min(base[:,1]), np.max(base[:,1]), size=k)
    
    C_3 = np.random.randint(np.min(base[:,2]), np.max(base[:,2]), size=k)
    
    
    C = np.array(list(zip(C_1, C_2,C_3)), dtype=np.float32)
    
    colors = ['r', 'g', 'b', 'y', 'c', 'm']
        
    #clusters anteriores
    C_ant = np.zeros(C.shape)
    #cluester
    clusters = np.zeros(len(base))
    #  
    distancias = np.zeros(k)
    ssdresults = []
    aux = math.inf
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    #ax.scatter(base[:,0],base[:,1],base[:,2],c = 'r',marker = 'o')
    
    ax.set_xlabel('1 Atributo')
    ax.set_ylabel('2 Atributo')
    ax.set_zlabel('3 Atributo')
    plt.title('Base de dados')
    plt.show()
    C_ant = deepcopy(C)
    while aux >= 0.001:
        for i in range(len(base)):
            for j in range(k): 
                distancias[j] = np.linalg.norm(base[i,:] - C[j])**2
            clusters[i] = np.argmax(distancias)
        C_ant = deepcopy(C)
        
        for i in range(len(base)):
            #print(C[clusters[i]])
            C[clusters[i]] = np.array(C[clusters[i]] + (1/np.sum(clusters==clusters[i]))*(base[i,:] - C[clusters[i]]),dtype=np.float32 )
            #print(C[clusters[i]])
        ssdresults.append(ssd(base,C))
        error = np.linalg.norm(C - C_ant,axis = 1)
        aux = np.sum(error)

    return clusters,C,ssdresults
    
def ssd(x,C):
    k = C.shape[0]
    aux =0
    ssd = np.zeros(k)
    #print(ssd)
    for j in range(k):
        for i in range(len(x)):
            aux = aux + np.linalg.norm((x[i] - C[j]))**2
        
        ssd[j] = aux
        aux = 0
    return np.sum(ssd)

def check(C):
    test = np.isnan(C).reshape(-1)
    for i in range(len(test)):
        if test[i] == True:
            return True
    return False