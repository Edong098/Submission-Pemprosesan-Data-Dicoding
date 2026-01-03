import unittest
import pandas as pd # type: ignore
from utils.transform import transform_to_dataframe, transform_data

class TestTransform(unittest.TestCase):

    def test_transform_to_dataframe(self):
        data = [
            {"Title": "A", "Price": "$10", "Rating": 5, "Colors": "3", "Size": "M", "Gender": "Men"}
        ]
        df = transform_to_dataframe(data)

        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 1)

    def test_transform_data(self):
        data = {
            "Title": ["A"],
            "Price": ["$10"],
            "Rating": [5],
            "Colors": ["3"],
            "Size": ["M"],
            "Gender": ["Men"]
        }

        df = pd.DataFrame(data)
        df = transform_data(df, 16000)

        self.assertIn("Price", df.columns)
        self.assertEqual(df["Rating"].iloc[0], 5)

if __name__ == "__main__":
    unittest.main()