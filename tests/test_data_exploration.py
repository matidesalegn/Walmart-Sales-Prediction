import unittest
from src.data_exploration import DataExploration
import pandas as pd

class TestDataExploration(unittest.TestCase):
    def setUp(self):
        self.dataframes = {
            'Train': pd.read_csv('../data/train.csv'),
            'Macro Economic': pd.read_csv('../data/macro_economic.csv'),
            'Events and Holidays': pd.read_csv('../data/Events_HolidaysData.csv'),
            'Weather': pd.read_csv('../data/WeatherData.csv')
        }

    def test_display_head(self):
        DataExploration.display_head(self.dataframes)

if __name__ == '__main__':
    unittest.main()