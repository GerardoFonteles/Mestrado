# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 14:15:08 2017

@author: Labvis
"""

import numpy as np
import matplotlib.pyplot as plt

k = np.linspace(-5, 5, 100)
r = np.zeros(len(k))

for i in range(len(k)):
    r[i] = -np.sqrt(6)/(np.sqrt(3)*np.sqrt(k[i]))

plt.plot(r)