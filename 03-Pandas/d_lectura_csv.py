# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 17:55:28 2020

@author: LENOVO
"""
import pandas as pd
import os

path = "./data/artwork_data.csv"

df1 = pd.read_csv(
    path,
    nrows = 10)

#definir columnas a usar
columnas = ['id', 'artist', 'title',
            'medium', 'year', 
            'acquisitionYear', 'height',
            'width', 'units']

df2 = pd.read_csv(
    path,
    nrows=10,
    usecols = columnas)
#para q otra columna se fije como indice
df3 = pd.read_csv(
    path,
    usecols = columnas,
    index_col = 'id')


#para guardar los datos generados
path_guardado = "./data/artwork_data.pickle"

df3.to_pickle(path_guardado)

df4 = pd.read_pickle(path_guardado)
















































