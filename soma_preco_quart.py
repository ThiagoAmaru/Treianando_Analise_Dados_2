import pandas as pd

data = pd.read_csv('dataset/kc_house_data.csv')

#Qual a soma de todos os preços de compra por número de quartos

num_quart = sorted(data["bedrooms"].unique())

for x in num_quart:
    new_data = data.loc[data['bedrooms'] == x]
    print('A soma dos precos das casa com', x, 'quartos foi de', sum(new_data['price']))