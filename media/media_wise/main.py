import streamlit as st

from custom_setup import setup
from form import form
from map_ import map_
from model import load_model
from utils import load_data

setup()
data = load_data()

col1, col2 = st.columns([4, 1])

with col1.container():
    st_data = map_(data)

with col2.container():
    data = form()
    if data:
        st.write("Результат:", load_model())
