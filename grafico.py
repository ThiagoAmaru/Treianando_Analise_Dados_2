import pandas as pd

from matplotlib import pyplot as plt

from matplotlib import gridspec

data = pd.read_csv('dataset/kc_house_data.csv')

plt.figure(figsize=(20,12))

fig = plt.figure()

specs = gridspec.GridSpec( ncols = 2, nrows = 2, figure = fig)

ax1= fig.add_subplot(specs [0, : ])

ax2= fig.add_subplot(specs [1, 0 ])

ax3= fig.add_subplot(specs [1, 1 ])

data['year'] = pd.to_datetime(data['date']).dt.year
by_year = data[['price', 'year']].groupby('year').sum().reset_index()
ax1.bar(by_year['year'],  by_year['price'])

data['day'] = pd.to_datetime(data['date']).dt.day
by_year = data[['price', 'day']].groupby('day').mean().reset_index()
ax2.bar(by_year['day'],  by_year['price'])

data['year_week'] = pd.to_datetime(data['date']).dt.strftime('%Y-%U')
by_year = data[['price', 'year_week']].groupby('year_week').mean().reset_index()
ax3.bar(by_year['year_week'],  by_year['price'])


plt.show()