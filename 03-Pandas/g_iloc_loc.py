# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 07:58:22 2020

@author: LENOVO
"""
#g_iloc_loc .py

import pandas as pd

path_guardado = "./data/artwork_data.pickle"

df = pd.read_pickle(path_guardado)

# loc, cogemos un registro
# mandamos el indice y devuelve la serie

filtrado_horizontal = df.loc[1035] # serie
print(filtrado_horizontal)
print(filtrado_horizontal['artist'])
print(filtrado_horizontal.index) # Indices columnas

serie_vertical = df['artist']
print(serie_vertical)
print(serie_vertical.index)#Indices son los indices

# filtrado por indice
df_1035 = df[df.index == 1035]
segundo = df.loc[1035] # filtrar por indice (1)
segundo = df.loc[[1035,1036]] # filtrar x arreglo de indice

segundo = df.loc[3:5] # Filtrar desde "x" indice 
                      # hasta y indice

segundo = df.loc[df.index == 1035]# fitrar por un 
                                  # arreglo -->True y FALSE

segundo = df.loc[1035, 'artist'] # 1 indice
segundo = df.loc[1035, ['artist', 'medium']] # varios indices

                    
# para este caso estamos mandando 
 # primero = df.loc[1035, 'artist']

tercero = df.iloc[0]
tercero = df.iloc[[0,1]]
tercero = df.iloc[0:10]
tercero = df.iloc[df.index == 1035]

tercero = df.iloc [0:10, 0:4]# filtrado indices
# por rango de indices 0:4





























