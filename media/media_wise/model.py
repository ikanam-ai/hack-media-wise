from catboost import CatBoostRegressor
import pickle
import streamlit as st
import numpy as np
from sklearn.metrics import mean_squared_error


@st.cache_resource
def load_model():
    """ Загрузка модели catboost"""
    loaded_model = CatBoostRegressor()
    loaded_model.load_model(r'raw_data/catboost_model.cbm')

    return loaded_model


def predict() -> float:
    """ Предсказание на тестовых данных"""
    model = load_model()

    with open(r'raw_data/test_data.pkl', 'rb') as f:
        X_test_loaded, y_test_loaded = pickle.load(f)

    y_pred = model.predict(X_test_loaded)
    rmse = np.sqrt(mean_squared_error(y_test_loaded, y_pred))

    return rmse
