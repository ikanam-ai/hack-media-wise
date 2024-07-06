def create_hexagons_from_geojson(geojson_data: gpd.GeoDataFrame, resolution: int = 8):
    import h3pandas
    gdf_exp = geojson_data.explode()
    hexo = gdf_exp.h3.polyfill_resample(resolution)
    hexo.to_file('file.geojson', driver='GeoJSON')
    print("complete")

    return hexo