# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 15:27:48 2017

@author: Labvis
"""
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import matplotlib.patches as mpatches
from scipy.stats import norm, chi2


def cov_ellipse(cov, q=None, nsig=None, **kwargs):
    
    if q is not None:
        q = np.asarray(q)
    elif nsig is not None:
        q = 2 * norm.cdf(nsig) - 1

    r2 = chi2.ppf(q, 2)

    val, vec = np.linalg.eigh(cov)
    width, height = 2 * np.sqrt(val[:, None] * r2)
    rotation = np.degrees(np.arctan2(*vec[::-1, 0]))

    return width, height, rotation

def plot_point_cov(points, nstd=2, ax=None, **kwargs):
    
    #Calcula a média dos dados
    pos = points.mean(axis=0)
    #calcula a matriz de covariância dos dados
    cov = np.cov(points, rowvar=False)
    #Retorno da função será as elipses
    return plot_cov_ellipse(cov, pos, nstd, ax, **kwargs)

def plot_cov_ellipse(cov, pos, nstd, ax=None, **kwargs):
    def eigsorted(cov):
        #calcula os autovalores e autovetores
        vals, vecs = np.linalg.eigh(cov)
        #ordena os valores de autovetores 
        order = vals.argsort()[::-1]
        return vals[order], vecs[:,order]

    if ax is None:
        ax = plt.gca()
    
    #Calcula os valores e os ângulos
    vals, vecs = eigsorted(cov)
    theta = np.degrees(np.arctan2(*vecs[:,0][::-1]))

    #Calcula a altura e a largura
    width, height, theta = cov_ellipse(cov,nstd,ax)
    #Forma a elipse
    ellip = Ellipse(xy=pos, width=width, height=height, angle=theta, **kwargs)
    #ellip.set_facecolor('NONE')
    ax.add_artist(ellip)
    #ax.add_artist(plt.quiver(pos[0],pos[1],vecs[0],vecs[1],color = 'orange')) 
    return ellip

if __name__ == '__main__':
    # Gera dados com a dispersão da matriz de covariancia 
    dados = np.random.multivariate_normal(mean=(1,1), cov=[[9,-0.5],[-0.5,4]], size=1000)
    x, y= dados.T
    
    covariance = np.cov(x,y)
    vals, vecs = np.linalg.eigh(covariance)
    
    coeficiente = covariance[0,1]/(np.sqrt(covariance[0,0])*np.sqrt(covariance[1,1]))
    
    ##Plota os dados
    plt.plot(x, y, '+',color = 'blue')

    #Plota a elipse com diferentes valores de desvio
    plot_point_cov(dados, nstd=0.95, alpha=2, color='#FF6347')
    plot_point_cov(dados, nstd=0.68, alpha=1, color='red')
    plt.axis([-10, 12, -10, 10])
    
    autovalor, autovetores = np.linalg.eig(covariance)
    
    #Calculo da reta
    a = (covariance[1,1]/covariance[0,0])*coeficiente
    b = np.mean(y) - a*np.mean(x)
    x = np.arange(-9,12, dtype=np.float)
    y = a*x + b
    blue_patch = mpatches.Patch(color='blue', label='Dados')
    orange_patch = mpatches.Patch(color='red', label='Curvas de Contornos')
    green_patch = mpatches.Patch(color='green', label='Linha de tendência')
    plt.legend(handles=[blue_patch,orange_patch,green_patch],loc = 1)
    plt.plot(x,y,'g--')
    plt.show()