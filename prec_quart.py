import pandas as pd

data = pd.read_csv('dataset/kc_house_data.csv')

# Descobrir qual o preço de compra mais alto por cada número de quarto

num_quart = sorted(data["bedrooms"].unique())

for x in num_quart:
    new_data = (data.loc[data['bedrooms'] == x, ])
    print('O maior preço da casa com', x, 'quartos é do valor de', max(new_data['price']))
