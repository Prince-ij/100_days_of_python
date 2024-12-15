#!/bin/python3
import math
print("Welcome to BMI calculator")

height = float(input("What is your height in metres? "))
weight = float(input("What is your weight in kg? "))

bmi = math.floor(weight / height ** 2)

bmi_message = ""

if bmi < 18.5:
    bmi_message = "underweight"
elif 18.5 <= bmi < 25:
    bmi_message = "normal"
elif 25 <= bmi < 30:
    bmi_message = "overweight"
elif 30 <= bmi < 35:
    bmi_message = "obese"
else:
    bmi_message = "clinically obese"

print("Your Body Mass Index is", bmi, "and you are", bmi_message)
