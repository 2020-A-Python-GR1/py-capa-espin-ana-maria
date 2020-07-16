# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 08:13:23 2020

@author: LENOVO
"""
# b_series.py
import numpy as np
import pandas as pd

lista_numeros = [1,2,3,4]
tupla_numeros = (1,2,3,4)
np_numeros = np.array((1,2,3,4))

#para hacer series
series_a = pd.Series(
    lista_numeros)

series_b = pd.Series(
    tupla_numeros)

series_c = pd.Series(
    np_numeros)

series_d = pd.Series(
    [True,
    False,
    12,
    12,12,
    "aNA",
    None,
    (1),
    [1],
    {"nombre","Ana"}
    ]  
    )

print(series_d[3])

lista_ciudades = [
    "AMBATO",
    "Loja",
    "Quito",
    "Guayaquil"]
serie_ciudades = pd.Series(
    lista_ciudades,
    index = [
        "A",
        "L",
        "Q",
        "G"])
print(serie_ciudades[3])

valores_ciudad = {
    "Ibarra": 9500,
     "Guayaquil": 10000,
     "Cuenca": 7000
     }

series_valor_ciudad = pd.Series(
     valores_ciudad)

ciudad_menor_5k = series_valor_ciudad < 5000

print(type(series_valor_ciudad)) #panda.core.series
print(type(ciudad_menor_5k)) 
print(ciudad_menor_5k)

s5 = series_valor_ciudad[ciudad_menor_5k]

series_valor_ciudad = series_valor_ciudad * 1.1
series_valor_ciudad["Cuenca"] = series_valor_ciudad["Cuenca"] - 50

print("Lima" in series_valor_ciudad)


  
  
  



