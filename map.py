import folium 

import pandas 

map = folium.Map(location = [39, -105], zoom_start = 4, tiles = "StamenTerrain")

# feature group - building object pass one time as opposed to above 
fg = folium.FeatureGroup(name = "Map")

# import volcano file above 
data = pandas.read_csv("volcano.txt") #for importing volcano file 
print(data)

latitude = list(data["LAT"]) #90 -90 // 100 -100
longitude = list(data["LON"])
name = list(data["NAME"])
elevation = list(data["ELEV"])


def find_color(elevation):
    if elevation < 1000:
        return "pink"
    elif 1000 <= elevation < 3000:
        return "orange"
    else: 
        return "purple"


for lt, ln, nm, el in zip(latitude, longitude, name, elevation):
    fg.add_child(folium.Marker(location = [lt, ln], 
    popup = nm + " located at " + str(el) + " elevation level ", 
    #fill_color = find_color(el), #pass in CircleMarker after folium. to be able to use this 
    icon = folium.Icon(color = find_color(el))))

fg.add_child(folium.GeoJson(data = open("world.json", "r", encoding="utf-8-sig").read())) #this shows the outlines in the map  

map.add_child(fg)

map.save("Map1.html")

