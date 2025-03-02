from functions import game_instructions, game
from globals import game_intro
from player import Player
import os
import time

os.system('clear')

print(game_intro)
game_instructions()

print('************** Do you have a friend or Do you wish to challenge Me ******************')

choice = input("Play Against a Friend: Y/N:  ").upper()
if choice == 'Y':
    os.system('clear')
    print('************* You will take turns to Play with your Friend **************')
    choice = True
else:
    os.system('clear')
    print('************* Get ready to be Crushed by My gaming Prowess ***************')
    choice = False

time.sleep(3)
os.system('clear')

print('************* Player One ****************')
player_1 = Player(input('Your name : '), input('Choose a Letter, X or Y: '))
os.system('clear')
print('************* Player Two ****************')
if choice == False:
    player_2 = Player('Computer', 'X' if player_1.letter == 'Y' else 'Y', auto=True)
else:
    player_2 = Player(input('Your name : '), 'X' if player_1.letter == 'Y' else 'Y')

game(player_1, player_2)
