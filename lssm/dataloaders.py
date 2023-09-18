# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/03_dataloaders.ipynb.

# %% auto 0
__all__ = ['SpectralDataset', 'get_dls']

# %% ../nbs/03_dataloaders.ipynb 3
from pathlib import Path
from tqdm import tqdm
from collections import namedtuple
import fastcore.all as fc

from torch.utils.data import Dataset, DataLoader

# %% ../nbs/03_dataloaders.ipynb 5
class SpectralDataset(Dataset):
    def __init__(self, X, y, metadata=None):
        self.X = X
        self.y = y
        self.metadata = metadata
        
    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        return self.X[idx,:][None,:], self.y[idx,:]

# %% ../nbs/03_dataloaders.ipynb 6
def get_dls(train_ds, valid_ds, bs, **kwargs):
    Dataloaders = namedtuple('Dataloader', ['train', 'valid'])
    return Dataloaders(
        DataLoader(train_ds, batch_size=bs, shuffle=True, **kwargs),
        DataLoader(valid_ds, batch_size=bs*2, **kwargs)) 
