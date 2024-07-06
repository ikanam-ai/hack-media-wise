import folium
import streamlit as st
from streamlit_folium import st_folium
from utils import gender_convert, get_geo_data, style_function, GeoFile


@st.cache_resource
def add_districts():
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
    for line in js[0:2]:
        fg = folium.FeatureGroup(name=line['hash'], show=False)
        for point in line['points']:
            name = f"""<div style="width: max-content">
            Название: {line['targetAudience']['name'].replace(' ', ' ')};</br>
            Возраст: {line['targetAudience']['ageFrom']}-{line['targetAudience']['ageTo']};</br>
            Пол: {gender_convert(line['targetAudience']['gender'])};</br>
            Доход: {line['targetAudience']['income']};</br>
            Value: {line['value']}
            </div>
            """
            m = folium.Marker(location=[point['lat'], point['lon']], popup=name,)
            m.add_to(fg)
        fg.add_to(f_map)

    folium.LayerControl().add_to(f_map)


def map_(js):
    moscow_location = [55.751244, 37.618423]
    f_map = folium.Map(location=moscow_location, zoom_start=10, attributionControl=False)
    if st.session_state.get('hexagons') is None:
        st.session_state['hexagons'] = [add_ao(), add_districts()]

    for area, hexagons in st.session_state["hexagons"]:
        area.add_to(f_map)
        hexagons.add_to(f_map)

    # add_points(js, f_map)

    return st_folium(f_map, use_container_width=True, key="new")
