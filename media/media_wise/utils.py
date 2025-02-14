import json
import random
import streamlit as st
from enum import Enum
import geopandas as gpd
import pandas as pd


@st.cache_resource
def load_data():
    """ Загрузка данных тренировки из файла """
    with open("raw_data/train_data.json", "r", encoding="utf-8") as f:
        data = f.read()
        return json.loads(data)


def gender_convert(name: str) -> str:
    """ Конвертация русского названия пола в английское и наоборот """
    genders_r = {"мужской": "male", "женский": "female", "любой": "all"}
    genders_e = {v: k for k, v in genders_r.items()}

    genders = {**genders_e, **genders_r}
    found_name = genders.get(name.lower(), "all")

    return found_name.capitalize() if found_name in genders_r else found_name


@st.cache_resource
def load_ao_hex() -> pd.DataFrame:
    """ Загрузка данных по районам c hex-ячейками """
    return pd.read_csv("raw_data/df_res_eval_ao.csv")


class GeoFile(Enum):
    """ Файлы с геоданными"""
    moscow_districts = "moscow_districts"
    moscow_districts_hex = "moscow_districts_hex"
    moscow_ao = "moscow_ao"
    moscow_ao_hex = "moscow_ao_hex"
    moscow_pois = "moscow_pois"
    moscow_ao_hex_val = "moscow_ao_hex_val"


@st.cache_resource
def get_geo_data(filename: GeoFile = GeoFile.moscow_ao) -> gpd.GeoDataFrame:
    """ Загрузка геоданных из файла """
    url = f'raw_data/{filename.name}.geojson'

    return gpd.read_file(url)


def style_function(feature: dict) -> dict:
    """ Стилизация геоданных"""
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
