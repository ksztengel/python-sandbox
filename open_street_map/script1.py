import folium
map1=folium.Map(location=[45.372, -121.697],zoom_start=12, tiles="Stamen Terrain")
folium.Marker([45.3288,-121.6625],popup="Mt. Hood Meadows", icon = folium.Icon(color='red')).add_to(map1)
folium.Marker([45.311,-121.7311],popup="Timberlake Lodge",icon = folium.Icon(color='green')).add_to(map1)
map1.save("map1.html")
