# -*- coding: utf-8 -*-
"""
Created on Wed May  3 10:41:49 2017

@author: Labvis
"""

import numpy as np
import sys
import os
import time
import random
import math
#import evaluateSolutions
import matplotlib.pyplot as plt
import pylab
import time
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter



fig = plt.figure()
ax = fig.gca(projection='3d')

X = np.arange(-5.5,5.5,0.1)
Y = np.arange(-5.5,5.5,0.1)
X, Y = np.meshgrid(X, Y)
R = 20 + X**2 + Y**2 -10*(np.cos(2*math.pi*X) + np.cos(2*math.pi*Y))

surf = ax.plot_surface(X, Y, R, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)


plt.figure()
plt.contour(X,Y,R)
plt.show()