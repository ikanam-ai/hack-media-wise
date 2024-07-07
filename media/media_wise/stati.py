import streamlit as st


def stati(points: list[object]) -> None:
    """Отображение статистики по точкам"""
    # Создаем Streamlit приложение
    with st.container():
        st.subheader("Оптимальные точки")
        points_text = ""
        for point in sorted(points, key=lambda x: x['val'], reverse=True):
            if len(point['points']) > 0:
                coord = point['points'][0]
                points_text += f"{point['name']}\nШирота: {coord['lat']}\nДолгота: {coord['lon']}\nОхват: {point['val']:.3f}\n\n"

        st.text_area("Точки", points_text, disabled=True, height=240)

