# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

import numpy as np
import sys
import aptidao
#import aptidao2
import selecao
import matplotlib.patches as mpatches
import cruzamento
import mutacao
import matplotlib.pyplot as plt
import timeit

start = timeit.default_timer()

#Parametros do AG
N=30;    # Tamanho da populacao
M=22;     # Tamanho do cromossomo (no. de genes)
pc=0.5;  # Probabilidade de cruzamento
pm=0.01; # Probabilidade de mutacao
Ng=50;   # Numero de geracoes
S = (Ng,N)
iterationevolucion = np.zeros(S)
media = np.zeros(Ng)
minimo = np.zeros(Ng)

#os.mkdir('C:/Users/Labvis/Desktop/IC/trabalho1/Questao1/')

#Geracao da populacao inicial 
#P = np.matrix.round(particles)
P = np.matrix.round(np.random.rand(N,M),0);

X,F,Fn = aptidao.aptidao(P)
F_results = np.zeros(Ng)
F_resultsmax = np.zeros(Ng)
#print X,F,Fn


# Roda AG por Ng geracoes

for index in range(Ng):
    geracao = index
    #print (geracao)
    S = selecao.selecao_torneio(P,Fn)
    P = cruzamento.cruzamento(P,S,pc)
    P = mutacao.mutacao(P,pm)
    #X,F,Fn = aptidao.aptidao(P)
    X,F,Fn = aptidao.aptidao(P)
    #F_results[index] = min(F)
    #F_resultsmax[index] = max(F) 
    #print X
    
    iterationevolucion[index] = F
    minimo[index] = np.min(F)
    media[index] = np.mean(F)
    #print "\n"
#    P = P2

plt.figure()
t = np.arange(0, Ng, 1)
for p in range(N):
    plt.plot(t,np.sort(iterationevolucion[:,p])[::-1])   
axes = plt.gca()
axes.set_xlim(0,Ng)
#plt.savefig('C:/Users/Labvis/Desktop/IC/trabalho1/Questao1/',encoding='utf-8',format='eps', dpi=1000)

plt.figure()

t = np.arange(0, Ng, 1)
blue_patch = mpatches.Patch(color='blue', label='Aptidão média')
orange_patch = mpatches.Patch(color='orange', label='Melhor Indivíduo')
plt.legend(handles=[blue_patch,orange_patch])
line1 = plt.plot(t,np.sort(media)[::-1],color = 'blue')
line2 = plt.plot(t,np.sort(minimo)[::-1],color = 'orange')
axes = plt.gca()
axes.set_xlim(0,Ng)

stop = timeit.default_timer()
tempo = stop - start