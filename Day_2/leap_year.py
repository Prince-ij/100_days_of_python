#!/bin/env python3
"""
This programs checks to see whether a given year
is a leap year or not. 
"""
print("Welcome to leap year checker program")
year = int(input("Enter the year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("That is a leap year")
else:
    print("Not a leap year")
