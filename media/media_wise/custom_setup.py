import streamlit as st


def setup() -> None:
    st.set_page_config(layout="wide", )
    st.markdown(f"""
        <style>
            div.withScreencast > div > div > div > section > div.block-container {{
                padding-bottom: 0;
                padding-top: 2.5rem;
            }}
        </style>""",
        unsafe_allow_html=True,
    )

