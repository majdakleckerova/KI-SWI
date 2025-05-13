
import unittest
import pandas as pd
from solutions.U2A import prumer_znamek

class TestZnamky(unittest.TestCase):
    def test_average(self):
        data = {"student": ["A", "B"], "predmet": ["Math", "Math"], "znamka": [2, 4]}
        df = pd.DataFrame(data)
        result = prumer_znamek(df)
        self.assertEqual(result["Math"], 3.0)

    def test_empty(self):
        df = pd.DataFrame(columns=["student", "predmet", "znamka"])
        result = prumer_znamek(df)
        self.assertTrue(result.empty)

    def test_multiple_subjects(self):
        data = {"student": ["A", "B", "C"], "predmet": ["Math", "Physics", "Math"], "znamka": [1, 2, 3]}
        df = pd.DataFrame(data)
        result = prumer_znamek(df)
        self.assertEqual(result["Math"], 2.0)
        self.assertEqual(result["Physics"], 2.0)

if __name__ == '__main__':
    unittest.main()
