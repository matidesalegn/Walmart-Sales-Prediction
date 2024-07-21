import unittest
import pandas as pd
from src.data_preprocessing import DataPreprocessing

class TestDataPreprocessing(unittest.TestCase):
    def setUp(self):
        self.train = pd.read_csv('../data/train.csv')
        self.macro = pd.read_csv('../data/macro_economic.csv')

    def test_handle_missing_values(self):
        DataPreprocessing.handle_missing_values(self.train, self.macro)
        self.assertFalse(self.train.isnull().sum().any())
        self.assertFalse(self.macro.isnull().sum().any())

    def test_remove_outliers(self):
        original_shape = self.train.shape
        train_cleaned = DataPreprocessing.remove_outliers(self.train)
        self.assertTrue(train_cleaned.shape[0] < original_shape[0])

if __name__ == '__main__':
    unittest.main()