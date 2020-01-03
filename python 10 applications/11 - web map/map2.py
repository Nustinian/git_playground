import folium, pandas

volcanoes_data = pandas.read_csv("volcanoes.csv")

latitudes = list(volcanoes_data["LAT"])
longitudes = list(volcanoes_data["LON"])
names = list(volcanoes_data["NAME"])
elevations = list(volcanoes_data["ELEV"])

locations = {
    "Home": [35.4718, 139.6218],
    "Spot 2": [35.4, 139.6],
    "Spot 3": [35.5, 139.7],
    "Spot 4": [35.3, 139.5],
    "Spot 5": [35.5, 139.6],
    "Spot 6": [35.42, 139.61]
}

def color_decider(elevation):
    if elevation < 1500:
        return "green"
    elif elevation < 3000:
        return "orange"
    else:
        return "red"

map = folium.Map(location = locations.get("Home"), max_zoom = 16, zoom_start = 12, tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name = "My Map")
for name, coordinates in locations.items():
    fg.add_child(folium.Marker(location = coordinates, popup = name, icon = folium.Icon(color = "purple")))

map.add_child(fg)

volcanoes = folium.FeatureGroup(name = "Volcanoes")
for latitude, longitude, name, elevation in zip(latitudes, longitudes, names, elevations):
    volcanoes.add_child(folium.CircleMarker(location = [latitude, longitude], radius = 6, weight = 1,
    color = "grey", popup = name + ", " + str(elevation) + "m", fill_opacity = 0.7, fill = True,
    fill_color = color_decider(elevation)))

population_layer = folium.FeatureGroup(name = "Populations")

population_layer.add_child(folium.GeoJson(data = open("world.json", "r", encoding = "utf-8-sig").read(),
    style_function = lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
    else 'orange' if 10000000 <= x['properties']['POP2005'] < 40000000
    else 'red'}))

map.add_child(volcanoes)
map.add_child(population_layer)

map.add_child(folium.LayerControl())

map.save("map2.html")
