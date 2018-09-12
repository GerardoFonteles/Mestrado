# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 12:14:50 2017

@author: JoseGerardo
"""

from scipy.spatial import distance

def compute_s(i, x, labels, clusters):
    
	s = 0
	for x in clusters:
		# print x
		s += distance.euclidean(x, clusters[i])#calcula a distancia a soma das distancias
	return s

def compute_Rij(i, j, x, labels, clusters, nc):#Calcula o Rij 
	Rij = 0
	try:
		# print "h"
		d = distance.euclidean(clusters[i],clusters[j])
		#print(d)
		Rij = (compute_s(i, x, labels, clusters) + compute_s(j, x, labels, clusters))/d
		#print(Rij)
	except:
		Rij = 0	
	return Rij

def compute_R(i, x, labels, clusters, nc): 
	list_r = []
	for i in range(nc):
		for j in range(nc):
			if(i!=j):
				temp = compute_Rij(i, j, x, labels, clusters, nc)
				list_r.append(temp)

	return max(list_r)

def compute_DB_index(x, labels, clusters, nc):
	# print x
	sigma_R = 0.0
	for i in range(nc):
		sigma_R = sigma_R + compute_R(i, x, labels, clusters, nc)

	DB_index = float(sigma_R)/float(nc)
	return DB_index
