import pandas as pd

class DataExploration:
    @staticmethod
    def display_head(dataframes):
        for name, df in dataframes.items():
            print(f"{name} Data:\n", df.head())
    
    @staticmethod
    def print_columns(dataframes):
        for name, df in dataframes.items():
            print(f"\nColumns in {name} Data:\n", df.columns)
    
    @staticmethod
    def check_dtypes(dataframes):
        for name, df in dataframes.items():
            print(f"\nData Types in {name} Data:\n", df.dtypes)
    
    @staticmethod
    def summary_statistics(dataframes):
        for name, df in dataframes.items():
            print(f"\n{name} Data Summary:\n", df.describe())
    
    @staticmethod
    def check_missing_values(dataframes):
        for name, df in dataframes.items():
            print(f"\nMissing values in {name} Data:\n", df.isnull().sum())