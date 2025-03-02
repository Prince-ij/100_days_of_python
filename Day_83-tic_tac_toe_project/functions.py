from globals import winning_criteria, game_bar
import os
import math

def check_win():
    for win in winning_criteria:
        if eval(win):
            return True

    else:
        return False


def check_fill(pos):
    value = game_bar[pos]
    return True if isinstance(value, float) else False


def check_valid(pos):
    if pos in game_bar.keys():
        return True
    else:
        return False


def game_instructions():
    print('''
*********************** Welcome to TIC TAC TOE GAME ***************************
          ## Step 1: choose play mode (against a friend or computer)
          ## Step 2: pick your letter (X or O)
          ## Step 3: Play by entering the position marked from top left to bottom right
                     (a, b, c, d, e, f, g, h, i)
          ## Remember: input must be a valid position from step 3
          ## GOODLUCK ............................
''')
    if (input('I have read and understand. Y/N:  ').upper() == 'Y'):
        os.system('clear')
    else:
        os.system('clear')

def game(player_1, player_2):
    condition = any(math.isnan(value) for value in game_bar.values() if isinstance(value, float))

    while(condition):
        player_1.play()
        if check_win():
            print(f'{player_1.name} wins the Game')
            break
        player_2.play()
        if check_win():
            print(f'{player_2.name} wins the Game')
            break
    else:
        print('No winner')
