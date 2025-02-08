import random, os
from art import logo

def black_jack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    user = []
    dealer = []

    for _ in range(2):
        user.append(random.choice(cards))
    for _ in range(2):
        dealer.append(random.choice(cards))

    print(f"Your cards: {user}")
    print(f"Dealer first card: {dealer[0]}")

    user_score, dealer_score = sum(user), sum(dealer)
    flag = True
    while(flag):
        if (user_score == 21 and len(user) == 2):
            print(f"BlackJack !!! : {user}\nYou win !")
            return
        elif (dealer_score == 21):
            print(f"Dealer got a Blackjack: {dealer},\nYou lose !")
            return
        elif (user_score == dealer_score):
             print(F"Draw: user = {user}, dealer = {dealer}")
             return

        if (user_score > 21) and (11 in user):
            ace = user.index(11)
            if 1 + user[ace or not(0)] > 21:
                print(f"Burst: {user}, You lose !")
            return
        elif user_score > 21:
            print(f"Burst: {user}, You lose !")
            return
        else:
            card_again = input("Do you want to get a card ? 'y' or 'n': ")
            if card_again == 'y':
                user.append(random.choice(cards))
                print(f"Your cards: {user}")
                user_score = sum(user)
            else:
                flag = False

    dealer.append(random.choice(cards))
    print("Dealer draws a card")
    while(dealer_score := sum(dealer) < 16 ):
        dealer.append(random.choice(cards))
    dealer_score = sum(dealer)
    if dealer_score > 21:
        print(f"Dealer Bursted !!!: {dealer}\nYou win !")
        return
    elif user_score > dealer_score:
        print(f"\nYou win!!!  {user}")
        return
    elif user_score < dealer_score:
        print(f"Dealer Wins : {dealer} !\n You lose")
        return
    else:
        print(F"Draw: user = {user}, dealer = {dealer}");
        return

while(play := input("Do you want to play a game of Black Jack ? 'y' or 'n': ") == 'y'):
    os.system('clear')
    print(logo)
    black_jack()
