import plotly.express as px

# Dane punktowe (koordynaty)
lats = [45.5236, 46.9424, 47.5234]
lons = [15.6454, 16.4532, 17.2341]

# Rysowanie punktów na mapie
fig = px.scatter_geo(
    lat=lats,
    lon=lons,
    scope='world',  # Domyślne tło mapy
    height=300
)

# Wyświetlenie wykresu
fig.show()
