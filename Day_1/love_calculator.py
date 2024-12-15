#!/bin/env python3
print("Welcome to the love Calculator !")
print("Make we check una compatibility ")

first_name = input("Enter your name: ").lower()
last_name = input("Enter lover's name: ").lower()

# cn stands for combined name
cn = first_name + last_name
check_true = cn.count("t") + cn.count("r") + cn.count("u") + cn.count("e")
check_love = cn.count("l") + cn.count("o") + cn.count("v") + cn.count("e")

# lv stands for love compatibility
lv = str(check_true) + str(check_love)

love_score = int(lv)

if love_score < 10 or love_score > 90:
    print(f"Your score is {lv}, you go together like coke and mentos.")
elif 40 <= love_score <= 50:
    print(f"Your score is {lv}, you are alright together.")
else:
    print(f"Your score is {lv}")
