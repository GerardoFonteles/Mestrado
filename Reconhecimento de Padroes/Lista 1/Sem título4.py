# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 15:27:48 2017

@author: Labvis
"""

import numpy as np
from numpy.linalg import inv
from io import StringIO
from scipy.spatial.distance import pdist


X = np.array([[1,-0.6,0.4],[-0.6,9,-0.5],[0.4,-0.5,4]])

coef = X[1,2]/(X[1,1]*X[2,2])

#Coeficiente a da reta
a = (X[2,2]/X[1,1])*coef

#Coeficiente de b
b = np.mean(X,axis=2) - a*np.mean(X,axis=1)