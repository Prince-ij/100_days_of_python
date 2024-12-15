import random

print("Welcome to the Number Guessing Game !")
number = random.randrange(1, 101)

print("I am thinking of a number between 1 and 100")

def game():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    num = 5
    while num:
        if difficulty == 'easy':
            num = 10
        print(f"You have {num} attempts remaining.")
        guess = int(input("Make a Guess: "))
        if guess == number:
            print("You win !!!")
            return
        elif guess > number:
            print("Too High")
        else:
            print("Too Low")
        num -= 1
    print("You lose !!!")

game()
