# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 09:26:28 2020

@author: LENOVO
"""


# h_group.py

import pandas as pd
import math
import numpy as np

path_guardado = "./data/artwork_data.pickle"

df = pd.read_pickle(path_guardado)

# ASEMOS UNACOPIAENEL DATAFRAME  seccion_df

seccion_df = df.iloc[49980:50019,:].copy()

# vamos a agrupar

df_agrupar_artista = seccion_df.groupby('artist')

print(type(df_agrupar_artista))

for x,y in df_agrupar_artista:
    print(type(x))
    print(x)
    print(type(y))
    print(y)
    
for columna, df_agrupado in df_agrupar_artista:
    print(type(columna))
    print(columna)
    print(type(df_agrupado))
    print(df_agrupado)
    
## llenar nos vacios que se tenga
## sacar promedio
#1 de la seccion del df contar las unidades
    
a = seccion_df['units'].value_counts() # 38 (mm)
                                        # 1 nan (tiene valor
#pero no es numero)

# empty nos sirve pa identificar si lacolumna esta vacia
print(seccion_df['units'].empty)
print(a.empty)

def llenar_valores_vacios (series, tipo):
    lista_valores = series.value_counts()
    # si esta vacio no hacemos nada
    if (lista_valores.empty == True):
        return series
    else:
        # podemos llenar con el promedio
        #primero sacamos el promedio
        if(tipo == 'promedio'):
            suma = 0
            numero_valores = 0
            for valor_serie in series:
                if(isinstance(valor_Serie, str)):
                    valor = int(valor_Serie)
                    numero_valores = numero_valores + 1
                    suma = suma + valor
                    #sino es tipo string pasar
                else:
                    pass
                    promedio = suma / numero_valores
                    #llenamos con el promedio
                    #usamos fillna
                    series_valores_llenos = series.fillna(promedio)
                    #retornamso los valores llenos con el promedio
                    return series_valores_llenos
            ## podemos llenar con mas repedito
            #definir con q quiere llenar los vacios
        if(tipo == 'mas repetido'): 
           valor_repetido  =  series.value_counts().idxmax()
            serie_valores_llenos  =  series.fillna(valor_repetido)
            return  serie_valores_llenos
#definir series


def transformar_df (df):
    df_artist = df.groupby('artist')
    lista_df = []
    for artista, df in df_artist:
        copia_df = df.copy()
        
        serie_w = copia_df['width']
        serie_h= copia_df['height']
        serie_u = copia_df['units']
        serie_i = copia_df['title']
        #de la copia vamos a cojer toda lacopia
        # y llenamos la columna width
        copia_df.loc[:,'width'] = llenar_valores_vacios(
            serie_w,
            'promedio')
        
        copia_df.loc[:,'hight'] = llenar_valores_vacios(
            serie_h,
            'promedio')
        
         copia_df.loc[:,'units'] = llenar_valores_vacios(
            serie_u,
            'mas_repetido')
         
         copia_df.loc[:,'title'] = llenar_valores_vacios(
            serie_i,
            'mas_repetido')
         
         lista_df.append(copia)
    df_completo = pd.concat(lista_df)
    return df_completo

df_lleno = transformar_df(seccion_df)
    