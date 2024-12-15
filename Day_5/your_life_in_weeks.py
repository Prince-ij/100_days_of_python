#!/bin/env python3
print("This programs tells you how many days, weeks and months")
print("you have left, assuming you live till 90")

age = int(input("Enter your age: "))

years_left = 90 - age
months_left = years_left * 12
days_left = years_left * 365
weeks_left = years_left * 52

print(F"You have {days_left} days, {weeks_left} weeks and {months_left} months left")
