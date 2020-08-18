# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 18:06:38 2020

@author: LENOVO
"""


# Deber grafica Excell

import  pandas  as  pd
import xlsxwriter

path_guardado = "./data/artwork_data.pickle"

df = pd.read_pickle(path_guardado)

sub_df = df.iloc[49980:50519,:].copy()
num_artistas = sub_df["artist"].value_counts()


workbook = xlsxwriter.Workbook('grafica_excel.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write_column('A1', num_artistas.index)
worksheet.write_column('B1', num_artistas)

chart = workbook.add_chart({'type': 'line'})


chart.add_series({
    'name':       'Artistas',
    'categories': '=Sheet1!$A$1:$A$85',
    'values':     '=Sheet1!$B$1:$B$85',
    'marker': {'type' : 'circle'}
 
})

worksheet.insert_chart('D2', chart)



workbook.close()
