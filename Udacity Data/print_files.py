import pandas as pd


df = pd.read_csv('./survey_results_public.csv')
print(df.head())
print("Anzahl der Zeilen:", df.shape[0])
print("Anzahl der Spalten:", df.shape[1])


