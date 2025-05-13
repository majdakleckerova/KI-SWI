
import unittest
from solutions.U3B import is_palindrom

class TestPalindrom(unittest.TestCase):
    def test_simple_palindrome(self):
        self.assertTrue(is_palindrom("kajak"))

    def test_ignore_case_space(self):
        self.assertTrue(is_palindrom("A man a plan a canal Panama"))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrom("hello"))

    def test_empty_string(self):
        self.assertTrue(is_palindrom(""))

    def test_single_char(self):
        self.assertTrue(is_palindrom("x"))

if __name__ == '__main__':
    unittest.main()
