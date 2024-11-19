#!/bin/python3
import math
print("Welcome to BMI calculator")

height = float(input("What is your height in metres? "))
weight = float(input("What is your weight in kg? "))

bmi = math.floor(weight / height ** 2)

print("Your Body Mass Index is", bmi, ".")
