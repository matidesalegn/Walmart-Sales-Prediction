import numpy as np
import pandas as pd
from collections import Counter

class DataPreprocessing:
    @staticmethod
    def handle_missing_values(train, macro):
        train['Sales(In ThousandDollars)'] = train['Sales(In ThousandDollars)'].fillna(train['Sales(In ThousandDollars)'].median())
        macro.replace("?", np.nan, inplace=True)
        macro['AdvertisingExpenses (in Thousand Dollars)'] = pd.to_numeric(macro['AdvertisingExpenses (in Thousand Dollars)'], errors='coerce')
        macro['AdvertisingExpenses (in Thousand Dollars)'] = macro['AdvertisingExpenses (in Thousand Dollars)'].fillna(macro['AdvertisingExpenses (in Thousand Dollars)'].median())

    @staticmethod
    def remove_outliers(train):
        outliers_to_drop = DataPreprocessing.detect_outliers(train, 2, ['Sales(In ThousandDollars)'])
        return train.drop(outliers_to_drop, axis=0).reset_index(drop=True)

    @staticmethod
    def detect_outliers(df, n, features):
        outlier_indices = []
        for col in features:
            Q1 = np.percentile(df[col], 25)
            Q3 = np.percentile(df[col], 75)
            IQR = Q3 - Q1
            outlier_step = 1.5 * IQR
            outlier_list_col = df[(df[col] < Q1 - outlier_step) | (df[col] > Q3 + outlier_step)].index
            outlier_indices.extend(outlier_list_col)
        outlier_indices = Counter(outlier_indices)
        return [k for k, v in outlier_indices.items() if v > n]

    @staticmethod
    def convert_categorical_variables(train, macro, events):
        if 'ProductCategory' in train.columns:
            train = pd.get_dummies(train, columns=['ProductCategory'])
        if 'PartyInPower' in macro.columns:
            macro = pd.get_dummies(macro, columns=['PartyInPower'])
        if 'Event' in events.columns:
            events = pd.get_dummies(events, columns=['Event'])
        if 'DayCategory' in events.columns:
            events = pd.get_dummies(events, columns=['DayCategory'])
        return train, macro, events

    @staticmethod
    def save_preprocessed_data(train, macro, events, weather):
        preprocessed_dir = 'data/preprocessed'
        if not os.path.exists(preprocessed_dir):
            os.makedirs(preprocessed_dir)
        train.to_csv(os.path.join(preprocessed_dir, 'train_cleaned.csv'), index=False)
        macro.to_csv(os.path.join(preprocessed_dir, 'macro_cleaned.csv'), index=False)
        events.to_csv(os.path.join(preprocessed_dir, 'events_cleaned.csv'), index=False)
        weather.to_csv(os.path.join(preprocessed_dir, 'weather_cleaned.csv'), index=False)