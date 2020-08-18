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

#############
# Crear diccionario
datos = {
    "nota 1":{
        "Pepito": 7,
        "Juanito": 8,
        "Maria": 9
        },
    "disciplina": {
        "Pepito": 4,
        "Juanito": 9,
        "Maria": 2
        },
    }

notas = pd.DataFrame(datos)

# queremos ver si pasa el semestre

condicion_nota = notas["nota 1"]>7
#condicion_nota_dos = notas["nota 2"]>7
condicion_disc = notas["disciplina"]>7

mayores_siete = notas.loc[condicion_nota, ["nota 1"]]
# sepuede poner varios arreglos de condicion True oFalse
# al ejecutar valida condicionse

pasaron = notas.loc[condicion_nota][condicion_disc]

#para cambiaruna nota
notas.loc["Maria", "disciplina"] = 7
# para cambiar a todos la nota

notas.loc[:,"disciplina"] = 7

## Ejercicio: Promedio delas 3notas (no1 + n02 + disc)/3
###hacer
## cuando se quiera filtrardatos no usardirecto el 
#data Frame USAR ILOC o LOC












































