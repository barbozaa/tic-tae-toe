from src.utils.utils import *
import itertools


class TicTacToe(object):
    def __init__(self):
        self.board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

    def welcome(self):
        print('Welcome! Here is your board: ')

    def print(self):
        print('    0    1    2')
        for col, row in enumerate(self.board):
            print(col, row)

    def reset(self):
        self.board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        self.welcome()
        self.print()

    def horizontal(self):
        for row in self.board:
            if all_equal(row) and row[0] != '-':
                return True
        return False

    def vertical(self):
        for col in range(len(self.board)):
            cols = []
            for r in self.board:
                cols.append(r[col])
            if all_equal(cols) and cols[0] != '-':
                return True
        return False

    def diagonal_normal(self):
        diagonal = []
        for i in range(len(self.board)):
            diagonal.append(self.board[i][i])
        if all_equal(diagonal) and diagonal[0] != '-':
            return True
        return False

    def diagonal_reversed(self):
        diagonal = []
        for col, row in enumerate(reversed(range(len(self.board)))):
            diagonal.append(self.board[row][col])
        if all_equal(diagonal) and diagonal[0] != '-':
            return True
        return False

    def check(self, player):
        if self.horizontal() or self.vertical() or self.diagonal_normal() or self.diagonal_reversed():
            print('Player {} wins!'.format(player))
            return True
        return False

    def request_answer(self, player):
        while True:
            move = input('Player ({}) where would you like to move? '.format(player))
            try:
                pos = move.split(' ')
                return [int(pos[0]), int(pos[1])]
            except (IndexError, ValueError):
                print('oops!, please enter a valid position {}'.format(move))
                continue

    def play_game(self, player):
        try:
            [col, row] = self.request_answer(player)
            if self.board[col][row] in 'XO':
                raise ValueError
            self.board[col][row] = 'X' if player == 'X' else 'O'
            self.print()
        except ValueError as e:
            print('oops!, you cannot move to this position', e)
        except Exception as e:
            print('Internal Error!', e)


if __name__ == '__main__':
    option = ''
    t = TicTacToe()
    t.welcome()
    t.print()
    won = False
    players = itertools.cycle(['X', 'O'])
    while not won:
        current_player = next(players)
        t.play_game(current_player)
        won = t.check(current_player)
        if won:
            answer = input('Game is over, would you like to play again? Y/N ')
            if answer == 'Y' or answer == 'y':
                won = False
                t.reset()
            elif answer == 'N' or answer == 'n':
                won = True

