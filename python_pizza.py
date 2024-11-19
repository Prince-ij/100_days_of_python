#!/bin/env python3
""" A python program to calculate bills based on
    total purchases in a pizza restaurant sim
"""
bill = 0
print("Welcome to python pizza delivery")

size = input("Which size of pizza do you need? M, S, or L : ")
if size == "M":
    print("You chose medium size pizza")
    bill += 20
    peproni = input("Do you want Pepperoni, Y or N: ")
    if peproni == "Y":
        print("Pepperoni added")
        bill += 3
    cheese = input("Do you need extra cheese, Y or N: ")
    if cheese == "Y":
        bill += 1
elif size == "L":
    print("You chose a large pizza")
    bill += 25
    peproni = input("Do you want pepperoni, Y or N: ")
    if peproni == "Y":
        print("pepperoni added")
        bill += 3
    cheese = input("You want cheese boss ?, Y or N: ")
    if cheese == "Y":
        bill += 3
elif size == "S":
    print("You picked a small pizza")
    bill += 15
    peproni = ("Can you afford to buy our pepperoni ? Y or N ")
    if peproni == "Y":
        print("We've added pepperoni, hope you won't regret it")
        bill += 2
    cheese = input("Do you also want cheese , nigga ? Y or N: ")
    if cheese == "Y":
        bill += 2
print("Your total bill is: $" + str(bill))
