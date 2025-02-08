#!/bin/env python3
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Rock Paper Scissors Game ")
gamer = input("What do you choose, Type 0 for rock, 1 for paper, or 2 for Scissors  ")

list = [0, 1, 2]
computer = random.choice(list)


