# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 09:32:40 2020

@author: LENOVO
"""

# e_out_data.py
import pandas as pd
import numpy as np
import os
import sqlite3

path_guardado = "./data/artwork_data.pickle"

df = pd.read_pickle(path_guardado)

sub_df = df.iloc[49980:50519,:].copy()

# permite subir diferentes archivo
#tipos archivos
#JSON
#Excel
#SQL

# Excel #
path_excel = "./data/artwork_data.xls"
#path_excel_indice = "./data/artwork_data_indice.xls"
#artwork_data.xlsx
#artwork_data_indice.xlsx
#artwork_data_columnas.xls

#con elindice como columna
#sub_df.to_excel(path_excel)

#"SIN el índice como columna"
#sub_df.to_excel(path_excel_indice, index = False)

columnas = ['artist','title', 'year']

sub_df.to_excel(path_excel, columns = columnas)

# Multiples hojas de trabajo #

path_excel_mt = "./data/artwork_data_mt.xlsx"

#Crear Writer 

writer = pd.ExcelWriter(path_excel_mt,
                        engine = 'xlsxwriter')

#para crear las hojas

sub_df.to_excel(writer, sheet_name = 'Primera')

sub_df.to_excel(writer, sheet_name = 'Segunda')

sub_df.to_excel(writer, sheet_name = 'Tercera')

writer.save()

# Formato condicional dentro del Excel#

# Ver artistar dentro del sub dataFrame

num_artistas = sub_df['artist'].value_counts()
# value_counts cuenta los numeros repetidos
print(type(num_artistas))
print(num_artistas)

path_excel_colores = "./data/artwork_data_colores.xlsx"
#crear el writer
writer = pd.ExcelWriter(path_excel_colores,
                        engine = 'xlsxwriter')

# Serie y vamos a guardar en hoja artistas
num_artistas.to_excel(writer,
                      sheet_name ='Artistas')

#seleccionando hoja de trabajo
hoja_artistas = writer.sheets['Artistas']

# rango de celda para aplicar un formato
#condicional
# es decir de donde a donde voy a imprimir
# al rango le sumamos 1
rango_celdas = 'B2:B{}'.format(len(num_artistas.index)+1)
print (rango_celdas)

# Formato
formato_artistas = {
    "type": "2_color_scale",
    "min_value":"10",
    "min_type": "percentile",
    "max_value":"99",
    "max_type": "percentile"}

hoja_artistas.conditional_format(rango_celdas,
                                    formato_artistas)

writer.save()

########## GUARDAR EN SQL######
# CREAR CONEXION
with sqlite3.connect("bdd_artist.bdd") as conexion:
    sub_df.to_sql('py_artistas', conexion)

######## GuRDAR JSON#######
sub_df.to_json('artistas.json')
sub_df.to_json('artistas_tabla.json', orient ='table')
    
    





























