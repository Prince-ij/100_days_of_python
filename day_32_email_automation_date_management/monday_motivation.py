import yagmail
import random
from datetime import datetime

with open("quotes.txt") as file:
    motivations = file.readlines()



day = datetime.now().weekday()

motivation = random.choice(motivations)
yag = yagmail.SMTP("baaby.dudu@gmail.com", "kcnkfizmwvonulem")
if day == 0:
    yag.send("princeij56@gmail.com", "Daily Motivation", motivation)

print(motivation)
