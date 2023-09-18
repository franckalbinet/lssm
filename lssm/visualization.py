# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_visualization.ipynb.

# %% auto 0
__all__ = ['plot_spectra']

# %% ../nbs/01_visualization.ipynb 3
from pathlib import Path

from .loading import load_ossl

import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

# %% ../nbs/01_visualization.ipynb 4
def plot_spectra(X, X_names, sample=50, 
                 ascending=True,
                 alpha=0.8, color='#333', 
                 xlabel='Wavenumber',
                 ylabel='Absorbance',
                 figsize=(20, 4)):
    sns.set_style("whitegrid")
    sns.despine()
    
    plt.figure(figsize=figsize)
    idx = np.random.randint(X.shape[0], size=sample)
    X = X[idx,:]
    
    _min, _max = np.min(X_names), np.max(X_names)
    _order = [_min, _max] if ascending else [_min, _max]
    plt.xlim(*_order)
    
    for i in range(X.shape[0]): 
        sns.lineplot(x=X_names, y=X[i,:], lw=1, c=color, alpha=alpha)
    
    plt.locator_params(axis="x", nbins=20)    
    plt.xlabel(xlabel)
    plt.ylabel(ylabel);
    
