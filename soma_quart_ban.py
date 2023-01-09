import pandas as pd

data = pd.read_csv('dataset/kc_house_data.csv')

# Qual a soma de todos os preços de compra por número de quartos e banheiros

num_quart =  sorted(data['bedrooms'].unique())
num_ban =  sorted(data['bathrooms'].unique())

for x in num_quart:
    for y in num_ban:
        new_data = data.loc[(data['bedrooms'] == x) & (data['bathrooms'] == y)]
        if sum(new_data['price']) > 0:
            print('A soma dos preço para', x, 'quartos e', y, 'banheiros é igual a:', sum(new_data['price']))


