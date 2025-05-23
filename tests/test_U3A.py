import unittest
from solutions.U3A import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_range(self):
        result = fizzbuzz(1, 16)
        expected = ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
                    "11", "Fizz", "13", "14", "FizzBuzz"]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
