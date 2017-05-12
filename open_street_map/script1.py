
#import folium module
import folium
import pandas

df=pandas.read_csv("Volcanoes_USA.txt")

#create object
map1=folium.Map(location=[45.372, -121.697],zoom_start=4, tiles="Stamen Terrain")

def color(elev):
    if elev in range(0,1000):
        col="green"
    elif elev in range(1000,3000):
        col="orange"
    else:
        col="red"
    return col

for lat,lon,name,elev in zip(df['LAT'], df['LON'], df['NAME'], df['ELEV']):
    folium.Marker([lat,lon],popup=name, icon = folium.Icon(color=color(elev))).add_to(map1)


#save to html file
map1.save("map1.html")
