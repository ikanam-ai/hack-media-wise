import streamlit as st

from custom_setup import setup
from form import form
from map_ import map_
from calculation import calculate

setup()

col1, col2 = st.columns([4, 1])

if st.session_state.get('points_count') is None:
    st.session_state['points_count'] = []

with col2:
    form_data = form()
    if form_data:
        st.session_state['points_count'] = calculate(form_data['points_count'])

with col1:
    st_data = map_(st.session_state['points_count'])
