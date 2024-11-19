#!/bin/env python3

print("Program to get maximum value of a list")

values = input("Enter values seperated by space: ").split()

for i in range(len(values)):
    values[i] = int(values[i])

max_value = values[0]

for value in values:
    if value > max_value:
        max_value = value

print("The maximum value is :", max_value)
