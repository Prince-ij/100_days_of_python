#!/bin/python3

def prime_checker(number):
    for i in range(2, number):
        if number % i == 0:
            print("It's not a prime number")
            return

    print("It is a prime number")

n = int(input("Enter number you want to check: "))
prime_checker(n)
