import folium
import pandas as pd

sample_data = pd.read_csv('demo49\demo49.csv', sep=',')
#sample_data = pd.read_csv('data/demo49.csv', encoding='big5', sep=',')

print(sample_data.shape)
print(sample_data.columns)
sample_data.columns = ['sec','road','road_detail','lon','lat','extra']
print(sample_data.columns)

# 建立一個目錄map

taipei = [25.137176, 121.508335]
zoom = 18
map_osm = folium.Map(location=taipei, zoom_start=zoom)

for i in range(len(sample_data)):
    coordinate = [sample_data.loc[i, 'lat'], sample_data.loc[i, 'lon']]
    # color='green','black'
    #default_icon = folium.Icon(color='black',icon='info-sign')

    message = f'[{i}]{sample_data.loc[i, "road"]}{sample_data.loc[i, "road_detail"]}'
    default_icon = folium.Icon(color='green', icon='heart')
    folium.Marker(coordinate, icon=default_icon, popup=message).add_to(map_osm)
    print(i, coordinate)

ucom_taipei = [25.051947, 121.544008]
tun_hwa_junior = [25.051121, 121.546422]
folium.Circle(ucom_taipei, radius=100, popup='ucom taipei',fill_color='#C0FFEE').add_to(map_osm)
folium.CircleMarker(tun_hwa_junior, radius=100, popup='敦化國中', fill_color="#FFC0EE").add_to(map_osm)

map_osm.save('map/demo49.html')
