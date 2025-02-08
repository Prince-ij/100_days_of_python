from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()
maker = CoffeeMaker()
money_processor = MoneyMachine()
flag = True
while flag:
    options = my_menu.get_items()
    string = f"What would you like ? ({options}): "
    choice = input(string)
    if choice == 'off':
        flag = False
        continue
    if choice == 'report':
        maker.report()
        money_processor.report()
        continue
    order = my_menu.find_drink(choice)
    if maker.is_resource_sufficient(order):
        if money_processor.make_payment(order.cost):
            maker.make_coffee(order)
