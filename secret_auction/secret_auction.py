from art import logo
import os

print(logo)

auction_list = []

print("Welcome to the secret auction program ")

again = True
while(again):
    name = input("What's your name ? ")
    bid = float(input("What's your bid?  $"))

    new_bid = {
        "name": name,
        "bid": bid
    }

    auction_list.append(new_bid)

    again = input("Are there any other bidders, yes or no ? ").lower()
    if again == "no":
        again = False
    else:
        os.system('clear')

bid_winner = ""
win_price = auction_list[0]["bid"]
for bid in auction_list:
    if bid["bid"] > win_price:
        win_price = bid["bid"]
        bid_winner = bid["name"]
os.system('clear')
print(f"The winner is {bid_winner} with a bid of ${win_price}.")
