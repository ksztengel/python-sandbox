
#import folium module
import folium
import pandas

df=pandas.read_csv("Volcanoes_USA.txt")

#create object
map1=folium.Map(location=[df['LAT'].mean(), df['LON'].mean()],zoom_start=6, tiles="Stamen Terrain")

def color(elev):
    minimum = int(min(df['ELEV']))
    step = int((max(df['ELEV'])-min(df['ELEV']))/3)
    if elev in range(minimum,minimum+step):
        col="green"
    elif elev in range(minimum+step,minimum+step*2):
        col="orange"
    else:
        col="red"
    return col

for lat,lon,name,elev in zip(df['LAT'], df['LON'], df['NAME'], df['ELEV']):
    folium.Marker([lat,lon],popup=name, icon = folium.Icon(color=color(elev))).add_to(map1)


#save to html file
map1.save("map1.html")
