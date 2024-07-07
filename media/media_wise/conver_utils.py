import geopandas as gpd
import h3pandas


def create_hexagons_from_geojson(geojson_data: gpd.GeoDataFrame, resolution: int = 8) -> gpd.GeoDataFrame:
    """Создание hexagon grid из geojson данных"""
    gdf_exp = geojson_data.explode()
    hexo = gdf_exp.h3.polyfill_resample(resolution)
    hexo.to_file('file.geojson', driver='GeoJSON')

    return hexo