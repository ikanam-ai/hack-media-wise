import json
import random
import streamlit as st
from enum import Enum
import geopandas as gpd

def load_data():
    with open("raw_data/train_data.json", "r", encoding="utf-8") as f:
        data = f.read()
        return json.loads(data)


def gender_convert(name: str) -> str:
    genders_r = {"мужской": "male", "женский": "female", "любой": "all"}
    genders_e = {v: k for k, v in genders_r.items()}

    genders = {**genders_e, **genders_r}
    found_name = genders.get(name.lower(), "all")

    return found_name.capitalize() if found_name in genders_r else found_name


class GeoFile(Enum):
    moscow_districts = "moscow_districts"
    moscow_ao = "moscow_ao"
    moscow_pois = "moscow_pois"


def get_geo_data(filename: GeoFile = GeoFile.moscow_ao) -> gpd.GeoDataFrame:
    url = f'raw_data/{filename.name}.geojson'

    return gpd.read_file(url)


def style_function(feature):
    name = feature['properties']['name']
    if st.session_state.get('colors') is None:
        st.session_state['colors'] = {}
    if st.session_state.get('colors').get(name) is None:
        st.session_state['colors'][name] = f"#{random.randint(0, 0xFFFFFF):06x}"

    color = st.session_state.get('colors').get(name)

    return {
        'fillColor': color,
        'color': 'black',
        'weight': 1.5,
        'fillOpacity': 0.6,
    }
