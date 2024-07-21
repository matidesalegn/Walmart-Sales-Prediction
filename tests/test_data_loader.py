import unittest
from src.data_loader import DataLoader

class TestDataLoader(unittest.TestCase):
    def test_load_csv(self):
        df = DataLoader.load_csv('../data/train.csv')
        self.assertFalse(df.empty)

if __name__ == '__main__':
    unittest.main()