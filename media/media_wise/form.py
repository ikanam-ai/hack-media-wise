import streamlit as st
from utils import gender_convert


def form() -> None | dict:
    """ Форма ввода параметров для подбора точек"""
    with st.form(key='form', border=False):
        f, t = st.columns(2)
        age_from = f.number_input("Возраст от", min_value=1, max_value=100, step=1)
        age_to = t.number_input("Возраст до", min_value=1, max_value=100, step=1)
        g, count = st.columns(2)
        gender = g.selectbox("Пол", ["Мужской", "Женский", "Любой"])
        points_count = count.number_input("Количество точек", min_value=1, step=1)
        st.write("Доход (комбинация букв a, b, c)")
        cols = st.columns(3)
        income_checkboxes = [col.checkbox(name) for col, name in zip(cols, 'abc')]
        income = ''.join([letter for letter, selected in zip('abc', income_checkboxes) if selected])

        submit = st.form_submit_button("Рассчитать", use_container_width=True)

        if submit:
            return {
                "age_from": age_from,
                "age_to": age_to,
                "gender": gender_convert(gender),
                "income": income,
                "points_count": points_count,

            }