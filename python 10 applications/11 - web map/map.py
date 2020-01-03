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
    volcanoes.add_child(folium.Marker(location = [latitude, longitude], popup = name + ", " + str(elevation) + "m", icon = folium.Icon(color = color_decider(elevation))))

map.add_child(volcanoes)

map.save("map1.html")
