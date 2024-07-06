import folium
import geopandas as gpd


def add_hexagons_to_map(m, hexagons_polygons: gpd.GeoDataFrame):
    for _, row in hexagons_polygons.iterrows():
        geojson = gpd.GeoSeries([row['geometry']]).__geo_interface__
        folium.GeoJson(geojson, style_function=lambda feature, col="blue": {
            'fillColor': col,
            'color': col,
            'weight': 1,
            'fillOpacity': 0.1
        }, name="hello").add_to(m)
