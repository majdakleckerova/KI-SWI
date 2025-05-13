
import unittest
import pandas as pd
from solutions.U2B import trzby_za_zakazniky

class TestTrzby(unittest.TestCase):
    def test_filter_and_sum(self):
        data = {
            "id": [1, 2],
            "datum": ["2024-01-01", "2024-06-01"],
            "zakaznik": ["A", "A"],
            "produkt": ["X", "Y"],
            "mnozstvi": [2, 3],
            "cena": [100, 200]
        }
        df = pd.DataFrame(data)
        result = trzby_za_zakazniky(df)
        self.assertEqual(result["A"], 2*100 + 3*200)

    def test_ignore_other_years(self):
        data = {
            "id": [1, 2],
            "datum": ["2023-01-01", "2022-06-01"],
            "zakaznik": ["A", "B"],
            "produkt": ["X", "Y"],
            "mnozstvi": [1, 1],
            "cena": [100, 100]
        }
        df = pd.DataFrame(data)
        result = trzby_za_zakazniky(df)
        self.assertTrue(result.empty)

if __name__ == '__main__':
    unittest.main()
