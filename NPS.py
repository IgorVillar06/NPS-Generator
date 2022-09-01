from hashlib import new
from lib2to3.pytree import convert
import pandas as pd
import numpy as np

database = pd.read_csv("report.csv", sep=';', index_col=0)
database = database.drop_duplicates()

#agente1 = database [database['Agente'] == 'Igor Villar']

avaliacoes = database [(database['Nota'] >= 1) & (database['Agente'] == 'Igor Villar')]
contar_avaliacoes = avaliacoes ['Nota'].value_counts(dropna=False, ascending=False). to_frame()
total_avaliacoes = contar_avaliacoes.sum()

promotor = database [(database['Nota'] >= 9) & (database['Agente'] == 'Igor Villar')]
contar_promotor = promotor ['Nota'].value_counts(dropna=False, ascending=False). to_frame()
total_promotores = contar_promotor.sum()

detrator = database [(database['Nota'] >= 0) & (database['Nota'] <= 6) & (database['Agente'] == 'Igor Villar')] 
contar_detrator = detrator ['Nota'].value_counts(dropna=False, ascending=False). to_frame()
total_detrator = contar_detrator.sum()

nps = [((total_promotores - total_detrator) / total_avaliacoes) * 100]
print("o nps de Igor é: ", nps)