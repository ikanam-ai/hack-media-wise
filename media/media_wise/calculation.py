from utils import load_ao_hex, get_geo_data, GeoFile
import json
import numpy as np
import pandas as pd
import geopandas as gpd


def calculate_all_points(data: gpd.GeoDataFrame) -> dict[str, list]:
    """ Расчет всех точек для карты, для быстрого доступа к ним"""
    data['points'] = data['points'].apply(json.loads)
    points = {}
    for i, row in data.iterrows():
        name = row['ref']
        if points.get(name) is None:
            points[name] = []
        points[name].append(row)

    for point in points.values():
        point.sort(key=lambda x: x['val'], reverse=True)

    return points


geo_points: dict[str, list] = calculate_all_points(get_geo_data(GeoFile.moscow_ao_hex_val))


def balance_points(points_count: int, df: pd.DataFrame) -> pd.DataFrame:
    """ Балансировка точек для карты, если их количество не совпадает с заданным"""
    df = df.copy()
    val_sum = df['val'].sum()
    df.loc[:, 'points_count'] = np.round((df['val'] / val_sum) * points_count).astype(int)
    all_points = df['points_count'].sum()
    while all_points > points_count:
        min_val = df['val'].min()
        mask = (df['val'] == min_val) & (df['points_count'] >= 1)
        df.loc[mask, 'points_count'] -= 1
        all_points = df['points_count'].sum()
    while all_points < points_count:
        max_val = df['val'].min()
        mask = df['val'] == max_val
        df.loc[mask, 'points_count'] += 1
        all_points = df['points_count'].sum()

    return df


def pick_points(frame: pd.DataFrame) -> list[object]:
    """ Выбор точек для карты"""
    points = []
    for i, row in frame.iterrows():
        points_count = row['points_count']
        name = row['ref']
        points.extend(geo_points[name][:points_count])

    return points


def calculate(points_count: int) -> list[object]:
    """ Расчет точек для карты"""
    filter_d = {"ЗАО", "ТАО", "НАО", "ЗелАО", "ТАО", "НАО"}
    df = load_ao_hex()
    mask = ~df['ref'].isin(filter_d)
    filtered_df = df[mask]
    balanced = balance_points(points_count, filtered_df)

    return pick_points(balanced)