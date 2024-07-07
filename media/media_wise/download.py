import geopandas as gpd
import streamlit as st


def download(points:  list[object]):
    gdf = gpd.GeoDataFrame(points)
    geojson = gdf.to_json()
    """Скачать полученные точки"""
    st.download_button('Скачать данные',
                       geojson,
                       mime='application/geo+json',
                       file_name="points.geojson",
                       use_container_width=True
                       )
