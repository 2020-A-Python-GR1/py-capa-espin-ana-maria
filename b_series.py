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

svc_cuadrado = np.square(series_valor_ciudad)

ciudades_uno = pd.Series({
    "Montañita": 300,
    "Guayaquil": 10000,
    "Quito": 2000})

ciudades_dos = pd.Series({
    "Loja": 300,
    "Guayaquil": 10000})

ciudades_uno["Loja"] = 0

print(ciudades_uno + ciudades_dos)

ciudades_add = ciudades_uno.add(ciudades_dos)

#ciud_concat = pd.append([
 #   ciudades_uno,
  #  ciudades_dos])

ciud_concat_verify = ciudades_uno.append([
    ciudades_dos],
    verify_integrity =  False)

#devolver mayor valor
print (ciudades_uno.max())
print (pd.Series.max(ciudades_uno))
print (np.max(ciudades_uno))

print (ciudades_uno.min())
print (pd.Series.min(ciudades_uno))
print (np.min(ciudades_uno))

#universal funtion
#print(ciudades_uno.mean())
#print(ciudades_uno.median())
#print(np.average(ciudades_uno)
      
#print(ciudades_uno.head(2))
#print(ciudaes_uno.tail(2))

print(ciudades_uno.sort_values(
    ascending = False).head(2))
print(ciudades_uno.sort_values().tail(2))

#0 -10005%
#1001 - 5000 10%
# 5001 -2000 15%

def calcular(valor_serie):
    if(valor_serie <= 1000):
        return valor_serie * 1.05
    if(valor_serie > 100 and valor_serie <= 5000):
        return valor_serie * 1.10
    if(valor_serie > 5000):
        return valor_serie * 1.15

ciudad_calculada = ciudades_uno.map(calcular)

# if else
# Cuando NO cumple la condicion, aplica

resultado = ciudades_uno.where(ciudades_uno <1000,
                               ciudades_uno * 1.05)

series_numeros = pd.Series(['1.0', '2', -3])

print(pd.to_numeric(series_numeros))

#ínteger', 'signed', 'unsigned', 'float'
print(pd.to_numeric(series_numeros, downcast = 'integer'))

series_numeros_err = pd.Series(['no tiene', '1.0', '2', -3])

# ignore, coerce, raise (default)
#print(pd.to_numeric(series_numeros_err))
print(pd.to_numeric(series_numeros_err, errors='ignore'))
print(pd.to_numeric(series_numeros_err, errors='coerse'))
































  
  



