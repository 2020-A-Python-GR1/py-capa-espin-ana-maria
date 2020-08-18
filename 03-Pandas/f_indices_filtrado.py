# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 07:32:56 2020

@author: LENOVO
"""


# f_indices_filtrado.py

import pandas as pd

path_guardado = "./data/artwork_data.pickle"
df = pd.read_pickle(path_guardado)

serie_artistas_dup = df ['artist']
# solo contiene las columnas no repetidas o unicas
artistas = pd.unique(serie_artistas_dup)

type(artistas)# numpy array

print(artistas.size)
print(len(artistas))

# para filtrar por obras
blake = df['artist'] == 'Blake, William'#esto es una serie

print(blake.value_counts())

df_blake = df[blake] #dataframe






























