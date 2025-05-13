
import unittest
from solutions.U1B import get_winner

class TestKamenNuzkyPapir(unittest.TestCase):
    def test_player_wins(self):
        self.assertEqual(get_winner("rock", "scissors"), "player")

    def test_ai_wins(self):
        self.assertEqual(get_winner("scissors", "rock"), "ai")

    def test_draw(self):
        self.assertEqual(get_winner("rock", "rock"), "draw")

    def test_paper_beats_rock(self):
        self.assertEqual(get_winner("paper", "rock"), "player")

    def test_scissors_beat_paper(self):
        self.assertEqual(get_winner("scissors", "paper"), "player")

if __name__ == '__main__':
    unittest.main()
