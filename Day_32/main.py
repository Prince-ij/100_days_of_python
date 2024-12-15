##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas
import yagmail
from random import choice
from datetime import datetime

birthdays = pandas.read_csv("birthdays.csv")
day = datetime.now().day
month = datetime.now().month
year = datetime.now().year

current_date = [day, month, year]

letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

with open(f"letter_templates/{choice(letters)}") as file:
    letter = file.read()

yag = yagmail.SMTP("baaby.dudu@gmail.com", "kcnkfizmwvonulem")

b_days = birthdays.to_dict(orient="records")
for b in b_days:
    b_day = b['day']
    b_year = b['year']
    b_month = b['month']
    b_name = b['name']
    b_mail = b['email']
    birth_date = [b_day, b_month, b_year]

    name = b_name
    letter = letter.replace("[NAME]", name)


    if current_date == birth_date:
        yag.send(b_mail, "Birthday Wishes", letter)
