from catboost import CatBoostRegressor
import pickle
import numpy as np
from sklearn.metrics import mean_squared_error


def load_model():
    loaded_model = CatBoostRegressor()
    loaded_model.load_model(r'raw_data/catboost_model.cbm')

    with open(r'raw_data/test_data.pkl', 'rb') as f:
        X_test_loaded, y_test_loaded = pickle.load(f)

    # Прогнозирование и подсчет метрик
    y_pred = loaded_model.predict(X_test_loaded)
    rmse = np.sqrt(mean_squared_error(y_test_loaded, y_pred))

    return rmse
