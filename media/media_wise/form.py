import streamlit as st
from utils import gender_convert


def form():
    f, t = st.columns(2)
    age_from = f.number_input("Возраст от", min_value=0, max_value=100, step=1)
    age_to = t.number_input("Возраст до", min_value=age_from, max_value=100, step=1)
    g, count = st.columns(2)
    gender = g.selectbox("Пол", ["Мужской", "Женский", "Любой"])
    points_count = count.number_input("Количество точек", min_value=1, step=1)
    st.write("Доход (комбинация букв a, b, c)")
    cols = st.columns(3)
    income_checkboxes = [col.checkbox(name) for col, name in zip(cols, 'abc')]
    income = ''.join([letter for letter, selected in zip('abc', income_checkboxes) if selected])

    st.button("Рассчитать", use_container_width=True, on_click=lambda : st.session_state.__setitem__('form', {
            "age_from": age_from,
            "age_to": age_to,
            "gender": gender_convert(gender),
            "income": income,
            "points_count": points_count
        }))

    return st.session_state.get('form')
