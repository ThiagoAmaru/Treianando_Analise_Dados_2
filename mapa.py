import plotly.express as px
import pandas as pd

data = pd.read_csv('dataset/kc_house_data.csv')

houses = data[['id', 'lat', 'long', 'price']]

fig = px.scatter_mapbox(houses, lat = 'lat', lon = 'long', size= 'price', color_continuous_scale= px.colors.cyclical.IceFire, size_max=35, zoom= 10)

fig.update_layout ( mapbox_style = 'open-street-map')

fig.update_layout ( height = 600, margin = {'r': 0 , 't': 0, 'l': 0, 'b': 0})

fig.show()

