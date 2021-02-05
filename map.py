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

fgvolcano = folium.FeatureGroup( name = "Volcanos" )
for lt, ln, el in zip(latitude, longitude, elevation):
    fgvolcano.add_child(folium.CircleMarker(location = [lt, ln], radius = 8, popup = str(el)+ "mt.", 
                                        fill_color= find_color(el),
                                        color = "black", 
                                        fill_opacity = 0.9))

for lt, ln, nm, el in zip(latitude, longitude, name, elevation):
    fg.add_child(folium.Marker(location = [lt, ln], 
    popup = nm + " located at " + str(el) + " elevation level ", 
    #fill_color = find_color(el), #pass in CircleMarker after folium. to be able to use this 
    icon = folium.Icon(color = find_color(el))))

fg.add_child(folium.GeoJson(data = open("world.json", "r", encoding="utf-8-sig").read(),
                            style_function = lambda x: 
                            {"fillColor":"yellow" 
                            if x["properties"]["POP2005"] < 100000 
                            else
                            ("purple")
                                if 100000 <= x["properties"]["POP2005"] < 900000 
                                else 
                                    ("red")
                                }
                                ))
                             #this shows the outlines in the map  


map.add_child(fg)

map.save("Map1.html")

