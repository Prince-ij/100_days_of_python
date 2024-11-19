#!/bin/env python3
print("Welcome to me tip calculator")

bill = float(input("What's em total bill: $"))
homies = int(input("How many ema homies got ya ? "))
tip = int(input("give some tip to our dude, show some love  %"))

total_bill = bill * (tip / 100) + bill
homie_bill = round(total_bill / homies, 2)

print(f"EACH OF YA GONNA GIVE OUT ${homie_bill:.2f}.")

