from data import *

def report():
    for resource, value in resources.items():
        print(resource + ":", value)
    print(f"Money : ${profit:.2f}" )


def process_coins(coffee):
    quarter = int(input("How many quarters? : ")) * 0.25
    dime = int(input("How many dimes? : ")) * 0.10
    nickel = int(input("How many nickels? : ")) * 0.05
    penny = int(input("How many pennies? : ")) * 0.01
    global profit; money = 0
    money += quarter + dime + nickel + penny

    if money > coffee['cost']:
        change = money - coffee["cost"]
        profit += coffee['cost']
        print(f'Here is ${change:.2f} in change')
        return True
    elif money == coffee['cost']:
        money = 0
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def check_resources(coffee):
    ci = coffee['ingredients'] # ci holds the ingredients dictionary for the coffee
    coffee_resources = [ci['water'], ci['coffee'], ci.get('milk', 0)]
    current_resources = [resources['water'], resources['coffee'], resources.get('milk', 0)]

    for i in range(3):
        if current_resources[i] < coffee_resources[i]:
            print(f"Sorry, there is not enough {list(ci.keys())[i]}.")
            return False
    return True


def make_coffee(coffee, prompt):
    if check_resources(coffee):
        ci = coffee['ingredients']
        resources['water'] -= ci['water']
        resources['coffee'] -= ci['coffee']
        resources['milk'] -= ci.get('milk', 0)
    else:
        return
    if process_coins(coffee):
        print(f"Here is your {prompt} ☕ Enjoy!.")
    else:
        return
