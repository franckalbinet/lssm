# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_loading.ipynb.

# %% auto 0
__all__ = ['load_ossl']

# %% ../nbs/00_loading.ipynb 3
from pathlib import Path
from tqdm import tqdm
from typing import Union, List

import pandas as pd
from sklearn.preprocessing import LabelEncoder

import warnings
warnings.filterwarnings('ignore')

# %% ../nbs/00_loading.ipynb 4
def load_ossl(fname: Path,  # Path to OSSL gzipped csv dump
              # Using OSSL's analytes naming conventions
              analytes: Union[str, List[str]],
              spectra_type: str,  # Possible values: 'mir', 'visnir'
              ):
    analytes = [analytes] if isinstance(analytes, str) else analytes
    df = pd.read_csv(fname, compression='infer', low_memory=True)

    scan_repr = {'visnir': 'scan_visnir.350_ref', 'mir': 'scan_mir.600_abs'}
    subset = analytes + [scan_repr[spectra_type]]
    df = df.dropna(subset=subset)

    cols_ref = [name for name in df.columns if f'scan_{spectra_type}.' in name]
    X = df[cols_ref].values

    y = df[analytes].values
    smp_idx = df['id.layer_uuid_txt'].values

    ds_name_encoder = LabelEncoder()
    ds_name = ds_name_encoder.fit_transform(df['dataset.code_ascii_txt'])

    return X, y, smp_idx, ds_name, ds_name_encoder.classes_

