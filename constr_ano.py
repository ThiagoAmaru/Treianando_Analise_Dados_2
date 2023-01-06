import pandas as pd

data = pd.read_csv('dataset/kc_house_data.csv')

#Metodo para descobrir qual o numero de imoveis por ano de construção.

#Ordenando os valores, retirando duplicatas, assim é possivel colocar os anos possiveis em uma lista

anos_de_constr = sorted((data['yr_built'].unique()))

#Aqui utilizo o comando for para passar pela lista trazendo um ano por vez e o distribuindo na formula com o x
for x in anos_de_constr:
    print('O numero de construções de casa no ano de:', x, 'é de', data.loc[data['yr_built'] == x, 'id'].shape[0], 'casas')
