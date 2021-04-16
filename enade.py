import pandas as pd

# Carrega dataframe
pdEnade = pd.read_csv("microdados_enade_2019.txt", sep = ';', low_memory=False)

# Quantas linhas e colunas no dataframe
pdEnade.shape