##
# 姓名:王昱翔
# 座位號碼:07
# 修改檔名到你的座位號碼
##

import folium
import requests

URL1 = "https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json"

sample_data = requests.get(URL1)

taipei = [25.047916, 121.517438]
zoom = 14
map_osm = folium.Map(location=taipei, zoom_start=zoom)

returnValues = sample_data.json()["retVal"]
for i in returnValues.values():
    coordinate = [float(i["lat"]), float(i["lng"])]
    default_icon = folium.Icon(color='green', icon='repeat')
    folium.Marker(coordinate, icon=default_icon, popup=None).add_to(map_osm)



map_osm.save('map_07/hw4_07.html')