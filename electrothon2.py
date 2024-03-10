import folium
import pandas as pd
from folium.plugins import HeatMap


sample_data = [
    [37.7749, -122.4194, 3],  
    [34.0522, -118.2437, 2],  
    [40.7128, -74.0060, 4],  
    
]


df = pd.DataFrame(sample_data, columns=['Latitude', 'Longitude', 'Congestion'])


base_map = folium.Map(location=[37.7749, -122.4194], zoom_start=4)


heatmap_layer = HeatMap(data=df[['Latitude', 'Longitude', 'Congestion']], radius=15)
heatmap_layer.add_to(base_map)


base_map.save('real_time_traffic_heatmap.html')

