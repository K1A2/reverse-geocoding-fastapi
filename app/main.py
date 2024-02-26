from fastapi import FastAPI
import geopandas as gpd
from shapely.geometry import Point

app = FastAPI()

shp_file_path = './data/adm_polygon.shp'
shp_data = gpd.read_file(shp_file_path)

@app.get('/map/reverse-geocode')
async def reverse_geocode(
        lat: float = 37.553979,
        lon: float = 126.922668,
        type: int = 2,
        near: int = 0):
    point = Point(lon, lat)
    region = shp_data[shp_data.geometry.contains(point)]
    if region.empty:
        region_name = "Unknown"
        if not near:
            return {'region_name': region_name}
        min_distance = float('inf')
        region = None
        for _, row in shp_data.iterrows():
            distance = point.distance(row['geometry'])
            if distance < min_distance:
                min_distance = distance
                region = row
    else:
        region = region.iloc[0, :]
    region_name = ''
    if type <= 2:
        region_name += region['ADM_NM_F']
    if type <= 1:
        region_name += f" {region['ADM_NM_M']}"
    if type <= 0:
        region_name += f" {region['ADM_NM_L']}"
    return {'region_name': region_name}
