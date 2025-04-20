from globals import game_bar, game_board
from globals import positions as ps
from functions import check_fill, check_valid
from random import choice
import time
import os

class Player:
    def __init__(self, name, letter, auto=False):
        self.letter = letter.upper()
        self.name = name.title()
        self.auto = auto

    def play(self):
        while True:
            if self.auto:
                while True:
                    init_pos = choice(list(game_bar.keys()))
                    if (check_fill(init_pos)):
                        pos = init_pos
                        print(f'{self.name} has entered into position: {pos}')
                        time.sleep(2)
                        break
            else:
                pos = input(f'{self.name} - Enter position to play: ')

                if not check_valid(pos):
                    print('Invalid Position, must be from the list - (a, b, c, d, e, f, g, h, i)')
                    continue

                if not check_fill(pos):
                    print('Are you blind, position has already been filled')
                    continue


            game_bar[pos] = self.letter
            break
        os.system('clear')
        global game_board
        new_board = game_board[0:ps[pos]] + self.letter + game_board[ps[pos] + 1:]
        game_board = new_board
        print(game_board)
