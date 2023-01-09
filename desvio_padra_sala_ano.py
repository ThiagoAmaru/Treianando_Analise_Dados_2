import pandas as pd

data = pd.read_csv('dataset/kc_house_data.csv')

# Qual o devios padrão das salas dos imoveis por ano de construção

anos_constr = sorted(data['yr_built'].unique())

for x in anos_constr:
    h = data.loc[data['yr_built'] == x]
    print('O desvio padrão das salas no ano de', x , 'é igual a ', h['sqft_living'].std())
