from data import *
from modules import *

flag = True
while flag != False:
    prompt = input("What would you like? (espresso/latte/cappuccino): ")
    if prompt == 'off':
        flag = False
        continue
    if prompt == 'report':
        report()
        continue
    order = MENU[prompt]
    make_coffee(order, prompt)
