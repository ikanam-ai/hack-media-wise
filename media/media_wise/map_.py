import folium
import streamlit as st
from streamlit_folium import st_folium
from utils import get_geo_data, style_function, GeoFile


@st.cache_resource
def add_districts():
    """Добавление районов на карту"""
    return folium.GeoJson(
        get_geo_data(GeoFile.moscow_districts),
        style_function=style_function,
        tooltip=folium.GeoJsonTooltip(fields=['name']),
        name="Районы",
        show=False
    ), folium.GeoJson(
        get_geo_data(GeoFile.moscow_districts_hex),
        style_function=style_function,
        tooltip=folium.GeoJsonTooltip(fields=['name']),
        name="Районы hex",
        show=False
    )


@st.cache_resource
def add_ao():
    """Добавление автономных округов на карту"""
    return folium.GeoJson(
        get_geo_data(GeoFile.moscow_ao),
        style_function=style_function,
        tooltip=folium.GeoJsonTooltip(fields=['name']),
        name="Автономные округа",
        show=False
    ), folium.GeoJson(
        get_geo_data(GeoFile.moscow_ao_hex),
        style_function=style_function,
        tooltip=folium.GeoJsonTooltip(fields=['name']),
        name="Автономные округа hex",
        show=False
    )


def add_points(js, f_map):
    """Добавление итоговыых точек на карту"""
    for line in js:
        fg = folium.FeatureGroup(name="Рекламные точки")
        for point in line['points']:
            name = f"""<div style="width: max-content">
            Округ: {line["name:ru"].replace(' ', ' ')};</br>
            Охват: {line['val']:.3f}
            </div>
            """
            m = folium.Marker(location=[point['lat'], point['lon']], popup=name)
            m.add_to(fg)
        fg.add_to(f_map)

    folium.LayerControl().add_to(f_map)


def map_(js: list[object]):
    """Отображение карты с точками и hex-ми"""
    moscow_location = [55.751244, 37.618423]
    f_map = folium.Map(location=moscow_location, zoom_start=10, attributionControl=False)
    if st.session_state.get('hexagons') is None:
        st.session_state['hexagons'] = [add_ao()]

    # for area, hexagons in st.session_state["hexagons"]:
    #     area.add_to(f_map)
    #     hexagons.add_to(f_map)

    add_points(js, f_map)
    # if len(js):
    #     folium.GeoJson(
    #         js[0],
    #         style_function=style_function,
    #         tooltip=folium.GeoJsonTooltip(fields=['name']),
    #         name="Автономные округа hex",
    #         show=False
    #     ).add_to(f_map)

    return st_folium(f_map, use_container_width=True, key="new")
