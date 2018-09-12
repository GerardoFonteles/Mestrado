# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 11:29:46 2017

@author: Labvis
"""

import numpy as np

def normaliza(dados):
    normalizado = (dados - np.mean(dados))/np.std(dados)
    return normalizado