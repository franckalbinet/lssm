# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/02_preprocessing.ipynb.

# %% auto 0
__all__ = ['ToAbsorbance', 'ContinuumRemoval', 'SNV']

# %% ../nbs/02_preprocessing.ipynb 3
from pathlib import Path
from tqdm import tqdm

from .loading import load_ossl
from .visualization import plot_spectra

import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from scipy.spatial import ConvexHull
from scipy.interpolate import interp1d


# %% ../nbs/02_preprocessing.ipynb 5
class ToAbsorbance(BaseEstimator, TransformerMixin):
    """Transform Reflectance to Absorbance"""
    def __init__(self, eps=1e-5): self.eps = eps
    def fit(self, X, y=None): return self
    def transform(self, X, y=None): 
        X[X < 0] = 0
        return -np.log10(X + self.eps)

# %% ../nbs/02_preprocessing.ipynb 9
class ContinuumRemoval(BaseEstimator, TransformerMixin):
    """Creates continnum removal custom transformer"""

    def __init__(self, wls):
        self.wls = wls

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        continuum_removed_spectra = np.zeros_like(X)
        
        for i, spectrum in enumerate(tqdm(X)):
            points = np.c_[self.wls, spectrum]
            x, y = points.T 
            # trick to exclude lower part of convex hull 
            augmented = np.concatenate([points, [(x[0], np.max(y)+1), (x[-1], np.max(y)+1)]], axis=0)
            hull = ConvexHull(augmented)
            continuum_points = points[np.sort([v for v in hull.vertices if v < len(points)])]
            continuum_function = interp1d(*continuum_points.T)
            continuum_removed_spectra[i, :] = y / continuum_function(x)
    
        return continuum_removed_spectra

# %% ../nbs/02_preprocessing.ipynb 12
class SNV(BaseEstimator, TransformerMixin):
    """Creates scikit-learn SNV custom transformer"""
    def fit(self, X, y=None): return self
    def transform(self, X, y=None):
        mean, std = np.mean(X, axis=1).reshape(-1, 1), np.std(X, axis=1).reshape(-1, 1)
        return (X - mean)/std
