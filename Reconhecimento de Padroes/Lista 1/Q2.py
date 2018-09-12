# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 08:45:04 2017

@author: Labvis
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

x = np.arange(0,2.1,0.1)
y = np.ones(x.size)
t = np.arange(0,2.1,0.1)
gamma = 0.5


z = np.exp(-gamma*(np.transpose(x-y)*(x-y)))
z2 = 1/(1+(np.abs(x-y))**2)

plt.figure()
blue_patch = mpatches.Patch(color='blue', label='Exponencial')
orange_patch = mpatches.Patch(color='orange', label='Fração')
plt.legend(handles=[blue_patch,orange_patch])
plt.plot(t,z,color = 'orange')
plt.plot(t,z2,color = 'blue')
