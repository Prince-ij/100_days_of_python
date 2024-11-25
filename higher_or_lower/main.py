from game_data import data
from art import logo, vs
import random, os

a = random.choice(data)
b = random.choice(data)
while b == a:
    b = random.choice(data)
score = 0
choice = 0
highest = 0

while choice == highest:
    highest = a['follower_count'] if a['follower_count'] > b['follower_count'] else b['follower_count']

    print(logo)
    print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}.")
    print(vs)
    print(f"Against B: {b['name']}, {b['description']}, from {b['country']}.")

    choice = input("Who has more followers? Type 'A' or 'B': ")
    choice = a['follower_count'] if choice == 'A' else b['follower_count']
    score += 1
    b = a.copy()
    b == random.choice(data)
    while b == a:
        b = random.choice(data)
    os.system('clear')

os.system('clear')
print(logo)
print(f"Sorry, You lost !!!. Your score: {score}.")
