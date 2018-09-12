# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 09:34:19 2017

@author: Labvis
"""

import numpy as np
from numpy.linalg import inv
from io import StringIO
from scipy.spatial.distance import pdist


x = np.asarray([80.07 ,48.07, 52.40, 32.01])
ms = np.asarray([51.69 ,12.82, 43.54, 38.86])
me = np.asarray([71.51 ,20.75, 64.11, 50.77])
mh = np.asarray([47.64 ,17.40, 35.46, 30.24])
distancia = np.zeros(3)

distancia[0] = np.linalg.norm(x-ms)
distancia[1] = np.linalg.norm(x-me)
distancia[2] = np.linalg.norm(x-mh)

resultado = np.argmin(distancia)
         



