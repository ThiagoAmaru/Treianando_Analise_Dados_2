import pandas as pd

data = pd.read_csv('dataset/kc_house_data.csv')

# Metodo para descobrir qual o menor numero de quartos por ano de construção de imóveis

anos_constr = sorted(data['yr_built'].unique())

for x in anos_constr:
    datas = data.loc[data['yr_built'] == x]
    print('O menor numero de quartos no ano', x,'foi de', min(datas['bedrooms']), 'quartos')

