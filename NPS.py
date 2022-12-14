import pandas as pd
import numpy as np

database = pd.read_csv("report5hub.csv", sep=',', index_col=0)
database = database.drop_duplicates().dropna()

avaliacoes = database [(database['Nota'] >= 10)]
contar_avaliacoes = avaliacoes ['Nota'].value_counts(dropna=False, ascending=False). to_frame()
total_avaliacoes = contar_avaliacoes.sum()

promotor = database [(database['Nota'] >= 90)]
contar_promotor = promotor ['Nota'].value_counts(dropna=False, ascending=False). to_frame()
total_promotores = contar_promotor.sum()

detrator = database [(database['Nota'] >= 0) & (database['Nota'] <= 60)] 
contar_detrator = detrator ['Nota'].value_counts(dropna=False, ascending=False). to_frame()
total_detrator = contar_detrator.sum()

nps_time = ((total_promotores - total_detrator) / total_avaliacoes) * 100
nps_time = int(nps_time['Nota'])
print("NPS do time (5Hub):", nps_time)

print("==========================================================================================")

for Agente in database['Agente'].drop_duplicates():
    avaliacoes = database[(database['Nota'] >= 10) & (database['Agente'] == Agente)]
    contar_avaliacoes = avaliacoes['Nota'].value_counts(dropna=False, ascending=False). to_frame()
    total_avaliacoes = contar_avaliacoes.sum()

    promotor = database[(database['Nota'] >= 90) & (database['Agente'] == Agente)]
    contar_promotor = promotor['Nota'].value_counts(dropna=False, ascending=False). to_frame()
    total_promotores = contar_promotor.sum()

    detrator = database[(database['Nota'] >= 0) & (database['Nota'] <= 60) & (database['Agente'] == Agente)]
    contar_detrator = detrator['Nota'].value_counts(
    dropna=False, ascending=False). to_frame()
    total_detrator = contar_detrator.sum()

    nps_time = (((total_promotores - total_detrator) / total_avaliacoes) * 100)
    nps_time = int(nps_time['Nota'])
    print("NPS de", Agente, "(5Hub):", nps_time)

print("==========================================================================================")    
    
database = pd.read_csv("report.csv", sep=';', index_col=0)
database = database.drop_duplicates().dropna()

avaliacoes = database [(database['Nota'] >= 1)]
contar_avaliacoes = avaliacoes ['Nota'].value_counts(dropna=False, ascending=False). to_frame()
total_avaliacoes = contar_avaliacoes.sum()

promotor = database [(database['Nota'] >= 9)]
contar_promotor = promotor ['Nota'].value_counts(dropna=False, ascending=False). to_frame()
total_promotores = contar_promotor.sum()

detrator = database [(database['Nota'] >= 0) & (database['Nota'] <= 6)] 
contar_detrator = detrator ['Nota'].value_counts(dropna=False, ascending=False). to_frame()
total_detrator = contar_detrator.sum()

nps_time = ((total_promotores - total_detrator) / total_avaliacoes) * 100
nps_time = int(nps_time['Nota'])
print("NPS do time (Native):", nps_time)

print("==========================================================================================")

for Agente in database['Agente'].drop_duplicates():
    avaliacoes = database[(database['Nota'] >= 1) & (database['Agente'] == Agente)]
    contar_avaliacoes = avaliacoes['Nota'].value_counts(dropna=False, ascending=False). to_frame()
    total_avaliacoes = contar_avaliacoes.sum()

    promotor = database[(database['Nota'] >= 9) & (database['Agente'] == Agente)]
    contar_promotor = promotor['Nota'].value_counts(dropna=False, ascending=False). to_frame()
    total_promotores = contar_promotor.sum()

    detrator = database[(database['Nota'] >= 0) & (database['Nota'] <= 6) & (database['Agente'] == Agente)]
    contar_detrator = detrator['Nota'].value_counts(
    dropna=False, ascending=False). to_frame()
    total_detrator = contar_detrator.sum()

    nps_time = (((total_promotores - total_detrator) / total_avaliacoes) * 100)
    nps_time = int(nps_time['Nota'])
    print("NPS de", Agente, "(Native):", nps_time)