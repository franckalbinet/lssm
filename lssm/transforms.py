# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/04_transforms.ipynb.

# %% auto 0
__all__ = ['GADFTfm', 'StatsTfm', 'SNVTfm']

# %% ../nbs/04_transforms.ipynb 3
from pathlib import Path

import numpy as np
import fastcore.all as fc

import torch
from torchvision import transforms as T


# %% ../nbs/04_transforms.ipynb 5
class GADFTfm(): 
    """
    Transform batch of spectra S (B, 1, len(S)) into their Grammian Difference Matrix Field (GADF) of shape (B, 1, H, W)
    
    Notes:
    https://arxiv.org/pdf/1506.00327.pdf
    """
    def __init__(self, neg=True):
        self.neg = neg
        
    def rescale(self, x):
        m = torch.min(x, dim=-1, keepdim=True).values
        M = torch.max(x, dim=-1, keepdim=True).values
        return ((x - M) + (x - m)) / (M - m) if self.neg else (x - m) / (M - m)

    def __call__(self, 
                 b # Batch of spectra S: (B, 1, len(S))
                 ): 
        x, y, *metadata = b
        X, I = self.rescale(x), torch.ones_like(x)
        K = torch.sqrt(I - torch.square(X))
        x = (torch.matmul(torch.transpose(K, 1, 2), X) - 
             torch.matmul(torch.transpose(X, 1, 2), K)).unsqueeze_(1)
        return x, y, *metadata

# %% ../nbs/04_transforms.ipynb 9
def _resizeTfm(b, size=224):
    "Resize image"
    x, y, *metadata  = b
    return T.Resize(size)(x), y, *metadata

# %% ../nbs/04_transforms.ipynb 11
class StatsTfm(): 
    """
    Set pre-trained statistics.
    """
    def __init__(self, 
                 cfgs
                 ):
        self.mean = np.array(cfgs['mean']).mean()
        self.std = np.array(cfgs['std']).mean()

    def __call__(self, b): 
        x, y, *metadata = b
        means = torch.mean(x, (2, 3), keepdim=True)
        stds = torch.std(x, (2, 3), keepdim=True)
        x = (((x - means) / stds) * self.std) + self.mean
        return x, y, *metadata

# %% ../nbs/04_transforms.ipynb 12
class SNVTfm(): 
    "Apply SNV to input or to both input and output when used with a Variational Auto-Encoder."
    def __init__(self, 
                 is_VAE:bool=False # If VAE apply SNV on both input and output.
                 ):
        self.is_VAE = is_VAE

    def _apply_snv(self, data):
        mean = torch.mean(data, axis=-1, keepdim=True)
        std = torch.std(data, axis=-1, keepdim=True)
        return (data - mean) / std
    
    def __call__(self, b): 
        if fc.isinstance_str(b, 'tuple'):
            x, y = b
            if self.is_VAE:
                b = torch.concat(b)
                b = self._apply_snv(b)
                bs = len(x)
                return b[:bs], b[bs:]
            else:
                x = self._apply_snv(x)
                return x, y
        else:
            return self._apply_snv(b)
