import unittest
import pandas as pd # type: ignore
from unittest.mock import patch
from utils.load_csv import save_to_csv

class TestLoad(unittest.TestCase):

    @patch("utils.load_csv.pd.DataFrame.to_csv")
    def test_save_to_csv(self, mock_to_csv):
        df = pd.DataFrame({"A": [1]})
        save_to_csv(df)

        mock_to_csv.assert_called_once()

if __name__ == "__main__":
    unittest.main()