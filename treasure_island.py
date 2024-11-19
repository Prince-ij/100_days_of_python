#!/bin/env python3
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to Treasure Island !!!")
print("Your goal is to find the treasure or die hahaha ")

print("You arrive to a two pathway, left is water , right is fire. which way do you go ?")

left = input("left or right? ").lower()

if left == "left":
    print("You reached there, you see a boat. You can take the boat or you can swim")
    boat = input("boat or swim ? ").lower()
    if boat == "boat":
        print("You arrived shore, you found three boxes, red , green and black. Which do you open ?")
        green = input("red, green, or black ").lower()
        if green == "green":
            print("Hurray, you found the treasure !!!")
            print("Congratulations , you won !")
        elif green == "red":
            print("You fool, you released the termites, they swarmed and surrounded you and swallowed you, while you cried for your life")
            print("What a miserable ending, Game Over !!!")
        else:
            print("The black box is Imhotebs coffin, you awaked the mummy and the first person he killed was you.")
            print("If only you were a little smarter, you could have saved your life. Game Over!!!")
    else:
        print("Idiot, you should have used the boat, the crocodiles had you for dinner.")
        print("Game Over !!!")
else:
    print("You got toasted and the hyenas had you for lunch")
    print("Game Over !!!")
