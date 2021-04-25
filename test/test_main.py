from src.main import TicTacToe
import unittest
from unittest.mock import patch


class TestTicTacToe(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = TicTacToe()

    def test_welcome(self):
        self.assertIsNone(self.obj.welcome())

    def test_print(self):
        self.assertIsNone(self.obj.print())

    def test_reset(self):
        self.assertIsNone(self.obj.reset())
        self.assertEqual(self.obj.board, [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']])

    def test_horizontal(self):
        board = [['X', 'X', 'X'],
                 ['-', '-', '-'],
                 ['-', '-', '-']]
        self.obj.board = board
        self.assertTrue(self.obj.horizontal())

    def test_vertical(self):
        board = [['X', '-', '-'],
                 ['X', '-', '-'],
                 ['X', '-', '-']]
        self.obj.board = board
        self.assertTrue(self.obj.vertical())

    def test_diagonal_normal(self):
        board = [['X', '-', '-'],
                 ['-', 'X', '-'],
                 ['-', '-', 'X']]
        self.obj.board = board
        self.assertTrue(self.obj.diagonal_normal())

    def test_diagonal_reversed(self):
        board = [['-', '-', 'X'],
                 ['-', 'X', '-'],
                 ['X', '-', '-']]
        self.obj.board = board
        self.assertTrue(self.obj.diagonal_reversed())

    def test_check(self):
        board = [['-', '-', 'X'],
                 ['-', 'X', '-'],
                 ['X', '-', '-']]
        self.obj.board = board
        self.assertTrue(self.obj.check('Test Player'))

    @patch('src.main.TicTacToe.request_answer', return_value='0 0')
    def test_request_answer(self, mock_input):
        answer = mock_input()
        self.assertEqual(answer, '0 0')

    @patch('src.main.TicTacToe.request_answer', return_value=[0, 1])
    def test_play_game(self, mock_input):
        self.assertIsNone(self.obj.play_game('test player'))


if __name__ == '__main__':
    unittest.main()
