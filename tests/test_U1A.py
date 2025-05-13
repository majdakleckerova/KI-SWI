
import unittest
from solutions.U1A import check_winner

class TestPiskvorky(unittest.TestCase):
    def test_row_win(self):
        board = [["X", "X", "X"], ["O", "", "O"], ["", "", ""]]
        self.assertEqual(check_winner(board), "X")

    def test_column_win(self):
        board = [["O", "X", ""], ["O", "X", ""], ["", "X", ""]]
        self.assertEqual(check_winner(board), "X")

    def test_diagonal_win(self):
        board = [["O", "", "X"], ["", "X", ""], ["X", "", ""]]
        self.assertEqual(check_winner(board), "X")

    def test_draw(self):
        board = [["X", "O", "X"], ["X", "O", "O"], ["O", "X", "X"]]
        self.assertIsNone(check_winner(board))

    def test_empty_board(self):
        board = [["", "", ""], ["", "", ""], ["", "", ""]]
        self.assertIsNone(check_winner(board))

if __name__ == '__main__':
    unittest.main()
