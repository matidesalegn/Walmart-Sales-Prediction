import pandas as pd

class DataLoader:
    @staticmethod
    def load_csv(filepath):
        try:
            return pd.read_csv(filepath, encoding='utf-8')
        except UnicodeDecodeError:
            return pd.read_csv(filepath, encoding='ISO-8859-1')