#!/usr/bin/python3
import random
from hangman_art import logo, stages
from hangman_words import word_list

print(logo)

print(stages[6])

chosen_word = random.choice(word_list)
original_word = chosen_word
blanks = ""
for _ in chosen_word:
    blanks += "_"
print()
print(blanks)

chosen_word = list(chosen_word)

blanks = list(blanks)
life = 6
guess_bank = []
while("_" in blanks):
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        index = original_word.index(guess)
        if blanks[index] == guess:
            print("You've already guessed this asshole !")
        else:
            blanks[index] = guess
    else:
        print("You guessed", guess, "and it is not part of the word")
        life -= 1

        if life > 0:
             print(stages[life])
             continue
        else:
            print("\n\n", stages[0])
            print("You are a loser !")
            print("As you be mumu, na", original_word, "u no fit guess")
            break
    blanks = "".join(blanks)
    print(blanks)
    chosen_word = list(chosen_word)
    blanks = list(blanks)
if "_" not in blanks:
    print("Congratulations, you WON !!!")
    print("Game Over !")
