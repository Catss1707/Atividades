import pandas as pd
import numpy as np

"""Atividade ocorrencia"""

valores_ausentes = ['**','##!','#####','****','*****','NULL']
df_oco = pd.read_csv('ocorrencia.csv', sep = ';', parse_dates = ['ocorrencia_dia'], dayfirst = True, na_values = valores_ausentes)

filtro_o = df_oco.ocorrencia_classificacao == 'INCIDENTE'
filtro_day = df_oco.ocorrencia_dia.dt.year == 2017
filtro_n = df_oco.ocorrencia_cidade.str.contains('RIO')

df_oco.loc[filtro_o & filtro_day & filtro_o]

filtro1 = df_oco.ocorrencia_dia.dt.year == 2012
filtro2 = df_oco.ocorrencia_dia.dt.month <= 3
filtro3 = df_oco.ocorrencia_cidade == 'RIO DE JANEIRO'
df20123 = df_oco.loc[filtro1 & filtro2 & filtro3]

df20123.groupby(['ocorrencia_classificacao']).size()

filtro1 = df_oco.ocorrencia_dia.dt.year == 2013
filtro2 = df_oco.ocorrencia_dia.dt.month <=3
filtro3 = df_oco.ocorrencia_cidade == 'RIO DE JANEIRO'
df20133 = df_oco.loc[filtro1 & filtro2 & filtro3]

df20133.groupby(['ocorrencia_classificacao']).size()

filtro1 = df_oco.ocorrencia_dia.dt.year == 2014
filtro2 = df_oco.ocorrencia_dia.dt.month <=3
filtro3 = df_oco.ocorrencia_cidade == 'RIO DE JANEIRO'
df20143 = df_oco.loc[filtro1 & filtro2 & filtro3]

df20143.groupby(['ocorrencia_classificacao']).size()

"""Atividade do enem"""

df = pd.read_csv('')

filtroSud = df.SG_UF_RESIDENCIA.isin(['RJ','SP','MG','ES'])
filtroS = df.SG_UF_RESIDENCIA.isin(['PR','SC','RS'])
filtroCO = df.SG_UF_RESIDENCIA.isin(['MT','DF','GO','MS'])
filtroN = df.SG_UF_RESIDENCIA.isin(['RR','AP','AM','PA','AC','RO','TO'])
filtroNor = df.SG_UF_RESIDENCIA.isin(['MA','PI','CE','RN','PB','PE','AL','SE','BA'])

"""Notas do Sudeste maior e menor que "450"
"""

filtroM = df.NU_NOTA_MEDIA <= 450.0
filtroSudeste = df.SG_UF_RESIDENCIA.isin(['RJ','SP','MG','ES'])
sudeste = df.loc[filtroM & filtroSudeste]
sudeste.groupby(['SG_UF_RESIDENCIA','NU_NOTA_MEDIA']).size().sort_values(ascending=False)

filtroM = df.NU_NOTA_MEDIA >= 450.0
filtroSudeste = df.SG_UF_RESIDENCIA.isin(['RJ','SP','MG','ES'])
sudeste = df.loc[filtroM & filtroSudeste]
sudeste.groupby(['SG_UF_RESIDENCIA','NU_NOTA_MEDIA']).size().sort_values(ascending=False)

"""Notas do"""